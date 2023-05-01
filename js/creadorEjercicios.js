let clickedButtonCount = 0;     //usado para conocer las distintas palabras clave a ocultar del código
let strCode;
let strCodeModed;
let resultadoTextAreaEx = document.getElementById("resultadoTextareaEx");
let stringKeysState = [];

function getStringCodeFromHTML(){
    strCode = document.getElementById("codeTextareaEx").value;
    strCodeModed = strCode;
    console.log(strCode);
}

function clickedButtonPlus(){
    if (clickedButtonCount<6){
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
    }else if (clickedButtonCount<6){
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
    let strInputID = `<input type="text" class="strKey${clickedButtonCount}">`;    //TODO id + clickedButtonCount para no repetir ids
    return strInputID;
}



function modifyStrCodeAdd(){
    console.log("clickedButtonCount"+clickedButtonCount);

    let strKey = document.getElementById("deleteInput").value;
    console.log(strKey);

    let regex = new RegExp(strKey, "gi");                   //Crea una expresion regular con lo pasado por input
    let count = (strCode.match(regex) || []).length;        //cuenta las ocurrencias
    console.log(strKey);
    let strCodeMod = strCodeModed;

    for (let i = 0; i < count; i++) {
        strCodeMod = strCodeMod.replace(strKey, createNewInputID(i));
    }
    strCodeModed = strCodeMod;
    saveState(strKey,count);
    resultadoTextAreaEx.innerHTML = strCodeMod;
    console.log(strCodeMod);
    console.log(count);
    console.log(JSON.stringify(stringKeysState));
}



function modifyStrCodeDelete(){
    getState();
}

function saveState(strKeyPassed,count){
    let JSONstringKeyState = {
        "id": clickedButtonCount,
        "value": strKeyPassed,
        "number": count
    };
    stringKeysState.push(JSONstringKeyState);
}

function getState(){

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


let buttonCreate = document.getElementById("buttonCreate");
buttonCreate.addEventListener("click", function(event){
    clickedButtonPlus()
    getStringCodeFromHTML();
    showText();
    pruebaDeGlobales();
});

let buttonReturn = document.getElementById("buttonReturn");
buttonReturn.addEventListener("click", function(event){
    modifyStrCodeDelete();
    clickedButtonMinus()
    if (clickedButtonCount==0){
        showStart();
    }else{
        showPrevious();
    }
    console.log(clickedButtonCount);
});

let buttonModify = document.getElementById("buttonModify");
buttonModify.addEventListener("click", function(event){
    modifyStrCodeAdd();
    clickedButtonPlus()
    if (clickedButtonCount==2){
        showNext();
    }else if (clickedButtonCount==6){
        showEnd();
    }
    console.log("clickedButtonCount"+clickedButtonCount);
});