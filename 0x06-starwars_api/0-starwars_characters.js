#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request(
  `https://swapi-api.alx-tools.com/api/films/${id}/`,
  async function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const peopleEndPoints = JSON.parse(body).characters;

      for (const endPoint of peopleEndPoints) {
        request(endPoint, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            console.log(JSON.parse(body).name);
          } else {
            console.log(error);
          }
        });
      }
    } else {
      console.error('Error:', error);
    }
  }
);
