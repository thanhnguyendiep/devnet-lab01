routers = [
    {"ten": "R1", "ip": "10.0.0.1", "os": "Juniper"},
    {"ten": "R2", "ip": "10.0.0.2", "os": "Cisco"},
    {"ten": "R3", "ip": "10.0.0.3", "os": "Juniper"},
    {"ten": "R4", "ip": "10.0.0.4", "os": "Cisco"},
    {"ten": "R5", "ip": "10.0.0.5", "os": "Juniper"}
]

def FindRouter(routerList, routerName):
    i = 0
    for r in routerList:        
        if r["ten"] == routerName:            
            return i   #nếu tìm thấy thì trả về số thứ tự trong routerList
        i = i + 1
    return -1   #nếu không tìm thấy thì trả về -1

i = FindRouter(routers, "R1")
if i == -1:
    print("Không tìm thấy")
else:
    print("Name: {0}".format(routers[i]["ten"]))
    print("IP: {0}".format(routers[i]["ip"]))
    print("OS: {0}".format(routers[i]["os"]))
