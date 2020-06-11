#!/bin/bash

# Script to sign user's certificate request with the CA key.
# The password of the CA key is obtained from CA_password.sh

password=$("${2}/CA_password.sh")

# params:	$1 csr2sign_file	$2 abs_dir
openssl ca -cert "${2}/CA_dir/CA.crt" -keyfile "${2}/CA_dir/CA.key" -in "${2}/csrs/${1}.csr" -out "${2}/certs/${1}.crt" -config "${2}/clinical_blockchain_certs.conf" -passin "pass:${password}" -notext -batch 

# Return value from script
echo "${2}/certs/${1}.crt"
