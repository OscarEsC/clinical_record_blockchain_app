#!/bin/bash

# Script to create a self-sign certificate to the Certification Authority
# both private key and certificate are saved in CA_dir

# subject to create the self-signed certificate 
subj_root='/C=MX/ST=CDMX/L=Coyoacan/O=clinical_blockchain/OU=blockchain_CA/CN=CertificationAuthority'
# Get password from secure script
password="$(./CA_password.sh)"

openssl req -x509 -days 3650 -newkey rsa:4096 -keyout CA_dir/CA.key -out CA_dir/CA.crt -config clinical_blockchain_certs.conf -subj $subj_root -passout "pass:${password}" &>/dev/null

# return 0 
echo -n "0"
