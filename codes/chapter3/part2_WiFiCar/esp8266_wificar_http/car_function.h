#define AE D1      //Motor A/B,E enable,D Direction
#define AD D3

#define BE D2
#define BD D4


//小车初始化函数
void carInit(){  
  pinMode(AE, OUTPUT);
  pinMode(AD, OUTPUT);
  pinMode(BE, OUTPUT);
  pinMode(BD, OUTPUT);

  Serial.begin(115200);
  Serial.println("Car begin");
}


 //小车前进函数
void goAhead(){
      digitalWrite(AE, HIGH);
      digitalWrite(AD, HIGH);
      digitalWrite(BE, HIGH);
      digitalWrite(BD, HIGH);
  }


//小车后退函数
void goBack(){
    digitalWrite(AE, HIGH);
    digitalWrite(AD, LOW);
    digitalWrite(BE, HIGH);
    digitalWrite(BD, LOW);
} 
	
  
//小车右转函数
void goRight(){
    digitalWrite(AE, HIGH);
    digitalWrite(AD, HIGH);
    digitalWrite(BE, LOW);
}


//小车左转函数
void goLeft(){
  digitalWrite(AE, LOW);
  digitalWrite(BE, HIGH);
  digitalWrite(BD, HIGH);   
}


//小车停车函数
void stopRobot(){  
      digitalWrite(AE, LOW);
      digitalWrite(BE, LOW);
}
