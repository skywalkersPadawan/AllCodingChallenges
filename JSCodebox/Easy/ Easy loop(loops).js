function easyLoop() {
  //   let numberDivisibleBySeven = '';
  let result = '';
  for (let i = 0; i <= 99; i++) {
    if (i % 7 == 0) {
      result = result + i.toString();
    }
  }

  return result;
}

console.log(easyLoop());
