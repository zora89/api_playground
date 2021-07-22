from twilio.rest import Client
import requests
import cred

account_sid = cred.id
auth_token = cred.token
client = Client(account_sid, auth_token)

people = requests.get('http://api.open-notify.org/astros.json')
dic = people.json()
print("Status Code: ", people.status_code)
print("People in space = ", dic['number'])
names = dic['people']
print('Names are ')
namez = " "
for i in names:
    namez += str(i['name'])
    namez += ","

iss_loc = requests.get('http://api.open-notify.org//iss-now.json')    
loc = iss_loc.json()
position = loc['iss_position']
print("Status Code: ", iss_loc.status_code)
lat = str(position['latitude'])
long = str(position['longitude'])
print(position)

Message = 'By ZP - Humans in space right now = ' + str(dic['number']) + "." + ' Their names: ' + namez + ' ISS Location: Lat {}, Long {}'.format(lat,long)
print(Message)
#formulate the message that will be sent



message_astratechz = client.messages.create(
to= "+918383965292",
from_="+18647272921",
body=Message)   
sent_ids = [message_astratechz.sid]
print(sent_ids)


''' 
message_papa = client.messages.create(
    to= "+919971355506",
    from_="+18647272921",
    body=Message) 
message_runa = client.messages.create(
    to= "+919999672846",
    from_="+18647272921",
    body=Message) 
message_jivi = client.messages.create(
    to= "+919816092658",
    from_="+18647272921",
    body=Message)    
message_guffy = client.messages.create(
    to= "+917814555255",
    from_="+18647272921",
    body=Message) 
message_tommy = client.messages.create(
    to= "+917042352818",
    from_="+18647272921",
    body=Message)    
message_puru = client.messages.create(
    to= "+919711102572",
    from_="+18647272921",
    body=Message)    
message_vidit = client.messages.create(
    to= "+919986700567",
    from_="+18647272921",
    body=Message)
message_yuvi = client.messages.create(
    to= "+919899893957",
    from_="+18647272921",
    body=Message)

message_ballu = client.messages.create(
    to= "+9198933358492",
    from_="+18647272921",
    body=Message)
message_goldy = client.messages.create(
    to= "+918900920830",
    from_="+18647272921",
    body=Message   ) 
message_hayat = client.messages.create(
    to= "+919820890948",
    from_="+18647272921",
    body=Message)
message_paru = client.messages.create(
    to= "+919702195757",
    from_="+18647272921",
    body=Message)
message_raoul = client.messages.create(
    to= "+919933236293",
    from_="+18647272921",
    body=Message)
message_sumona = client.messages.create(
    to= "+919819651683",
    from_="+18647272921",
    body=Message)
message = client.messages.create(
    to= "+919531839038",
    from_="+18647272921",
    body=Message) 

'''

sent_ids = [message_astratechz.sid]
#[message.sid, message_sumona.sid, message_raoul.sid, message_paru.sid, message_hayat.sid, message_goldy.sid, message_ballu.sid, message_yuvi.sid, message_vidit.sid, message_puru.sid, message_nitin.sid, message_jivi.sid, message_guffy.sid, message_papa.sid, message_runa.sid, message_tommy.sid]
for i in sent_ids:
    print(i)
