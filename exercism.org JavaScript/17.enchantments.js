
export function getCardPosition(stack, card) {
  return (stack.indexOf(card));
}


export function doesStackIncludeCard(stack, card) {
  return (stack.includes(card));
}


export function isEachCardEven(stack) {
  return (stack.every((num) => num % 2 === 0));
}


export function doesStackIncludeOddCard(stack) {
  return (stack.some((num) => num % 2 !== 0));
}


export function getFirstOddCard(stack) {
  return (stack.find((num) => num % 2 !== 0));
}


export function getFirstEvenCardPosition(stack) {
  return (stack.findIndex((num) => num % 2 === 0));
}