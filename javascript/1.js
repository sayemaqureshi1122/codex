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

//Q3] write a function that returns the largest number in an array.

function findlargest(arr){
    for( let i = 0; i < arr.length; i++){
        for( let j = 0; j < arr.length; j++){
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

///orrrrr
function largest(arr){
    let large = -Infinity; // or arr[0], any number that is smaller than all the no. in the arr.
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > large){
            large = arr[i]
        }
    }
    return large;
}
let arr = [1, 3, 5, 7, 0,  9, 5, 8, 11];
let ans = largest(arr);
console.log(ans);

//Q4 write a function that returns the smallest element in an array.
function smallest(arr){
    let small = arr[0]; // or arr[0], any number that is smaller than all the no. in the arr.
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < small){
            small = arr[i]
        }
    }
    return small;
}
let arr = [1, 3, 5, 7, 9, 5, 8, 11, -2, -1, -9, -8];
let ans = smallest(arr);
console.log(ans);

// Q4] write the function to return the second largest element in an array.
function second_largest(arr){
    for(let i = 0; i < arr.length; i++){
        for(let j = 0; j < arr.length; j++){
            if(arr[j]< arr[j+1]){
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }

        }
    }
    return arr;
}
let arr = [1, 2, 5, 8, 11, -3, -6, 5, 3, 7];
let ans = second_largest(arr);
console.log(ans[1]);

function second_largest(arr){
    let large = 0;
    let second_large = 0;
    for(let i = 0; i <arr.length; i++){
        if(arr[i] > large){
            large = arr[i];
        }
    }
    for(let j = 0; j <arr.length; j++){
        if(arr[j] < large && arr[j] > second_large){
            second_large = arr[j];

        }
    }
    return(large, second_large); 
}
let arr = [1, 4, 6, 3, 7, 50, 34, 88, 3];
let ans = second_largest(arr);
console.log(ans);
*/
function second_largest(arr){
    let large = 0;
    let second_large = 0;
    for(let i = 0; i <arr.length; i++){
        if(arr[i] > large){
            large = arr[i];
        }
    }
    for(let j = 0; j < arr.length; j++){
        if(arr[j] != large && arr[j] > second_large){   
            second_large = arr[j];
        }
    } 
    return(large, second_large);
}
let arr = [1, 4, 6, 3, 7, 50, 34, 88, 3];
let ans = second_largest(arr);
console.log(ans);
