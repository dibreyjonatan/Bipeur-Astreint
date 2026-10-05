/*
 * PROFESSIONAL MQTT EXPERIMENT - ESP32
 * * Features:
 * - Non-blocking Architecture (No delay())
 * - Automatic Reconnection (WiFi & MQTT)
 * - LWT (Last Will & Testament) for State Monitoring
 * - JSON Data Serialization
 * - Remote Command Handling
 */

#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#define MAX 100
// ==========================================
// 1. CONFIGURATION (Edit these)
// ==========================================
const char* ssid = "OPPO A73";
const char* password = "123456789";

// MQTT Broker Settings (Using public HiveMQ for demo, change for production)
const char* mqtt_server = "test.mosquitto.org" ;
const int mqtt_port = 1883; 
const char* mqtt_user = ""; // Leave blank for public brokers
const char* mqtt_pass = "";

// Unique Device ID (Must be unique on the broker)
const char* device_id = "ESP32_WROOM_01"; 


const char* topic_recieve   = "/envoie";   

// ==========================================
// 2. GLOBAL OBJECTS & VARIABLES
// ==========================================

WiFiClient espClient;
PubSubClient client(espClient);

#define LED_PIN 2 

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

// ==========================================
// 4. CALLBACK (Handle Incoming Messages)
// ==========================================
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");

  // Convert payload to string for easier handling
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);

  if (String(topic) == topic_recieve ) {
      digitalWrite(LED_PIN, HIGH);
      delay(2000); 
    } 

     //digitalWrite(LED_PIN, LOW);

    }
  
  


// ==========================================
// 5. RECONNECT (The Engine Room)
// ==========================================
void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");

    if (client.connect(device_id, mqtt_user, mqtt_pass)) {
      Serial.println(" connected!");

      client.subscribe(topic_recieve);
      Serial.println("Subscribed to /sender");

    } else {
      Serial.print(" failed, rc=");
      Serial.print(client.state());
      Serial.println(" retrying in 2 seconds");
      delay(2000);
    }
  }
}

// ==========================================
// 6. MAIN SETUP
// ==========================================
void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  
  setup_wifi();
  
  client.setServer(mqtt_server, mqtt_port);
  client.subscribe(topic_recieve);
  client.setCallback(callback);
}

// ==========================================
// 7. MAIN LOOP
// ==========================================
void loop() {
  // Ensure we stay connected
  if (!client.connected()) {
    reconnect();
  }
  client.loop(); // Keep MQTT alive
}