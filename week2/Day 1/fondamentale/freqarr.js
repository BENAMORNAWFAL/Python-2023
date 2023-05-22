const arr1=["a","a","a"]
const expected1={"a":3}
function makefrequencyTable(arr){
    var expected={}
    for(var i=0;i<arr.length;i++){
            if(expected.hasOwnProperty(arr[i])){
                expected[arr[i]]++;
            }else{
                expected[arr[i]]=1;
            }
    }    
    return expected
}


console.log(makefrequencyTable(arr1))