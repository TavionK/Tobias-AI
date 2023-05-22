# IMPORTS -------------------------------------------------------------------------------
import skills

# FIND SKILL ---------------------------------------------------------------------------
# All inputs will be transformed to lowercase

def command_(query):
	if 'tobias' in query and 'time' in query:
		return skills.time_()

	if 'tobias' in query and 'date' in query:
		return skills.date_()

	if 'tobias' in query and 'version' in query:
		return skills.version_()

	if 'tobias' in query and 'your name' in query:
		return skills.name_()

	if 'tobias' in query and 'your creator' in query:
		return skills.creator_()

	if 'tobias' in query and 'your birthday' in query:
		return skills.bday_()

	if 'tobias' in query and 'your age' in query or 'how old are you' in query:
		return skills.age_()

	if 'tobias' in query and 'in' in query and 'weather' in query or 'temperature' in query:
		# split the query after in to find the location
		x = query.split('in ')
		# split it after the location in case other words are picked up
		all_after_in = x[1].split()
		place = all_after_in[0]
		return skills.weather_(place)

	elif 'tobias' in query and 'weather' in query or 'temperature' in query:
		return skills.weather_()
	
	if 'tobias' in query and 'joke' in query:
		return skills.joke_()

	else:
		return "no valid query"