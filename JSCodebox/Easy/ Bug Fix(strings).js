function bugFix(string) {
  return string.replace('bug', 'flower');
}

const result = bugFix('the word bug will be replaced with the word flower');
console.log(result);
