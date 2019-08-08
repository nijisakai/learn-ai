/*
         @authors:
  Yash Chandak    Ankit Dhall
*/
//Define pin numbers

//right motor
int m1f = 7;
int m1r = 5;
//left motor
int m2f = 4;
int m2r = 6;
int led = 13;
char value;
int val[3];
int len;
int direc;


void setup()
{
  //start serial communication at Baud rate of 9600
  Serial.begin(115200);
  pinMode(m1f, OUTPUT);
  pinMode(m1r, OUTPUT);
  pinMode(m2f, OUTPUT);
  pinMode(m2r, OUTPUT);
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  pinMode(2, OUTPUT);
}

void execute()
{
  int no;
  int i = 0;

  //convert ASCII value from serial buffer into int
  no = value - '0';
  Serial.println(no);

  int a, b, c, d;

  /*
    """
    Direction control Index:

    '<' , '>' are the frame check bits for serial communication

    Numbers represent the direction to be moved as per their     	position on numpad
    1: Back Left
    2: Back
    3: Back right
    4: Left
    5: Stay still
    6: Right
    7: Front Left
    8: Forward
    9: Forward right
    """
  */

  switch (no)
  {
    case 8:
      a = 0; b = 0; c = 150; d = 150;//forward
      break;
    case 2:
      a = 1; b = 1; c = 150; d = 150;//backward
      break;
    case 7:
      a = 0; b = 0; c = 100; d = 200;//forward_left
      break;
    case 9:
      a = 0; b = 0; c = 200; d = 100;//forward_right
      break;
    case 1:
      a = 1; b = 1; c = 100; d = 200;//back_left
      break;
    case 3:
      a = 1; b = 1; c = 200; d = 100;//back_right
      break;
    case 4:
      a = 0; b = 1; c = 150; d = 150;//left
      break;
    case 6:
      a = 1; b = 0; c = 150; d = 150;//right
      break;
    case 5:
      a = 0; b = 0; c = 0; d = 0;//stay still
      break;
    case 0:
      a = 0; b = 0; c = 0; d = 00;//stop
      break;
  }

  digitalWrite(m1f, a);
  digitalWrite(m2f, b);
  analogWrite(m1r, c);
  analogWrite(m2r, d);
  //delay(255);
}

void loop()
{
  if (Serial.available())
  {
    //Check for frame control bits
    char ch = Serial.read();
    //Serial.print(ch);
    if (ch == '<')
    {
      len = 0;
    }
    else if (ch == '>')
    {
      execute();
      //Serial.println(value);
      len = 1;
    }
    else if (len == 0)
      value = ch;
  }
}  
