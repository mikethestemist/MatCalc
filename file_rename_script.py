import os

for i in os.listdir(): 
  if i.endswith('.py'): 
    print(i, i[3:-3] + '_' + i[:3] + i[-3:])
    os.rename(i, i[3:-3] + '_' + i[:3] + i[-3:])

print('Done')