const str1="creature";
const str2="dog";
const str3="hello";
const str4="";


function reverseString(str){
    var expected="";
    for(var i=str.length-1;i>=0;i--){
        expected=expected+str[i];
    }
    console.log(expected)
}
reverseString(str1);
reverseString(str2);
reverseString(str3);
reverseString(str4);