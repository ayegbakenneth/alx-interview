#!/usr/bin/node

const request = require('request');

function retriveMovieChar(filmId) {
  const site = `https://swapi.dev/api/films/${filmId}/`;

  request(site, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Cant fetch the data');
      return;
    }

    const filmData = JSON.parse(body);
    const siteCharacter = filmData.characters;

    siteCharacter.forEach((siteCharacter) => {
      request(siteCharacter, (errorChar, responseChar, bodyChar) => {
        if (errorChar) {
          console.error('Error retriving character:', errorChar);
          return;
        }

        if (responseChar.statusCode !== 200) {
          console.error('Cannot retrieve character data');
          return;
        }

        const data = JSON.parse(bodyChar);
        console.log(data.name);
      });
    });
  });
}

const filmId = process.argv[2];
if (!filmId) {
  console.log('Usage: node script.js <film_id>');
} else {
  retriveMovieChar(filmId);
}
