from pyodide.ffi import create_proxy        #Go to inspect -> settings gear -> Uncheck 'enable javascript source maps' and 'enable css source map'. https://github.com/dart-lang/webdev/issues/1500
from js import alert, document
from io import StringIO
import time
import sys

stringEjercicio = "Ejercicio: Ordena y dibuja un dataframe con las siguientes columnas 'col1': [3, 1, 5], 'col2': [2, 4, 6]"
stringPista = "#Ordenado de menor a mayor respecto a col1\n"

document.getElementById("enunciadoEjercicio").innerHTML = stringEjercicio

document.getElementById("codeTextarea1").innerHTML = stringPista

