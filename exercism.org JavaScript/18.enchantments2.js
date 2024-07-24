export function cardTypeCheck(stack, card) {
  let counter = 0;
  stack.forEach(item => {
    if (item === card) {
      counter += 1;
    }
  });
  return counter;
}

export function determineOddEvenCards(stack, type) {
  let counter = 0;
  for (const num of stack) {
    if (type === true) {
      if (num % 2 === 0) counter += 1;
    }
    else {
      if (num % 2 !== 0) counter += 1;
    }
  }
  return counter
}