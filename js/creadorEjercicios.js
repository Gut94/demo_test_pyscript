var clickedButtonCount = 0;
var strCode = '';
var resultadoTextAreaEx = document.getElementById("resultadoTextareaEx");

function getStringCodeFromHTML(){
    strCode = document.getElementById("codeTextareaEx").value;
    console.log(strCode);
}

function clickedButtonPlus(){
    if (clickedButtonCount<5){
        clickedButtonCount++;
    }
    
}

function clickedButtonMinus(){
    if (clickedButtonCount>0){
        clickedButtonCount--;
    }
}


function showEnd(){
    document.getElementById("buttonModify").style.display = 'none';
}

function showText(){
    resultadoTextAreaEx.innerHTML = strCode;
    document.getElementById("codeTextareaExDiv").style.display = 'none';
    document.getElementById("resultadoTextareaExDiv").style.display = 'flex';
    document.getElementById("buttonSection1").style.display = 'none';
    document.getElementById("inputSection1").style.display = 'flex';
    document.getElementById("buttonSection2").style.display = 'block';
    
}

function showNext(){
    document.getElementById("buttonFinish").style.display = 'inline';
    document.getElementById("buttonModify").innerHTML = "Seguir Modificando"
    
    
}

function showPrevious(){
    if (clickedButtonCount<2){
        document.getElementById("buttonModify").innerHTML = "Modificar";
    }
    if (clickedButtonCount<5){
        document.getElementById("buttonModify").style.display = 'inline';
    }
}

function showStart(){
    document.getElementById("codeTextareaExDiv").style.display = 'flex';
    document.getElementById("resultadoTextareaExDiv").style.display = 'none';
    document.getElementById("buttonSection1").style.display = 'block';
    document.getElementById("inputSection1").style.display = 'none';
    document.getElementById("buttonSection2").style.display = 'none';
    document.getElementById("buttonModify").innerHTML = "Modificar";

}

function createNewInputID(id){
    //strInputID = `string text ${expression} string text`;
    var strInputID = `<input type="text" id=${id}>`;
    return strInputID;
}

function modifyStrCode(){
    var strKey = document.getElementById("deleteInput").value;
    console.log(strKey);
    let regex = new RegExp(strKey, "gi");                   //Crea una expresion regular con lo pasado por input
    let count = (strCode.match(regex) || []).length;        //cuenta las ocurrencias
    console.log(strKey);
    var strCodeMod = strCode;
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
    clickedButtonMinus()
    if (clickedButtonCount==0){
        showStart();
    }else{
        showPrevious();
    }
    console.log(clickedButtonCount);
});

var buttonReturn = document.getElementById("buttonModify");
buttonReturn.addEventListener("click", function(event){
    modifyStrCode();
    clickedButtonPlus()
    if (clickedButtonCount==1){
        showNext();
    }else if (clickedButtonCount==5){
        showEnd();
    }
    console.log(clickedButtonCount);
});