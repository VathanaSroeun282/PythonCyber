X = 'Remove String'
print('Data Before remove: ', X)
d = input('Enter your letter that u ward to delete : ')
if d in X:
    X = X.replace(d, '')
    print('Data has been remove')
else:
    print ('Data search no Found')
print('Data after remove :', X)