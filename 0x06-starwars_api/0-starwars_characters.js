#!/usr/bin/node

const fetch = require('node-fetch');

async function starwarMovieChar(movieId) {
  try {
    const response = await fetch(`https://swapi.dev/api/films/${movieId}/`);
    const data = await response.json();
    const urlsChar = data.characters;

    for (const url of urlsChar) {
      const responseChar = await fetch(url);
      const data = await responseChar.json();
      console.log(data.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

const id = process.argv[2];
if (!id) {
  console.log('Usage: node script.js <movie_id>');
} else {
  starwarMovieChar(id);
}
