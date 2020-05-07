#we already made our Arduino and sensor working
#all we need to do is make numbers meanigful for others and what's the best way of doing it ??????
#Graphs !!!!!
#this script simply takes the data from arduino serial com and sends it to Microsoft's POWER BI
# POWER BI helps us in creating a simple dashboard for our little iot project so it can be meaningful

#importing serial library for serial commmunication with arduino 
import serial
#time to get delay function or in python sleep
import time
#datetime to generate timestamps
from datetime import datetime
#requests for simply sending and recieving request from POWER BI API
import requests
# Pandas to manage data 
import pandas as pd
# link is where i storer my api token
link='https://api.powerbi.com/beta/d4963ce2-af94-4122-95a9-644e8b01624d/datasets/535b5418-5974-4c0b-9ca0-10ccb67f1802/rows?noSignUpCheck=1&key=VMsdgfV%2Fd0Fb%2BzCLCMkmGM8fn7CwvuPurHfw7O2ZMFQFm0ej0F%2BL5m9AFvzgAirEWtXMQE%2FHApITQkwxeCybCA%3D%3D'
#make a serial object and establish connection with com3 my board is on com3 and or favourite baud rate 9600
ArduinoSerial = serial.Serial('com3',9600)
#well we want to give our board a chance to genrate data so why don't make our program sleep for a second
time.sleep(1)
#start reading the data from serial line interface
#this is to initiate the data
data=ArduinoSerial.readline()


#well the only sensor i hvae as of now is a ultrasonic sensor 
#so let's forge some data
#so my data packet is going to have:
#timestamp
#my sensor value from serial interface
#a false location u can actually use a gps module but i broke mine so well let's forge the value
#and reference max and min
#since i am not using any database in between it needs to str max and min every time
def read_serial():
    minpoint=0
    maxpoint=100
    lat=12.972391
    lon=79.157675
    targ=20
    loc="VIT CHENNAI"
    data=ArduinoSerial.readline()
    data_real=data.decode('utf-8')
    datetime_object = datetime.now()
    #this is our succesfully genrated data packet  
    return[data_real,datetime_object,minpoint,maxpoint,lat,lon,loc,targ]

#now sending this data
while True:
  data_raw=[]
  #generating one data packet every time
  for i in range(1):
    #generate a data packet  
    row=read_serial()
    data_raw.append(row)
    print("RAW_DATA",data_raw)
  #here comes pandas our data is still numers
  #we need to give meaningful headers to it   
  HEADER=["CAPACITY","DATE_TIME","MIN","MAX","LATITUDE","LONGITUDE","LOCATION","TARGET"]
  #making a data frame using pandas with our values and data header
  data_df=pd.DataFrame(data_raw,columns=HEADER)
  #convert everything to json data first 
  #encoding evrything to bytes stream for transmission and default encoding is utf-8 
  data_json=bytes(data_df.to_json(orient='records'),encoding='utf-8')
  print("JSON dataset",data_json)
  #and away it go !!!!!
  req=requests.post(link,data_json)
  
