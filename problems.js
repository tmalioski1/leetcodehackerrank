// const getPrintedStrings = (arrays) => {
//     let printedStrings = []
//     let cursorPosition = 0
//     let word = ''
//     arrays.forEach((array) => {
//         let command = array[0]
//         let value = array[1]
//         if (command == 'Insert'){
//             word = value
//             cursorPosition += value.length
//         }
//         else if (command == 'Left') {
//             let left = Number(value)
//             cursorPosition -= left
//             if (cursorPosition < 0){
//                 cursorPosition = 0
//             }
//         }
//         else if (command == 'Delete') {
//             let deleteHere = Number(value)
//             if (deleteHere < word.length - cursorPosition){
//                 word = word.slice(0, cursorPosition) + word.slice(cursorPosition + deleteHere, word.length)
//             }
//             else {
//                 word = word.slice(0, cursorPosition)
//             }
//         }
//         else if (command == 'Right') {
//             let right = Number(value)
//             cursorPosition += right
//         }
//         else if (command == 'Backspace'){
//            let backSpace = Number(value)
//            if (backSpace < cursorPosition){
//             word = word.slice(0, cursorPosition - backSpace) + word.slice(cursorPosition, word.length)
//             cursorPosition -= backSpace
//            }
//         }
//         else{
//             printedVal = Number(value)
//             if (cursorPosition > printedVal){
//                 appendedWord = word.slice(cursorPosition - printedVal, cursorPosition + printedVal)
//             }
//             else {
//                 appendedWord= word
//             }
//             printedStrings.push(appendedWord)
//             cursorPosition = 0
//         }
//     })
//     return printedStrings

// }


// const twoDArray = [['Insert', 'hello'], ['Left', '3'], ['Delete', '1'], ['Right', '2'], ['Backspace', '1'], ['Print', '4'],['Insert', 'goodbye'], ['Print', '7']]

// console.log(getPrintedStrings(twoDArray))



// let word = 'hello'
// let deleteHere = Number('1')
// let cursorPosition = 2
// word = word.slice(0, cursorPosition) + word.slice(cursorPosition + deleteHere, word.length)
// console.log('word---', word)



// Given an integer array nums, find the subarray with the largest sum, and return its sum.

// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Explanation: The subarray [1] has the largest sum 1.
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23
// Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
//Set up an outer loop to iterate through each number in the array//
//At each number, set up an inner loop, that adds up the total sum of the values of each number in the array, popping the last value in the array off each time//
// function greatestSub(nums) {
//     let maxSum = 0;

//     for (let i = 0; i <= nums.length - 1; i++) {
//       let copyNums = [...nums]

//       while (copyNums.length > 0) {
//         let sum = 0;

//         for (let j = copyNums.length - 1; j >= 0; j--) {
//           let num = copyNums[j];
//           sum += num;
//         }

//         if (sum > maxSum) {
//           maxSum = sum;
//         }

//         copyNums.pop();
//       }
//     }

//     return maxSum;
//   }
// const nums = [5,4,-1,7,8]
// console.log(greatestSub(nums))

class ListNode {
  constructor(val) {
      this.val = val;
      this.next = null;
  }
}

// var mergeTwoLists = function(list1, list2) {
//   let dummy = new ListNode();
//   let current = dummy; // Use a current pointer to keep track of the current node in the merged list


//   while (list1 && list2) {
//       if (list1.val <= list2.val) {
//           current.next = list1; // Connect current to list1
//           list1 = list1.next;
//       } else {
//           current.next = list2; // Connect current to list2
//           list2 = list2.next;
//       }
//       current = current.next; // Move the current pointer to the newly added node
//   }

//   // After the loop, either list1 or list2 may have remaining elements
//   if (list1) {
//       current.next = list1; // Connect the remaining of list1
//   }
//   if (list2) {
//       current.next = list2; // Connect the remaining of list2
//   }

//   return dummy.next;
// };

// const node1 = new ListNode(1);
// const node2 = new ListNode(3);
// const node3 = new ListNode(5);

// node1.next = node2;
// node2.next = node3;

// const anotherNode1 = new ListNode(1);
// const anotherNode2 = new ListNode(2);
// const anotherNode3 = new ListNode(7);

// anotherNode1.next = anotherNode2;
// anotherNode2.next = anotherNode3;

// const mergedList = mergeTwoLists(node1, anotherNode1);

// // Print the linked list values
// let current = mergedList;
// while (current) {
//   console.log(current.val);
//   current = current.next;
// }


// function removeNthFromEnd(head, n) {
//   // Create a dummy node to handle edge cases
//   const dummy = new ListNode(0);
//   dummy.next = head;
//   let first = dummy;
//   let second = dummy;

