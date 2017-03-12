import sys
sys.path.append('F:/Python file/第十章')
import hello
a=[123,123,324,435,657,'234','dsf','hc45']
b=','.join(str(i) for i in a)
print (b)
hello.hello()