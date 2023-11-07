/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let res = [];
    
    // res array where nums will be concatenated
    // loop through nums 
    for(let i=0; i < nums.length; i++) {
        res.push(nums[i])
    }
    
     for(let i=0; i < nums.length; i++) {
        res.push(nums[i])
    }
    
    return res;
};