

function getStringCodeFromHTML(){
    strCode = document.getElementById("codeTextareaEx").value;
    console.log(strCode);
}

function showText(){
    resultadoTextAreaEx = document.getElementById("resultadoTextareaEx");
    resultadoTextAreaEx.innerHTML = strCode;
    document.getElementById("codeTextareaExDiv").style.display = 'none';
    document.getElementById("resultadoTextareaExDiv").style.display = 'flex';
    document.getElementById("buttonSection1").style.display = 'none';
    document.getElementById("inputSection1").style.display = 'flex';
    document.getElementById("buttonSection2").style.display = 'block';
    
}

function showPrevious(){
    document.getElementById("codeTextareaExDiv").style.display = 'flex';
    document.getElementById("resultadoTextareaExDiv").style.display = 'none';
    document.getElementById("buttonSection1").style.display = 'block';
    document.getElementById("inputSection1").style.display = 'none';
    document.getElementById("buttonSection2").style.display = 'none';

}

function createNewInputID(id){
    //strInputID = `string text ${expression} string text`;
    strInputID = `<input type="text" id=${id}></input>`;
    return strInputID;
}

function modifyStrCode(){
    strKey = document.getElementById("deleteInput").value;
    console.log(strKey);
    let regex = new RegExp(strKey, "gi");                   //Crea una expresion regular con lo pasado por input
    let count = (strCode.match(regex) || []).length;        //cuenta las ocurrencias
    console.log(strKey);
    strCodeMod = strCode;
    for (let i = 0; i < count; i++) {
        strCodeMod = strCodeMod.replace(strKey, createNewInputID(i))
    }
    console.log(strCodeMod);
    resultadoTextAreaEx.innerHTML = strCodeMod;
    console.log(count);
}

function pruebaDeGlobales(){
    console.log(strCode);
}


/* function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}
  
  function replaceAll(str, find, replace) {
    return str.replace(new RegExp(escapeRegExp(find), 'g'), replace);
} */


var buttonCreate = document.getElementById("buttonCreate");
buttonCreate.addEventListener("click", function(event){
    getStringCodeFromHTML();
    showText();
    pruebaDeGlobales();
});

var buttonReturn = document.getElementById("buttonReturn");
buttonReturn.addEventListener("click", function(event){
    showPrevious();
});

var buttonReturn = document.getElementById("buttonModify");
buttonReturn.addEventListener("click", function(event){
    modifyStrCode();
});