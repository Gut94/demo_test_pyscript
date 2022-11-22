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
    resultCode = x                          #sacamos la variable que queremos del codigo pasado a exec
    print('x',resultCode)
    

def evaluaCodigo():
    print('resultado a comprobar',resultCode)
    if condicionesNecesarias(resultCode):              
        print('Resultado correcto')         #print devulelve el salto de linea por defecto 
    else:
        print('Resultado incorrecto')

def condicionesNecesarias(resultCode):      #comprobamos tipo y resultado
    return ((type(resultCode) is int) and (resultCode == 4))

def button_click(event):                    #crear antes de create_proxy
 execCodigo()
 evaluaCodigo()

click_proxy = create_proxy(button_click)
#document.getElementById("buttonRun").addEventListener("click", click_proxy)
e = document.getElementById("buttonRun")
e.addEventListener("click", click_proxy)