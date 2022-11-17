#import asyncio
from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document, getstrCode
from io import StringIO
import sys

resultCode = 0

def execCodigo():
    global resultCode
    stringCode = getstrCode()
    tmp = sys.stdout
    my_result = StringIO()
    sys.stdout = my_result
    exec(stringCode)
    sys.stdout = tmp
    resultCode = my_result.getvalue()
    print('VARIABLE:', my_result.getvalue())
    

def evaluaCodigo():
    print('resultado en comprueba',resultCode)
    if resultCode == '4\n':                 #print devulelve el salto de linea por defecto 
        print('Resultado correcto')
    else:
        print('Resultado incorrecto')


def button_click(event):                    #crear antes de create_proxy
 #alert(f"Prueba desde {getstrCode()}")
 execCodigo()
 evaluaCodigo()

click_proxy = create_proxy(button_click)
#document.getElementById("buttonRun").addEventListener("click", click_proxy)
e = document.getElementById("buttonRun")
e.addEventListener("click", click_proxy)