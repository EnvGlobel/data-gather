const puppeteer = require("puppeteer");
const weather = require("./weather");

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

takeWeatherData = async (timestamp) => {
  await weather(timestamp);
};

getTimestamp = () => {
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
  return timestamp;
};

takeCurrentScreenshot = () => {
  var timestamp = getTimestamp();
  takeScreenshot(timestamp);
};

takeCurrentWeatherData = () => {
  var timestamp = getTimestamp();
  takeWeatherData(timestamp);
};

takeCurrentScreenshot();
setInterval(takeCurrentScreenshot, 600000);
takeCurrentWeatherData();
setInterval(takeCurrentWeatherData, 3600000);
