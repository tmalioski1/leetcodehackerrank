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


function maxColumn(matrix) {
  const height = matrix.length;
  const width = matrix[0].length;

  const maxColumns = [];
  for (let col = 0 ; col < width ; col++) {
    let colMax = matrix[0][col];
    for (let row = 1 ; row < height ; row++) {
        if (matrix[row][col] > colMax) {
            colMax = matrix[row][col];
        }
    }
    maxColumns.push(colMax);
  }


  return maxColumns;
}

matrix = [[ 5,  9, 21],
          [ 9, 19,  6],
          [12, 14, 15]]


console.log(maxColumn(matrix)); // [12, 19, 21]
