from CityNodeFile import CityNode
import matplotlib.pyplot as plt#用于绘图

#############################
#          时间配置          #
#############################
TimeLimit=50#时间限制
TimeStep=1#采样周期

#############################
#          主程序           #
#############################
city1=CityNode()#两个城市用于对照
print("\n对参照对象进行配置（建议使用默认配置）：")
print("-------------------------------------")
city1.city_set()
city2=CityNode()
print("\n对实验对象进行配置：")
print("-------------------------------------")
city2.city_set()

x=[]
y1=[]
y2=[]
i=1
while(i<TimeLimit):
    city1.SI_change(i)
    city2.SI_change(i)
    x.append(i)
    y1.append(city1.get_i())
    y2.append(city2.get_i())
    i=i+TimeStep

#绘图
plt.plot(x, y1, 'ro-',color='#4169E1', label='default')
plt.plot(x, y2, 'ro-', color='#025955',label='change')

plt.legend(loc="upper left")
plt.xlabel('time')
plt.ylabel('infected rate')

plt.show()