import time
import paho.mqtt.client as mqtt
import pyttsx3
import time
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru') 




#Callbacks
def on_connect(client,userdata,flags,rc):
    print('Connected with code'+str(rc))
    #Sub
    client.subscribe("Inform/#")
def on_message(client,userdata,msg):
    tts.say('Внимание! Зафиксировано движение возле Охранной системы')
	tts.runAndWait()


client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

client.connect("m16.cloudmqtt.com",11729,60)
client.username_pw_set("tizzoqtl", "sqCYE8vpFV1P")

time.sleep(1)
client.loop_start()
while True:
    client.publish("Tutorial/","Getting started with MQTT")
    time.sleep(15)

client.loop_stop()
client.disconnect()
