from django.http import JsonResponse
from django.shortcuts import render
from ideam.entity import Entity
import requests
import time
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def get_temperature_data(request):
	#return render(request, 'sequential_analysis_app/homepage.html')
	'''
	"APIKey":"6a1236dd9569454db85920455b91d736","Subscription Queue Name":"smartapplication","ResourceID":"smartapplication","accessEndPoint":https://smartcity.rbccps.org/api/0.1.0/historicData,"Registration":"success","publicationEndPoint":https://smartcity.rbccps.org/api/0.1.0/publish,"resourceAPIInfo":https://rbccps-iisc.github.io,"AllowedAPIs":"publish,subscribe,historic,cat","subscriptionEndPoint":https://smartcity.rbccps.org/api/0.1.0/subscribe
	'''
	OWNER_API_KEY="6a1236dd9569454db85920455b91d736"
	LISTENING_DEVICE_NAME="5CCF7F3D7499"
	RESOURCE_TYPE="Indoor Temperature Humidity and Light Sensor"	
	LISTENING_DEVICE_API_KEY="6a1236dd9569454db85920455b91d736"
	num_data_points = 1

	#API call starts
	'''
	applicationHandler = Entity(LISTENING_DEVICE_NAME, OWNER_API_KEY)
	applicationHandler.set_entity_api_key(LISTENING_DEVICE_API_KEY)
	historical_data=applicationHandler.db("rbccpsEnergy.EM_D0025860")
	return JsonResponse(historical_data)
	'''
	historical_data=os.popen("curl -XGET -k 'https://smartcity.rbccps.org/api/0.1.0/historicData?pretty=true&sort=@timestamp:desc&size=1' -H 'apikey: 6a1236dd9569454db85920455b91d736' -H 'Content-Type: application/json' -d '{ \"query\":{ \"multi_match\":{\"query\":\"5CCF7F3D7F2D\", \"fields\" : [\"_all\"]}}}'").read()

	historical_data=json.loads(json.loads(historical_data)["hits"]["hits"][0]["_source"]["data"])

	historical_data["epoch"]=time.strftime('%H:%M:%S %d-%m-%Y', time.localtime(int(historical_data["epoch"])))

	return render(request, 'temperature_analytics_app/index.html', {
		"time":historical_data["epoch"],
		"temperature":historical_data["temperature"],
		"humidity": historical_data["humidity"],
		"light_state": historical_data["light_state"] ,"device_id":LISTENING_DEVICE_NAME})


	#return JsonResponse(json.loads(historical_data))