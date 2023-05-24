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
excepcionFlag=False



def execCodigo():
    global resultCode
    global fig
    global excepcionFlag
    stringCode = getstrCode()
    stringCodeMod=stringCode                #pyodide necesita declarar global la variable que usamos? 'global x\n'+stringCode
    
    try:
        exec(stringCodeMod, globals())          #es exec quien necesita añadir las globales
        resultCode = df                         #variable a sacar del codigo pasado a exec
        #display(fig, target="grafico1")
        #pyscript.write("grafico1",fig)          #https://towardsdatascience.com/create-an-interactive-web-app-with-pyscript-and-pandas-3918ad2dada1 obsoleto pronto
        Element("grafico1").write(fig)
        excepcionFlag = False
    except:
        excepcionFlag = True
    js.console.log('df',resultCode)
    


def evaluaCodigo():                         #comprueba tipo y resultado
    resultadoBool = condicion1() and condicion2()
    return resultadoBool

def condicion1():                           #comprueba tipo, en este caso seria mejor eliminar esta funcion
    condicion1Bool = (type(resultCode) is pd.core.frame.DataFrame)
    return condicion1Bool 

def condicion2():                           #comprueba resultado y tipo
    dfComprobacion = pd.DataFrame({
        'col1': [3, 1, 5],
        'col2': [2, 4, 6]
        }
)
    dfComprobacion.sort_values('col1', inplace=True)

    condicion2Bool = (dfComprobacion.equals(resultCode))
    return condicion2Bool

def resultadoCorrectoHTML():
    document.getElementById("resultadoTextarea1").style.backgroundColor = "#90EE90"     #green
    document.getElementById("alertas").style.display = 'flex'
    document.getElementById("alertaCorrecto").style.display = 'block'
    document.getElementById("alertaError").style.display = 'none'
    document.getElementById("zonaGraficos").style.display = 'flex'

def resultadoIncorrectoHTML():
    document.getElementById("resultadoTextarea1").style.backgroundColor = "#ffcccb"     #red
    document.getElementById("alertas").style.display = 'flex'
    document.getElementById("alertaCorrecto").style.display = 'none'
    document.getElementById("alertaError").style.display = 'block'
    document.getElementById("zonaGraficos").style.display = 'none'

def mensajeAlertaErrorHTML(strAlerta):
    document.getElementById("alertError").innerHTML = strAlerta

def imprimePorHTML():
    js.console.log('hola')
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
                mensajeAlertaErrorHTML("Comprueba que sea un dataframe")
            elif condicion1() and not condicion2():
                mensajeAlertaErrorHTML("Resultado incorrecto") 
            resultadoIncorrectoHTML()

    else:
        js.console.log('Excepcion true')
        mensajeAlertaErrorHTML("Código incompleto o nombre de las variables incorrecto")
        resultadoIncorrectoHTML()


def reseteaVariables():
    global fig
    try:
        del fig                     #borra el resultado anterior cada vez que ejecuto el botón (solo fig de momento)
    except:
        js.console.log("Variable no iniciada")


def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

#(el valor pasado por el input, el codigo que se va ir remplazando con ese valor, el valor elegido por el profesor, el string que se intercambia por el valor)
def  modifyStrCode(inputStrKey, strCodeIter, strKeyOriginal, stringACambiar):
    
    if not isinstance(strCodeIter, str):
        strCodeIter = str(strCodeIter)
    
    strCodeIter = strCodeIter.replace(stringACambiar, inputStrKey)
    print(type(inputStrKey))
    print(type(strCodeIter))
    print(type(strKeyOriginal))
    print(type(stringACambiar))
    return strCodeIter

#recoge los valores de los inputs y por clase comprueba que son iguales, si lo son los pasa modificar el codigo (si cumple otras condiciones)
# TODO: aceptar valores distintos que no sean strings
def getstrCode():

    strCodeIter = strCodeRecovery

    for stringKeys_item in stringKeys_list:
        stringACambiar = "strKey"+str(stringKeys_item['id'])
        listaInputs = document.getElementsByClassName(stringACambiar)
        print(listaInputs)
        valueClassList = []

        for inputValues in listaInputs:
            valueClassList.append(inputValues.value)
            print(valueClassList)  
        
        if stringKeys_item['number']>1 and all_equal(valueClassList):
            print("Son todos iguales")
            strCodeIter = modifyStrCode(valueClassList[0], strCodeIter, stringKeys_item['value'], stringACambiar)
        elif stringKeys_item['number']==1:
            print("Solo hay uno")
            strCodeIter = modifyStrCode(valueClassList[0], strCodeIter, stringKeys_item['value'], stringACambiar)
        else:
            print("No son iguales")
    
    return strCodeIter

def button_click(event):            #crear antes de create_proxy
    execCodigo()
    imprimePorHTML()
    reseteaVariables()


click_proxy = create_proxy(button_click)
#document.getElementById("buttonRun").addEventListener("click", click_proxy)
e = document.getElementById("buttonRun")
e.addEventListener("click", click_proxy)
