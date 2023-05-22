const str1= "a x a"
const str2= "racecar"
const str3="Dud"
const str4="ohox"
expected=Boolean
function palind(str){
    
    for(var i=0;i>str.length-1;i++){
        if(str[i]!=str[str.length-1-i]){
            return false          
        }
    }
    return true
    
}

console.log("str is palindrome? ",palind())