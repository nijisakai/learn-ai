#include <ESP8266WiFi.h>
#include <FS.h>
#include <Servo.h>
#include "server.h"
//#include <Stepper.h>
//// pins used for the rgb led
//char serial_line[100] ="";
//int serial_line_length=0;
//char val='/';
//#define STEPS 100
//Stepper stepper(STEPS, 8, 9, 10, 11);
//int pos;
//int pos1;
//int i ;
// Wifi: SSID and password
const char* WIFI_SSID = "AI";
const char* WIFI_PASSWORD = "raspberry";

Servo servos[12];
uint8_t servo_pins[12] = {D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11};
uint8_t count = 12;
void setAngle(uint8_t di,uint8_t vi){
    if(di< 12 && vi < 180)
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

void handleNotFound(){
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
}

void setup() {
    // init the serial
    Serial.begin(115200);
    Serial.println();
    Serial.println("Server initial");
    //init the server
    SPIFFS.begin();
        Serial.println("SPIFFS begin");
    attachServos();
    Serial.println("Servos attached");
    server.serveStatic("/", SPIFFS, "/index.html");
    server.on("/set-servo", [](){
    String uri = server.uri();
    Serial.println(uri);
    String di = server.arg("di");
    String vi = server.arg("vi");
    Serial.println("di="+di+" vi="+vi);
    setAngle(di.toInt(),vi.toInt());
    server.send(200, "text/plain", String("set to ")+"di="+di+" vi="+vi);
    });
    server.onNotFound(handleNotFound);
    server.begin();
    Serial.println("HTTP server started");
    

    // init the WiFi connection
    Serial.println();
    Serial.println();
    Serial.print("INFO: Connecting to ");
    WiFi.mode(WIFI_STA);
    Serial.println(WIFI_SSID);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    }

    Serial.println("");
    Serial.println("INFO: WiFi connected");
    Serial.print("INFO: IP address: ");
    Serial.println(WiFi.localIP());

}

void loop() {
    server.handleClient();
}