/**
 * Find the second largest element in the array
 * 
 * @param {*} arr 
 */
function findSecondLargestElement(arr) {
    /**
     * TODO: find the largest element and do a second iteration to find the second largest element
     */
    if(arr.length==0) {
        return -1;
    }

    let maxIndex = 0;
    let secondMax = 0;

    for(let i=0;i<arr.length;i++) {
        if(arr[i]>arr[maxIndex]) {
            maxIndex = i;
        }
    }

    for(let j=0;j<arr.length;j++) {
        if(arr[j]>arr[secondMax] && arr[j]!=arr[maxIndex]) {
            secondMax = j;
        }
    }

    if(maxIndex===secondMax) {
        return -1;
    }

    return secondMax;
}

console.log(findSecondLargestElement([10,20,300,100,2,3,21,99]))
console.log(findSecondLargestElement([10,10,10]))