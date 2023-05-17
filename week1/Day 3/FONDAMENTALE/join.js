const arr1=[1, 2, 3];
 
function join(arr,separator){
    var joined="";
    if(!arr.length){
        return joined;
    }
    for(var i=0;i<arr.length-1;i++){
        joined+=arr[i]+separator;
    }
    return joined+arr[arr.length-1]
}
separator1=', ';
console.log(join(arr1,separator1));
separator2='-';
console.log(join(arr1,separator2));
separator3=' - ';
console.log(join(arr1,separator3));
const arr4=[1];
separator4=',  ';
console.log(join(arr4,separator4));
const arr5=[];
separator5=', ';
console.log(join(arr5,separator5));