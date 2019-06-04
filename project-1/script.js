function sum35(max) {
  var sum = 0;

  for (var i = 0; i < max; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }

  return sum;
}

console.log(sum35(1000));
