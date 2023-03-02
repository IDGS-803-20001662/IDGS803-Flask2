from wtforms import Form;
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula', [validators.DataRequired(message="El campo es requerido"), 
                                          validators.length(min=4, max=15, message="No cumple la longitud del campo")])
    nombre = StringField('Nombre' , [validators.DataRequired(message="El campo es requerido")])
    apaterno = StringField('Apaterno', [mi_validacion])
    email = EmailField('Correo')

class LoginForm(Form):
    username = StringField('usuario', [validators.DataRequired(message='El campo es requerido'),
                                       validators.length(min=4, max=15, message='No cuumple la longitud para el campo')])
    password = StringField('password', [validators.DataRequired(message='El campo es requerido'),
                                       validators.length(min=4, max=15, message='No cuumple la longitud para el campo')])

# -------------------------------------- ACTIVIDAD 2 -----------------------------------------------------    
class DiccionarioForm(Form):
    palabraEspañol = StringField('Español', [validators.DataRequired(message="El campo es requerido"), 
                                          validators.length(min=1, max=23, message="No cumple la longitud del campo")])
    palabraIngles = StringField('Inglés', [validators.DataRequired(message="El campo es requerido"), 
                                          validators.length(min=1, max=23, message="No cumple la longitud del campo")])
    palabraTraducir = StringField('Palabra a traducir')

# ------------------------------------------ ACTIVIDAD 3 -----------------------------------------------
class ResistenciasForm(Form):
    banda1 = SelectField('Banda 1:', choices=[('0', 'Negro'), ('1', 'Marron'), ('2', 'Rojo'), ('3', 'Naranja'), 
                                              ('4', 'Amarillo'), ('5', 'Verde'), ('6', 'Azul'), ('7', 'Violeta'),
                                              ('8', 'Gris'), ('9', 'Blanco')])
    banda2 = SelectField('Banda 2:', choices=[('0', 'Negro'), ('1', 'Marron'), ('2', 'Rojo'), ('3', 'Naranja'), 
                                              ('4', 'Amarillo'), ('5', 'Verde'), ('6', 'Azul'), ('7', 'Violeta'),
                                              ('8', 'Gris'), ('9', 'Blanco')])
    banda3 = SelectField('Banda 3:', choices=[('1', 'Negro'), ('10', 'Marron'), ('100', 'Rojo'), ('1000', 'Naranja'), 
                                              ('10000', 'Amarillo'), ('100000', 'Verde'), ('1000000', 'Azul'), ('10000000', 'Violeta'),
                                              ('100000000', 'Gris'), ('1000000000', 'Blanco'), ('0.1', 'Dorado'), ('0.01', 'Plateado')])
    tolerancia = RadioField('Elige la tolerancia:', choices=[('0.5', 'Oro = 0.50'), ('0.10', 'Plata = 0.10'), ('0.20', 'Sin banda')])