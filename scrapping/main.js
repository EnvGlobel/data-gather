const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.setViewport({
    width: 2000,
    height: 2000,
    deviceScaleFactor: 1,
  });
  await page.goto('https://www.google.com/maps/@4.6528093,-74.0863529,13z/data=!5m1!1e1');
  await page.screenshot({path: 'screenshot.png'});
  await browser.close();
})();