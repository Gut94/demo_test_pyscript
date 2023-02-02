

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

function pruebaDeGlobales(){
    console.log(strCode);
}



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