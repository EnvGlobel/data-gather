const fetch = require("node-fetch");
const fs = require("fs");

const fetch_retry = (url, n) =>
  fetch(url)
    .then((response) => {
      if (response.status >= 400 && response.status < 600) {
        throw new Error(`Bad response from server at ${url}`);
      }
      return response;
    })
    .catch((error) => {
      if (n === 1) throw error;
      return fetch_retry(url, n - 1);
    });

getPollutionData = async (timestamp) => {
  const stations = 12;
  for (let id = 0; id < stations; id++) {
    getPollutionDataForId(timestamp, id + 1);
  }
};

getPollutionDataForId = async (timestamp, id) => {
  const retries = 10;
  await fetch_retry(
    `http://iboca.ambientebogota.gov.co/iboca/service/stationHistoricalHours/${id}`,
    retries
  )
    .then((response) => response.text())
    .then((data) => {
      const dir = `pollution/${id}`;
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir);
      }
      fs.writeFileSync(`${dir}/${timestamp}.json`, data);
    })
    .catch((err) => console.log(err));
};

module.exports = getPollutionData;
