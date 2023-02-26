from flask import Flask, render_template
from flask import request
import forms
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

# ---------------------- PREVENCION DE ATAQUES CROSS SITE REQUEST FORGERY -------------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = "Esta es la clave encriptada"
csrf = CSRFProtect()

# ------------------------------------------ MANEJO DE ERRORES -----------------------------------------------
@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'), 404

# ------------------------------------------- MANEJO DE COOKIES -----------------------------------------------
@app.route("/cookies", methods=['GET', 'POST'])
def cookies():
    reg_user = forms.LoginForm(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user+'@'+passw
        success_message = "Bienvenid@ {}".format(user)
        flash(success_message)
    
    response = make_response(render_template("cookies.html", form = reg_user))
    if len(datos) > 0:
        response.set_cookie('datos_user',datos)

    return response

@app.route("/saludo", methods=['GET', 'POST'])
def saludo():
    valor_cookie = request.cookies.get("datos_user")
    nombres = valor_cookie.split('@')
    return render_template('saludo.html', nom = nombres[0])

# ------------------------------------- FORMULARIO MANUAL CON FLASK --------------------------------------------
@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

# ------------------------------------ FORMULARIO CON FORMS DE FLASK ----------------------------------------------
@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)

    return render_template("alumnos.html", form = alum_form)

# -------------------------------------------- ACTIVIDAD 2 --------------------------------------------------
@app.route("/diccionario", methods=['GET', 'POST'])
def diccionario():
    dic_form = forms.DiccionarioForm(request.form)
    return render_template("diccionario.html", form = dic_form)

@app.route("/traducir", methods=['GET', 'POST'])
def traducir():
    dic_form = forms.DiccionarioForm(request.form)
    print(dic_form.palabraEspañol.data)
    print(dic_form.palabraIngles.data)
    palabraEspanol = dic_form.palabraEspañol.data
    palabraEspanol = palabraEspanol.upper()
    palabraIngles = dic_form.palabraIngles.data
    palabraIngles = palabraIngles.upper()
    guardarPalabras(palabraEspanol, palabraIngles)

    return render_template("traducir.html", form = dic_form)

@app.route("/traduccion", methods=['GET', 'POST'])
def traduccion():
    dic_form = forms.DiccionarioForm(request.form)
    palabraTraducir = dic_form.palabraTraducir.data
    idiomaRBN = request.form.get("rbnIdiomas") # E - I
        
    if len(palabraTraducir) == 0:
        flash("Introduce alguna palabra en el campo")
    else:
        palabraTraducir = palabraTraducir.upper()
        palabraTraducida = devolverPalabra(palabraTraducir, idiomaRBN)
        if len(palabraTraducida) == 0:
            flash("La palabra no se encuentra en el diccionario actual")
    
    return render_template('traduccion.html', palabraTraducida = palabraTraducida)

def guardarPalabras(palabraEspanol, palabraIngles):
    dic = "{} - {}".format(palabraEspanol,palabraIngles)
    f = open('diccionario.txt','a')
    f.write('\n' + dic)
    f.close()

def devolverPalabra(palabraTraducir, idioma):
    res = ""

    f = open('diccionario.txt','r')
    pares = f.readlines()
    print(pares)
    f.close()

    for par in pares:
        print(par)
        if(par.count(palabraTraducir)):
            palabras = par.split() # E,-,I
            print(palabras)
            if(idioma == "I"): #español - ingles
                print(palabras[0])
                print(palabras[1])
                print(palabras[2])
                print(palabraTraducir)
                print(palabras[0] == palabraTraducir)

                if palabras[0] == palabraTraducir:
                    return palabras[2]
                else:
                    res = ""

            elif idioma == "E": #ingles - español
                if palabras[2] == palabraTraducir:
                    return palabras[0]
                else:
                    res = ""
            else:
                res = ""
        else:
            res = ""

    return res

# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)