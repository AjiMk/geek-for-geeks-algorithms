/**
 * Reverse the given array 
 * 
 * @param {*} arr 
 */
function reverseArray(arr) {
    if(arr.length===0) {
        return -1;
    }

    let revArr = [];

    for(let i=arr.length-1;i>=0;i--) {
        revArr.push(arr[i]);
    }

    return revArr;
}

console.log(reverseArray([1,2,3,4,5,6]))