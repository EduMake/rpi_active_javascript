#set up
get the submodules
init and get submodules for active_javascript

#Node for grunt
curl -sLS https://apt.adafruit.com/add | sudo bash
sudo apt-get install node npm
npm install
sudo npm install -g grunt-cli

#Temp sensor setup

[sourcecode language=”bash”]
apt-get install libusb-dev
git clone https://github.com/petervojtek/usb-thermometer.git
cd usb-thermometer/
cp 99-tempsensor.rules /etc/udev/rules.d/
make
cp pcsensor /usr/local/bin/
[/sourcecode]

Reboot the server.

To test the dongle run the pcsensor command .
You must get this kind of output.

2012/04/11 14:30:50 Temperature 60.58F 15.88C

From http://bailey.st/blog/2012/04/12/dirt-cheap-usb-temperature-sensor-with-python-sms-alerting-system/



