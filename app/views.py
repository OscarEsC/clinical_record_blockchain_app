import datetime
import json

import requests
from flask import render_template, redirect, request, send_from_directory

from app import app
from app.auxiliar.auxiliar import *


# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []

@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='Medical Blockchain',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)

@app.route('/history')
def home():
    return render_template('history.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('Signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    user = request.form["user"]
    rfc = request.form["rfc"]
    password = request.form["password"]
    
    certName = username_to_certName(user)
    dir_, zip_file = create_user_cert_request(certName, password) 
    return send_from_directory(dir_, filename=zip_file, as_attachment=True)

@app.route('/medical')
def medical():
    return render_template('medical.html')

@app.route('/history', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    num_hist = request.form["num_hist"]
    id_paciente = request.form["id_paciente"]
    apellidos = request.form["apellidos"]
    nombres = request.form["nombres"]
    edad = request.form["edad"]
    sexo = request.form["sexo"]
    ocupacion = request.form["ocupacion"]
    fecha_nac = request.form["fecha_nac"]
    edo_civil = request.form["edo_civil"]
    nacionalidad = request.form["nacionalidad"]
    grad_est = request.form["grad_est"]
    fecha = request.form["fecha"]
    piso = request.form["piso"]
    cama = request.form["cama"]
    motiv_consulta = request.form["motiv_consulta"]
    enf_actual = request.form["enf_actual"]
    enf_antecedentes = request.form["enf_antecedentes"]
    habitos_toxicos = request.form["habitos_toxicos"]
    habitos_fisiologicos = request.form["habitos_fisiologicos"]
    padecimientos = request.form["padecimientos"]
    heredofamiliares = request.form["heredofamiliares"]
    peso = request.form["peso"]
    estatura = request.form["estatura"]
    imc = request.form["imc"]
    temperatura = request.form["temperatura"]
    diagnostico = request.form["diagnostico"]
    otros = request.form["otros"]

    post_object = {
        'num_hist' : num_hist,
        'id_paciente' : id_paciente,
        'apellidos' : apellidos,
        'nombres' : nombres,
        'edad' : edad,
        'sexo' : sexo,
        'ocupacion' : ocupacion,
        'fecha_nac' : fecha_nac,
        'edo_civil' : edo_civil,
        'nacionalidad' : nacionalidad,
        'fecha' : fecha,
        'piso' : piso,
        'cama' : cama,
        'motiv_consulta' : motiv_consulta,
        'enf_actual' : enf_actual,
        'enf_antecedentes' : enf_antecedentes,
        'habitos_toxicos' : habitos_toxicos,
        'habitos_fisiologicos' : habitos_fisiologicos,
        'padecimientos' : padecimientos,
        'heredofamiliares' : heredofamiliares,
        'peso' : peso,
        'estatura' : estatura,
        'imc' : imc,
        'temperatura' : temperatura,
        'diagnostico' : diagnostico,
        'otros' : otros,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})
    
    print(post_object)
    return redirect('/')

@app.route('/medical', methods=['POST'])
def submit_textarea_medical():
    """
    Endpoint to create a new transaction via our application.
    """
    num_hist = request.form["num_hist"]
    id_paciente = request.form["id_paciente"]
    apellidos = request.form["apellidos"]
    nombres = request.form["nombres"]
    edad = request.form["edad"]
    sexo = request.form["sexo"]
    fecha = request.form["fecha"]
    motiv_consulta = request.form["motiv_consulta"]
    enf_actual = request.form["enf_actual"]
    peso = request.form["peso"]
    estatura = request.form["estatura"]
    imc = request.form["imc"]
    temperatura = request.form["temperatura"]
    diagnostico = request.form["diagnostico"]

    post_object = {
        'num_hist' : num_hist,
        'id_paciente' : id_paciente,
        'apellidos' : apellidos,
        'nombres' : nombres,
        'edad' : edad,
        'sexo' : sexo,
        'fecha' : fecha,
        'motiv_consulta' : motiv_consulta,
        'enf_actual' : enf_actual,
        'estatura' : estatura,
        'imc' : imc,
        'temperatura' : temperatura,
        'diagnostico' : diagnostico,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction_medical".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})
    
    print(post_object)
    return redirect('/')

