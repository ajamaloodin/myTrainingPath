/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */
export function cookingStatus(remainingTime) {
    if (remainingTime === 0) return 'Lasagna is done.';
    if (remainingTime === undefined) return 'You forgot to set the timer.'
    return 'Not done, please wait.'
  }
  
  export function preparationTime(layers, avPrepTime = 2) {
    return layers.length * avPrepTime;
  }
  
  export function quantities(layers) {
    const noodlesQ = 50 * layers.reduce((total,x) => total+(x=='noodles'), 0)
    const sauceQ = 0.2 * layers.reduce((total,x) => total+(x=='sauce'), 0)
    return {
      'noodles' : noodlesQ,
      'sauce'   : sauceQ
    }
  }
  
  export function addSecretIngredient(friendsList, myList) {
    myList.push(friendsList[friendsList.length - 1])
  }
  
  export function scaleRecipe(recipe, portions) {
    let result = structuredClone(recipe);
    for (let clave in result) {
      result[clave] = result[clave] * portions / 2;
    }
    return result;
  }
  