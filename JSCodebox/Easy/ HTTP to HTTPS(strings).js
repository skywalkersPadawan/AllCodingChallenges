function http2https(url) {
  return url.replaceAll('http', 'https');
}

const result = http2https('http://jscodebox.com/');
console.log(result);

// the code is working as intended and this is the end of the code control instruction syntax
