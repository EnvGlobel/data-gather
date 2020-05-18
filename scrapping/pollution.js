const fetch = require("node-fetch");
const fs = require("fs");

getPollutionData = async (timestamp) => {
  const stations = 12;
  for (let id = 0; id < stations; id++) {
    getPollutionDataForId(timestamp, id);
  }
};

getPollutionDataForId = async (timestamp, id) => {
  await fetch(
    `http://iboca.ambientebogota.gov.co/iboca/service/stationHistoricalHours/${id}`
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
