import requests
import wget
import os
import os.path
import subprocess

from bs4 import BeautifulSoup, SoupStrainer

#Testing your internet speed. This is optional
#subprocess.call(['speedtest'])


urlIP = "http://ksuweb.kennesaw.edu/~jgarrido/CS4720_assign/"
urlOS = "http://ksuweb.kennesaw.edu/~jgarrido/CS3502_assign/"
urlIPNotes = "http://ksuweb.kennesaw.edu/~jgarrido/CS4720_notes/"
urlOSNotes = "http://ksuweb.kennesaw.edu/~jgarrido/CS3502_notes/"
OUTPUT_DIR_IP = '' #output directory for internet programming
OUTPUT_DIR_OS = ''#output directory for OS
OUTPUT_DIR_AA = ''#output directory for algorithm analysis
Assignments = '' #Folder for assigments
Notes = '' #Folder for Notes
file_types = ['.a','.b','.css','.d','.f','.g','.i','.j','.q','.p','.sqlite','.zip']

webdir = "http://ksuweb.kennesaw.edu"

def urlParserGarrido(url, directory, folder):
	tmp = directory
	for file_type in file_types:
		response = requests.get(url)
		for link in BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer("a")):
			
			directory = tmp
			if link.has_attr("href"):
				if file_type in link["href"]:
					full_path = webdir + str(link["href"])
					full_path = full_path.replace("%20", " " )
					filename = full_path.replace(url,'')
					if not os.path.exists(directory+folder+filename):
						print("\nDownloading: " + full_path + '\n')
						directory = (directory+folder)
						print(directory)
						wget.download(full_path, directory)
						print("\n")
					else:
						print("You already have:  " + filename)


def urlParserDKIM(url, directory, folder):
	tmp = directory
	for file_type in file_types:
		response = requests.get(url)
		for link in BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer("a")):
			
			directory = tmp
			if link.has_attr("href"):
				if file_type in link["href"]:
					full_path = webdir+'/~dkim76/courses/Fall 2016 - CS4306/'+str(link["href"])
					full_path = full_path.replace("%20", " " )
					filename = full_path.replace(webdir+'/~dkim76/courses/Fall 2016 - CS4306/','')
					if not os.path.exists(directory+filename):
						print("\nDownloading: " + full_path + '\n')
						directory = (directory+folder)
						print(directory)
						wget.download(full_path, directory)
						print("\n")
					else:
						print("You already have:  " + filename)

print('\n\n----------------------------------------------------------\n')
print('--------------Internet Programming------------------------\n')
print('----------------------------------------------------------\n')
print('\n\nAssignments\n')
urlParserGarrido(urlIP,OUTPUT_DIR_IP,Assignments)
print('\n\nNotes\n')
urlParserGarrido(urlIPNotes,OUTPUT_DIR_IP,Notes)

print('\n\n----------------------------------------------------------\n')
print('-----------------Operating Systems------------------------\n')
print('----------------------------------------------------------\n')
print('\n\nAssignments\n')				
urlParserGarrido(urlOS,OUTPUT_DIR_OS,Assignments)
print('\n\nNotes\n')
urlParserGarrido(urlOSNotes,OUTPUT_DIR_OS,Notes)


print('\n\n----------------------------------------------------------\n')
print('-----------------Algorithm Analysis------------------------\n')
print('----------------------------------------------------------\n')

urlParserDKIM("http://ksuweb.kennesaw.edu/~dkim76/courses/Fall%202016%20-%20CS4306/Fall%202016%20-%20CS4306.html",OUTPUT_DIR_AA,"")
print("\n\n\n")
input("Press any enter to quit...\n\n\n")