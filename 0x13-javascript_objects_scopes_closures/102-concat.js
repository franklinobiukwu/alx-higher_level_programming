#!/usr/bin/node

/* Write a script that concats 2 files.
    * The first argument is the file path of the first source file
    * The second argument is the file path of the second source file
    * The third argument is the file path of the destination */

const fs = require('fs').promises;

const joinScripts = async (file1, file2, destination) => {
    try {
        const fileOneData = await fs.readFile(file1, 'utf-8');

        const fileTwoData = await fs.readFile(file2, 'utf-8');

        const fileThreeData = String(fileOneData) + String(fileTwoData);

        await fs.writeFile(destination, fileThreeData);

    } catch (error){
        console.error('Error: ', error.message)
    }
}

const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: node script.js file1 file2 destination');
  process.exit(1);
}

joinScripts(args[0], args[1], args[2]);
