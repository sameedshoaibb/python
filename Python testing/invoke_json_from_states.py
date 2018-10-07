import json 
import logging
import time

LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="json.log",level=logging.DEBUG,format=LOG_FORMAT)
logger=logging.getLogger()

try:
	with open('states.json') as fx:
		data=json.load(fx)
		logger.debug("Json has been loaded")

	for state in data['book']:
		print state['language']
		time.sleep(5)
	logger.debug("For loop has been run succesfully")
except KeyboardInterrupt:
	logger.error("Unexpected keyboard interruption")
else:
	print "All well that ends well"

