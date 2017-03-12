import re
patt = re.compile('From: (.{6})<.*?>')
m = patt.match('From: chence<364437360@qq.com>')
if m: print(m.group(1))