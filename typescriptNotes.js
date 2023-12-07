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
Object.defineProperty(exports, "__esModule", { value: true });
exports.DnDCharacter = void 0;
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
class DnDCharacter {
    static generateAbilityScore() {
        let sum;
        do {
            const diceValues = [];
            for (let i = 0; i < 4; i++) {
                diceValues.push(Math.floor(Math.random() * 6) + 1);
            }
            diceValues.sort((a, b) => b - a);
            sum = diceValues[0] + diceValues[1] + diceValues[2];
        } while (isNaN(sum));
        return sum;
    }
    static getModifierFor(abilityValue) {
        if (typeof abilityValue !== 'number' || isNaN(abilityValue)) {
            return 0;
        }
        return Math.floor((abilityValue - 10) / 2);
    }
    static generateCharacter() {
        const abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma'];
        const abilityScores = {};
        for (const ability of abilities) {
            abilityScores[ability] = this.generateAbilityScore();
        }
        const conModifier = this.getModifierFor(abilityScores['Constitution']);
        const hitpoints = 10 + conModifier;
        return {
            'Strength': abilityScores['Strength'],
            'Dexterity': abilityScores['Dexterity'],
            'Constitution': abilityScores['Constitution'],
            'Intelligence': abilityScores['Intelligence'],
            'Wisdom': abilityScores['Wisdom'],
            'Charisma': abilityScores['Charisma'],
            'Constitution Modifier': conModifier,
            'Hitpoints': hitpoints,
        };
    }
}
exports.DnDCharacter = DnDCharacter;
// Example usage:
const characterData = DnDCharacter.generateCharacter();
console.log(characterData);
