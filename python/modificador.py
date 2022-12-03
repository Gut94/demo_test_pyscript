from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document
from io import StringIO
import time
import sys

stringEjercicio = "Ejercicio: Devuelve un entero igual a 4"
stringPista = "x="

document.getElementById("enunciadoEjercicio").innerHTML = stringEjercicio

document.getElementById("codeTextarea1").innerHTML = stringPista
