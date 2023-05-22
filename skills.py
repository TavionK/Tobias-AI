# IMPORTS ----------------------------------------------------------------------------

# import datetime
import datetime
# import requests
import requests
# import time
import time


# import tobias class
from tobias import Tobias


# GENERIC SKILLS ----------------------------------------------------------------------

# tell the current time
def time_():
	return "The current time is " + datetime.datetime.now().strftime("%I:%M")

# tell the date
def date_():
	return "The date is " + datetime.datetime.now().strftime("%B %d, %Y")

# gets the version
def version_():
	return "This is Tobias Mark " + str(t.getMk())

# gets the name
def name_():
	return "My name is " + t.getName() + ". Which stands for 'Tavion's Original But Intelligent Artificial System'"

# gets the creator's (me) name
def creator_():
	return "I was created by " + t.getCreator() + ". Tobias Mark " + str(t.getMk()) + " began production on " + str(t.getBday())

# gets birthday
def bday_():
	return "I was created on " + str(t.getBday())

# gets age
def age_():
	return "I am " + t.getAge()

# ADVANCED SKILLS -----------------------------------------------------------------------

# get weather in a specific location
def weather_(*args):
	if len(args) == 1:
		url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=da1b3912cd52cc458f77d90cae5c2986".format(args[0])
		res=requests.get(url)
		data=res.json()
		temp=data['main']['temp']
		return "The weather in " + args[0] + " is " + str(int(temp))
	else:
		url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=da1b3912cd52cc458f77d90cae5c2986".format(t.getLoc())
		res=requests.get(url)
		data=res.json()
		temp=data['main']['temp']
		return "The weather in " + t.getLoc() + " is " + str(int(temp))

# gets a joke
def joke_():
	url = "https://official-joke-api.appspot.com/random_joke"
	res=requests.get(url)
	data=res.json()
	setup =data['setup']
	punchline=data['punchline']

	return str(setup) + "       " + str(punchline)

t = Tobias()






































# spacer
