const puppeteer = require("puppeteer");
const [,, htmlPath, outPath, timeArg] = process.argv;
(async () => {
  const browser = await puppeteer.launch({
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
    defaultViewport: { width: 1080, height: 1920, deviceScaleFactor: 1 },
  });
  const page = await browser.newPage();
  await page.goto("file://" + htmlPath, { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate((t) => { gsap.globalTimeline.pause(); gsap.globalTimeline.time(t); }, parseFloat(timeArg));
  await page.screenshot({ path: outPath, type: "png" });
  await browser.close();
  console.log("saved " + outPath);
})().catch(e => { console.error(e); process.exit(1); });
