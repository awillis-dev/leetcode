/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    
            
    // push open () to stack
    // if curr is closed() & stack isnt empty & last stack item is matching opening(), pop
    // return true if stack is empty
    
    if (s.length % 2 !== 0) {
        return false
    }
        
        
    let stack = []
    
    for (char of s) {
        
        if (char === '(' || char === '[' || char === '{') {
            stack.push(char)
        } 
        
        else if ((char === ')' && stack.length !== 0 && stack[stack.length-1] === '(') ||
                (char === ']' && stack.length !== 0 && stack[stack.length-1] === '[') ||
                (char === '}' && stack.length !== 0 && stack[stack.length-1] === '{')) {
                stack.pop()           
        } else {
            return false
        }
        
    }
    
    return stack.length === 0

};