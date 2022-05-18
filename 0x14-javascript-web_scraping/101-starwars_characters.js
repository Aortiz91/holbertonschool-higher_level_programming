#!/usr/bin/node

const axios = require('axios');
(async () => {
  try {
    const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`);
    for (const items of response.data.characters) {
      const char = await axios.get(items);
      console.log(char.data.name);
    }
  } catch (error) {
    console.error(error);
  }
})();
