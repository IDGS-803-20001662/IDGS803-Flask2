from flask import Flask, render_template
from flask import request
import forms

app = Flask(__name__)

@app.route("/numeros", methods=['GET', 'POST'])
def numeros():
    if request.method == "POST":
        num = int(request.form.get("txtNumero"))
        return render_template("numerosOptions.html", num=num)
    else:
        return render_template("numeros.html")

@app.route("/numerosresultado", methods=['POST'])
def numerosresultado():
    num = int(request.form.get("txtNumeroO"))
    lista_num = []
    promedio = 0
    suma = 0
    numerosRepetidos = []
    numeroRepeticiones = []


    for i in range(num):
        index = "txtN" + str(i+1)
        print(index)
        lista_num.append(request.form.get(index))

    max = int(lista_num[0])
    min = int(lista_num[0])
    
    for item in lista_num:
        suma = suma + int(item)
        if (max <= int(item)):
            max = int(item)
        if (min >= int(item)):
            min = int(item)
        if lista_num.count(item) > 1:
            if numerosRepetidos.count(item) == 0 or numerosRepetidos.count(item) == False:
                numerosRepetidos.append(item)
                numeroRepeticiones.append(lista_num.count(item))
                   
    promedio = suma / len(lista_num)
    numR = len(numeroRepeticiones)

    return render_template("numerosResultado.html", lista_num = lista_num, max = max, min = min, promedio = promedio, numerosRepetidos=numerosRepetidos, numeroRepeticiones=numeroRepeticiones, numR = numR)
    

# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True)