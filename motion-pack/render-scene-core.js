// Windows render wrapper: puppeteer-core + system Chrome (no Chromium download).
// Usage: node render-scene-core.js <html> <output.mp4> <durationSec> [--preview]
const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const [,, htmlArg, outArg, durArg, ...rest] = process.argv;
if (!htmlArg || !outArg || !durArg) {
  console.error("usage: node render-scene-core.js <html> <output.mp4> <durationSec> [--preview]");
  process.exit(1);
}
const PREVIEW = rest.includes("--preview");
const CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe";
const HTML_PATH = path.resolve(htmlArg);
const OUT_PATH = path.resolve(outArg);
const DURATION = parseFloat(durArg);
const FPS = PREVIEW ? 15 : 30;   // preview lowers fps only; layout stays true 1080x1920
const WIDTH = 1080;
const HEIGHT = 1920;
const SCALE = 1;
const GIF_W = PREVIEW ? 540 : WIDTH;
const TOTAL_FRAMES = Math.round(DURATION * FPS);
const FRAMES_DIR = path.join(path.dirname(OUT_PATH), ".frames-" + path.basename(OUT_PATH, path.extname(OUT_PATH)));

(async () => {
  fs.mkdirSync(path.dirname(OUT_PATH), { recursive: true });
  if (fs.existsSync(FRAMES_DIR)) fs.rmSync(FRAMES_DIR, { recursive: true });
  fs.mkdirSync(FRAMES_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--allow-file-access-from-files", "--force-color-profile=srgb"],
    defaultViewport: { width: WIDTH, height: HEIGHT, deviceScaleFactor: SCALE },
  });
  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: SCALE });
  await page.goto("file://" + HTML_PATH, { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  // wait for images
  await page.evaluate(async () => {
    const imgs = Array.from(document.images);
    await Promise.all(imgs.map(im => im.complete ? 1 : new Promise(r => { im.onload = im.onerror = r; })));
  });
  await page.evaluate(() => { if (window.gsap) gsap.globalTimeline.pause(); });

  console.log(`Rendering ${TOTAL_FRAMES} frames @ ${FPS}fps for ${DURATION}s ${PREVIEW ? "(PREVIEW)" : ""}`);
  for (let i = 0; i < TOTAL_FRAMES; i++) {
    const t = i / FPS;
    await page.evaluate((time) => { if (window.gsap) gsap.globalTimeline.time(time); }, t);
    await page.screenshot({ path: path.join(FRAMES_DIR, `frame-${String(i).padStart(5, "0")}.png`), type: "png",
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT } });
    if (i % 15 === 0) process.stdout.write(`  ${i}/${TOTAL_FRAMES}\r`);
  }
  console.log(`  ${TOTAL_FRAMES}/${TOTAL_FRAMES} done`);
  await browser.close();

  const isGif = OUT_PATH.toLowerCase().endsWith(".gif");
  console.log(isGif ? "Encoding GIF..." : "Encoding MP4...");
  if (isGif) {
    execSync(`ffmpeg -y -framerate ${FPS} -i "${FRAMES_DIR}/frame-%05d.png" -vf "fps=${FPS},scale=${GIF_W}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" "${OUT_PATH}"`, { stdio: "pipe" });
  } else {
    execSync(`ffmpeg -y -framerate ${FPS} -i "${FRAMES_DIR}/frame-%05d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow -movflags +faststart "${OUT_PATH}"`, { stdio: "pipe" });
  }
  fs.rmSync(FRAMES_DIR, { recursive: true });
  console.log(`→ ${OUT_PATH}`);
})().catch(e => { console.error(e); process.exit(1); });
