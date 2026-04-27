# 4. Grade Calculator
# Idea: Convert marks to grade

marks = int(input('enter your marks jaale :'))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print('Grade B')
elif marks >= 70:
    print('Grade C')
elif marks >= 60:
    print('Grade D')
else:
    print("Fail")