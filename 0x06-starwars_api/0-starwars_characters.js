#!/usr/bin/node

const request = require('request');

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        return reject(new Error('something went wrong'));
      }
      resolve(JSON.parse(body));
    });
  });
}

const id = process.argv[2];

async function fetchCharacterNames () {
  requestPromise(`https://swapi-api.alx-tools.com/api/films/${id}/`)
    .then((filmBody) => {
      const peopleEndPoints = filmBody.characters;

      let promiseChain = Promise.resolve();

      peopleEndPoints.forEach((endPoint) => {
        promiseChain = promiseChain
          .then(() => requestPromise(endPoint))
          .then((characterBody) => {
            console.log(characterBody.name);
          })
          .catch((error) => {
            console.error(error);
          });
      });
      return promiseChain;
    })
    .catch((error) => {
      console.error(error);
    });
}

fetchCharacterNames();
