import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple', 'orange', 'banana', 'peach']
	#return bottle.template('hello_world', username="Henry", things=mythings)
	return bottle.template('hello_world', {'username': "Henryy",
											'things': mythings})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
