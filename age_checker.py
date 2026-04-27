# 1. Age Checker (Adult or Not)
# Idea: Check if a person is adult

name = str(input('What is Your name ?'))
age = int(input('enter your age :'))

print('Welcome Mr', name.capitalize())

if age >= 18:
    print('You are a great man Jaale.')
else:
    print('You are still young.')