//   // Move the first pointer n nodes ahead
//   for (let i = 0; i <= n; i++) {
//     first = first.next;
//     console.log('this is first', first)
//   }

//   // Move both pointers one node at a time until first reaches the end
//   while (first !== null) {
//     first = first.next;
//     console.log('this is second ', second)
//     second = second.next;
//     console.log('this is first again',first)
//     console.log('this is second again', second)
//   }

//   // Remove the nth node from the end
//   second.next = second.next.next;

//   // Return the head of the modified linked list
//   return dummy.next;
// }

// const node1 = new ListNode(1);
// const node2 = new ListNode(3);
// const node3 = new ListNode(5);

// node1.next = node2;
// node2.next = node3;

// const finalList = removeNthFromEnd(node1, 2)
// let current = finalList
// while (current) {
//   console.log(current.val);
//   current = current.next;
// }

















/*
 * Complete the 'getResponses' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts following parameters:
 *  1. STRING_ARRAY valid_auth_tokens
 *  2. 2D_STRING_ARRAY requests
 */

// function getResponses(valid_auth_tokens, requests) {
//     console.log('this is valid_auth', valid_auth_tokens)
//     console.log('requests', requests)
//     requests.forEach((request) => {
//         let requestCompare = request[1].split('=')[1]
//         let nextRequestCompare = requestCompare.split('&')[0]
//         if (valid_auth_tokens.includes(nextRequestCompare)) {
//             console.log('Valid', )
//         }
//         else{
//           console.log('INVALID')
//         }

//     })

// }

// const validAuthTokens = ["ah37j2ha483u",
// "safh34ywb0p5", "ba34wyi8t902"]
// const requests1 = [
//   ["GET", "https://example.com/?token=347sd6k8iu2&name=alex"],
//   ["GET", "https://example.com/?token=safh34vwb005&name=sam"],
//   ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
//   ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"]
// ]

// getResponses(validAuthTokens, requests1)


// const selfDividingNumber =  (left, right) => {
// let selfDivideArray = []
// for (let i = left; i <=right; i++) {
//   let stringNum = i.toString()
//   if (stringNum.includes('0')){
//     continue
//   }
//   let isSelfDividing = true
//   for (let j = 0; j < stringNum.length; j++) {
//     let digitChar = stringNum[j]
//     individualInt = Number(digitChar)
//     if (i % individualInt !=0) {
//       isSelfDividing= false
//       break
//     }
//   }
//   if (isSelfDividing) {
//     selfDivideArray.push(i)
//   }
// }
// return selfDivideArray
// }


// console.log(selfDividingNumber(1, 22))
// const twoDimensionalSum = function (arr) {
//   let sum = 0
//   for (let i = 0; i < arr.length; i++) {
//     let row = arr[i]
//     for (let j = 0; j < row.length; j++) {
//       sum += row[j]

//     }
//   }
//    return sum
// }
// let arr1 = [
//   [1, 3],
//   [-4, 7, 10],
//   [2]
// ];
// console.log(twoDimensionalSum(arr1)); // 19

// let arr2 = [
//   [],
//   [3, 1, 2],
// ];
// console.log(twoDimensionalSum(arr2)); // 6


// function maxColumn(matrix) {
//   const height = matrix.length;
//   const width = matrix[0].length;

//   const maxColumns = [];
//   for (let col = 0 ; col < width ; col++) {
//     let colMax = matrix[0][col];
//     for (let row = 1 ; row < height ; row++) {
//         if (matrix[row][col] > colMax) {
//             colMax = matrix[row][col];
//         }
//     }
//     maxColumns.push(colMax);
//   }


//   return maxColumns;
// }

// matrix = [[ 5,  9, 21],
//           [ 9, 19,  6],
//           [12, 14, 15]]


// console.log(maxColumn(matrix)); // [12, 19, 21]


// const zip = (arr1, arr2) => {
//   let twoDArray = [[arr1[0], arr2[0]]]
//   for (let i = 1; i <arr1.length; i++) {
//     let val1 = arr1[i]
//     let val2 = arr2[i]
//     twoDArray.push([val1, val2])
//   }
//   return twoDArray
// }

// console.log(zip([1, 2, 3, 4], ['eins', 'zwei', 'drei', 'vier']));
// // [ [ 1, 'eins' ], [ 2, 'zwei' ], [ 3, 'drei' ], [ 4, 'vier' ] ]

// console.log(zip(['eins', 'zwei', 'drei'], [1, 2, 3]));
// // [ [ 'eins', 1 ], [ 'zwei', 2 ], [ 'drei', 3 ] ]

