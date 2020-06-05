import datetime
import json

import requests
from flask import render_template, redirect, request

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
    print(certName, rfc, password)
    return render_template('Signup.html')

@app.route('/submit', methods=['POST'])
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
    cert = request.form["cert"]

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
        'cert' : cert,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')

