#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WebServer.h>
// utlrasonic pinout
#define ULTRASONIC_TRIG_PIN     5   // pin TRIG to D1
#define ULTRASONIC_ECHO_PIN     4   // pin ECHO to D2

// user config: TODO
const char* wifi_ssid = "AI";             // SSID
const char* wifi_password = "raspberry";         // WIFI
ESP8266WebServer server(80);
ESP8266WiFiMulti WiFiMulti;

void setup() {

  Serial.begin(115200);
  Serial.println("*****************************************************");
  Serial.println("********** Program Start : Connect Ultrasonic HC-SR04 + ESP8266 to AskSensors over HTTP");
  Serial.println("Wait for WiFi... ");
  Serial.print("********** connecting to WIFI : ");
  Serial.println(wifi_ssid);
  WiFi.begin(wifi_ssid, wifi_password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("-> WiFi connected");
  Serial.println("-> IP address: ");
  Serial.println(WiFi.localIP());
  // ultraonic setup 
  pinMode(ULTRASONIC_TRIG_PIN, OUTPUT);
  pinMode(ULTRASONIC_ECHO_PIN, INPUT);
  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);
  server.begin();
}


void loop() {
  
  server.handleClient();
  
}

void handle_OnConnect() {
  long duration, distance;
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  delayMicroseconds(2); 
  digitalWrite(ULTRASONIC_TRIG_PIN, HIGH);
  delayMicroseconds(10); 
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  duration = pulseIn(ULTRASONIC_ECHO_PIN, HIGH);
  distance = (duration/2) / 29.1;
  server.send(200, "text/html", SendHTML(distance)); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}

String SendHTML(long distance){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>ESP8266 DHT11</title>\n";
//  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
//  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;}\n";
//  ptr +="p {font-size: 24px;color: #444444;margin-bottom: 10px;}\n";
//  ptr +="</style>\n";
  ptr +="<script>\n";
  ptr +="setInterval(loadDoc,200);\n";
  ptr +="function loadDoc() {\n";
  ptr +="var xhttp = new XMLHttpRequest();\n";
  ptr +="xhttp.onreadystatechange = function() {\n";
  ptr +="if (this.readyState == 4 && this.status == 200) {\n";
  ptr +="document.getElementById(\"webpage\").innerHTML =this.rESPonseText}\n";
  ptr +="};\n";
  ptr +="xhttp.open(\"GET\", \"/\", true);\n";
  ptr +="xhttp.send();\n";
  ptr +="}\n";
  ptr +="</script>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<div id=\"webpage\">\n";
//  ptr +="<h1>ESP8266 Distance</h1>\n";
  
  ptr +="<p>距离: ";
  ptr +=(float)distance;
  ptr +="厘米</p>";
//  ptr +="<p>湿度: ";
//  ptr +=(int)Humiditystat;
//  ptr +="%</p>";
  
  ptr +="</div>\n";
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}
