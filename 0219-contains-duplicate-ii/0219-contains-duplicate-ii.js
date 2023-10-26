/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
      let dupes = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in dupes) {
      if (Math.abs(i - dupes[nums[i]]) <= k) {
        return true;
      }
    }
    dupes[nums[i]] = i;
  }

  return false;
};

