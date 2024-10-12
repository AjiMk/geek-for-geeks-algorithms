
/**
 * Find the largest element in the array
 * 
 * @param {array} arr 
 */
function findTheLargest(arr) {
    if(arr.length===0) {
        return -1;
    }

    let maxIndex = 0;

    for(let i=0;i<arr.length;i++) {
        if(arr[i]>=arr[maxIndex]) {
            maxIndex = i;
        }
    }

    return maxIndex;
}


console.log(findTheLargest([100,2,200,10,12,20,3000]));