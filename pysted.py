#-*-coding:utf-8-*-
from mechanize import Browser
from os import system
from sys import argv


bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

k_link = []

def logo():
	system("clear")
	print bold+"\t\t\t PySted | Python Script Share"+endcolor
	print bold+"\t\t\t------------------------------"+endcolor
	print "\t\t\t--==[{}CoderLab / ExitStars{}]==--".format(yellow, endcolor)
	print bold+"\t\t\t------------------------------"+endcolor

def yapistir():
	br = Browser()
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0')]
	br.set_handle_robots(False)

	br.open("http://paste.ubuntu.com")
	br.select_form("pasteform")

	br['poster'] = coder
	br.find_control(name="syntax").value = ["python"]

	dosya_ac = open(dosya)
	kodlar = dosya_ac.read()
	br['content'] = kodlar
	br.submit()
	for link in br.links():
		k_link.append(link.url)

logo()
if len(argv) != 5:
	coder = raw_input(bold+yellow+"Kullanıcı Adınız: "+endcolor)
	dosya = raw_input(bold+yellow+"Dosya Adı: "+endcolor)
else:
	coder = argv[2]
	dosya = argv[4]

yapistir()

l_link = k_link[0]
y_link = l_link.split("/")
a_link = "http://paste.ubuntu.com/"+y_link[1]+"/"
print bold+blue+"Kayıtlı Kodlar"+endcolor+": "+a_link
raw_input()
