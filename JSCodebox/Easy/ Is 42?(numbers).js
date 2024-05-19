function is42(a, b) {
  // combine the conditions for better readability
  if (a === 42 || b === 42 || a + b === 42) {
    return true;
  } else return false;
}

const result = is42(41, 0);
console.log(result);
