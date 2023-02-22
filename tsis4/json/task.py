import json
import pprint
with open('tsis4\json\sample.json','r') as file:
    data=json.load(file)
print('''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------''')
for i in data['imdata']:
    print(i["l1PhysIf"]['attributes']['dn'],'\t',i["l1PhysIf"]['attributes']['descr'],'\t\t       ',i["l1PhysIf"]['attributes']['speed'],' ',i["l1PhysIf"]['attributes']['mtu'])