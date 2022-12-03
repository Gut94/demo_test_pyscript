#import asyncio
from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document
from io import StringIO
import time
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
    resultadoBool = condicion1() and condicion2()
    return resultadoBool

def condicion1():                           #comprueba tipo
    condicion1Bool = (type(resultCode) is int)
    return condicion1Bool

def condicion2():                           #comprueba resultado
    condicion2Bool = (resultCode == 4)
    return condicion2Bool



def imprimePorHTML():
    print('hola')
    resultadoTextArea1 = document.getElementById("resultadoTextarea1")
    #resultadoTextArea1.select()
    resultadoTextArea1.innerHTML = resultCode
    condicionesBool = evaluaCodigo()
    print('resultado a comprobar',resultCode)
    if condicionesBool:              
        print('Resultado correcto')         #print devulelve el salto de linea por defecto 
        document.getElementById("resultadoTextarea1").style.backgroundColor = "#90EE90"     #green
        document.getElementById("alertas").style.display = 'flex'
        document.getElementById("alertaCorrecto").style.display = 'block'
        document.getElementById("alertaError").style.display = 'none'
    else:
        print('Resultado incorrecto')
        document.getElementById("resultadoTextarea1").style.backgroundColor = "#ffcccb"     #red
        document.getElementById("alertas").style.display = 'flex'
        document.getElementById("alertaCorrecto").style.display = 'none'
        document.getElementById("alertaError").style.display = 'block'



def getstrCode():
    return document.getElementById("codeTextarea1").value


def button_click(event):                    #crear antes de create_proxy
    execCodigo()
    imprimePorHTML()
    


click_proxy = create_proxy(button_click)
#document.getElementById("buttonRun").addEventListener("click", click_proxy)
e = document.getElementById("buttonRun")
e.addEventListener("click", click_proxy)
