guest_list= ['Ahmed' ,'Raheem', 'Ali']
print('sorry guys, only 2 people are invited for dinner')
print('Sorry ' + guest_list[1] + ' you are\'nt invited for dinner')
guest_list.pop(1)
print(guest_list)

print('Dear ' + guest_list[0] +' you\'re still invited :) ')
print('Dear ' + guest_list[1] +' you\'re still invited :) ')

del guest_list[:]
print('Guest list:', guest_list)