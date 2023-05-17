#import asyncio
from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document
from io import StringIO
#from jsToPyscript import strCodeHTML, strCodeRecovery, stringKeys_list
import time
import sys

resultCode = 0
excepcionFlag=False
stringCode = ""


def execCodigo():
    global resultCode
    global x
    global excepcionFlag
    global stringCode
    stringCode = getstrCode()
    stringCodeMod=stringCode                #pyodide necesita declarar global la variable que usamos? 'global x\n'+stringCode
    
    try:
        exec(stringCodeMod, globals())          #es exec quien necesita añadir las globales
        resultCode = x                         #variable a sacar del codigo pasado a exec
        excepcionFlag = False
    except:
        excepcionFlag = True
    js.console.log('x',resultCode)
    


def evaluaCodigo():                         #comprueba tipo y resultado
    resultadoBool = condicion1() and condicion2() and condicion3()
    return resultadoBool

def condicion1():                           #comprueba tipo
    condicion1Bool = (type(resultCode) is int)
    return condicion1Bool

def condicion2():                           #comprueba resultado
    condicion2Bool = (resultCode == 4)
    return condicion2Bool

def condicion3():                           #comprueba condiciones del codigo
    condicion3Bool = "+" in stringCode
    return condicion3Bool

def resultadoCorrectoHTML():
    document.getElementById("resultadoTextarea1").style.backgroundColor = "#90EE90"     #green
    document.getElementById("alertas").style.display = 'flex'
    document.getElementById("alertaCorrecto").style.display = 'block'
    document.getElementById("alertaError").style.display = 'none'

def resultadoIncorrectoHTML():
    document.getElementById("resultadoTextarea1").style.backgroundColor = "#ffcccb"     #red
    document.getElementById("alertas").style.display = 'flex'
    document.getElementById("alertaCorrecto").style.display = 'none'
    document.getElementById("alertaError").style.display = 'block'

def mensajeAlertaErrorHTML(strAlerta):
    document.getElementById("alertError").innerHTML = strAlerta

def imprimePorHTML():
    js.console.log('imprimePorHTML')
    resultadoTextArea1 = document.getElementById("resultadoTextarea1")
    #resultadoTextArea1.select()
    resultadoTextArea1.value = resultCode
    condicionesBool = evaluaCodigo()
    js.console.log('resultado a comprobar',resultCode)

    if not excepcionFlag:
        js.console.log('Excepcion false')
        if condicionesBool:
            #print('Resultado correcto')                #print() falla de momento https://github.com/pyscript/pyscript/issues/230 https://github.com/pyscript/pyscript/issues/472
            js.console.log('Resultado correcto')           #print() devulelve el salto de linea por defecto, inserta directamente elementos html en modificador.py, usar js.console.log() de javascript
            resultadoCorrectoHTML()    
            
        else:
            js.console.log('Resultado incorrecto')
            if not condicion1() and condicion2():
                mensajeAlertaErrorHTML("Comprueba que sea un entero")
            elif condicion1() and not condicion2():
                mensajeAlertaErrorHTML("Resultado incorrecto")
            elif not condicion3():
                mensajeAlertaErrorHTML("No es una suma")
            resultadoIncorrectoHTML()

    else:
        js.console.log('Excepcion true')
        mensajeAlertaErrorHTML("Código incompleto o nombre de las variables incorrecto")
        resultadoIncorrectoHTML()


def reseteaVariables():
    global x
    try:
        del x                     #borra el resultado anterior cada vez que ejecuto el botón (solo fig de momento)
    except:
        js.console.log("Variable no iniciada")




def getstrCode():
    return document.getElementById("codeTextarea1").value


def button_click(event):                    #crear antes de create_proxy
    execCodigo()
    imprimePorHTML()
    reseteaVariables()
    


click_proxy = create_proxy(button_click)
#document.getElementById("buttonRun").addEventListener("click", click_proxy)
e = document.getElementById("buttonRun")
e.addEventListener("click", click_proxy)
