/**
 * Find the second largest number
 * 
 * @param {*} arr 
 */
function findTheSecondLargest(arr) {
    if(arr.length==0) {
        return -1;
    }

    let res = -1;
    let largest = 0;

    for(let i=0;i<arr.length;i++) {
        /**
         * Updating the first and second largest numbers
         * 
         */
        if(arr[i]>=arr[largest]) {
            res = largest;
            largest = i;
        }else{
            /**
             * if res===-1: update the second largest number as i
             * if arr[i]<=arr[res]: ignore
             * if arr[i]>arr[res]: update the res
             * 
             */
            if(res===-1|| arr[i]>arr[res]) {
                res = i; 
            }
        }
    }

    return res;
}

console.log(findTheSecondLargest([9,20,12,13,4,2,100,10]))

