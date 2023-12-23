// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
    switch (name) {
      case 'Pure Strawberry Joy':
        return 0.5;
      case 'Energizer':
        return 1.5;
      case 'Green Garden':
        return 1.5;
      case 'Tropical Island':
        return 3;
      case 'All or Nothing':
        return 5;
      default:
        return 2.5;
    }
  }
  
  /**
   * Calculates the number of limes that need to be cut
   * to reach a certain supply.
   *
   * @param {number} wedgesNeeded
   * @param {string[]} limes
   * @returns {number} number of limes cut
   */
  export function limesToCut(wedgesNeeded, limes) {
    if (wedgesNeeded === 0) return 0;
    let count = 0;
    let how_many = 0;
    let index = 0;
    while ((count <= wedgesNeeded) && (index < limes.length)) {
      switch (limes[index]) {
      case 'small':
        count = count + 6;
        break;
      case 'medium':
        count = count + 8;
        break;
      case 'large':
        count = count + 10;
        break;
      }
      index++;
      how_many++;  
    }
    return how_many
  }
  
  /**
   * Determines which juices still need to be prepared after the end of the shift.
   *
   * @param {number} timeLeft
   * @param {string[]} orders
   * @returns {string[]} remaining orders after the time is up
   */
  export function remainingOrders(timeLeft, orders) {
    let pendings = [];
    let index = 0;
    while ((timeLeft > 0 ) && (index < orders.length)) {
      timeLeft = timeLeft - timeToMixJuice(orders[index])
      index++;
    }
    while (index < orders.length) {
      pendings.push(orders[index]);
      index++;
    }
    return pendings;
  }