
#define LED_L 2 


void setup() {
 
  pinMode(LED_L, OUTPUT);
}

void loop() {

  digitalWrite(LED_L, HIGH);  
  delay(1000);                      
  digitalWrite(LED_L, LOW);   
  delay(1000);      
                 
}