// console.log(zip(['alef', 'bet'], ['alpha', 'beta']));
// // [ [ 'alef', 'alpha' ], [ 'bet', 'beta' ] ]

// const twoDimensionalSum = (arr) => {
//   let sum = 0
//   for (let i = 0; i < arr.length; i++) {
//     let subArray = arr[i]
//     for (let j = 0; j < subArray.length; j++){
//       sum += subArray[j]
//     }

//   }
//   return sum
// }
// let arr1 = [
//   [1, 3],
//   [-4, 7, 10],
//   [2]
// ];
// console.log(twoDimensionalSum(arr1)); // 19

// let arr2 = [
//   [],
//   [3, 1, 2],
// ];
// console.log(twoDimensionalSum(arr2)); // 6

// function luckyNumbers(matrix) {
//   const luckyNumbers = [];

//   for (let i = 0; i < matrix.length; i++) {
//       const minInRow = Math.min(...matrix[i]);

//       const columnIndex = matrix[i].indexOf(minInRow);

//       // Check if the current number is also the maximum in its column
//       if (matrix.every(row => row[columnIndex] <= minInRow)) {
//           luckyNumbers.push(minInRow);
//       }
//   }

//   return luckyNumbers;
// }

// matrix = [[ 5,  9, 21],
//           [ 9, 19,  6],
//           [12, 14, 15]]

// console.log(luckyNumbers(matrix)); // [12]

// matrix = [[ 5, 10,  8,  6],
//           [10,  2,  7,  9],
//           [21, 15, 19, 10]]

// console.log(luckyNumbers(matrix)); // [10]

// function spiralOrder(matrix) {
//   let firstRow = matrix[0]
//   let middleNumbers = middleRowAddition(matrix)
//   let lastRow = matrix[matrix.length -1].reverse()
//   let middleRow = matrix[1].splice(0, matrix[1].length -1)
//   return [...firstRow, ...middleNumbers, ...lastRow, ...middleRow]


// }

// function middleRowAddition(matrix) {
//   let middleRowMatrix = []
//   for (let i = 1; i <matrix.length -1; i++) {
//     let row = matrix[i]
//     let lastNum = row[row.length -1]
//     middleRowMatrix.push(lastNum)
//   }
//   return middleRowMatrix
// }


// matrix = [[ 1, 2, 3],
//           [ 4, 5, 6],
//           [ 7, 8, 9]]

// console.log(spiralOrder(matrix)); // [1,2,3,6,9,8,7,4,5]
// // console.log(middleRowAddition(matrix)); // [1,2,3,6,9,8,7,4,5]

// matrix = [[1, 2, 3, 4],
//           [5, 6, 7, 8],
//           [9,10,11,12]]


// console.log(spiralOrder(matrix)); // [1,2,3,4,8,12,11,10,9,5,6,7]
// // console.log(middleRowAddition(matrix)); // [1,2,3,4,8,12,11,10,9,5,6,7]

// const pyramidArray = (base) => {
//   let twoDArray = [base]
//   let baseCopy = base
//   while (baseCopy.length >= 2) {
//     baseCopy = addToSubtract(baseCopy);
//     twoDArray.push(baseCopy);
//   }
//   return twoDArray.reverse()
// }
// const addToSubtract = (arr) => {
//   let newArr= []
//   for (let i = 0; i < arr.length -1; i++) {
//     let num = arr[i]
//     let secondNum = arr[i+1]
//     newArr.push(num + secondNum)
//   }
//   return newArr
// }

// let p1 = pyramidArray([2, 3, 7, 5, 9]);
// console.log(p1);
// // [
// //   [ 85 ],
// //   [ 37, 48 ],
// //   [ 15, 22, 26 ],
// //   [ 5, 10, 12, 14 ],
// //   [ 2, 3, 7, 5, 9 ]
// // ]

// let p2 = pyramidArray([2, 2, 2, 2]);
// console.log(p2);
// // [
// //   [ 16 ],
// //   [ 8, 8 ],
// //   [ 4, 4, 4 ],
// //   [ 2, 2, 2, 2 ]
// // ]

// const getWinner = (arr, k) => {
//   if (k >= arr.length) {
//     return Math.max(...arr)
//   }
//   let wins = 0
//   let currWinner = arr[0]
//   let i = 1
//   while (wins < k && i < arr.length) {
//     const opponent = arr[i]
//     if (currWinner > opponent) {
//       wins++
//     }
//     else {
//       currWinner = opponent
//       wins = 1
//     }
//     i++
//     i %= arr.length
//   }
//   return currWinner
// }

