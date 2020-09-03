def time_to_type(keyboard,text):
    key_pad={}
    position=0
    time=0

    for pos,char in enumerate(keyboard):
        key_pad[char]=pos

    for char in text:
        pos=key_pad[char]
        time+=abs(pos-position)
        position=pos

    return time


print(time_to_type("abcdefghijklmnopqrstuvwxy","cba"))