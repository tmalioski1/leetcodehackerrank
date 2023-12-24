"use strict";
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
// const age = (planet: string, seconds: number): number => {
//     interface Planet {
//         [key:string] : number
//     }
//     const planetRatios: Planet = {
//     mercury: 0.2408467,
//     venus: 0.61519726,
//     earth: 1,
//     mars: 1.8808158,
//     jupiter: 11.862615,
//     saturn: 29.447498,
//     uranus: 84.016846,
//     neptune: 164.79132
//     }
//    return Number((seconds/31557600/planetRatios[planet]).toFixed(2))
// }
// interface Player {
// }
// export class DnDCharacter {
//     public static generateAbilityScore(): number {
//       let sum: number;
//       do {
//         const diceValues: number[] = [];
//         for (let i = 0; i < 4; i++) {
//           diceValues.push(Math.floor(Math.random() * 6) + 1);
//         }
//         diceValues.sort((a, b) => b - a);
//         sum = diceValues[0] + diceValues[1] + diceValues[2];
//       } while (isNaN(sum));
//       return sum;
//     }
//     public static getModifierFor(abilityValue: number): number {
//       if (typeof abilityValue !== 'number' || isNaN(abilityValue)) {
//         return 0;
//       }
//       return Math.floor((abilityValue - 10) / 2);
//     }
//     public static generateCharacter(): { [key: string]: number } {
//       const abilities: string[] = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'];
//       const abilityScores: { [key: string]: number } = {};
//       for (const ability of abilities) {
//         abilityScores[ability] = this.generateAbilityScore();
//       }
//       const conModifier: number = this.getModifierFor(abilityScores['Constitution']);
//       const hitpoints: number = 10 + conModifier;
//       return {
//         'Strength': abilityScores['Strength'],
//         'Dexterity': abilityScores['Dexterity'],
//         'Constitution': abilityScores['Constitution'],
//         'Intelligence': abilityScores['Intelligence'],
//         'Wisdom': abilityScores['Wisdom'],
//         'Charisma': abilityScores['Charisma'],
//         'Constitution Modifier': conModifier,
//         'Hitpoints': hitpoints,
//       };
//     }
//   }
//   // Example usage:
//   const characterData = DnDCharacter.generateCharacter();
//   console.log(characterData);
// const counter = <T>(iterable: Iterable<T>): Record<string, number> => {
//   let count: Record<string, number> = {};
//   for (const item of iterable) {
//     const char = String(item); // Convert the item to a string
//     if (char !== undefined) {
//       if (count[char] !== undefined && count[char] >= 1) {
//         count[char] += 1;
//       } else {
//         count[char] = 1;
//       }
//     }
//   }
//   return count;
// };
//   const countCharacters = (words: string[], chars: string): Number => {
//     let total = 0;
//     let count = counter(chars);
//     console.log('count', count);
//     words.forEach((word) => {
//       let wordCount = counter(word);
//       console.log('wordCount', wordCount);
//       if (Array.from(word).every((char) => wordCount[char] <= count[char])) {
//         total += word.length;
//       }
//     });
//     return total;
//   };
//   console.log(countCharacters(["cat","bt","hat","tree"], 'atach'))
// const score = (x: number, y: number): number => {
//   const distance = Math.sqrt(x ** 2 + y ** 2)
//   if (distance <= 1) {
//     return 10
//   } else if (distance <= 5){
//     return 5
//   } else if (distance <= 10) {
//     return 1
//   } else {
//     return 0
//   }
// }
// const getLatestKRequests = (requests: string[], K: number): string[] => {
//   let seen = new Set()
//   let res = new Array()
//   for (let i = requests.length -1; i >= 0; i--) {
//     let req = requests[i]
//     console.log('this is the req', req)
//     if (!seen.has(req)) {
//       seen.add(req)
//       res.push(req)
//     }
//     if (res.length === K) {
//       break
//     }
//   }
//   return res
// }
// console.log(getLatestKRequests(['item3', 'item2', 'item1', 'item2', 'item3'], 4))
// const commonSubstring = (a: string[], b: string[]): void => {
//    for (let i = 0; i <a.length; i++) {
//     let elementA = a[i]
//     let elementB = b[i]
//     let foundCommonChar = false
//     for (let i = 0; i <elementA.length; i++) {
//       let char = elementA[i]
//       if (elementB.includes(char)) {
//         console.log('YES')
//         foundCommonChar= true
//         break
//       }
//     }
//     if (!foundCommonChar) {
//       console.log('NO')
//     }
//    }
// }
// commonSubstring(['hello', 'world'], ['he', 'bye'])
// const isPangram = (stringy: string): boolean => {
//     const newString = stringy.toLowerCase()
//     const alphabet = 'abcdefghijklmnopqrstuvwxyz'
//     for (let i = 0; i < alphabet.length; i++) {
//         let letter = alphabet[i]
//         if (!newString.includes(letter)) {
//             return false
//         }
//     }
//     return true
// }
// const isPangram = (stringy: string): boolean => {
//     return new Set(stringy.toLowerCase().replace(/[^a-z]/g, '')).size === 26
// }
// const onesMinusZeros = (grid: number[][]): number[][] => {
//     const ROWS = grid.length;
//     const COLS = grid[0].length;
//     let difference = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
//     let rowOnes = Array(ROWS).fill(0);
//     let colOnes = Array(COLS).fill(0);
//     for (let r = 0; r < ROWS; r++) {
//       for (let c = 0; c < COLS; c++) {
//         if (grid[r][c] === 1) {
//           rowOnes[r]++;
//           colOnes[c]++;
//         }
//       }
//     }
//     for (let r = 0; r < ROWS; r++) {
//       for (let c = 0; c < COLS; c++) {
//         difference[r][c] =
//           rowOnes[r] + colOnes[c] - (ROWS - rowOnes[r]) - (COLS - colOnes[c]);
//       }
//     }
//     return difference;
//   };
// console.log(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
// type AdjacencyList = {
//     [key in number]: number[];
// }
// const adjList: AdjacencyList = {
//     1: [2, 5],
//     2: [1, 3, 5],
//     3: [2, 4],
//     4: [3, 5, 6],
//     5: [1, 2, 4],
//     6: [4]
//   }
//   function printBreadthFirst(start: number):void {
//     const queue = new Array()
//     queue.push(start)
//     const visitedSet = new Set()
//     visitedSet.add(start)
//     while (queue.length > 0) {
//       let node = queue.shift()
//       console.log(node)
//     let numarray = adjList[node]
//     numarray.forEach((neighbor) => {
//         if (!visitedSet.has(neighbor)){
//             queue.push(neighbor)
//             visitedSet.add(neighbor)
//         }
//     })
//   }
//   }
//   console.log("First Test:")
//   printBreadthFirst(3); // Prints 1 through 6 in Breadth-first order, starting with 3
//                         // One possible solution:  3, 2, 4, 1, 5, 6
//   console.log("Second Test:")
//   printBreadthFirst(6); // Prints 1 through 6 in Breadth-first order, starting with 6
//                         // One possible solution:  6, 4, 3, 5, 2, 1
//   console.log("Third Test:")
//   printBreadthFirst(4); // Prints 1 through 6 in Breadth-first order, starting with 4
//                         // One possible solution:  4, 3, 5, 6, 2, 1
// const compressedString = (message: string): string => {
//   let newStr = '';
//   let seenLetter = '';
//   let count = 0;
//   for (let i = 0; i < message.length; i++) {
//     let letter = message[i];
//     if (letter != seenLetter) {
//       newStr += `${seenLetter}${count > 1 ? count : ''}`;
//       seenLetter = letter;
//       count = 1; // Reset count for the new letter
//     } else {
//       count += 1;
//     }
//     // Add the last letter and count after the last iteration of the loop
//     if (i === message.length - 1) {
//       newStr += `${seenLetter}${count > 1 ? count : ''}`;
//     }
//   }
//   return newStr;
// };
// console.log(compressedString('aabcccd')); // Output: 'a2b1c3d1'
// const minimumMoves = (arr1: number[], arr2: number[]):number => {
//   let count = 0
//   for (let i = 0; i < arr1.length; i++) {
//     let number1 = String(arr1[i])
//     let number2 = String(arr2[i])
//     for (let j = 0; j <number1.length; j++) {
//       let digit1 = Number(number1[j])
//       let digit2 = Number(number2[j])
//       if (digit1 === digit2) {
//         count += 0
//       } else {
//         count += Math.abs(digit1 - digit2)
//       }
//     }
//   }
//   return count
// }
// const arr1 = [123, 956]
// const arr2 = [224, 456]
// console.log(minimumMoves(arr1, arr2))
// const subsets = (nums: number[]): number[][] => {
//     const subsetArrays: number[][]= [];
//     const queue: [number[], number[]][] = [];
//     queue.push([[], nums]);
//     while (queue.length > 0) {
//     let currentVars: [number[], number[]] = queue.shift()!;
//     let currentSubset: number[] = currentVars[0];
//     let remainingNums: number[] = currentVars[1];
//     subsetArrays.push(currentSubset);
//       for (let i = 0; i < remainingNums.length; i++) {
//         queue.push([currentSubset.concat(remainingNums[i]), remainingNums.slice(i + 1)]);
//       }
//     }
//     return subsetArrays;
//   };
// const nums = [1, 2, 3];
// const result = subsets(nums);
// console.log(result);
const sum = (array) => {
    let total = 0;
    array.forEach((number) => {
        total += number;
    });
    return total;
};
class DesktopDirectory {
    constructor() {
        this.config = {
            default: {
                encoding: 'utf-8',
                permissions: 'drw-rw-rw-',
            }
        };
    }
    addFile(name) {
        console.log(`Adding file: ${name}`);
    }
    showPreview(name) {
        console.log(`Opening preview of file: ${name}`);
    }
}
const Desktop = new DesktopDirectory();
console.log(Desktop.config);
