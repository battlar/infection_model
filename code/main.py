from CityNodeFile import CityNode
import matplotlib.pyplot as plt#用于绘图

city1=CityNode()#两个城市用于对照
print("对city1进行配置：")
city1.city_set()
city2=CityNode()
print("对city2进行配置：")
city2.city_set()

x=[]
y1=[]
y2=[]
i=1
while(i<50):
    city1.SI_change(i)
    city2.SI_change(i)
    x.append(i)
    y1.append(city1.get_i())
    y2.append(city2.get_i())
    i=i+1

#绘图
plt.plot(x, y1, 'ro-',color='#4169E1', label='city1')
plt.plot(x, y2, 'ro-', color='#025955',label='city2')

plt.legend(loc="upper left")
plt.xlabel('time')
plt.ylabel('infected rate')

plt.show()