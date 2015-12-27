var express = require('express');
var app = express();
var promise = require('bluebird');
var pgp = require('pg-promise')({
    promiseLib: promise
});

var cn = {
    host: 'localhost', // server name or IP address;
    port: 5432,
    database: 'pto_tracker',
    user: 'pto_tracker',
    password: '26fbb64a0c95fa83b69585c11610543e'
};

var db = pgp(cn);

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.get('/write', function (req, res) {
  var random = getRandomInt(1, 1000);
  db.none("insert into team(manager_id, name) values($1, $2)", [random, "Team: " + random])
    .then(function () {
      // success;
      res.send('written!');
    })
    .catch(function (error) {
      res.send(error);
    });
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});