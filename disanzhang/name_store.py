def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
def lookup(data,label,name):
    return data[label].get(name)
def store(data,*full_names):
    for full_name in full_names:
        name = full_name.split()
        if len(name) == 2: name.insert(1,'')
        label = 'first','middle','last'
        for na ,la in zip(name,label):
            people = lookup(data,la,na)
            if people:
                people.append(full_name)
            else :
                data[la][na] = [full_name]

MyNames ={}
init(MyNames)
store(MyNames,'magqwe los int','dsfjkdhs los sdfkgh')
print(lookup(MyNames,'middle','los'))