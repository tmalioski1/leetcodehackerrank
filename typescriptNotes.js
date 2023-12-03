"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Colors = exports.decodedValue = void 0;
function greet(name) {
    console.log(`Hello, ${name}!`);
}
greet("TypeScript");
function decodedValue(colors) {
    let abbreviatedColors = colors.splice(0, 2);
    let colorNumArray = [];
    for (let i = 0; i < abbreviatedColors.length; i++) {
        let color = abbreviatedColors[i];
        console.log('this is the color---', color);
        let colorNum = exports.Colors.indexOf(color);
        console.log('this is the colorNum', colorNum);
        colorNumArray.push(colorNum);
    }
    let colorString = colorNumArray.join('');
    let finalNum = Number(colorString);
    return finalNum;
}
exports.decodedValue = decodedValue;
exports.Colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'];
console.log(decodedValue(['brown', 'red', 'white']));
