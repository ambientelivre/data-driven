#!/bin/bash
# Remove a linha "http-server.https.keystore.path" do ConfigMap do Trino
sed '/http-server\.https\.keystore\.path=/d'
