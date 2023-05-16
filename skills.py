# IMPORTS ----------------------------------------------------------------------------

# import datetime
import datetime
# import requests
import requests


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
	return "This is Tobias Mark " + str(t.getMk()) + " version " + str(t.getVersion())

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

# get weather in Tobias location
def localWeather_():
	url="http://api.openweathermap.org/data/2.5/weather?q=Fredericksburg&units=imperial&appid=da1b3912cd52cc458f77d90cae5c2986"
	res=requests.get(url)
	data=res.json()
	temp=data['main']['temp']
	return "The weather in Fredericksburg is " +(str(temp))


# TESTING -------------------------------------------------------------------------------

t = Tobias()
print(localWeather_())