// console.log(getWinner([2,1,3,5,4,6,7], 2))
// console.log(getWinner([3,2,1], 10))
// const invertTree = (root) => {
//   if (!root) {
//     return null
//   }
//   const queue = []
//   queue.push(root)
//   while (queue.length >0) {
//     let node = queue.shift()
//     let temp = node.left;
//     node.left = node.right;
//     node.right = temp;
//     if (node.left) {
//       queue.push(node.left)
//     }
//     if (node.right) {
//       queue.push(node.right)
//     }
//   }
//   return root
// }

// const counter = (word) => {
//   let count = {}
//   for (let i = 0; i <= word.length; i++) {
//     let char = word[i]
//     if (char !== undefined) {  // Skip undefined characters
//       if (count[char] >= 1) {
//         count[char] += 1
//       } else {
//         count[char] = 1
//       }
//     }
//   }
//   return count
// }


// const countCharacters = (words, chars) => {
//   let total = 0;
//   let count = counter(chars);
//   console.log('count', count);

//   words.forEach((word) => {
//     let wordCount = counter(word);
//     console.log('wordCount', wordCount);

//     if (Array.from(word).every((char) => wordCount[char] <= count[char])) {
//       total += word.length;
//     }
//   });

//   return total;
// };


// console.log(countCharacters(["cat","bt","hat","tree"], 'atach'))

// function TreeNode(val, left, right) {
//   this.val = (val===undefined ? 0 : val)
//    this.left = (left===undefined ? null : left)
//   this.right = (right===undefined ? null : right)
//   }
// f

// const levelOrder = (root) => {
//   if (!root) {
//     return [];
//   } else {
//     const queue = [root];
//     const orderList = [];

//     while (queue.length > 0) {
//       const levelSubArray = [];
//       const levelSize = queue.length;

//       for (let i = 0; i < levelSize; i++) {
//         let node = queue.shift();
//         levelSubArray.push(node.val);

//         if (node.left) {
//           queue.push(node.left);
//         }

//         if (node.right) {
//           queue.push(node.right);
//         }
//       }

//       orderList.push(levelSubArray);
//     }

//     return orderList;
//   }

// }

// const rightSideView = (root) => {
//   if (!root) {
//     return []
//   } else {
//     const queue = new Array()
//     queue.push(root)
//     const rightList = []

//     while (queue.length >0) {
//       let levelSize = queue.length

//       for (let i = 0; i < levelSize; i++) {
//         let node = queue.shift()

//         if (i === levelSize -1) {
//           rightList.push(node.val)
//         }

//         if (node.left != null) {
//           queue.push(node.left)
//         }

//         if (node.right != null) {
//           queue.push(node.right)
//         }
//       }


//     }
//     return rightList
//   }
// }


// const onesMinusZeros = (grid) => {
//   const ROWS = grid.length;
//   const COLS = grid[0].length;

//   let difference = Array.from({ length: ROWS }, () => Array(COLS).fill(0));

//   let rowOnes = Array(ROWS).fill(0);
//   let colOnes = Array(COLS).fill(0);

//   for (let r = 0; r < ROWS; r++) {
//     for (let c = 0; c < COLS; c++) {
//       if (grid[r][c] === 1) {
//         rowOnes[r]++;
//         colOnes[c]++;
//       }
//     }
//   }

//   for (let r = 0; r < ROWS; r++) {
//     for (let c = 0; c < COLS; c++) {
//       difference[r][c] =
//         rowOnes[r] + colOnes[c] - (ROWS - rowOnes[r]) - (COLS - colOnes[c]);
//     }
//   }

//   return difference;
// };


// console.log(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))

// const adjList = {
//   1: [2, 5],
//   2: [1, 3, 5],
//   3: [2, 4],
//   4: [3, 5, 6],
//   5: [1, 2, 4],
//   6: [4]
// }

// function printBreadthFirst(start) {
//   const queue = new Array()
//   queue.push(start)
//   const visitedSet = new Set()
//   visitedSet.add(start)

//   while (queue.length > 0) {
//     let node = queue.shift()
//     console.log(node)
//     for (let i = 0; i < adjList[node].length; i++) {
//       let neighbor = adjList[node][i]
//       if (!visitedSet.has(neighbor)){
//         queue.push(neighbor)
//         visitedSet.add(neighbor)
//       }

//   }

// }
// }

// console.log("First Test:")
// printBreadthFirst(3); // Prints 1 through 6 in Breadth-first order, starting with 3
                      // One possible solution:  3, 2, 4, 1, 5, 6
