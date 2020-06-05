#!/bin/bash

# Script to sign user's certificate request with the CA key.
# The password of the CA key is obtained from CA_password.sh

password=$(./CA_password.sh)
echo $password
openssl ca -cert CA_dir/CA.crt -keyfile CA_dir/CA.key -in "csrs/${1}.csr" -out "certs/${1}.crt" -config clinical_blockchain_certs.conf -passin "pass:${password}" -notext -batch &>/dev/null

# Return value from script
echo "certs/${1}.crt"
