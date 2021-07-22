from twilio.rest import Client
import requests
import cred

account_sid = cred.id
auth_token = cred.token
client = Client(account_sid, auth_token)

people = requests.get('http://api.open-notify.org/astros.json')
dic = people.json()
print("People Status Code: ", people.status_code)
#print("People in space = ", dic['number'])
names = dic['people']
#print('Names are ')
namez = " "
for i in names:
    namez += str(i['name'])
    namez += ","

iss_loc = requests.get('http://api.open-notify.org//iss-now.json')    
loc = iss_loc.json()
position = loc['iss_position']
print("Location Status Code: ", iss_loc.status_code)
lat = str(position['latitude'])
long = str(position['longitude'])
#print(position)

Message = 'By ZP - Humans in space right now = ' + str(dic['number']) + "." + ' Their names: ' + namez + ' ISS Location: Lat {}, Long {}'.format(lat,long)

Message1 = 'Want a website or app development solution? Check out ASTRATECHZ.online'

#print(Message)
#formulate the message that will be sent


message_astratechz = client.messages.create( 
    from_='whatsapp:+14155238886',
    body=Message1,
    to='whatsapp:+918383965292')

sent_ids = [message_astratechz.sid]
print(sent_ids)
