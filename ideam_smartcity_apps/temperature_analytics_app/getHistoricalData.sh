#!/bin/bash
#OWNER_API_KEY="6a1236dd9569454db85920455b91d736"
#LISTENING_DEVICE_NAME="5CCF7F3D7499"
#num_data_points=1
#url="'https://smartcity.rbccps.org/api/0.1.0/historicData?pretty=true&sort=@timestamp:desc&size="
#url+=$num_data_points
#url+="' -H 'apikey:"
#url+=$OWNER_API_KEY
#url+="' -H 'Content-Type: application/json' -d '{ \"query\":{ \"multi_match\":{\"query\":\""
#url+=$LISTENING_DEVICE_NAME
#url+="\", \"fields\" : [\"_all\"]}}}'"
#echo $url 
curl -XGET -k 'https://smartcity.rbccps.org/api/0.1.0/historicData?pretty=true&sort=@timestamp:desc&size=1' -H 'apikey: 6a1236dd9569454db85920455b91d736' -H 'Content-Type: application/json' -d '{ "query":{ "multi_match":{"query":"5CCF7F3D7499", "fields" : ["_all"]}}}'