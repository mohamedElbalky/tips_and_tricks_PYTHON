name = 'momo'

# bad logic!!!
# if name == 'abc' or 'def' or  'ghi':
#     print('Access Granted!')
# else:
#     print('Access Denied!')


if name in ['abc' or 'def' or  'ghi']:
    print('Access Granted! :)')
else:
    print('Access Denied! :(')