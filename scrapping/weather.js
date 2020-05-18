const fetch = require("node-fetch");
const fs = require("fs");

points = {
  Bogota: "2132226",
  ElListon: "32349921",
  Paloquemao: "32132246",
  Ricaurte: "32201116",
  MariscalSucre: "32180376",
  LosMartires: "32313241",
  LaPepita: "32329021",
  Estanzuela: "32218516",
  AlcaldiaMayor: "32275346",
  SedeNCun: "32216996",
  SedeJCun: "32301661",
  Cedritos: "32155981",
};

getWeatherData = async (timestamp) => {
  Object.keys(points).forEach((item) => {
    getWeatherDataForId(timestamp, item);
  });
};

getWeatherDataForId = async (timestamp, id) => {
  getEndpointDataForId(timestamp, id, "forecast");
  getEndpointDataForId(timestamp, id, "meteogram");
};

getEndpointDataForId = async (timestamp, id, endpoint) => {
  await fetch(`https://meteobox.co/json/${endpoint}/2-${points[id]}-es.json`)
    .then((response) => response.text())
    .then((data) => {
      const dir = `${endpoint}/${id}`;
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir);
      }
      fs.writeFileSync(`${dir}/${timestamp}.json`, data);
    })
    .catch((err) => console.log(err));
};

module.exports = getWeatherData;
