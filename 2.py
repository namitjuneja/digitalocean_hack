def send_request(i):
	import requests

	url = 'https://digitalocean-28a4c.firebaseio.com/temp.json'



	temp1 = '"' + "temp" + '"'

	data_gender = '{' + temp1 + ':' + str(i) + '}'


	response_gender = requests.patch(url, data=data_gender)
	# response = requests.patch(url, data=)

for i in range(0,100,10):
	send_request(float(i)/float(100))