#================ if/elif/else/while/for  =======================
x = True 
if (x): 
    print('statement entered')
elif (x): 
    print('Statment not printed')
else:
    print('statement not enetered')

q=0
while x: 
    print('still true')
    q += 1
    if q==10:
        x = False
        print('not true')

x = ['banana', 'strawberry', 'orange']
for y in x:
    if y=='orange':
        print('found the orange')
        break


