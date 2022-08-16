msg="Welcome to Python 101: Strings"
print(msg)

# find and replace 

print(msg.find('Python'))

print(msg.replace('Python', 'JavaScript'))


# check for 'Python' in msg
print('Python' in msg)

name='TERRY'
color = 'RED'
msg2 = '[' + name + '] loves the color ' + color.lower() + '!'
msg3 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg2)
print(msg3)

name='Vally'
color = 'RED'
msg2 = '[' + name + '] loves the color ' + color.lower() + '!'
msg3 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg2)
print(msg3) 