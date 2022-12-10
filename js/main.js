
//para hacer tab dentro de textarea https://stackoverflow.com/questions/6637341/use-tab-to-indent-in-textarea
//no identa bien para python

document.getElementById('codeTextarea1').addEventListener('keydown', function(e) {    
    if (e.key == 'Tab') {
      e.preventDefault();
      var start = this.selectionStart;
      var end = this.selectionEnd;
  
      // set textarea value to: text before caret + tab + text after caret
      this.value = this.value.substring(0, start) +
        "\t" + this.value.substring(end);
  
      // put caret at right position again
      this.selectionStart =
        this.selectionEnd = start + 1;
    }
  });




/* var strCode = "Prueba";

function getStringCodeFromHTML(){
    strCode = document.getElementById("codeTextarea1").value;
    console.log(strCode);
} */

/* function pruebaDeGlobales(){
    console.log(strCode);
} */

/* function getstrCode(){
    return strCode;
}

const element = document.getElementById("buttonRun");
element.addEventListener("click", function(){
    getStringCodeFromHTML()
    pruebaDeGlobales()
 });

console.log(strCode); */

//alert("Prueba desde js")



