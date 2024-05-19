function checkPassword(password, passwordRepeat) {
  console.log(password.length);
  if (password === passwordRepeat && password.length >= 20) {
    return Boolean(true);
  } else return Boolean(false);
}

const result = checkPassword(
  'this is the passworddgdf',
  'this is the passworddgdf'
);
console.log(result);
