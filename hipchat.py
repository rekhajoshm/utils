import json
import codecs
import subprocess
import yaml
import sys
#from django.utils.encoding import smart_str
from pprint import pprint

#todo: Raise exception if no argument auth token passed

#Get all rooms this auth token has access to
parurl ='https://api.hipchat.com/v2/room?auth_token='+ sys.argv[1]
psub = subprocess.Popen(['curl', '', parurl], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
curlstdout, curlstderr = psub.communicate()
data_parent = json.loads(curlstdout)

for i in range(0,len(data_parent["items"])-1):
		
	#Get all history for the iterated room
	childurl ='https://api.hipchat.com/v2/room/' + str(data_parent["items"][i]["id"]) + '/history?auth_token=' + sys.argv[1]
        psub = subprocess.Popen(['curl', '', childurl], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        curlstdout, curlstderr = psub.communicate()
        data = json.loads(curlstdout)

        f = open('hc_msgs', 'w')
        for j in range(0,len(data["items"])-1):
		q = json.dumps(data["items"][j]["message"] + "\n")
                f.write(q)
                #pprint(data["items"][j]["from"]["mention_name"])
                #pprint(str(j) + data["items"][j]["message"])
	        #pprint(data["items"]["message"])	

	f.close()
