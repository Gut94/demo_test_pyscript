let clickedButtonCount = 0;     //usado para conocer las distintas palabras clave a ocultar del código
let strCode;
let strCodeModed;
let strCodeRecovery;
let resultadoTextAreaEx = document.getElementById("resultadoTextareaEx");
let stringKeysState = [];
let strCodeState = [];
let strCodeRecoveryState = [];
let flagDirection = true;

function getStringCodeFromHTML(){
    strCode = document.getElementById("codeTextareaEx").value;
    strCodeModed = strCode;
    strCodeRecovery = strCode;
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

function stringKeyRecovery(){
    //strInputID = `string text ${expression} string text`;
    let strKeyRecovery = `strKey${clickedButtonCount}`;    
    return strKeyRecovery;
}



function modifyStrCodeAdd(){
    console.log("clickedButtonCount"+clickedButtonCount);

    let strKey = document.getElementById("deleteInput").value;
    console.log(strKey);

    let regex = new RegExp("\\b"+strKey+"\\b", "gi");                   //Crea una expresion regular con lo pasado por input (solo palabras completas, varias a la vez, case-insensitive)
    let count = (strCode.match(regex) || []).length;                    //cuenta las ocurrencias
    console.log(strKey);
    let strCodeMod = strCodeModed;

    for (let i = 0; i < count; i++) {
        strCodeMod = strCodeMod.replace(regex, createNewInputID(i));
        strCodeRecovery = strCodeRecovery.replace(regex,  stringKeyRecovery());
    }
    strCodeModed = strCodeMod;
    saveState(strKey,count);
    resultadoTextAreaEx.innerHTML = strCodeModed;
    console.log(strCodeMod);
    console.log(count);
    console.log(JSON.stringify(stringKeysState));
    console.log(strCodeRecovery);
}



function modifyStrCodeDelete(){
    getState();
    resultadoTextAreaEx.innerHTML = strCodeModed;
    console.log(strCodeModed);
    console.log(JSON.stringify(stringKeysState));
    console.log(strCodeRecovery);
}

function saveState(strKeyPassed,count){
    let JSONstringKeyState = {
        "id": clickedButtonCount,
        "value": strKeyPassed,
        "number": count
    };
    stringKeysState.push(JSONstringKeyState);
    strCodeState.push(strCodeModed);
    strCodeRecoveryState.push(strCodeRecovery);
}

function getState(){
    
    if (clickedButtonCount==2){
        strCodeModed = strCode;
        strCodeRecovery = strCode;
    }else{
        if (flagDirection){
            stringKeysState.pop();
            strCodeRecoveryState.pop();
            strCodeRecovery = strCodeRecoveryState.pop();
            strCodeState.pop();
            strCodeModed = strCodeState.pop();
        }else{
            stringKeysState.pop();
            strCodeRecovery = strCodeRecoveryState.pop();
            strCodeModed = strCodeState.pop();
        }
        
    }
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
    console.log("Create"+clickedButtonCount);
});

let buttonReturn = document.getElementById("buttonReturn");
buttonReturn.addEventListener("click", function(event){
    modifyStrCodeDelete();          //primero se modificará y despues se actualiza el contador, las cuentas van por delante
    clickedButtonMinus()
    if (clickedButtonCount==0){
        showStart();
    }else{
        showPrevious();
    }
    flagDirection = false;
    console.log("clickedButtonCount"+clickedButtonCount);
    console.log("Return"+clickedButtonCount);
});

let buttonModify = document.getElementById("buttonModify");
buttonModify.addEventListener("click", function(event){
    modifyStrCodeAdd();             //primero se modificará y despues se actualiza el contador, las cuentas van por detras
    clickedButtonPlus()
    if (clickedButtonCount==2){
        showNext();
    }else if (clickedButtonCount==6){
        showEnd();
    }
    flagDirection = true;
    console.log("clickedButtonCount"+clickedButtonCount);
    console.log("Modify"+clickedButtonCount);
    
});


let buttonFinish = document.getElementById("buttonFinish");
buttonFinish.addEventListener("click", function(event){
    console.log("Finish"+clickedButtonCount);
    window.location.href="/index.html";
});