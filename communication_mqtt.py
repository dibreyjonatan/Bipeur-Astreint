from PySide6.QtCore import Qt,QThread
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
class send_mqtt():
    def send(topic,value,hostname) : 
        publish.single(topic, value, hostname)
class Fetch_mqtt(QThread):
    def __init__(self,broker,port):
        super().__init__()
        self.broker=broker 
        self.port=port 
    def on_connect(self, reason_code):
        
        if reason_code.is_failure:
           text=f"Failed to connect: {reason_code}. loop_forever() will retry connection"
           print(text)
        else :
           text="connected successfully"
           print(text)
           
    def on_message(self, message):
    
        v=(str(message.payload.decode("utf-8")))
        v=v.split(',')
        return (v)
    def run(self):
        client= mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        #connect to the broker
        client.connect(self.broker,self.port)
        #sunscribe to the topic 
        client.subscribe("/data")
        client.loop_forever() 

class MQTT(Fetch_mqtt, send_mqtt) :
    def __init__(self,broker,port):
            super().__init__(broker,port)
    
