/**
 * Reverse array
 * 
 * Time complexity theta(n/2)
 * 
 * @param {*} arr 
 */
function reverseArray(arr) {

    let low = 0;
    let high = arr.length-1;

    while(low<high) {
        let temp = arr[low]

        // swap
        arr[low] = arr[high]
        arr[high] = temp

        high-=1
        low+=1
    }

    return arr;
}

console.log(reverseArray([1,2,3,4,5]))