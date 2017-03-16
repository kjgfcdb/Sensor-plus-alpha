import re
import matplotlib.pyplot as plt
import numpy as np
label = {'swing':0,'right':1}
ret = re.compile(r":.*?]")
g = open("ex_data1.txt","w")
for dicname in ['swing','right']:
        for index in range(1,11):
            with open("C:/Users/Chen Dengbo/Desktop/Octave/"+dicname+"/"+str(index)+".txt", 'r') as f:
                lines  = f.readlines()
                Ax,Ay,Az,Aroll,Ayaw = [],[],[],[],[]
                Bx,By,Bz,Broll,Byaw = [],[],[],[],[]
                for line in lines:
                    temp = ret.findall(line)
                    if "roll1" in line:
                        Aroll.append(float(temp[0][1:-1]))
                        Ayaw.append(float(temp[2][1:-1]))
                        Ax.append(float(temp[3][1:-1]))
                        Ay.append(float(temp[4][1:-1]))
                        Az.append(float(temp[5][1:-1]))
                    else:
                        Broll.append(float(temp[0][1:-1]))
                        Byaw.append(float(temp[2][1:-1]))
                        Bx.append(float(temp[3][1:-1]))
                        By.append(float(temp[4][1:-1]))
                        Bz.append(float(temp[5][1:-1]))
                tempX = np.mean(Ax)
                tempY = np.mean(Ay)
                tempZ = np.mean(Az)
                tempBX = np.mean(Bx)
                tempBY = np.mean(By)
                tempBZ = np.mean(Bz)
                tempAroll = np.mean(Aroll)
                tempAyaw = np.mean(Ayaw)
                tempBroll = np.mean(Broll)
                tempByaw = np.mean(Byaw)
                g.write("%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%d\n"%\
                        (tempX,tempY,tempZ,tempBX,tempBY,tempBZ,tempAroll,tempAyaw,tempBroll,tempByaw,label[dicname]))
g.close()
#for index in range(1,10):
#    with open("C:/Users/Chen Dengbo/Desktop/Octave/swing/"+str(index)+".txt", 'r') as f:
#        lines  = f.readlines()
#        Ax,Ay,Az = [],[],[]
#        for line in lines:
#            if "roll2" in line:
#                temp = ret.findall(line)
#                Ax.append(float(temp[3][1:-1]))
#                Ay.append(float(temp[4][1:-1]))
#                Az.append(float(temp[5][1:-1]))
#        plt.subplot(3,3,index)
#        plt.plot(Ax)
#plt.show()
