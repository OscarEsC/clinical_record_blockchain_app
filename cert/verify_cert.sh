#!/bin/bash

# Script to verify a certificate with our CA entity

# params:	$1 cert_file to verify	$2 abs_dir to app root

output=$(openssl verify -CAfile "${2}/cert/CA_dir/CA.crt" "${2}/certs_to_verify/${1}" | grep -E -c "certs_to_verify/${1}: OK")

#return 1 if valid
echo -n "${output}"
