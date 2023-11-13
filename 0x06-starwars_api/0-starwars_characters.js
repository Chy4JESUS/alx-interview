#!/usr/bin/node

function ordered (characters, i) {
  if (i >= characters.length) {
    return;
  }
  request(characters[i], function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      const person = JSON.parse(body);
      console.log(person.name);
      return ordered(characters, ++i);
    } else {
      console.log('error ocurred, Status code: ' + response.statusCode);
    }
  });
}

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const num = process.argv[2];
request(url + num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonified = JSON.parse(body);
    ordered(jsonified.characters, 0);
  } else {
    console.log('error ocurred, Status code: ' + response.statusCode);
  }
});
