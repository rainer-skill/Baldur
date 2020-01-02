from flask import Flask, json, request
from neopixel import Color
import baldur_2
import json

with open('Database_Baldur.json', 'r') as outfile:
    data = outfile.read()

print(data);
#data['modus'].append({
#    'V1': '1',
#    'V2': '2',
#    'V3': '3'
#})

api = Flask(__name__)

@api.route('/RainbowCycle', methods=['GET'])
def helloWorld(): 
    baldur.rainbowCycle()
    return 'RainbowCycle!'

@api.route('/clear', methods=['GET'])
def clearStripe(): 
    baldur.stop()
    baldur.colorWipe(Color(0,0,0))
    return 'Cleared!'

@api.route('/colors', methods=['POST'])
def setColors(): 
    baldur.stop()
    colors = request.json["colors"]
    data['colors'] = colors
    with open('Database_Baldur.json', 'w') as outfile:
        json.dump(data, outfile)
        
    color = Color(colors[0]["G"], colors[0]["R"], colors[0]["B"])
    baldur.colorWipe(color)
    return 'Cleared!'

@api.route('/modi', methods=['GET'])
def getModi(): 
    with open('Baldur_modi_config.json', 'r') as outfile:
        data = outfile.read()
    return data

@api.route('/modi', methods=['POST'])
def setModi(): 
    modi = request.json["active"]
    with open('Database_Baldur.json', 'w') as outfile:
        json.dump(data, outfile)
    return data
    

if __name__ == '__main__':
    baldur = baldur_2.Baldur()
    clearStripe()
    api.run(host = '0.0.0.0')

