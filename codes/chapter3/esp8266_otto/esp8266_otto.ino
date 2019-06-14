
#include <esp8266WiFi.h>
#include <FS.h>
#include <Servo.h>
#include "Server.h"
#include "Otto2.h"

// pins used for the rgb led

// Wifi: SSID and password
const char* WIFI_SSID = "AI";
const char* WIFI_PASSWORD = "raspberry";

Servo servos[12];
uint8_t servo_pins[12] = {D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11};
uint8_t count = 12;
void setAngle(uint8_t di,uint8_t vi){
  if(di< 12 && vi < 180){
    servos[di].attach(servo_pins[di]);
    servos[di].write(vi);
  }
}
void attachServos(){
  for (uint8_t i = 0; i < count; ++i){
    servos[i].attach(servo_pins[i]);
  }
}

void dettachServos(){
  for (uint8_t i = 0; i < count; ++i){
    servos[i].detach();
  }  
}

void servoHome(){
  attachServos();
  for (uint8_t i = 0; i < count; ++i){
    servos[i].write(90);
  }
  delay(1000);
  dettachServos();   
}


Otto2 otto2;

void setup() {
  // init the serial
  Serial.begin(115200);
  Serial.println();
  Serial.println("Server initial");
  //init the server
  SPIFFS.begin();
  Serial.println("SPIFFS begin");
  // attachServos();
  // Serial.println("Servos attached");

  otto2.init(D6,D7,D8,D9,true);
//  otto2.init(D2,D3,D4,D5,true);
  Serial.println("Otto initialed");


  server.serveStatic("/", SPIFFS, "/index.html");
  server.serveStatic("/test", SPIFFS, "/test.html");  
  server.on("/set-servo", [](){
    String uri = server.uri();
    Serial.println(uri);
    String di = server.arg("di");
    String vi = server.arg("vi");
    Serial.println("di="+di+" vi="+vi);
    setAngle(di.toInt(),vi.toInt());
    server.send(200, "text/plain", String("set to ")+"di="+di+" vi="+vi);
  });
  server.on("/attach-servos",[](){
    attachServos();
    server.send(200, "text/plain", String("attached Servos"));
  });
  server.on("/dettach-servos",[](){
    dettachServos();
    server.send(200, "text/plain", String("dettached Servos"));
  });

  server.on("/servos-home",[](){
    servoHome();
    server.send(200, "text/plain", String("set servos to 90 degree"));
  });

  server.on("/otto-home",[](){
    otto2.home();
    server.send(200, "text/plain", String("otto-home"));
  });

  server.on("/otto-walk",[](){
    otto2.walk();
    server.send(200, "text/plain", String("otto-walk"));
  });

  server.on("/otto-walk-back",[](){
    otto2.walk(4,1000,BACKWARD);
    server.send(200, "text/plain", String("otto-walk"));
  });

  server.on("/otto-bend",[](){
    otto2.bend();
    server.send(200, "text/plain", String("otto-bend"));
  });

  server.on("/otto-jump",[](){
    otto2.jump();
    server.send(200, "text/plain", String("otto-jump"));
  });

  server.on("/otto-turn",[](){
    otto2.turn();
    server.send(200, "text/plain", String("otto-turn"));
  });

  server.on("/otto-turn-right",[](){
    otto2.turn(4,2000,RIGHT);
    server.send(200, "text/plain", String("otto-turn-right"));
  });

  server.on("/otto-shakeLeg",[](){
    otto2.shakeLeg();
    server.send(200, "text/plain", String("otto-shakeLeg"));
  });

  server.on("/otto-updown",[](){
    otto2.updown();
    server.send(200, "text/plain", String("otto-updown"));
  });
  
  server.on("/otto-swing",[](){
    otto2.swing();
    server.send(200, "text/plain", String("otto-swing"));
  });

  server.on("/otto-tiptoeSwing",[](){
    otto2.tiptoeSwing();
    server.send(200, "text/plain", String("otto-tiptoeSwing"));
  });  

  server.on("/otto-jitter",[](){
    otto2.jitter();
    server.send(200, "text/plain", String("otto-jitter"));
  });  


  server.on("/otto-moonwalker",[](){
    otto2.moonwalker();
    server.send(200, "text/plain", String("otto-moonwalker"));
  });  


  server.on("/otto-crusaito",[](){
    otto2.crusaito();
    server.send(200, "text/plain", String("otto-crusaito"));
  });  


  server.on("/otto-flapping",[](){
    otto2.flapping();
    server.send(200, "text/plain", String("otto-flapping"));
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
