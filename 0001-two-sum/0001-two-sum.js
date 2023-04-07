/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let sums = {};
    for(let i = 0; i < nums.length; i++) {
        
        const diff = target - nums[i]
        if(diff in sums) {
            return [i, sums[diff]]
        }
        
        sums[nums[i]] = i
    }
};