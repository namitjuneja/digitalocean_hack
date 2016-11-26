import numpy as np

import cv2
import numpy as np


def send_request(i):
	import requests

	url = 'https://digitalocean-28a4c.firebaseio.com/temp.json'



	temp1 = '"' + "temp" + '"'

	data_gender = '{' + temp1 + ':' + str(i) + '}'


	response_gender = requests.patch(url, data=data_gender)
	# response = requests.patch(url, data=)

count = 0
cap = cv2.VideoCapture(0)

while(1):
	count += 1


	# Take each frame
	_, frame = cap.read()

	if count % 50 == 0:

		# Convert BGR to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		sum = 0
		rows = len(hsv)
		cols = len(hsv[0])


		for row in range(0,rows,10):
			for col in range(0,cols,10):
				sum += hsv[row][col][2]

		br = sum / (rows*cols/100)

		print "br", br


		final_br = float(br)/float(200)

		send_request(final_br)


	cv2.imshow('frame',frame)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()