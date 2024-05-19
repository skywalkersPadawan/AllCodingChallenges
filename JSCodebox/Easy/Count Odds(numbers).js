function countOdds(numbers) {
  let oddCount = 0;
  for (const number of numbers) {
    if (number % 2 !== 0) {
      oddCount++; // here we will increment the counter if the number is odd
    }
  }

  return oddCount;
}

const numbers = [0, 1, 2, 3, 4, 5, 6, 7];
const result = countOdds(numbers);
console.log(result);
