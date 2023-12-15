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
const adjList = {
    1: [2, 5],
    2: [1, 3, 5],
    3: [2, 4],
    4: [3, 5, 6],
    5: [1, 2, 4],
    6: [4]
};
function printBreadthFirst(start) {
    const queue = new Array();
    queue.push(start);
    const visitedSet = new Set();
    visitedSet.add(start);
    while (queue.length > 0) {
        let node = queue.shift();
        console.log(node);
        //   for (let i = 0; i < adjList[node].length; i++) {
        //     let neighbor = adjList[node][i]
        //     if (!visitedSet.has(neighbor)){
        //       queue.push(neighbor)
        //       visitedSet.add(neighbor)
        //     }
        // }
        let numarray = adjList[node];
        numarray.forEach((neighbor) => {
            if (!visitedSet.has(neighbor)) {
                queue.push(neighbor);
                visitedSet.add(neighbor);
            }
        });
    }
}
console.log("First Test:");
printBreadthFirst(3); // Prints 1 through 6 in Breadth-first order, starting with 3
// One possible solution:  3, 2, 4, 1, 5, 6
console.log("Second Test:");
printBreadthFirst(6); // Prints 1 through 6 in Breadth-first order, starting with 6
// One possible solution:  6, 4, 3, 5, 2, 1
console.log("Third Test:");
printBreadthFirst(4); // Prints 1 through 6 in Breadth-first order, starting with 4
// One possible solution:  4, 3, 5, 6, 2, 1
