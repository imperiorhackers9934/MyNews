import pyttsx3
import requests
import json
import os
import sys
import time
#=======Color=====#
N = '\033[0m'    # Normal Color
Y = '\033[1;33m' # Yellow Color
R = '\033[1;31m' # Red Color
G = '\033[1;32m' # Green Color
W = '\033[1;37m' # White Color
D = '\033[1;9;31m'  # DelBold Color
#==================#
def speak(news):
    engine.say(news)
    engine.runAndWait()
def get_news(x):
    src = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0d67f467dfff4f0281713fcd65eaa1d4')
    if(src.status_code == 404 or src.status_code == False):
        print("===================================================")
        print("----------------[News Not Found]------------------")
        print("===================================================")
    news = json.loads(src.content)
    lol = str(news['articles'][x]['title'])
    lol1 = str(news['articles'][x]['description'])
    lol2 = int(news['totalResults'])
    if(x == 1):
        speak(f"Welcome Sir News Number{x}")
    else:
        speak(f"News Number{x}")
    print("%s===================================================%s" % (Y,N))
    print(f"%s-------------[ News Number: {x} ]------------------%s" % (G,N))
    print("%s===================================================%s" % (Y,N))
    print(f"  Title :>> {lol}")
    print("%s===================================================%s" % (Y,N))
    print(f"  Description :>> {lol1}")
    print("")
    print("")
    speak(lol)
    speak(lol1)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 178)
os.system('cls')
print(''' %s
    ███╗   ██╗███████╗██╗    ██╗███████╗
    ████╗  ██║██╔════╝██║    ██║██╔════╝
    ██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗
    ██║╚██╗██║██╔══╝  ██║███╗██║╚════██║
    ██║ ╚████║███████╗╚███╔███╔╝███████║
    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝
%s''' % (G,N)
+''' %s                                   
    [Developed by Imperior Hackers]
%s''' % (Y,N))
print("%s   [1] Start News%s" % (G,N))
print("%s   [2] Exit Program%s" % (G,N))
print("")

try:
    Abc = int(input("Select :>> "))

    if (Abc == 1 or Abc == "01"):
        x = 1
        while(True):
            get_news(x)
            x = x+1
    elif(Abc == 2 or Abc == "02"):
        sys.exit()
    else:
        print("%sWrong Input,Please try again%s" % (R,N))
        time.sleep(1)
        os.system("python News.py")

except ValueError: 
    print("%sWrong Input,Please try again%s" % (R,N))
    time.sleep(1)
    os.system("python News.py")