

// function decodedResistorValue(colorsArray: string[]): string {
//   const numsArray = colorsArray.map((color) => Colors.indexOf(color))
//   const firstTwoNums = numsArray[0] * 10 + numsArray[1]
//   const thirdNum = numsArray[2]
//   let nums = firstTwoNums;
//   if (thirdNum === 0) {
//     nums = firstTwoNums
//     return `${nums} ohms`
//   }
//   for (let i = 1; i < Colors.length; i++) {
//     nums = nums*10
//     let color = Colors[i]
//     if (thirdNum === Colors.indexOf(color)) {
//       break
//     }
//   }
//   if (nums < 1000) {
//   return `${nums} ohms`
//   }
//   else if (nums >= 1000 && nums < 1000000) {
//     let kiloNums = nums / 1000
//     return `${kiloNums} kiloohms`
//   }
//   else if (nums >= 1000000 && nums < 1000000000) {
//     let megaNums = nums / 1000000
//     return `${megaNums} megaohms`
//   }
//   let gigaNums = nums / 1000000000
//   return `${gigaNums} gigaohms`

//   }



// const Colors: string[]= ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

// console.log(decodedResistorValue(['orange', 'orange', 'black']))
// console.log(decodedResistorValue(['blue', 'grey', 'brown']))
// console.log(decodedResistorValue(['red', 'black', 'red']))
// console.log(decodedResistorValue(['green', 'brown', 'orange']))
// console.log(decodedResistorValue(['yellow', 'violet', 'yellow']))
// console.log(decodedResistorValue(['blue', 'violet', 'blue']))
// console.log(decodedResistorValue(['black', 'black', 'black']))
// console.log(decodedResistorValue(['white', 'white', 'white']))
// console.log(decodedResistorValue(['black', 'grey', 'black']))

// const isLeap = (year: number): boolean => {
//     if (year % 4 === 0 && (year % 100 != 0 || (year % 100 === 0 && year % 400 === 0))) {
//         return true
//     }
//     return false
// }

// console.log(isLeap(2015))
// console.log(isLeap(1970))
// console.log(isLeap(1996))
// console.log(isLeap(1960))
// console.log(isLeap(2100))
// console.log(isLeap(1900))
// console.log(isLeap(2000))
// console.log(isLeap(2400))
// console.log(isLeap(1800))


// const toRNA = (nucleotide: string): string => {
//     let newString = '';
//     for (let i = 0; i < nucleotide.length; i++) {
//         let char = nucleotide[i];
//         console.log('char', char);
//         if (char == 'C') {
//             newString += 'G';
//         } else if (char == 'G') {
//             newString += 'C';
//         } else if (char == 'A') {
//             newString += 'U';
//         } else if (char == 'T') {
//             newString += 'A';
//         } else {
//             throw new Error('Invalid input DNA.');
//         }
//     }
//     return newString;
// };

// console.log(toRNA('C'))
