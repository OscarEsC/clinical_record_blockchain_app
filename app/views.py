import datetime
import json

import requests
from flask import render_template, redirect, request, send_from_directory

from app import app
from app.auxiliar.auxiliar import *
from os.path import join
from werkzeug.utils import secure_filename


# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []

def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)

@app.route('/', methods=['GET'])
def index():
    #fetch_posts()
    return render_template('index.html',
                           title='Medical Blockchain')

@app.route('/', methods=['POST'])
def index_post():
    fetch_posts()
    to_search = request.form['search']
    founded = search_in_chain(posts, to_search)
    return render_template('search.html',
                           title='Transactions founded',
                           posts=founded,
                           readable_time=timestamp_to_string)


@app.route('/history')
def home():
    return render_template('history.html',
                            title='Medical History')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('Signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    user = request.form["user"]
    rfc = request.form["rfc"]
    password = request.form["password"]
    
    certName = username_to_certName(user)
    dir_, zip_file = new_certificate(certName, password) 
    return send_from_directory(dir_, filename=zip_file, as_attachment=True)

@app.route('/medical', methods=['GET'])
def medical():
    return render_template('medical.html',
                            title='Medical Advice')

@app.route('/transactions')
def transaction():
    fetch_posts()
    return render_template('/transactions.html',
                           title='Transaction',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)

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
        'grad_est' : grad_est,
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

    # If does not upload a file
    if 'cert' not in request.files:
        # SHOW ERROR MESSAGE
        print("no file")
        return redirect('/history')
    cert_file = request.files['cert']
    if cert_file.filename == '':
        # SHOW ERROR MESSAGE
        print("no file")
        return redirect('/history')
    # Upload the .cert file to verify
    if allowed_file(cert_file.filename):
        filename = secure_filename(cert_file.filename)
        cert_file.save(join(upload_dir(), filename))
    
    # Verify the certificate
    if not is_valid_certificate(filename):
        # SHOW ERROR MESSAGE
        print("error")
        return redirect('/history')

    print("success")
    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})
    
    #print(post_object)
    return redirect('/transactions')

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
        'peso' : peso,
        'estatura' : estatura,
        'imc' : imc,
        'temperatura' : temperatura,
        'diagnostico' : diagnostico,
    }
    # If does not upload a file
    if 'cert' not in request.files:
        # SHOW ERROR MESSAGE
        print("no file")
        return redirect('/medical')
    cert_file = request.files['cert']
    if cert_file.filename == '':
        # SHOW ERROR MESSAGE
        print("no file")
        return redirect('/medical')
    # Upload the .cert file to verify
    if allowed_file(cert_file.filename):
        filename = secure_filename(cert_file.filename)
        cert_file.save(join(upload_dir(), filename))
    
    # Verify the certificate
    if not is_valid_certificate(filename):
        # SHOW ERROR MESSAGE
        print("error")
        return redirect('/medical')

    print("success")
    # Submit a transaction
    new_tx_address = "{}/new_transaction_medical".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})
    
    #print(post_object)
    return redirect('/transactions')

@app.route('/register_new_node', methods=['GET'])
def register_node():
    return render_template('register_node.html',
                            title='Register Node')

@app.route('/register_new_node', methods=['POST'])
def register_node_post():
    new_host = request.form['node']
    print(new_host)
    # If does not upload a file
    if 'cert' not in request.files:
        # SHOW ERROR MESSAGE
        print("no file 1")
        return redirect('/register_new_node')
    cert_file = request.files['cert']
    if cert_file.filename == '':
        # SHOW ERROR MESSAGE
        print("no file 2")
        return redirect('/register_new_node')
    # Upload the .cert file to verify
    if allowed_file(cert_file.filename):
        filename = secure_filename(cert_file.filename)
        cert_file.save(join(upload_dir(), filename))
    
    # Verify the certificate
    if not is_valid_certificate(filename):
        # SHOW ERROR MESSAGE
        print("error")
        return redirect('/register_new_node')

    print("success")
    data = {'node_address': CONNECTED_NODE_ADDRESS}
    headers = {'Content-Type': 'application/json'}
    register_post = new_host + '/register_with'
    response = requests.post(register_post,json=data,headers=headers)
    if response.status_code == 200:
        return redirect('/register_new_node')
    else:
        print("error al registrar nuevo nodo")
        return redirect('/register_new_node')