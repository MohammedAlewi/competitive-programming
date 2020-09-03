def max_time(given_time):
    
    # hour 

    if given_time[0]=="?":
        if given_time[1]=="?" or int(given_time[1])<=3:
            given_time="2"+given_time[1:]
        else:
            given_time="1"+given_time[1:]

    if given_time[1]=="?":
        if given_time[0]=="2":
            given_time=given_time[:1]+"3"+given_time[2:]
        else:
            given_time=given_time[:1]+"9"+given_time[2:]

    # minute

    if given_time[3]=='?':
        given_time=given_time[:3]+"5"+given_time[4:]

    if given_time[4]=='?':
        given_time=given_time[:4]+"9"

    return given_time


print(max_time("0?:??"))