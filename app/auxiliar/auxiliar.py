import datetime
import json
import requests
from subprocess import Popen, PIPE, STDOUT
from app import app
from os.path import basename, abspath, join
from os import pardir

CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

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
    shell_file = join(cert_dir, "ec.sh")
    out = Popen([shell_file,'hola'], stdout=PIPE, stderr=STDOUT)
    stdout, stderr = out.communicate()
    print(stdout)