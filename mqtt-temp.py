#!/usr/bin/python3

import glob
import time
import paho.mqtt.publish as publish

#MQTT broker address and credentials
Broker = ''
auth = {
    'username': '',
    'password': '',
}

#MQTT topic
pub_topic = 'home/temperature'

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
    valid = False
    temp = 0
    with open(device_file, 'r') as f:
        for line in f:
            if line.strip()[-3:] == 'YES':
                valid = True
            temp_pos = line.find(' t=')
            if temp_pos != -1:
                temp = float(line[temp_pos + 3:]) / 1000.0
                temp_f = 9.0/5.0 * temp + 32
                temp_f = round(temp_f, 2)

    if valid:
        return temp_f
    else:
        return None


while True:
    temp = read_temp()
    if temp is not None:
      try:
        publish.single(pub_topic, str(temp),
                hostname=Broker, port=8883,
                auth=auth, tls={"ca_certs":""})
      except:
        print("Error posting info to mqqt")
    time.sleep(60)
