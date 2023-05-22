#!/usr/bin/python3

from itertools import cycle
from argparse import ArgumentParser
import sys
def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-f', help = 'File with ShellCode in Bytes')
    parser.add_argument('-s', default = 'secret123', help = 'Secret')
    parser.add_argument('-o', default = 'result.txt', help = 'Output File (Must be .py format)')
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
    parser = create_parser()
    if len(sys.argv)==1:
    	parser.print_help(sys.stderr)
    	sys.exit(1)
    parser_args = parser.parse_args()
    file = parser_args.f
    secret = parser_args.s
    output_file = parser_args.o
    crypted_message = crypter(file, secret)
    file_write(output_file, crypted_message, secret)
