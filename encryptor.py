#!/usr/bin/python3
import subprocess
from itertools import cycle
from argparse import ArgumentParser

import sys

args = ['-f', '-s', '-o']
packages_to_install = {
    'argparse': ''
}

def install_packages(packages):
    try:
        for package, version in packages.items():
            if version:
                package_spec = f"{package}=={version}"
            else:
                package_spec = package
            subprocess.check_call(['pip', 'install', package_spec])
        print("Установка пакетов завершена успешно.")
    except subprocess.CalledProcessError:
        print("Ошибка при установке пакетов.")

def create_parser():
    parser = ArgumentParser()
    for arg in args:
        parser.add_argument(arg)
    return parser

def crypter(bytes_file, secret):
	with open(bytes_file, 'r') as f:
		cryptedMessage = ''.join(chr(ord(c)^ord(k)) for c,k in zip(f.read(), cycle(secret)))	
	return cryptedMessage

def file_write(file_name, crypted_string, secret_key):
	with open("./main_script", "r") as r:
		with open(file_name, 'w') as w:
			w.write(r.read().format(data = crypted_string, secret = secret_key))
if __name__=="__main__":
    install_packages(packages_to_install)
    parser = create_parser()
    #if len(sys.argv)==1:
    	#parser.print_help(sys.stderr)
    	#sys.exit(1)
    parser_args = parser.parse_args()
    file = parser_args.f
    secret = parser_args.s
    output_file = parser_args.o
    crypted_message = crypter(file, secret)
    file_write(output_file, crypted_message, secret)
