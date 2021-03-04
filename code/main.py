from CityNodeFile import CityNode
import matplotlib.pyplot as plt#用于绘图

#############################
#          时间配置          #
#############################
TimeLimit=50#时间限制
TimeStep=1#采样周期

#############################
#          主变量            #
#############################
city1=CityNode()#两个城市用于对照
city2=CityNode()
x=[]#用于作图的参数
y1=[]
y2=[]
i=1

#############################
#      选择模拟用的模型      #
#############################
print("\n对参照对象进行配置（建议使用默认配置）：")
print("-------------------------------------")
city1.city_set()
print("\n对实验对象进行配置(建议一次只修改一个变量)：")
print("-------------------------------------")
city2.city_set()
model=input("请选择使用的模型（SI,SIS):").strip()

while(i<TimeLimit):
    if(model=="SI"):#使用SI模型
        city1.SI_change(i)
        city2.SI_change(i)
    elif(model=="SIS"):#使用SIS模型
        city1.SIS_change(i)
        city2.SIS_change(i)
    x.append(i)
    y1.append(city1.get_i())
    y2.append(city2.get_i())
    i=i+TimeStep
    
#############################
#            绘图           #
#############################
plt.plot(x, y1, 'ro-',color='#4169E1', label='default')
plt.plot(x, y2, 'ro-', color='#025955',label='change')

plt.legend(loc="upper left")
plt.xlabel('time')
plt.ylabel('infected rate')

plt.show()