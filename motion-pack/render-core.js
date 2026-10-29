// render-scene.js variant for machines with puppeteer-core only (uses system Chrome).
// Usage:
//   node render-core.js <html> <out.mp4> <durationSec>   → full render @1080x1920 30fps
//   node render-core.js <html> <out.png> <seekSec>       → single preview frame
const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const [,, htmlArg, outArg, tArg] = process.argv;
if (!htmlArg || !outArg || !tArg) {
  console.error("usage: node render-core.js <html> <out.mp4|out.png> <durationSec|seekSec>");
  process.exit(1);
}
const HTML_PATH = path.resolve(htmlArg);
const OUT_PATH = path.resolve(outArg);
const T = parseFloat(tArg);
const FPS = 30, WIDTH = 1080, HEIGHT = 1920;
const IS_PREVIEW = OUT_PATH.toLowerCase().endsWith(".png");

(async () => {
  fs.mkdirSync(path.dirname(OUT_PATH), { recursive: true });
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
    defaultViewport: { width: WIDTH, height: HEIGHT, deviceScaleFactor: 1 },
  });
  const page = await browser.newPage();
  await page.goto("file://" + HTML_PATH, { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => { if (window.gsap) gsap.globalTimeline.pause(); });

  if (IS_PREVIEW) {
    await page.evaluate((t) => { if (window.gsap) gsap.globalTimeline.time(t); }, T);
    await page.screenshot({ path: OUT_PATH, type: "png" });
    await browser.close();
    console.log("→ " + OUT_PATH);
    return;
  }

  const TOTAL_FRAMES = Math.round(T * FPS);
  const FRAMES_DIR = path.join(path.dirname(OUT_PATH), ".frames-" + path.basename(OUT_PATH, ".mp4"));
  if (fs.existsSync(FRAMES_DIR)) fs.rmSync(FRAMES_DIR, { recursive: true });
  fs.mkdirSync(FRAMES_DIR, { recursive: true });
  console.log(`Rendering ${TOTAL_FRAMES} frames @ ${FPS}fps for ${T}s`);
  for (let i = 0; i < TOTAL_FRAMES; i++) {
    await page.evaluate((time) => { if (window.gsap) gsap.globalTimeline.time(time); }, i / FPS);
    await page.screenshot({
      path: path.join(FRAMES_DIR, `frame-${String(i).padStart(5, "0")}.png`),
      type: "png",
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
    });
    if (i % 30 === 0) process.stdout.write(`  ${i}/${TOTAL_FRAMES}\r`);
  }
  console.log(`  ${TOTAL_FRAMES}/${TOTAL_FRAMES} done`);
  await browser.close();
  console.log("Encoding MP4...");
  execSync(
    `ffmpeg -y -framerate ${FPS} -i "${FRAMES_DIR}/frame-%05d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow -movflags +faststart "${OUT_PATH}"`,
    { stdio: "pipe" }
  );
  fs.rmSync(FRAMES_DIR, { recursive: true });
  console.log(`→ ${OUT_PATH}`);
})().catch(e => { console.error(e); process.exit(1); });
