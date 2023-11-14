#!/usr/bin/node
const squareSize = Math.floor(Number(process.argv[2]));
if (isNaN(SquareSize)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < squareSize; r++) {
    let row = '';
    for (let c = 0; c < squareSize; c++) row += 'X';
    console.log(row);
  }
}
