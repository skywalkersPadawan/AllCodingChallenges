function more4than0(n) {
  let countForFour = 0;
  let countForZero = 0;
  for (const num of n) {
    if (num === 4) {
      countForFour++;
    } else if (num === 0) {
      countForZero++;
    }
  }

  // check if the count of 4 is greater than the count of 0 and both
  // counts are positive
  return countForFour > countForZero;
}

const arrayOne = [1, 4, 1, 1, 4];
const result = more4than0(arrayOne);
console.log(result);
