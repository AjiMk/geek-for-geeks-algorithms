/**
 * Check sorted
 * 
 * @param {array} arr 
 */
function checkSorted(arr) {
    if(arr.length===0) {
        return -1;
    }

    let res = true;

    for(let i=1;i<arr.length;i++) {
        if(arr[i-1]>arr[i]) {
            res = false;
            break;
        }
    }

    return res;
}


console.log(checkSorted([1,2,3,4,5]))
console.log(checkSorted([10,2,3,4,5]))
