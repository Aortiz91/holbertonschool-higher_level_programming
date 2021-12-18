#!/usr/bin/node
const lista = require('./100-data.js').list;
console.log(lista);
const mapnew = lista.map((x, index) => x * index);
console.log(mapnew);
