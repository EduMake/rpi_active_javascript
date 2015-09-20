#!/usr/bin/python
import signal, time
import cherrypy
import string  
import sys
import subprocess

#sudo pip install cherrypy
cherrypy.config.update("server.conf")

class HouseServer(object):
    def __init__(self, initialcommand="stop"):
        self.status = "stop"
        

    @cherrypy.expose
    def forward(self, speed=95):
        self.status = "forward"
        return self.status
    
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/static/index.html?house")

    @cherrypy.expose
    def getstatus(self):
        return self.status
    
    @cherrypy.expose
    def temp(self):
        output = subprocess.Popen(["/usr/local/bin/pcsensor"], stdout=subprocess.PIPE).communicate()[0]
        output2 = output.split()[4]
        temp = output2[:2]
        return temp
        #if int(temp) &gt; threshold:
    
    def do_command(self, cmd=""):
        if (cmd == "forward"):
            self.forward()
        elif cmd == "backward":
            self.backward()
        elif cmd == "left":
            self.left()
        elif cmd == "right":
            self.right()
        elif cmd == "stop":
            self.stop()
        return self.status
    
    #Replicate original k9 interface
    @cherrypy.expose
    def handle_analog(self, pin, value):
        print (pin.name, value, self.status)
        if (value > 2 and self.status != "stop"):
            if (self.status != "bump"):
                self.oldstatus = self.status
            self.status = "bump"
            explorerhat.motor.one.stop()
            explorerhat.motor.two.stop()
            time.sleep(0.2)
            explorerhat.motor.one.backward()
            explorerhat.motor.two.backward()
            time.sleep(0.7)
                
            time.sleep(0.5)
            
            self.do_command(self.oldstatus)
            
if __name__ == '__main__':
    cherrypy.quickstart(HouseServer(), config="app.conf")
    
    
    
