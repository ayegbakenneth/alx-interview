#!/usr/bin/node

const request = require('request');

const data = (req, j) => {
  if (j === req.length) return;
  request(req[j], (error, response, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
      data(req, j + 1);
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
