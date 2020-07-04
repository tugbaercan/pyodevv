def shut_down(s):
    if s.lower() == 'yes':
        print ('Shutting Down')
    elif s.lower() == 'no':
        print('Shutt Down')
    else:
        print('Sorry')

shut_down('yes')
shut_down('no')
shut_down('NO')
shut_down('')

