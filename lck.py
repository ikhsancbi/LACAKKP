
import sys, os, time, signal, webbrowser, platform, subprocess

#~~~~ Keybord interruption ~~~~
def signal_handler(signal, frame):
		KURO()
		LOGO()
		print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
		time.sleep(2)
		menu()
signal.signal(signal.SIGINT, signal_handler)

#~~~ Function KURO ~~~~
def lck():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')

#~~~~ M E N U ~~~~
def LOGO():
	lck()

	print ('''
     ''')

def menu():

	LOGO()
	time.sleep(1) 
	print ("""
\033[1;33m    	1.\033[1;m Name
\033[1;33m     	2.\033[1;m Phone number
\033[1;33m     	3.\033[1;m IP
\033[1;33m     	4.\033[1;m Username
\033[1;36m       99. About
	""")

	OPT = input("\033[1;35m  Select:\033[1;m ")
	if OPT == "1":
         ID()
	elif OPT == "2":
		 PHONE()
	elif OPT == "3":
		 IP()
	elif OPT == "4":
		USER()
	elif OPT == "99":
		lck()
		menu()
	else:
		lck()
		LOGO()
		print ("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def ID():
	lck()
	LOGO()  
	time.sleep(1)
	Name = input(" First Name:\033[1;m ")
	F_name = input("\033[1;35m Last name:\033[1;m ")


	print ("""\033[1;34m
 1. Facebook
 2. Pipl
 3. Flickr
 4. Tumblr
 5. Youtube
 6. Github
==============================
\033[1;36m   0. Exit   00. All
		""")
	Tracker = input("\033[1;35m Tr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")

	if Tracker == "1":
		KURO()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		lck()
		webbrowser.open('https://pipl.com/search/?q='+Name+ +F_name)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		lck()
		webbrowser.open('https://www.flickr.com/search/people/?username='+Name+ +F_name)
		time.sleep(2)
		menu()
	elif Tracker == "4":
		lck()
		webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "5":
		lck()
		webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "6":
		lck()
		webbrowser.open('https://github.com/'+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		lck()
		webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.flickr.com/search/people/?username='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://pipl.com/search/?q='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "0":
		lck()
		EXITMENU()
	else:
		lck()
		LOGO()
		print ("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def USER():
	lck()
	LOGO()  
	time.sleep(1)
	User = input(" Username:\033[1;m ")

	print ("""\033[1;34m
  1. Facebook         
  2. Steam  
  3. Twitter    
  4. Twitch
  5. Instagram
  6. kik
  7. Tiktok
  8. MyAnimeList
  9. Youtube
  10. Reddit
  11. Spotify
  12. Realmeye
  13. Discord Tracker
  14. Minecraft Profile
  15. Osu
  16. Roblox
  17. Xbox Live
  18. Github
 00. All
\033[1;m=========================
\033[1;36m  \033[1;31m  0. Exit
		""")
	Tracker = input("\033[1;35m Tr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;m ")

	if Tracker == "1":
		lck()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+User)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		lck()
		webbrowser.open('https://steamcommunity.com/id/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		lck()
		webbrowser.open('https://twitter.com/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "4":
		lck()
		webbrowser.open('https://www.twitch.tv/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "5":
		lck()
		webbrowser.open('https://www.instagram.com/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "6":
		lck()
		webbrowser.open('https://ws2.kik.com/user/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "7":
		lck()
		webbrowser.open('https://www.tiktok.com/@'+User)
		time.sleep(2)
		menu()
	elif Tracker == "8":
		lck()
		webbrowser.open('https://myanimelist.net/profile/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "9":
		lck()
		webbrowser.open('https://www.youtube.com/results?search_query='+User)
		time.sleep(2)
		menu()
	elif Tracker == "10":
		lck()
		webbrowser.open('https://www.reddit.com/user/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "11":
		lck()
		webbrowser.open('https://open.spotify.com/user/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "12":
		lck()
		webbrowser.open('https://www.realmeye.com/player/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "13":
		lck()
		webbrowser.open('https://tracr.co/users/1/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "14":
		lck()
		webbrowser.open('https://namemc.com/profile/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "15":
		lck()
		webbrowser.open('https://osu.ppy.sh/users/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "16":
		lck()
		webbrowser.open('https://www.roblox.com/user.aspx?username='+User)
		time.sleep(2)
		menu()
	elif Tracker == "17":
		lck()
		webbrowser.open('https://xboxgamertag.com/search/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "18":
		lck()
		webbrowser.open('https://github.com/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		lck()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+User)
		time.sleep(2)
		webbrowser.open('https://steamcommunity.com/id/'+User)
		time.sleep(2)
		webbrowser.open('https://twitter.com/'+User)
		time.sleep(2)
		webbrowser.open('https://www.twitch.tv/'+User)
		time.sleep(2)
		webbrowser.open('https://www.instagram.com/'+User)
		time.sleep(2)
		webbrowser.open('https://ws2.kik.com/user/'+User)
		time.sleep(2)
		webbrowser.open('https://www.tiktok.com/@'+User)
		time.sleep(2)
		webbrowser.open('https://myanimelist.net/profile/'+User)
		time.sleep(2)
		webbrowser.open('https://www.youtube.com/results?search_query='+User)
		time.sleep(2)
		webbrowser.open('https://www.reddit.com/user/'+User)
		time.sleep(2)
		webbrowser.open('https://open.spotify.com/user/'+User)
		time.sleep(2)
		webbrowser.open('https://www.realmeye.com/player/'+User)
		time.sleep(2)
		webbrowser.open('https://tracr.co/users/1/'+User)
		time.sleep(2)
		webbrowser.open('https://namemc.com/profile/'+User)
		time.sleep(2)
		webbrowser.open('https://osu.ppy.sh/users/'+User)
		time.sleep(2)
		webbrowser.open('https://www.roblox.com/user.aspx?username='+User)
		time.sleep(2)
		webbrowser.open('https://xboxgamertag.com/search/'+User)
		time.sleep(2)
		webbrowser.open('https://github.com/'+User)
		time.sleep(2)
		menu()
	elif Tracker == "0":
		lck()
		EXITMENU()
	else:
		lck()
		LOGO() 
		print ("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def PHONE():
	lck()
	LOGO()  
	time.sleep(1)
	Num = input(" Number:\033[1;m ")

	print ("""\033[1;34m
  1. Who-called (UK Only)        
  2. Unknownphone   
  3. Kiwisearch (US Only) \033[1;33m	    
 00. All
\033[1;m=========================
\033[1;36m  \033[1;31m  0. Exit
		""")
	Tracker = input("\033[1;35m Tr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;m ")

	if Tracker == "1":
		lck()
		webbrowser.open('https://who-called.co.uk/Number/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		lck()
		webbrowser.open('https://www.unknownphone.com/phone/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		lck()
		webbrowser.open('https://kiwisearches.com/phone/summary?phonenumber='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		lck()
		webbrowser.open('https://who-called.co.uk/Number/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.unknownphone.com/phone/'+Num)
		time.sleep(2)
		webbrowser.open('https://kiwisearches.com/phone/summary?phonenumber='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "0":
		lck()
		EXITMENU()
	else:
		lck()
		LOGO() 
		print ("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def IP():
	lck()
	LOGO()
	ip = input(" Ip:\033[1;m ")

	print ("""\033[1;34m
 
  1. G-force
  2. whatismyipaddress
 00. All\033[1;m
==============================
\033[1;36m    \033[1;31m    0. Exit
		""")
	Tracker = input("\033[1;35m Tr\033[0;31m@\033[1;35mck3r\033[1;m:~\033[1;34m/\033[1;m$\033[1;35m ")
	if Tracker == "1":
		lck()
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		lck()
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		lck()
		time.sleep(2)
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		menu()
	else:
		lck()
		LOGO()
		print ("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

#~~~~ EXIT ~~~~
def EXITMENU():
	lck()
	LOGO()
	time.sleep(2)
	print ("\033[1;m[\033[1;31mX\033[1;m]...\033[1;32mClosing")
	time.sleep(1)
	lck()
	sys.exit()
		
menu()
