import random
from paho.mqtt import client as mqtt_client

broker = "test.mosquitto.org"
port = 1883
topic = "/envoie"

client_id = f"python-mqtt-{random.randint(0, 100000)}"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(topic)
            print(f" Abonné au topic : {topic}")
        else:
            print(f" Failed to connect, return code {rc}")

    def on_disconnect(client, userdata, rc):
        print(f"Déconnecté du broker, code={rc}")

    def on_message(client, userdata, msg):
        message = msg.payload.decode("utf-8")
        print(f"Received `{message}` from `{msg.topic}`")

    client = mqtt_client.Client(
        mqtt_client.CallbackAPIVersion.VERSION1,
        client_id=client_id
    )

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    print(f"Connexion à {broker}:{port}...")
    client.connect(broker, port, keepalive=60)

    return client


def run():
    client = connect_mqtt()

    # Important : démarre la boucle MQTT
    client.loop_forever()


if __name__ == "__main__":
    run()
