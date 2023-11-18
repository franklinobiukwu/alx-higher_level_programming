#!/usr/bin/node

/*  a script that concats 2 files */
const fs = require('fs');

const args = process.argv.slice(2, -1);
const destinationFile = process.argv.slice(-1)[0];

let content = '';
let fileProcessed = 0;

args.forEach((filePath) => {
  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      console.log('Error reading file', error);
      return;
    }
    content += data;
    fileProcessed++;
    if (fileProcessed === args.length) {
      fs.writeFile(destinationFile, content, 'utf8', (error) => {
        if (error) {
          console.log('Error writing to file', error);
        }
      });
    }
  });
});
