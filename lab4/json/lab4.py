import json

with open('json_data') as file:
    json_data = json.load(file)





print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

arr = json_data['imdata']

for it in arr:
    l1 = it["l1PhysIf"]
    a = l1["attributes"]
    dn = a['dn']
    speed = a['speed']
    mtu = a['mtu']
    cout = ""
    if(len(dn) == 42):
        cout += dn + " " * 30 + speed + "   " + mtu
    else:
        cout += dn + " " * 31 + speed + "   " + mtu
    print(cout)
