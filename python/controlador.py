#import asyncio
from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document, getstrCode
from io import StringIO
import sys

resultCode = 0

def execCodigo():
    global resultCode
    stringCode = getstrCode()
    stringCodeMod='global x\n'+stringCode   #pyodide necesita declarar global la variable que usamos?
    exec(stringCodeMod)
    resultCode = x                          #variable a sacar del codigo pasado a exec
    print('x',resultCode)
    

def evaluaCodigo():                         #comprueba tipo y resultado
    resultadoBool = ((type(resultCode) is int) and (resultCode == 4))
    return resultadoBool


def button_click(event):                    #crear antes de create_proxy
    execCodigo()
    resultadoBool = evaluaCodigo()
    print('resultado a comprobar',resultCode)
    if resultadoBool:              
        print('Resultado correcto')         #print devulelve el salto de linea por defecto 
    else:
        print('Resultado incorrecto')

click_proxy = create_proxy(button_click)
#document.getElementById("buttonRun").addEventListener("click", click_proxy)
e = document.getElementById("buttonRun")
e.addEventListener("click", click_proxy)