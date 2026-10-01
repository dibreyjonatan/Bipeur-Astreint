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
    def on_connect(self,client, userdata, flags, reason_code, properties):
        global publish_state
        if reason_code.is_failure:
           text=f"Failed to connect: {reason_code}. loop_forever() will retry connection"
           print(text)
        else :
           text="connected successfully"
           print(text)
           
    def on_message(self,client, userdata, message):
        global inc,time,temperature,humidity,air,light,soil,publish_state
        v=(str(message.payload.decode("utf-8")))
        v=v.split(',')
        flow_data=[int(v[0]),int(v[1]),int(v[2]),int(v[3]),int(v[4])]
        print(flow_data)


class MQTT(Fetch_mqtt, send_mqtt) :
    pass 
