#import asyncio
from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document
from io import StringIO
import time
import sys
import pandas as pd
import matplotlib.pyplot as plt

resultCode = 0
resultFig = 0



def execCodigo():
    global resultCode
    global fig
    stringCode = getstrCode()
    stringCodeMod=stringCode                #pyodide necesita declarar global la variable que usamos? 'global x\n'+stringCode
    exec(stringCodeMod, globals())          #es exec quien necesita añadir las globales
    resultCode = df                         #variable a sacar del codigo pasado a exec
    resultFig = fig
    console.log('x',resultCode)
    


def evaluaCodigo():                         #comprueba tipo y resultado
    resultadoBool = condicion1() and condicion2()
    return resultadoBool

def condicion1():                           #comprueba tipo
    #condicion1Bool = (type(resultCode) is int)
    condicion1Bool = True
    return condicion1Bool 

def condicion2():                           #comprueba resultado y tipo
    dfComprobacion = pd.DataFrame({
        'col1': [1, 3, 5],
        'col2': [4, 2, 6]
        }
    )
    condicion2Bool = (dfComprobacion.equals(resultCode))
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
        if not condicion1() and condicion2():
           document.getElementById("alertError").innerHTML = "Comprueba que sea un entero"
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
