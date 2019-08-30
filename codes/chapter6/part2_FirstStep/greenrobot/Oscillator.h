//--------------------------------------------------------------
//-- Oscillator.pde
//-- Generate sinusoidal oscillations in the servos
//--------------------------------------------------------------
//-- (c) Juan Gonzalez-Gomez (Obijuan), Dec 2011
//-- GPL license
//--------------------------------------------------------------
#ifndef Oscillator_h
#define Oscillator_h

#ifndef debug
#define debug 0
#endif

#include "Servo.h"

//-- Macro for converting from degrees to radians
#ifndef DEG2RAD
  #define DEG2RAD(g) ((g)*M_PI)/180
#endif

class Oscillator
{
  public:
    Oscillator(int trim=0) {_trim=trim;};
    void attach(int pin, bool rev =false);
    void detach();
    
    void SetA(int8_t A) {_A=A;};
    void SetO(int8_t O) {_O=O;};
    void SetPh(double Ph) {_phase0=Ph;};
    void SetT(unsigned int T);
    void SetTrim(int trim){_trim=trim;};
    int getTrim() {return _trim;};
    void SetPosition(int position); 
    void Stop() {_stop=true;};
    void Play() {_stop=false;};
    void Reset() {_phase=0;};
    void refresh();
    void refresh_by_time(double t);
    
  private:
    bool next_sample();  
    
  private:
    //-- Servo that is attached to the oscillator
    Servo _servo;
    
    //-- Oscillators parameters
    int8_t _A;  //-- Amplitude (degrees)
    int8_t _O;  //-- Offset (degrees)
    unsigned int _T;  //-- Period (miliseconds)
    double _phase0;   //-- Phase (radians)
    
    //-- Internal variables
    int _pos;         //-- Current servo pos
    int _trim;        //-- Calibration offset
    double _phase;    //-- Current phase
    double _inc;      //-- Increment of phase
    double _NS;        //-- Number of samples
    unsigned int _TS; //-- sampling period (ms)
    
    long _previousMillis; 
    long _currentMillis;
    
    //-- Oscillation mode. If true, the servo is stopped
    bool _stop;

    //-- Reverse mode
    bool _rev;
};

#endif
