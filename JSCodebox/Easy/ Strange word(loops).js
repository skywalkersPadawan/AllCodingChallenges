function strangeWord(word) {
  let result = '';
  for (let i = 0; i < word.ngth; i = i + 2) {
    result = result + word[i];
  }

  // now return the result string that contains the 2nd letter
  // of the input string
  return result;
}

const word = strangeWord('thisisalongstringfortest');
console.log(word);
