function bugFixFinal(string) {
  return string.replaceAll('bug', 'flower');
}

const result = bugFixFinal(
  'the word bug will be replaced with the word flower'
);
console.log(result);
