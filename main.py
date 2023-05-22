# IMPORTS -----------------------------------------------------------------------
import command
# text to speech
import gtts
import playsound

# GET QUERY ---------------------------------------------------------------------
def getQuery_():
	query = input()
	return query

def speak_(query):
	tts = gtts.gTTS(command.command_(query))
	tts.save("response.mp3")
	playsound.playsound("response.mp3")

# MAIN -------------------------------------------------------------------------
if __name__ == '__main__':

	while True:
		# for now take query in as a text input on terminal
		print('please enter query')
		query = getQuery_().lower()
		speak_(query)


