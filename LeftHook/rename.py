import os
l = [i for i in os.listdir('.')]
for i in range(len(l)):
    if 'txt' in l[i]:
        os.rename(l[i],str(i)+'.txt')
