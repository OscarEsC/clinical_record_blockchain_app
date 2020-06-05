#!/bin/bash

# Script to prepare environment at first moment
# Create necessary files and dirs to Certification Authority
# see clinical_blockchain_certs.conf to more info

touch database_index
echo "01" > serial
mkdir CA_dir
mkdir certs
mkdir newcerts
mkdir keys
mkdir csrs
