const str1="object oriented programming";
const str2="abstraction polymorphism inheritace encapsulation"
const str3="software development life cycle"
const str4="  global   information tracher   "

function acronymize(str){
    var acronymize=str[0];
    var i=0;
    while(i<str.length-1){
        if(str[i]==" "){
            acronymize+=str[i+1];
        }
        i++;
        acronymize=acronymize.trim();
    }
    
    
    return (acronymize.toUpperCase());
}
console.log(acronymize(str1));
console.log(acronymize(str2));
console.log(acronymize(str3));
console.log(acronymize(str4));