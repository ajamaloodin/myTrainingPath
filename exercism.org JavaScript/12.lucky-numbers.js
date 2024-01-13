// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
    const num1 = Number(array1.join(''));
    const num2 = Number(array2.join(''));
    return num1 + num2;
  }
  
  /**
   * Checks whether a number is a palindrome.
   *
   * @param {number} value
   * @returns {boolean} whether the number is a palindrome or not
   */
  export function luckyNumber(value) {
      const strNum = String(value);
      const len = strNum.length;
      let numOfLoops, pleft, pright = 0;
    
      if (len % 2 === 0){
        if (strNum[len/2 -1] !== strNum[len/2]){
          return false;
        }
        numOfLoops = len - len/2 - 1;
        pleft  = len/2 - 2;
        pright = len/2 + 1;
      } 
      else {
        numOfLoops = Math.trunc(len - Math.trunc(len/2) - 1);
        pleft  = Math.trunc(len/2 - 1);
        pright = Math.trunc(len/2 + 1);
      }
      
      while (numOfLoops > 0){
          if (strNum[pleft] !== strNum[pright]) return false;
          numOfLoops--;
          pleft--;
          pright++;
        }
      return true;
      
    }
  
  /**
   * Determines the error message that should be shown to the user
   * for the given input value.
   * @returns {string} error message
   */
  export function errorMessage(input) {
    if (input === '') return 'Required field';
    if (input === null) return 'Required field';
    if (input === undefined) return 'Required field';
    if (isNaN(input) || (Number(input) === 0)) return 'Must be a number besides 0';
    return '';
  }