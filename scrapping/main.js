const puppeteer = require("puppeteer");

takeScreenshot = async (date) => {
  const browser = await puppeteer.launch({
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });
  const page = await browser.newPage();
  await page.setViewport({
    width: 2000,
    height: 2000,
    deviceScaleFactor: 1,
  });
  await page.goto(
    "https://www.google.com/maps/@4.6528093,-74.0863529,13z/data=!5m1!1e1"
  );
  await page.screenshot({ path: `screenshot/${date}.png` });
  await browser.close();
};
takeCurrentScreenshot = () => {
  const now = new Date();
  var timestamp =
    now.getFullYear() +
    "_" +
    now.getMonth() +
    "_" +
    now.getDate() +
    "_" +
    now.getHours() +
    "_" +
    now.getMinutes();
  takeScreenshot(timestamp);
};
takeCurrentScreenshot();
setInterval(takeCurrentScreenshot, 600000);
