const str1="a3b2c1d3"

function decoderstr(str){
    var expected=""
    for(var i=0;i<str.length-1;i++){
        var j=i-1
        x=parseInt(str[i])
        if(x==isNaN()){
            expected+=str[i]
        }else{
          
            expected+=toString(str[j].repeat(x))
        }
    }
    return expected
}

console.log(decoderstr(str1))