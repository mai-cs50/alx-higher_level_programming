#!/usr/bin/node
// script that concats 2 files

const args = process.argv.slice(2);
const file = require('fs');
const contentA = file.readfileSync(args[0] + 'utf8');
const contentB = file.readfileSync(args[1] + 'utf8');
file.writefileSync(args[2], contentA + contentB);
