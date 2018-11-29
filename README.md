# TempertureMqqtPiPython
Script to check the temparature from a sensor connected to a raspberry pi and send the data to mqqt

# Credit
https://www.earth.li/~noodles/blog/2018/05/rpi-mqtt-temp.html

# Instructions
Enable 1 wire bus
adding dtoverlay=w1-gpio line to /boot/config.txt

Install pip3 and mqtt library
sudo apt-get install python3-pip
sudo pip3 install paho-mqtt

Download mqtt-temp.py script.  Edit the address and credentials for the broker.  If needed add the path to the brokers CA (For self signed certs), otherwise remove tls parameter from publish.single tls={"ca_certs":""})

Create /etc/systemd/system/mqtt-temp.service

start service and enable it for auto on boot
systemctl start mqtt-temp
systemctl enable mqtt-temp

# Wiring notes
https://cdn-shop.adafruit.com/datasheets/DS18B20.pdf
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/

# Misc
pip for python 3 on pi https://stackoverflow.com/questions/10763440/how-to-install-python3-version-of-package-via-pip-on-ubuntu
