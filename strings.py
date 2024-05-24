course=" python's course for beginners"
first='emanuel'
last='bekele'
''' to format the string we use key word called "F + {}"'''
msg=f'{first} [{last}] is software engineer'
print(msg)
print(len(course))
print(course.upper())
print(first[3])
print(last.find('k'))
print(course.replace('beginners','absloute beginners'))

''' am methond called replace(,) is used as to reblace a string to other string character
and the key word  "in" is used to check the existance of the character in the string '''
print('course' in course)

