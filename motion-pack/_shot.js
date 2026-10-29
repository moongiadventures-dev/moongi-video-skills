const puppeteer = require("puppeteer-core");
const path = require("path");
const CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe";
const HTML = path.resolve(process.argv[2]);
const OUT = path.resolve(process.argv[3]);
(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, headless: "new",
    args:["--no-sandbox","--disable-setuid-sandbox","--allow-file-access-from-files","--force-color-profile=srgb"],
    defaultViewport:{width:1080,height:1920,deviceScaleFactor:1}});
  const p = await b.newPage();
  await p.setViewport({width:1080,height:1920,deviceScaleFactor:1});
  await p.goto("file://"+HTML,{waitUntil:"networkidle0"});
  await p.evaluate(()=>document.fonts.ready);
  await p.evaluate(async()=>{const i=[...document.images];await Promise.all(i.map(im=>im.complete?1:new Promise(r=>{im.onload=im.onerror=r;})));});
  await new Promise(r=>setTimeout(r,300));
  await p.screenshot({path:OUT,type:"png",clip:{x:0,y:0,width:1080,height:1920}});
  await b.close();
  console.log("OK "+OUT);
})().catch(e=>{console.error(e);process.exit(1);});
