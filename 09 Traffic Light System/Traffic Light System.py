
# 9. Traffic Light System
# Idea: Simple condition logic

light = input('Trafic light color (red / yellow / green): ')

if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Slow down')
elif light == 'green':
    print('Go')
else:
    print("Invalid color")