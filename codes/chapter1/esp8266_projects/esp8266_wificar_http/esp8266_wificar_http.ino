#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <FS.h>
#define Motor_AE D1      //Motor A/B,E enable,D Direction
#define Motor_AD D3

#define Motor_BE D2
#define Motor_BD D4

#define R_AHEAD HIGH
#define L_AHEAD LOW

String command;

ESP8266WebServer server(80);

const int led = 13;

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
  message += (server.method() == https_GET)?"GET":"POST";
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
  carInit();
  SPIFFS.begin();

  uint8_t mac[WL_MAC_ADDR_LENGTH];
  WiFi.softAPmacAddress(mac);
  String macID = String(mac[WL_MAC_ADDR_LENGTH - 2], HEX) + String(mac[WL_MAC_ADDR_LENGTH - 1], HEX);
  macID.toUpperCase();

  String AP_NameString = "Wifi Car - " + macID;

  char AP_NameChar[AP_NameString.length() + 1];
  memset(AP_NameChar, 0, AP_NameString.length() + 1);

  for (int i = 0; i < AP_NameString.length(); i++)
    AP_NameChar[i] = AP_NameString.charAt(i);

const char* ssid = "AI";
const char* password = "raspberry";
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  if (MDNS.begin("ESP8266")) {
    Serial.println("MDNS rESPonder started");
  }


  //server.on("/", handleRoot);
  server.serveStatic("/", SPIFFS, "/index.html");

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
  Serial.println("http server started");
}

void loop(void){
  server.handleClient();
}