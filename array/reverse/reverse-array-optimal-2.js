/**
 * Reverse an array
 * 
 * @param {*} arr 
 */
function reverseArray(arr) {
    const n = arr.length;
    for(let i=0;i<Math.floor(n/2);i++) {
        const temp = arr[i];
        arr[i] = arr[n-1-i];
        arr[n-1-i] = temp;

    }

    return arr;
}

console.log(reverseArray([1,2,3,4,5]))
