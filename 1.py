import numpy as np

import cv2, json
import numpy as np


def send_request():
	import requests

	url = 'https://digitalocean-28a4c.firebaseio.com/temp.json'

	response = json.loads(requests.get(url).text)["temp"]


	temp1 = '"' + "temp" + '"'

	data_gender = '{' + temp1 + ':' + str(response+1) + '}'


	response_gender = requests.patch(url, data=data_gender)
	# response = requests.patch(url, data=)

send_request()