#include <esp8266WiFi.h>
#include <WiFiClient.h>
#include <esp8266WebServer.h>
#include <esp8266mDNS.h>
#include <FS.h>
#include <Servo.h>

#define Motor_AE D1      //Motor A/B,E enable,D Direction
#define Motor_AD D3

#define Motor_BE D2
#define Motor_BD D4

#define R_AHEAD HIGH
#define L_AHEAD LOW

String command;

// D1 On / Off 
// D2 On / Off
// D3 Direction

esp8266WebServer server(80);

const int led = 13;


Servo servos[9];
uint8_t servo_pins[9] = {D0,D1,D2,D3,D4,D5,D6,D7,D8};
uint8_t count = 9;
void setAngle(uint8_t di,uint8_t vi){
  if(di< 9 && vi < 180)
    servos[di].write(vi);
}
void attachServos(){
  for (uint8_t i = 0; i < count; ++i){
    servos[i].attach(servo_pins[i]);
  }
}

void detachServos(){
  for (uint8_t i = 0; i < count; ++i){
    servos[i].detach();
  }  
}


void carInit(){  
   
  pinMode(Motor_AE, OUTPUT);
  pinMode(Motor_AD, OUTPUT);   
  pinMode(Motor_BE, OUTPUT);
  pinMode(Motor_BD, OUTPUT);

  Serial.begin(115200); 
  Serial.println("Car begin"); 
  } 
void goAhead(){ 
      digitalWrite(Motor_AE, HIGH);
      digitalWrite(Motor_AD, L_AHEAD);
      digitalWrite(Motor_BE, HIGH);
      digitalWrite(Motor_BD, R_AHEAD);
  }

void goBack(){ 
      digitalWrite(Motor_AE, HIGH);
      digitalWrite(Motor_AD, !L_AHEAD);
      digitalWrite(Motor_BE, HIGH);
      digitalWrite(Motor_BD, !R_AHEAD);
  }

void goRight(){ 
      digitalWrite(Motor_BE, LOW);
      digitalWrite(Motor_AE, HIGH);
      digitalWrite(Motor_AD, L_AHEAD);
  }

void goLeft(){
      digitalWrite(Motor_BE, HIGH);
      digitalWrite(Motor_AE, LOW);
      digitalWrite(Motor_BD, R_AHEAD);
  }

void stopRobot(){  
      digitalWrite(Motor_AE, LOW);
      digitalWrite(Motor_BE, LOW);
  }

void handleNotFound(){
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}

void setup(void){
  
  Serial.begin(115200);
  carInit();
  SPIFFS.begin();
  attachServos();
  Serial.println("Servos attached");
  server.serveStatic("/", SPIFFS, "/index.html");

const char* ssid = "AI";
const char* password = "raspberry";
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }








  server.on("/set-servo", [](){
    String uri = server.uri();
    Serial.println(uri);
    String di = server.arg("di");
    String vi = server.arg("vi");
    Serial.println("di="+di+" vi="+vi);
    setAngle(di.toInt(),vi.toInt());
    server.send(200, "text/plain", String("set to ")+"di="+di+" vi="+vi);
  });

  server.on("/get", [](){
    String uri = server.uri();
    Serial.println(uri);
    command = server.arg("command");
    if(command == "forward")
      goAhead();
    else if(command == "backward")
      goBack( );
    else if(command == "left")
      goLeft();
    else if(command == "right")
       goRight();
    else if(command == "stop")
       stopRobot();
    Serial.println(command);
//    setCorlor(red.toInt(),green.toInt(),blue.toInt());
    server.send(200, "text/plain", String("set to ")+command);
  });

  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void){
  server.handleClient();
}
