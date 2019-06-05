function fibonacciSum(max) {
  var fibonacci = 0;
  var i = 0;
  var j = 1;
  var sum = 0;

  for (i = 0; fibonacci < max;){
    fibonacci = i + j;
    i = j;
    j = fibonacci;

    if ( fibonacci % 2 == 0 ) {
      sum += fibonacci;
    }
  }

  return sum;
}

console.log(fibonacciSum(4000000));