// console.log("Second Test:")
// printBreadthFirst(6); // Prints 1 through 6 in Breadth-first order, starting with 6
//                       // One possible solution:  6, 4, 3, 5, 2, 1
// console.log("Third Test:")
// printBreadthFirst(4); // Prints 1 through 6 in Breadth-first order, starting with 4
//                       // One possible solution:  4, 3, 5, 6, 2, 1


// const adjList = {
//   1: [2, 5],
//   2: [1, 3, 5],
//   3: [2, 4],
//   4: [3, 5, 6],
//   5: [1, 2, 4],
//   6: [4]
// }

// function printDepthFirst(start) {
//   const stack = new Array()
//   stack.push(start)
//   const visitedSet = new Set()
//   visitedSet.add(start)
//   const newArray = new Array()
//   while (stack.length > 0) {
//     let node = stack.pop()
//     console.log(node)
//     adjList[node].forEach((number) => {
//       if (!visitedSet.has(number)) {
//         stack.push(number)
//         visitedSet.add(number)
//       }
//     })
//   }

// }

// console.log("First Test:")
// printDepthFirst(3);


// const adjList = {
//   1: [2, 5],
//   2: [1, 3, 5],
//   3: [2, 4],
//   4: [3, 5, 6],
//   5: [1, 2, 4],
//   6: [4]
// }

// function printBreadthFirst(start) {
//   const queue = new Array()
//   queue.push(start)
//   const visitedSet = new Set()
//   visitedSet.add(start)
//   const newArray = new Array()

//   while (queue.length > 0) {
//     let node = queue.shift()
//     newArray.push(node)
//     for (let i = 0; i < adjList[node].length; i++) {
//       let neighbor = adjList[node][i]
//       if (!visitedSet.has(neighbor)){
//         queue.push(neighbor)
//         visitedSet.add(neighbor)
//       }

//   }
// }
// return newArray
// }

// console.log("First Test:")
// console.log(printBreadthFirst(3)); // Prints 1 through 6 in Breadth-first order, starting with 3
//                       // One possible solution:  3, 2, 4, 1, 5, 6


// const adjList = {
//   1: [2, 5],
//   2: [1, 3, 5],
//   3: [2, 4],
//   4: [3, 5],
//   5: [1, 2, 4],
//   6: []
// }

// function breadthFirstSearch(start, end) {
//   const queue = new Array()
//   queue.push(start)
//   const visitedSet = new Set()
//   visitedSet.add(start)

//   while (queue.length > 0) {
//     let node = queue.shift()

//     if (node === end) {
//       return true
//     } else {
//       adjList[node].forEach((number) => {
//         if (!visitedSet.has(number)) {
//           queue.push(number)
//           visitedSet.add(number)
//         }
//       })
//     }
//   }
// return false

// }

// console.log("First Test:");
// console.log(breadthFirstSearch(1, 3)); // -> true
// console.log("Second Test:");
// console.log(breadthFirstSearch(4, 1)); // -> true
// console.log("Third Test:");
// console.log(breadthFirstSearch(6, 1)); // -> false


// const adjList = {
//   1: [2, 5],
//   2: [1, 3, 5],
//   3: [2, 4],
//   4: [3, 5],
//   5: [1, 2, 4],
//   6: []
// }

// function aShortestPath(start, end) {
//   const queue = new Array()
//   queue.push([start])
//   const visitedSet = new Set()
//   visitedSet.add(start)

//   while (queue.length > 0) {
//     let path = queue.shift()
//     let lastNode = path[path.length -1]

//     if (lastNode === end) {
//       return path.length -1
//     } else {
//       adjList[lastNode].forEach((neighbor) => {
//         if (!visitedSet.has(neighbor)){
//           visitedSet.add(neighbor)
//           copyPath = [...path]
//           copyPath.push(neighbor)
//           queue.push(copyPath)
//         }
//       })
//     }
//   }
// return false
// }

// console.log("First Test:");
// console.log(aShortestPath(1, 3)); // -> [ 1, 2, 3 ] (One possible solution)
// console.log("Second Test:");
// console.log(aShortestPath(6,1))


const subsets = (nums) => {
  const subsetArrays = [];
  const queue = [];
  queue.push([[], nums]);

  while (queue.length > 0) {
    let currentVars = queue.shift();
    let currentSubset = currentVars[0];
    let remainingNums = currentVars[1];
    subsetArrays.push(currentSubset);

    for (let i = 0; i < remainingNums.length; i++) {
      queue.push([currentSubset.concat(remainingNums[i]), remainingNums.slice(i + 1)]);
    }
  }

  return subsetArrays;
};

const nums = [1, 2, 3];
const result = subsets(nums);
console.log(result);
