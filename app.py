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

# -------------------------------------------- ACTIVIDAD 3 --------------------------------------------------

@app.route("/resistencias", methods=['GET', 'POST'])
def resistencias():
    res_form = forms.ResistenciasForm(request.form)

    if request.method == 'POST':
        b1 = ""
        b2 = ""
        b3 = ""
        tol = ""
        print(res_form.banda1.data)
        b1 = res_form.banda1.data
        print(res_form.banda2.data)
        b2 = res_form.banda2.data
        print(res_form.banda3.data)
        b3 = res_form.banda3.data
        print(res_form.tolerancia.data)
        tol = res_form.tolerancia.data

        colorb1 = ""
        labelb1 = ""
        colorb2 = ""
        labelb2 = ""
        colorb3 = ""
        labelb3 = ""
        colortol = ""
        labeltol = ""

        vb12 = int(b1 + b2)
        print(vb12)

        vb123 = vb12 * int(b3)
        print(vb123)

        vtol = vb123 * float(tol)
        print(vtol)

        vmax = vb123 + vtol
        print(vmax)

        vmin = vb123 - vtol
        print(vmin)

        if b1 == "0":
            labelb1 = "Negro"
            colorb1 = "background: #16110b; color: white"
        elif b1 == "1":
            labelb1 = "Marrón"
            colorb1 = "background: #884c21; color: white"
        elif b1 == "2":
            labelb1 = "Rojo"
            colorb1 = "background: #fa0505; color: white"
        elif b1 == "3":
            labelb1 = "Naranja"
            colorb1 = "background: #fe9800; color: black"
        elif b1 == "4":
            labelb1 = "Amarillo"
            colorb1 = "background: #fefe00; color: black"
        elif b1 == "5":
            labelb1 = "Verde"
            colorb1 = "background: #70ac46; color: white"
        elif b1 == "6":
            labelb1 = "Azul"
            colorb1 = "background: #2e74b4; color: white"
        elif b1 == "7":
            labelb1 = "Violeta"
            colorb1 = "background: #702f9f; color: white"
        elif b1 == "8":
            labelb1 = "Gris"
            colorb1 = "background: #585858; color: white"
        elif b1 == "9":
            labelb1 = "Blanco"
            colorb1 = "background: #fefefe; color: white"

        if b2 == "0":
            labelb2 = "Negro"
            colorb2 = "background: #16110b; color: white"
        elif b2 == "1":
            labelb2 = "Marrón"
            colorb2 = "background: #884c21; color: white"
        elif b2 == "2":
            labelb2 = "Rojo"
            colorb2 = "background: #fa0505; color: white"
        elif b2 == "3":
            labelb2 = "Naranja"
            colorb2 = "background: #fe9800; color: black"
        elif b2 == "4":
            labelb2 = "Amarillo"
            colorb2 = "background: #fefe00; color: black"
        elif b2 == "5":
            labelb2 = "Verde"
            colorb2 = "background: #70ac46; color: white"
        elif b2 == "6":
            labelb2 = "Azul"
            colorb2 = "background: #2e74b4; color: white"
        elif b2 == "7":
            labelb2 = "Violeta"
            colorb2 = "background: #702f9f; color: white"
        elif b2 == "8":
            labelb2 = "Gris"
            colorb2 = "background: #585858; color: white"
        elif b2 == "9":
            labelb2 = "Blanco"
            colorb2 = "background: #fefefe; color: white"

        if b3 == "1":
            labelb3 = "Negro"
            colorb3 = "background: #16110b; color: white"
        elif b3 == "10":
            labelb3 = "Marrón"
            colorb3 = "background: #884c21; color: white"
        elif b3 == "100":
            labelb3 = "Rojo"
            colorb3 = "background: #fa0505; color: white"
        elif b3 == "1000":
            labelb3 = "Naranja"
            colorb3 = "background: #fe9800; color: black"
        elif b3 == "10000":
            labelb3 = "Amarillo"
            colorb3 = "background: #fefe00; color: black"
        elif b3 == "100000":
            labelb3 = "Verde"
            colorb3 = "background: #70ac46; color: white"
        elif b3 == "1000000":
            labelb3 = "Azul"
            colorb3 = "background: #2e74b4; color: white"
        elif b3 == "10000000":
            labelb3 = "Violeta"
            colorb3 = "background: #702f9f; color: white"
        elif b3 == "100000000":
            labelb3 = "Gris"
            colorb3 = "background: #585858; color: white"
        elif b3 == "1000000000":
            labelb3 = "Blanco"
            colorb3 = "background: #fefefe; color: white"
        elif b3 == "0.1":
            labelb3 = "Dorado"
            colorb3 = "background: #b1a000; color: black"
        elif b3 == "0.01":
            labelb3 = "Plateado"
            colorb3 = "background: #a5a5a5; color: black"

        if tol == "0.5":
            labeltol = "Dorado"
            colortol = "background: #b1a000; color: black"
        elif tol == "0.10":
            labeltol = "Plateado"
            colortol = "background: #a5a5a5; color: black"
        elif tol == "0.20":
            labeltol = "Sin banda"
            colortol = "background: #fefefe; color: black"

        return render_template("resistencias.html", form = res_form, vb123=vb123, vmax=vmax, vmin=vmin, labelb1=labelb1, 
                               colorb1=colorb1, labelb2=labelb2, colorb2=colorb2, labelb3=labelb3, colorb3=colorb3, 
                               labeltol=labeltol, colortol=colortol)



    return render_template("resistencias.html", form = res_form)

# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)