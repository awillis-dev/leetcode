/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
    // check length of s, return false if odd
    if(s.length % 2 !== 0) {
        return false
    }
    
    // create stack var
    let stack = []
    
    // loop through string
        // push all opening brackets onto new stack
        // check all closing bracket cases: if char is a closing bracket, stack isnt empty, and stack contains corresponding opening bracket, pop. else: return false. return true if stack length = 0
        for(let char of s) {
        
        if(char === '(' || char === '[' || char === '{') {
            stack.push(char)
        }
        
        else if ( (char === ')' && stack.length !== 0 && stack[stack.length-1] === '(') || 
            (char === ']' && stack.length !== 0 && stack[stack.length-1] === '[') ||
            (char === '}' && stack.length !== 0 && stack[stack.length-1] === '{') ) {
            stack.pop()
        } else {
            return false
        }
    }
    
    return stack.length === 0
};