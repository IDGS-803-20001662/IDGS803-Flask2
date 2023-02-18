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
    # max = 0
    # min = 0
    # promedio = 0
    # suma = 0


    for i in range(num):
        index = i+1
        lista_num.append(request.form.get("txtN"+str(index)+'"'))
    
    #for item in lista_num:
    #    suma = suma + int(item)

        
    #promedio = suma / len(lista_num)

    return render_template("numerosResultado.html", lista_num = lista_num)
    

# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True)