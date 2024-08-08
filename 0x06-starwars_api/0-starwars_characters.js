#!/usr/bin/node
// File executable path

const request = require('request');

const data = (ken, j) => {
  if (j === ken.length) return;
  request(ken[j], (error, response, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
      data(ken, j + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const data_char = JSON.parse(body).characters;
      data(data_char, 0);
    }
  }
);

