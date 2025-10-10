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

// Q5] write the function to return the second largest element in an array.
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

let arr = [10, 20, 20];
let ans = second_largest(arr);
console.log(ans);
function second_largest(arr){
    let large = -Infinity;
    let second_large = -Infinity;
    if(arr.length < 2){
        return null;
    }
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > large){
            second_large = large;
            large = arr[i];
        }
        else if(arr[i] > second_large && arr[i] != large){   //agar ye condition nhi likhe to agar second-largest , largest ke baas hai to correct ans nhi dega.
            second_large = arr[i];
        }
    }
    return second_large;
}

//  printing pattern double loop
//Q1] for printing incementing pattern.
let n = 4;
for(let i = 0; i < n ; i++){
    let row = " ";
    for(let j = 0; j <= i; j++){ // j < i+1
        row += j+1;
        
    }
    console.log(row);
}

//Q2 print a right angle triangle.
n = 4;
for(let i = 0; i < n; i++){
    let row = ""
    for(let j = 0; j < i; j++){
        row += "*";

    }
    console.log(row);
}

//Q3 pattern - 1 22 333 4444
n = 5;
for(let i = 0; i < n; i++){
    let row = " "
    for(let j = 0; j <=i; j++){
        row +=i+1;
    }
    console.log(row);
}

//Q4]
let n = 3; 
for(let i = n; i >= 0; i--){
    let row = " ";
    for(let j = 0; j <= i; j++ ){
        row += j+1;
    }
    console.log(row);
}

//Q5]
let n = 4;
for(let i = 0; i < n ; i++){
    let row = " ";
    for(let j = 0; j < n-(i+1) ; j++){
        row +=" ";
    }
    for(let k = 0; k <i+1; k++){
        row +="*";
    }
    console.log(row);
}

//Q6,7
let n = 4;
for(let i = 0; i < n; i++){
    let row = " ", switch1 = 1;
    for(let j = 0; j <= i; j++){
        row += switch1; // Q6
        if(switch1 == 1){
            switch1 = 0;
        }
        else{
            switch1 = 1;
        }
        //row += switch1; // for Q7 uncomment this and comment the upper one
    }
console.log(row);
}

//Q8] 
let n = 4;
let num = 0;
for(let i = 0; i < n; i++){
    let row = " ";
    for(let j = 0; j <= i; j++){
        row += num; 
        num += 1;  
    }
    console.log(row);
   
}

// Q9]
let n = 4;
for(let i = 0; i < n; i++){
    let row = " ";
    for(let j = 0; j < n-i; j++){
        row +=" "; 
    }
    for(let k = 0; k < 2*i+1; k++){
        row +=k+1;
        
    }
    console.log(row);
}

//Q10]
let n = 4;
for(let i = 0;  i < n; i++){
    let row = " ";
    for(let j = 1; j <n -i; j++){
        row += " ";
    }
    for(let k = 0; k <= i ;k++){
        row += k+1;
    }
    for(let l = 0; l<i; l++){
        row +=(i-l);
    }
    console.log(row);
}

//Q11]
let n = 5;
for(let i = 0; i < n; i++){
    let row = " ";
    for(let j = 0; j < n; j++){
        if(i == 0 || i == n-1 || j == 0 || j == n-1){
                row += "*";
            }
        else{
            row += ".";
        }
    }
    console.log(row);
}

//Q12] ulta right angle triangle
let n = 5;
for(let i = 0; i < n; i++){
    let row = " ";
    for(let j = 1; j < n-i; j++){
                row += " ";
    }
    for(let k = 0; k <= i; k++){
        row += "*";
    }
    console.log(row);
}

//Q13] pura star triangle with space first
let n = 5;
for(let i = 0; i < n; i++){
    let row = " ";
    for(let j = 1; j < n-i; j++){
                row += " ";
    }
    for(let k = 0; k < 2*i-1; k++){
        row += "*";
    }
    console.log(row);
}

// Q14] write a function that return the number no digits in a number.
function digitcount(num){
    if(num == 0){
        return 1;
    }
    else if (num < 0){
        num  = -(num)
    }
    let count = 0;
    while(num > 0){
        num = Math.floor(num / 10); //ye ans me quotient deta hai
        count += 1;
    }
    return count;
}
let num = -983;
let res = digitcount(num);
console.log(res);
*/
//Q15] 1796. Second Largest Digit in a String
let s = "ab23456";
let digits = s.match(/\d/g);
let arr = digits.map(Number)

function second_largest(arr){
    let large = -Infinity;
    let second_large = -Infinity;
    if(arr.length < 2){
        return("not enough elements in an array");
    }
    for(let i = 0; i < arr.length;  i++){
        if(arr[i] > large){
            second_large = large;
            large = arr[i];
        }
        if(arr[i] > second_large && arr[i] != large){
            second_large = arr[i];
        }
    }
    return second_large;

}
res = second_largest(arr);
console.log(res);