import requests,random,sys,json,os,re,datetime,socket,pprint
from time import sleep as slp
from os import system as cmd
import os
totaldmp = 0
count = 0
try:
	os.mkdir('Data')
except:
	pass
try:
	os.remove('temp.txt')
except:
	pass
head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
logo = """____________ MR JADUGAR____________
_____________________________________
github   : not found                                
Facebook : Kashif Baloch                     
YouTube  : Mr Jadugar Gamers           
Whatsapp : not found                            
                                                 [DEAD USER]
_____________________________________ """
def Jadu():
	os.system("clear")
	os.system("xdg-open https://youtube.com/channel/UCrfVEu_7ylJI8XiVBrg4gmw")
	print(logo)
    
	print("its only for fun")
	print("_____________________________________")
	print(" [1] login with cookies")
	p = input(" Select An Option : ")
	if p in ['1','01']:
			main()

def login():
	os.system("clear")
	print(logo)
	now = datetime.datetime.now()
	print("Date and Time ")
	print(now.strftime("%y-%m-%d %H:%M:%S"))
	hostnm = socket.gethostname()
	ipaddress = socket.gethostbyname(hostnm)
	print("ip address is :", ipaddress)
	print("country : Pakistan")
	print("_____________________________________")
	try:
		fbcokis= input('[>>] Input Your Facebook Cookie : ')
		print(47*"\033[1;37;1m-")
		head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
		open("data/token.txt", "w").write(eaag.group(1))
		open("data/cookie.txt", "w").write(fbcokis)
		token = open('data/token.txt','r').read()
		main()
	except Exception as e:
		os.system("rm -f data/token.txt")
		print(f"[*] Error {e}")
		slp(2)
		login()
def grep(f):
	o = input('\033[0;97m[->] Save As : \033[1;32;1m')
	print(47*"\033[1;37;1m-")
	try:
		ask_link = int(input('[>>] Enter Grip ID Limit : \033[1;32;1m'))
		print(47*"\033[1;37;1m-")
	except:
		ask_link = 1
		completed = 0
	for links in range(ask_link):
		li = input('[✓] Separate Object : \033[1;32;1m')
		os.system('cat '+f+' | grep "'+li+'" >> '+o)
	print(47*"\033[1;37;1m-")
	print("[>>] Separating Successful ")
	print("[>>] New File Save \033[1;32;1m" + o)
	print(47*"\033[1;37;1m-")
	input("[>>] Press Inter to go Back < ")
	main()
def main():
	fbidz = []
	os.system("clear")
	print(logo)
	try:
		fbcokis = open("data/cookie.txt", "r").read()
		token = open('data/token.txt','r').read()
		ftoken = requests.get("https://business.facebook.com/business_locations", headers=head, cookies = {"cookie":fbcokis}).text
		eaag = re.search("(EAAG\w+)",str(ftoken))
	except:
		slp(1)
		login()
	global totaldmp,count
	try:
		token=open('data/token.txt','r').read()
		fbcokis = open("data/cookie.txt", "r").read()
	except FileNotFoundError:
		print("[*] Login Not Found")
		slp(1)
		cmd('rm -rf data/token.txt')
		login()
	try:
		cmd('clear')
		os.system("clear")
		print(logo)
		now = datetime.datetime.now()
		print("Date and Time ")
		print(now.strftime("%y-%m-%d %H:%M:%S"))
		hostnm = socket.gethostname()
		ipaddress = socket.gethostbyname(hostnm)
		print("ip address is :", ipaddress)
		print("_____________________________________")
		try:
			print("cookies already login")
			fbbuid = input("[->] Enter Public ID Link : ")
			dmp = requests.get("https://graph.facebook.com/"+fbbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
			for idnm in dmp['friends']['data']:
				totaldmp+=1
				fbidz.append(idnm['id'])
		except KeyError:
			print("[*] Public ID Not Found")
			main()
		filepath = input("[>>] Enter File Path : ")
		print("")
		print(47*"\033[1;37;1m-")
		apnd = open(filepath,'w')
		for fbuid in fbidz:
			count += 1
			try:
				dmp = requests.get("https://graph.facebook.com/"+fbuid+"?fields=friends.limit(5000)&access_token="+token,cookies = {"cookie":fbcokis}).json()
				for idnm in dmp['friends']['data']:
					apnd.write(idnm['id']+"|"+idnm['name']+'\n')
				print("\x1b[1;92m[>>] Dumping UID From : " + fbuid)
			except KeyError:
				print('\x1b[1;91m[>>] Dumping UID From : ' + fbuid)
		apnd.close()
		print(47*"\033[1;37;1m-")
		ch_x1 = input("[->] DoYou Want to Use DuplicateID Cuter (n/y) : ")
		if ch_x1 in ["yes","Yes","YES","Y","y"]:
			newfile = input("[->] File Without Duplicate ID Save As : ")
			os.system('sort -r '+filepath+' | uniq > '+newfile)
			ch_x2 = input("[->] DoYou Want to Use ID Separator (n/y) : ")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(newfile)
			else:
				print(47*"-")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {newfile} \x1b[0;37m")
				print(47*'-')
				input("[>>] Press Inter to go Back < ")
				menu()
		else:
			print('\n')
			ch_x2 = input("[->] Do You Want to Use ID Separator (n/y) : \033[1;32;1m")
			if ch_x2 in ["yes","Yes","YES","Y","y"]:
				grep(filepath)
			else:
				print(47*'\033[1;37;1m-')
				print (f"\x1b[0;37m Total ID Dump :\x1b[1;92m {totaldmp}")
				print (f"\x1b[0;37m Your Dump File Save As :\x1b[1;92m {filepath} ")
				print(47*'\033[1;37;1m-')
				input("[>>] Press Inter to go Back < ")
				menu()
	except Exception as e:
		print("[>>] Error : %s"%e)
		exit("")
if __name__ == '__main__':
	Jadu()