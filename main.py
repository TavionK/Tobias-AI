# IMPORTS -----------------------------------------------------------------------
import command

# GET QUERY ---------------------------------------------------------------------
def getQuery_():
	query = input()
	return query

# MAIN -------------------------------------------------------------------------
if __name__ == '__main__':

	while True:
		# for now take query in as a text input on terminal
		print('please enter query')
		query = getQuery_().lower()

		print(command.command_(query))
