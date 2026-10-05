// bits and pieces

function debounce(fn, ms) {
  let t;
  return (...a) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...a), ms);
  };
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

console.log(typeof sleep);
