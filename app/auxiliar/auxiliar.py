import datetime
import json
import requests
from subprocess import Popen, PIPE, STDOUT
from app import app
from os.path import basename, abspath, join
from os import pardir
from zipfile import ZipFile
from pyminizip import compress_multiple

CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

user_request = "create_user_request.sh"

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

def username_to_certName(user):
    user = user.split(' ')
    user = [x.capitalize() for x in user]
    certName = "".join(user)
    return certName

def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')

def create_user_cert_request(certName, password):
    cert_dir = abspath(join(app.root_path, pardir))
    cert_dir = join(cert_dir, "cert")
    shell_file = join(cert_dir, user_request)
    out = Popen([shell_file, certName, password, cert_dir], stdout=PIPE, stderr=STDOUT)
    stdout, stderr = out.communicate()
    file1, file2 = stdout.decode("utf-8").split(',')
    zip_file = zip_files(file1, file2, password, cert_dir)
    return cert_dir, zip_file

def zip_files(file1, file2, password, cert_dir):
    zip_name = basename(file1).split('.')[0] + '.zip'
    zip_name_dir = join(cert_dir, zip_name)
    compress_multiple([file1, file2], [], zip_name_dir, password, 4)

    return zip_name