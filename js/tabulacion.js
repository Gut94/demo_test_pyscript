
//para hacer tab dentro de textarea https://stackoverflow.com/questions/6637341/use-tab-to-indent-in-textarea
//añade 4 espacios en la tabulacion para python

document.getElementById('codeTextarea1').addEventListener('keydown', function(e) {    
    if (e.key == 'Tab') {
      e.preventDefault();
      var start = this.selectionStart;
      var end = this.selectionEnd;
  
      // set textarea value to: text before caret + tab + text after caret
      this.value = this.value.substring(0, start) +
        "    " + this.value.substring(end);
  
      // put caret at right position again
      this.selectionStart =
        this.selectionEnd = start + 4;
    }
  });





