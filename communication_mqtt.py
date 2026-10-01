from PySide6.QtCore import Qt,QThread
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
class send_mqtt():
    def send(self, topic, value, hostname, port=1883):
       # print("DEBUG")
       # print("topic    =", repr(topic))
        #print("value    =", repr(value))
        #print("hostname =", repr(hostname))
        #print("port     =", repr(port))
        publish.single(
            topic=topic,
            payload=value,
            hostname=hostname,
            port=port
        )

        #print("MQTT OK")
class Fetch_mqtt(QThread):
    def __init__(self,broker,port,topic_read):
        super().__init__()
        self.broker=broker 
        self.port=port 
        self.topic_read=topic_read
        self.data=None 
    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Connection failed: {reason_code}")

            
    def on_message(self, client, userdata, message):
        #print("je suis dans le message") for debug 
        v = message.payload.decode("utf-8")
        self.data = v

    def run(self):
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        # Connexion au broker
        client.connect(self.broker, self.port)
        # Abonnement au topic
        client.subscribe(self.topic_read)
        # loop forever
        client.loop_forever()
class MQTT(Fetch_mqtt, send_mqtt) :
    def __init__(self,broker,port,topic_read):
            super().__init__(broker,port,topic_read)
    
