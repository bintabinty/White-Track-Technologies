
// 1. Print numbers from 1 to 10

console.log("Program 1: Numbers from 1 to 10");

for (let i = 1; i <= 10; i++) {
    console.log(i);
}


// 2. Print numbers from 10 to 1

console.log("Program 2: Numbers from 10 to 1");

for (let i = 10; i >= 1; i--) {
    console.log(i);
}


// 3. Print even numbers from 2 to 20

console.log("Program 3: Even Numbers");

for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}


// 4. Print odd numbers from 1 to 15

console.log("Program 4: Odd Numbers");

for (let i = 1; i <= 15; i += 2) {
    console.log(i);
}


// 5. Calculate the sum of numbers from 1 to 10

console.log("Program 5: Sum of Numbers");

let sum = 0;

for (let i = 1; i <= 10; i++) {
    sum = sum + i;
}

console.log("Sum =", sum);
