// Render a GSAP scene to a TRANSPARENT (alpha) overlay video using system Chrome.
// Usage: node render-overlay.js <html> <out.mov> <durationSec> [chromePath]
// Output: ProRes 4444 MOV with alpha (drop over footage in any editor).
// Transparent PNG frames are kept in a sibling .frames-* dir (import as PNG seq for CapCut).

const puppeteer = require("puppeteer-core");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const [, , htmlArg, outArg, durArg, chromeArg] = process.argv;
if (!htmlArg || !outArg || !durArg) {
  console.error("usage: node render-overlay.js <html> <out.mov> <sec> [chromePath]");
  process.exit(1);
}
const HTML = path.resolve(htmlArg);
const OUT = path.resolve(outArg);
const DUR = parseFloat(durArg);
const CHROME = chromeArg || "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const FPS = 30, W = 1080, H = 1920, N = Math.round(DUR * FPS);
const FRAMES = path.join(path.dirname(OUT), ".frames-" + path.basename(OUT).replace(/\.[^.]+$/, ""));

(async () => {
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  if (fs.existsSync(FRAMES)) fs.rmSync(FRAMES, { recursive: true });
  fs.mkdirSync(FRAMES, { recursive: true });

  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--force-color-profile=srgb", "--hide-scrollbars"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
  await page.goto("file://" + HTML, { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => { if (window.gsap) gsap.globalTimeline.pause(); });

  console.log(`Rendering ${N} transparent frames @ ${FPS}fps...`);
  for (let i = 0; i < N; i++) {
    await page.evaluate((t) => { if (window.gsap) gsap.globalTimeline.time(t); }, i / FPS);
    await page.screenshot({
      path: path.join(FRAMES, `f-${String(i).padStart(5, "0")}.png`),
      type: "png", omitBackground: true,
      clip: { x: 0, y: 0, width: W, height: H },
    });
  }
  await browser.close();

  console.log("Encoding alpha MOV (ProRes 4444)...");
  execSync(
    `ffmpeg -y -framerate ${FPS} -i "${FRAMES}/f-%05d.png" -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le "${OUT}"`,
    { stdio: "pipe" }
  );
  console.log(`OK -> ${OUT}`);
  console.log(`PNG frames (for CapCut) -> ${FRAMES}`);
})().catch((e) => { console.error(e); process.exit(1); });
