/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let shuffled = [];
    let p1 = 0;
    let p2 = n;
    
    while(p1 < p2 && p2 < n*2) {
        shuffled.push(nums[p1]);
        shuffled.push(nums[p2]);
        p1++;
        p2++;
    }
    
    return shuffled;
};