import time
from paho.mqtt import client as mqtt_client

# Configuration MQTT
broker = "test.mosquitto.org"
port = 1883
topic = "/sender"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    def on_disconnect(client, userdata, rc):
        print(f"Disconnected from MQTT Broker, code={rc}")

    client = mqtt_client.Client(
        mqtt_client.CallbackAPIVersion.VERSION1,
        client_id="bipeur-producer"
    )

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    print(f"Connexion à {broker}:{port}...")

    client.connect(broker, port, keepalive=60)

    return client


def publish(client, message):
    result = client.publish(topic, message)

    if result[0] == 0:
        print(f"Message envoyé : `{message}` sur `{topic}`")
    else:
        print("Échec de l'envoi du message")


def run():
    client = connect_mqtt()

    # Démarre la boucle MQTT
    client.loop_start()

    # Attend la connexion
    time.sleep(1)
    while 1==1 : 
    # Envoie le message
         publish(client, "1")

    # Attend que le message soit envoyé
         time.sleep(1)

    # Arrête la boucle MQTT
    client.loop_stop()

    # Déconnexion
    client.disconnect()


if __name__ == "__main__":
    run()
