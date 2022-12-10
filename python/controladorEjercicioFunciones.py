#import asyncio
from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document
from io import StringIO
import time
import sys

resultCode = 0
excepcionFlag=False
stringCode = ""



def execCodigo():
    global resultCode
    global lista
    global excepcionFlag
    global stringCode
    stringCode = getstrCode()
    stringCodeMod = stringCode   
    exec(stringCodeMod, globals())
    try:
        resultCode = lista                            #variable a sacar del codigo pasado a exec
        listaMod = ordenaLista(resultCode)            #función a comprobar
        resultCode = listaMod                         #variable modificada con la funcion pasada a exec
        excepcionFlag = False
    except:
        excepcionFlag = True
    
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
    console.log('imprimePorHTML')
    resultadoTextArea1 = document.getElementById("resultadoTextarea1")
    #resultadoTextArea1.select()
    resultadoTextArea1.value = resultCode
    condicionesBool = evaluaCodigo()
    console.log('resultado a comprobar',resultCode)

    if not excepcionFlag:
        console.log('Excepcion false')
        if condicionesBool:
            #print('Resultado correcto')                #print() falla de momento https://github.com/pyscript/pyscript/issues/230 https://github.com/pyscript/pyscript/issues/472
            console.log('Resultado correcto')           #print() devulelve el salto de linea por defecto, inserta directamente elementos html en modificador.py, usar console.log() de javascript
            resultadoCorrectoHTML()    
            
        else:
            console.log('Resultado incorrecto')
            if not condicion1() and condicion2():
                mensajeAlertaErrorHTML("Comprueba que sea una lista")
            elif condicion1() and not condicion2():
                mensajeAlertaErrorHTML("Resultado incorrecto")
            resultadoIncorrectoHTML()
    else:
        console.log('Excepcion true')
        mensajeAlertaErrorHTML("Código incompleto o nombre de las variables incorrecto")
        resultadoIncorrectoHTML()


def reseteaVariables():
    global lista
    #print(globals())
    try:                              #en este caso no arregla con la funcion se queda con la anterior declaracion si el nombre es incorrecto ¿del globals()[func.func_name]?
        del lista                     #borra el resultado anterior cada vez que ejecuto el botón (solo fig de momento)
    except:
        console.log("Variable no iniciada")
    #print(globals())


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
