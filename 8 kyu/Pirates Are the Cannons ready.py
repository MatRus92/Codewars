def cannons_ready(gunners):
  if 'nay' in gunners.values():
      return 'Shiver me timbers!'
  else:
      return 'Fire!'

a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}

print(cannons_ready(a))
print(cannons_ready(b))