import time
import sys
import subprocess
import os
import base64
import uuid
import datetime
import traceback
import base64
import json
from time import gmtime, strftime
import math
import random, string
import time
import psutil
import uuid 
from getmac import get_mac_address

start = time.time()
uuid2 = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
end = time.time()
row = { }
row['host'] = os.uname()[1]
row['temperature'] = '70'
row['end'] = '{0}'.format( str(end ))
row['te'] = '{0}'.format(str(end-start))
row['systemtime'] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
row['cpu'] = psutil.cpu_percent(interval=1)
usage = psutil.disk_usage("/")
row['diskusage'] = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
row['memory'] = psutil.virtual_memory().percent
row['id'] = str(uuid2)
eth_mac = get_mac_address(interface="wlp2s0")
row['macaddress'] = ( str(eth_mac) )
json_string = json.dumps(row)
print(json_string)
