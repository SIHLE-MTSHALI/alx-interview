#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body).name);
      });
    });
  };

  Promise.all(characters.map(fetchCharacter))
    .then(names => names.forEach(name => console.log(name)))
    .catch(error => console.error('Error:', error));
});
