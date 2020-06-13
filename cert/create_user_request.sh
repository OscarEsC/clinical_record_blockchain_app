#!/bin/bash

# Script to create new user's private key and certificate request

# Var to set the organization parameters to certificate request
subj_root='/C=MX/ST=CDMX/L=Coyoacan/O=clinical_blockchain/OU=blockchain_user/CN='
# params:	$1 username	$2 user_password	$3 abs_dir
# Receive as unique parameter the common name used for both files and in CN section
openssl req -new -newkey rsa:4096 -keyout "${3}/keys/${1}.key" -out "${3}/csrs/${1}.csr" -config "${3}/clinical_blockchain_certs.conf" -subj "${subj_root}${1}" -passout "pass:${2}" -batch &>/dev/null 

# Return value from script
echo -n "${3}/keys/${1}.key,${3}/csrs/${1}.csr"
