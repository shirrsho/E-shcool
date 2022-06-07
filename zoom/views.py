from distutils.log import info
from django.shortcuts import render,redirect
import jwt
import requests
import json
from time import time

from zoom.forms import MeetingForm
from zoom.models import Meeting

# Enter your API key and your API secret
API_KEY = 'tSULkbOURwadQ_quYZHNoA'
API_SEC = '9aKKKTN2eEuA7iAfTijS2snoqhS3TLzasEb1'

def zoom(request):
    # run the create meeting function
    #createMeeting()
    return render(request, 'zoom/zoom.html')

def generateToken():
	token = jwt.encode(

		# Create a payload of the token containing
		# API Key & expiration time
		{'iss': API_KEY, 'exp': time() + 5000},

		# Secret used to generate token signature
		API_SEC,

		# Specify the hashing alg
		algorithm='HS256'
	)
	return token


# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
				"type": 2,
				"start_time": "2019-06-14T10: 21: 57",
				"duration": "45",
				"timezone": "Europe/Madrid",
				"agenda": "test",

				"recurrence": {"type": 1,
								"repeat_interval": 1
								},
				"settings": {"host_video": "true",
							"participant_video": "true",
							"join_before_host": "False",
							"mute_upon_entry": "False",
							"watermark": "true",
							"audio": "voip",
							"auto_recording": "cloud"
							}
				}

# send a request with headers including
# a token and meeting details


def createMeeting(request):
	headers = {'authorization': 'Bearer ' + generateToken(),
			'content-type': 'application/json'}
	r = requests.post(
		f'https://api.zoom.us/v2/users/me/meetings',
		headers=headers, data=json.dumps(meetingdetails))

	y = json.loads(r.text)
	join_URL = y['join_url']
	meetingPassword = y["password"]

	return {
		'link': join_URL,
	 	'password': meetingPassword
	}

def createForm(request):
	infos = createMeeting(request)
	if(request.method == "POST"):
		form = MeetingForm(request.POST)
		if(form.is_valid):
			t = form.save(commit=False)
			t.infos = infos['link']
			print(t.infos)
			t.save()
			return redirect('/zoom/form_list')

	else:
		form = MeetingForm()
	return render(request, 'zoom/createmeeting.html',{'form':form, 'infos':infos})

def zoom_list(request):
    zooms = Meeting.objects.all()
	#print("Start talking with the bot")
    return render(request, 'zoom/form_list.html', {
        'zooms': zooms
    })
