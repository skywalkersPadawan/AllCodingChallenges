function countOddNumbers(count) {
  const oddNumbers = [];
  for (let i = 1; i <= count * 2; i += 2) {
    oddNumbers.push(i);
  }
  return oddNumbers;
}

const oddCount = countOddNumbers(3);
console.log(countOddNumbers(oddCount));
