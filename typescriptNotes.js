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
const hey = (message) => {
    let lastChar = message[message.length - 1];
    if (message === message.toUpperCase()) {
        return 'Whoa, chill out!';
    }
    else if (lastChar === '?') {
        return 'Sure.';
    }
    else if (message === '') {
        return 'Fine. Be that way!';
    }
    else {
        return 'Whatever.';
    }
};
console.log(hey('Tom-ay-to, tom-aaaah-to.'));
console.log(hey('WATCH OUT!'));
console.log(!isNaN(5));
