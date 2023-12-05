"use strict";
function decodedResistorValue(colorsArray) {
    const numsArray = colorsArray.map((color) => Colors.indexOf(color));
    const firstTwoNums = numsArray[0] * 10 + numsArray[1];
    const thirdNum = numsArray[2];
    let nums = firstTwoNums;
    if (thirdNum === 0) {
        nums = firstTwoNums;
        return `${nums} ohms`;
    }
    for (let i = 1; i < Colors.length; i++) {
        nums = nums * 10;
        let color = Colors[i];
        if (thirdNum === Colors.indexOf(color)) {
            break;
        }
    }
    if (nums < 1000) {
        return `${nums} ohms`;
    }
    else if (nums >= 1000 && nums < 1000000) {
        let kiloNums = nums / 1000;
        return `${kiloNums} kiloohms`;
    }
    else if (nums >= 1000000 && nums < 1000000000) {
        let megaNums = nums / 1000000;
        return `${megaNums} megaohms`;
    }
    let gigaNums = nums / 1000000000;
    return `${gigaNums} gigaohms`;
}
const Colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'];
console.log(decodedResistorValue(['orange', 'orange', 'black']));
console.log(decodedResistorValue(['blue', 'grey', 'brown']));
console.log(decodedResistorValue(['red', 'black', 'red']));
console.log(decodedResistorValue(['green', 'brown', 'orange']));
console.log(decodedResistorValue(['yellow', 'violet', 'yellow']));
console.log(decodedResistorValue(['blue', 'violet', 'blue']));
console.log(decodedResistorValue(['black', 'black', 'black']));
console.log(decodedResistorValue(['white', 'white', 'white']));
console.log(decodedResistorValue(['black', 'grey', 'black']));
console.log(decodedResistorValue(['blue', 'green', 'yellow', 'orange']));
