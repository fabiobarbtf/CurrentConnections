lista =[
    #LISTA DE IPS E VIRTUAIS SERVERS
    ("IP","VS"),
    ("IP","VS"),
]

_current = 0
for ip,_keyword in lista:
    #print (ip+_keyword)
    #print (f"https://{ip}/tmui/login.jsp")
    #print (f"https://{ip}/tmui/Control/jspmap/tmui/locallb/virtual_server/stats.jsp")
    if ip != _current:
        print(ip,_current)
        _current = ip