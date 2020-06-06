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
  Usaquen: "32306271",
  LaUribe: "2322166312",
  Caobos: "32392451",
  LaIberia: "32127926",
  VillaMagdala: "32176221",
  PortalesDelNorte: "32368336",
  SanBenito: "13791491",
  ElSalitre: "32244696",
  Suba: "32274836",
  ElTambor: "32128031",
  Engativa: "32204001",
  FloresMonteVerde: "13793826",
  SantaMariaDeSube: "32205131",
  ChicoNorte: "32342616",
  EscuelaDeCaballeria: "13143941",
  SantaBarbaraCentral: "32119306",
  RinconDelChico: "32276601",
  Monaco: "32217881",
  BarriosUnidos: "32209671",
  SanMiguel: "32288021",
  Gaitan: "32387136",
  MinutoDeDios: "32144726",
  kennedy: "32170161",
  Torremolinos: "32071321",
  Teusaquillo: "32219226",
  CuidadUniversitaria: "32197146",
  RafaelUribe: "32193136",
  SantaIsabel: "32351911",
  Fontibon: "7594186",
  CiudadSalitre: "32203056",
  Bosa: "32122136",
  Brasilia: "32185726",
  CarlosAlban: "32354521",
  VillaAlsacia: "32084231",
  Mandalay: "32363636",
  CarvajalOsorio: "32369011",
  Tunjuelito: "32080846",
  SanVicenteFerrer: "32316806",
  Olaya: "32155516",
  Vergel: "32100366",
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
