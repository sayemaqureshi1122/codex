/*
//Q1] write a function that searches an element in an array and returns the index and if the element is not present return -1.
function search(arr, element) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == element) {
            return(i);
        }
    }
    return -1;
}
let arr = [1, 3, 7, 43, 45, 2, 8];
let res = search(arr, 45);
console.log(res);

//Q2] write a function that return the number of negative numbers in an array.
function countnegative(arr){
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            sum++;
        }
    }
    return sum;
}

let arr = [1, -4, 5, -5, -7, -9, 0, -3];
let ans = countnegative(arr);
console.log(ans);
*/
//Q3] write a function that returns the largest number in an array.

function findlargest(arr){
    for( let i = 0; i < arr.length; i++){
        for( let j = 0; j < arr. length; j++){
            if(arr[j] > arr[j+1]){
                let stack = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = stack;
            }
        }
    }
    return arr;
}
let arr = [1, 4, 5, 8, 7];
let ans = findlargest(arr);
console.log(ans);