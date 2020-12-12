import aiml
import os
import time, fnmatch, shutil
import forecastio
import datetime

def getWeather():
    api_key = "afee0c0bf36b4671b12c038a5aef80bf"
    lat = -31.967819
    lng = 115.87718
    current_time = datetime.datetime.now()
    forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)
    
    weather = forecast.currently()
    print weather.summary
	#for hourlyData in byHour.data:
	#print hourlyData.temperature
    print weather.temperature
    return;

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

# if os.path.isfile("bot_brain.brn"):
#   kernel.bootstrap(brainFile = "bot_brain.brn")
# else:
#   kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
#   kernel.saveBrain("bot_brain.brn")

kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

#SAVE EACH CONVO TO A FILE
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
fileName = ("Convo-" + timestamp + ".txt")
f = open(os.path.join("OldConversations", fileName), "w+")

# Press CTRL-C or "quit" to break this loop
while True:
    message = raw_input("Enter your message >> ")
    if message == "quit":
        exit()
        fclose()
    # elif message == "save":
    #     kernel.saveBrain("bot_brain.brn")
    # elif message.find("weather"):
    #     getWeather()
    else:
        response = kernel.respond(message)
        print(response)
        f.write("Enter your message >> " + message + "\n")
        f.write(response + "\n")

