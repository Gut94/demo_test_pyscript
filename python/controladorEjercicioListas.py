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
    stringCodeMod = 'global lista\n'+stringCode   #pyodide necesita declarar global la variable que usamos?
    exec(stringCodeMod)
    resultCode = lista                          #variable a sacar del codigo pasado a exec
    console.log('lista',resultCode)
    


def evaluaCodigo():                         #comprueba tipo y resultado
    resultadoBool = condicion1() and condicion2()
    return resultadoBool

def condicion1():                           #comprueba tipo
    condicion1Bool = (type(resultCode) is list)
    return condicion1Bool

def condicion2():                           #comprueba resultado
    listaSolucion = [1, 2, 3, 4, 5]
    condicion2Bool = (resultCode == listaSolucion)
    return condicion2Bool



def imprimePorHTML():
    console.log('hola')
    resultadoTextArea1 = document.getElementById("resultadoTextarea1")
    #resultadoTextArea1.select()
    resultadoTextArea1.value = resultCode
    condicionesBool = evaluaCodigo()
    console.log('resultado a comprobar',resultCode)
    if condicionesBool:                             #print() falla de momento https://github.com/pyscript/pyscript/issues/230 https://github.com/pyscript/pyscript/issues/472
        console.log('Resultado correcto')           #print() devulelve el salto de linea por defecto, inserta directamente elementos html en modificador.py, usar console.log() de javascript
        document.getElementById("resultadoTextarea1").style.backgroundColor = "#90EE90"     #green
        document.getElementById("alertas").style.display = 'flex'
        document.getElementById("alertaCorrecto").style.display = 'block'
        document.getElementById("alertaError").style.display = 'none'
    else:
        console.log('Resultado incorrecto')
        document.getElementById("resultadoTextarea1").style.backgroundColor = "#ffcccb"     #red
        if not condicion1():
           document.getElementById("alertError").innerHTML = "No se está devolviendo una lista"
        elif condicion1() and not condicion2():
            document.getElementById("alertError").innerHTML = "Resultado incorrecto"

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
