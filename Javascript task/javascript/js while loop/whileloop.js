
// 1. Print numbers from 1 to 10

console.log("Program 1: Numbers from 1 to 10");

let i = 1;

while (i <= 10) {
    console.log(i);
    i++;
}


// 2. Print numbers from 10 to 1

console.log("Program 2: Numbers from 10 to 1");

i = 10;

while (i >= 1) {
    console.log(i);
    i--;
}


// 3. Print even numbers from 2 to 20

console.log("Program 3: Even Numbers");

i = 2;

while (i <= 20) {
    console.log(i);
    i += 2;
}


// 4. Print odd numbers from 1 to 15

console.log("Program 4: Odd Numbers");

i = 1;

while (i <= 15) {
    console.log(i);
    i += 2;
}


// 5. Calculate the sum of numbers from 1 to 10

console.log("Program 5: Sum of Numbers");

i = 1;
let sum = 0;

while (i <= 10) {
    sum = sum + i;
    i++;
}

console.log("Sum =", sum);
