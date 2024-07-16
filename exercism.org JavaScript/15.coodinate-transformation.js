
export function translate2d(dx, dy) {
  return function(dz,dw) {
    return [dx+dz, dy+dw]
  }
}


export function scale2d(sx, sy) {
  return function(dz,dw) {
    return [sx*dz, sy*dw]
  }
}


export function composeTransform(f, g) {
  return function(x, y) {
    const [fx, fy] = f(x, y);
    return g(fx, fy);
  };
}


export function memoizeTransform(transform) {
    let lastArgs;
    let lastResult;

    return function(x, y) {
        const currentArgs = [x, y];
        if (!lastArgs || !arraysEqual(lastArgs, currentArgs)) {
            lastArgs = currentArgs;
            lastResult = transform(x, y);
        }
        return lastResult;
    };
}
export function arraysEqual(arr1, arr2) {
    return arr1.length === arr2.length && arr1.every((val, index) => val === arr2[index]);
}