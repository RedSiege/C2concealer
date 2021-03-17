#!/bin/bash

# Global Variables
runuser=$(whoami)
tempdir=$(pwd)
# Script Args
domain=$1
password=$2
domainStore=$3
# Echo Title
clear
echo '=========================================================================='
echo ' Script adapted from @KillSwitch-GUI'
echo ' Running LetsEncrypt to build a SSL cert for $domain' 
echo '=========================================================================='

#Local Vars
domainPkcs="$domain.p12"

# Environment Checks
func_check_env(){
  if [ $(id -u) -ne '0' ]; then
    echo
    echo ' [ERROR]: This Setup Script Requires root privileges!'
    echo '          Please run this setup script again with sudo or run as login as root.'
    echo
    exit 1
  fi
}

func_check_tools(){
  # Check Sudo Dependency going to need that!
  if [ $(which keytool) ]; then
    echo '[Sweet] java keytool is installed'
  else 
    echo
    echo ' [ERROR]: keytool does not seem to be installed'
    echo
    exit 1
  fi
  if [ $(which openssl) ]; then
    echo '[Sweet] openssl keytool is installed'
  else 
    echo
    echo ' [ERROR]: openssl does not seem to be installed'
    echo
    exit 1
  fi
  if [ $(which git) ]; then
    echo '[Sweet] git keytool is installed'
  else 
    echo
    echo ' [ERROR]: git does not seem to be installed'
    echo
    exit 1
   fi
}

func_apache_check(){
  
  if [ $(which java) ]; then
    echo '[Sweet] java is already installed'
    echo
  else
    apt-get update
    apt-get install default-jre -y 
    echo '[Success] java is now installed'
    echo
  fi
  if [ $(which apache2) ]; then
    echo '[Sweet] Apache2 is already installed'
    service apache2 start
    echo
  else
    apt-get update
    apt-get install apache2 -y 
    echo '[Success] Apache2 is now installed'
    echo
    service apache2 restart
    service apache2 start
  fi
  if [ $(netstat -antup | grep apache | grep LISTEN | grep -c ":80") -ge 1 ]; then  
    echo '[Success] Apache2 is up and running!'
  else 
    echo
    echo ' [ERROR]: Apache2 does not seem to be running on'
    echo '          port 80? Try manual start?'
    echo
    exit 1
  fi
  if [ $(which ufw) ]; then
    echo 'Looks like UFW is installed, opening ports 80 and 443'
    ufw allow 80/tcp
    ufw allow 443/tcp
    echo
  fi
}

func_install_letsencrypt(){
   echo '[Starting] snap install certbot'
   snap install --classic certbot
   echo '[Starting] link certbot'
   sudo ln -s /snap/bin/certbot /usr/bin/certbot
  echo '[Success] letsencrypt is built!'
  echo '[Starting] to build letsencrypt cert!'
  certbot --apache -d $domain -n --register-unsafely-without-email --agree-tos 
  if [ -e /etc/letsencrypt/live/$domain/fullchain.pem ]; then
    echo '[Success] letsencrypt certs are built!'
    service apache2 stop
    echo '[Info] Apache service stopped'
  else
    echo "[ERROR] letsencrypt certs failed to build.  Check that DNS A record is properly configured for this domain"
    service apache2 stop
    echo "[Info] Apache service stopped"
    exit 1
  fi
}

func_build_pkcs(){
  cd /etc/letsencrypt/live/$domain
  echo '[Starting] Building PKCS12 .p12 cert.'
  openssl pkcs12 -export -in fullchain.pem -inkey privkey.pem -out $domainPkcs -name $domain -passout pass:$password
  echo '[Success] Built $domainPkcs PKCS12 cert.'
  echo '[Starting] Building Java keystore via keytool.'
  keytool -importkeystore -deststorepass $password -destkeypass $password -destkeystore $domainStore -srckeystore $domainPkcs -srcstoretype PKCS12 -srcstorepass $password -alias $domain
  echo '[Success] Java keystore $domainStore built.'
  cp $domainStore $tempdir
  echo '[Success] Moved Java keystore to current working directory.'
}

# Main

main() {
  func_check_env
  func_check_tools
  func_apache_check
  func_install_letsencrypt
  func_build_pkcs
}

main
