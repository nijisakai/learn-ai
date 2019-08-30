#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <FS.h>

#include <Servo.h>
 
// setup servo
#define SERVORIGHT   50
#define SERVOCENTRE  100
#define SERVOLEFT    150
#define SERVOPIN     16
#define TRIGPIN      13    // pin no. 13  is D7 ESP8266
#define ECHOPIN      15    // pin no. 15  is D8 ESP8266
#include <WebSocketsServer.h>
String command;

ESP8266WebServer server(80);
int Speed = 900;  // max 1024
int TSpeed = 1020;  //Turning Speed
Servo servo;

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
void setup()
{   
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
  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }


    SPIFFS.begin();
    Serial.begin(115200);
 
    // set the servo data pin
    servo.attach(SERVOPIN);

    pinMode(5, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(0, OUTPUT);
    pinMode(2, OUTPUT);
    digitalWrite(5, 0);
    digitalWrite(4, 0);
    digitalWrite(0, 1);
    digitalWrite(2, 1);
    // set the trig pin to output (send sound waves)
    pinMode(TRIGPIN, OUTPUT);
 
    // set the echo pin to input (receive sound waves)
    pinMode(ECHOPIN, INPUT);

//display.init();
//display.flipScreenVertically();
//display.setFont(ArialMT_Plain_16);
//display.setTextAlignment(TEXT_ALIGN_LEFT);
    
    server.serveStatic("/", SPIFFS, "/index.html");

  server.on("/get", [](){
    String uri = server.uri();
    Serial.println(uri);
    command = server.arg("command");
    if(command == "forward")
      forward();
    else if(command == "backward")
      back( );
    else if(command == "left")
      left();
    else if(command == "right")
       right();
    else if(command == "stop")
       stopped();
    else if(command == "obstacle")
       obstacle();
    Serial.println(command);
//    setCorlor(red.toInt(),green.toInt(),blue.toInt());
    server.send(200, "text/plain", String("set to ")+command);
  });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("http server started");
}

void stopped()
{
    analogWrite(5, 0);
    analogWrite(4, 0);
    Serial.println("Stop");
}
 
void forward()
{
    analogWrite(5, Speed);
    analogWrite(4, Speed);
    digitalWrite(0, 1);
    digitalWrite(2, 1);
    Serial.println("forward");
}
 
void back()
{
    analogWrite(5, Speed);
    analogWrite(4, Speed);
    digitalWrite(0, 0);
    digitalWrite(2, 0);
    Serial.println("Back");
}
 
void left()
{
    analogWrite(5, TSpeed);
    analogWrite(4, TSpeed);
    digitalWrite(0, 0);
    digitalWrite(2, 1);
    Serial.println("Left");
}
 
void right()
{
    analogWrite(5, TSpeed);
    analogWrite(4, TSpeed);
    digitalWrite(0, 1);
    digitalWrite(2, 0);
    Serial.println("right");
}



int ping()
{
    // pause for 50ms between scans
    delay(50);
 
    // send ping
    digitalWrite(TRIGPIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIGPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGPIN, LOW);
 
    // read echo
    long duration = pulseIn(ECHOPIN, HIGH);
 
    // convert distance to cm
    unsigned int centimetres = int(duration / 2 / 29.1);
 
    return centimetres;
}
 
char scan()
{
    // ping times in microseconds
    unsigned int left_scan, centre_scan, right_scan;
    char choice;
 
    // scan left
    servo.write(SERVOLEFT);
    delay(300);
    left_scan = ping();
 
    // scan right
    servo.write(SERVORIGHT);
    delay(600);
    right_scan = ping();
 
    // scan straight ahead
    servo.write(SERVOCENTRE);
    delay(300);
    centre_scan = ping();
 
    if (left_scan>right_scan && left_scan>centre_scan)
    {
        choice = 'l';
    }
    else if (right_scan>left_scan && right_scan>centre_scan)
    {
        choice = 'r';
    }
    else {
      choice = 'c';
    }
 
    return choice;
}
 

void loop()
{   
    server.handleClient();
    // get distance from obstacle straight ahead
    
}
int stopCount = 0;
unsigned int distance = ping();
void obstacle()
{
    while(1){
    if (distance < 30 && distance > 0)
    {
        if (distance < 10)
        {
            // turn around
            Serial.println("Turn around..."); 
           // display.drawString(10, 40, "Turn around...") ;         
            back();
            delay(300);
            left();
            delay(700);
        }
        else
        {
            // stop both motors
            Serial.println("Motor stop...");
           // display.drawString(10, 40, "Motor stop...") ; 
            stopped();
            
            // scan for obstacles
            char turn_direction = scan();
 
            // turn left/right or ignore and go straight
            if (turn_direction == 'l')
            {
              Serial.println("Turn left...");
            //  display.drawString(10, 40, "Turn left...") ; 
                left();
                delay(500);
            }
            else if (turn_direction == 'r')
            {
              Serial.println("Turn right...");
            //  display.drawString(10, 40, "Turn right...") ; 
                right();
                delay(500);
            }
            else if (turn_direction == 'c')
            {
              stopCount++;
              if(stopCount > 3){
                stopCount = 0;
                Serial.println("Turn back...");
              //  display.drawString(10, 40, "Turn back...") ; 
                right();
                delay(700);
              }
              
            }
        }
    }
            else
            {
                // no obstacle, keep going forward
                Serial.println("No obstacle, keep going forward...");
            //  display.drawString(5, 40, "keep going forward...") ; 
                forward();
            }
    
    }
}    
