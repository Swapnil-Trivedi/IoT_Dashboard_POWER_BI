//setting constants values maxdepth=100
//hence mid depth is 50
//almost empty bin is 20 (or any number)
//reference variables are set to constant we don't want to change them at any cost
const int ref=100;
const int ref1=50;
const int ref2=20;

//setting trigger pin and echo pin for ultrasonicSensor
int trigpin=13;
int echopin=12;
//digital pin for buzzer
int dpbuzz=8;

//making a function to get the distance from ultrasonic sensor
int distance_uls(int trigpin, int echopin)
{
 long duration;
 //we trigger the sensors trigpin to generate a pulse for 20 useconds
 //and listen to it on echopin and get its time
 pinMode(trigpin,OUTPUT);
 pinMode(echopin,INPUT);
 digitalWrite(trigpin, LOW);
 delayMicroseconds(2);
 digitalWrite(trigpin,HIGH);
 delayMicroseconds(20);
 digitalWrite(trigpin,LOW);
 //to get the seconds for which the echopin listen
 //pulse in can be used to get length of pulse in milisecond
 duration=pulseIn(echopin,HIGH);
 //duration needs to get divide by a factor to get distance
 // it can vary, check sensor datasheet
 //i use 59 bcz my datasheet val is 59 
 duration=duration/59;
  // the check statement is standard from sensor example
 if((duration<2) || (duration > 300))
  //false is technically 0 in int so it will work
  return false;
 else
  return duration;
  
}
//setting up necessary values for the setup
void setup() {
 //setting buzzer pin as output 
 pinMode(dpbuzz,OUTPUT);
 digitalWrite(dpbuzz,LOW);
 //initial trigpin val is to be seet low
 digitalWrite(trigpin,LOW);

 //we also need serial interface
 //9600 our favourite and default baud rate 
 Serial.begin(9600);
 
}
//our process is simple :
//we listen to our sensor data
//store it in range check range with reference variables and voila we get our distance
// if bin status is full we simply put buzzer to work else we don't
//also  writing the serial monitor with status so we can read it later

//this is just going to be a bunchof if else nothing fancy...
void loop() {
int range=distance_uls(trigpin,echopin);
//before reading next value board need time to process the current value or it will show overflow
delay(2000);

if((range<=ref)&& (range>ref1))
  Serial.println(range);
else if((range<=ref1)&&(range>=ref2))
  Serial.println(range);
else 
{
 if(range<=ref2)
 {
  Serial.println(range);
  //at this point wew want to raise allarm so buzzer time!!!
  digitalWrite(dpbuzz,HIGH);
  //that buzzer is annoying gotta stop it too
  //we use tone it's better than using a simple audio
  tone(dpbuzz,50,100);
  // i hate this buzzer
  digitalWrite(dpbuzz,LOW);
 }
  
}
}
