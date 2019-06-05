function primeFactorization(n) {
  // Divide out all even numbers
  while (n % 2 == 0) {
    console.log(2 + " ");
    n /= 2;
  }

  // Find all factors up to the n's square root
  for (var i = 3; i <= Math.sqrt(n); i += 2) {
    while (n % i == 0) {
      console.log(i + " ");
      n /= i;
    }
  }

  // Print out anything leftover
  if (n > 2) {
    console.log(n + " ");
  }
}

console.log(primeFactorization(600851475143));
