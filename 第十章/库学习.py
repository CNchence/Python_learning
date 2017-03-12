import itchat
print([n for n in dir(itchat) if not n.startswith('_')])
print (itchat.__all__)