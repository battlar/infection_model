import math

class CityNode:
    def __init__(self):
        #主要指标
        self.HealthyS0=10000#城市中健康人数，比例s=HealthyS/(HealthyS+InfectedI)
        self.InfectedI0=1#城市中初始感染人数，比例i=InfercedI/(HealthyS+InfectedI)
        self.HealthyS=self.HealthyS0
        self.InfectedI=self.InfectedI0
        self.PeopleN=self.HealthyS0+self.InfectedI0#人口总数
        self.s=self.HealthyS0/(self.HealthyS0+self.InfectedI0)#健康人数比例
        self.i=self.InfectedI0/(self.HealthyS0+self.InfectedI0)#已感染人数比例
        

        #其它相关参数
        self.PeopleDensity=100.0#input("人口密度（0-200）：")#人口密度，单位：人/平方公里    分为三档：密集型200；平均型150；稀疏型10  故使用时除以200
        self.CommuniDistance=120.0#input("社交距离（0-750）：")#城市中人口社交距离，单位：cm，分为四档：0-45，45-120，120-360，360-750 使用时除以750
        self.MaskPopular=0.2#城市中口罩普及率。随疫情严重而提高，随疫情缓和而下降
        self.TrafficWill=1.0#市内人口流动意愿，随疫情发展而降低，随疫情缓和而升高
        self.DeadRate=0.02#病情致死率不变(病患中移除的比例)
        self.IsolatedRate=0.0#被感染者的隔离率

        #回归方程参数
        self.R0=20#一个周期内感染者接触到的人数,与健康人数负相关
        self.beta0=0.1#beta表示接触后健康人转化为病人的概率，原始传染率为1%
        self.gama0=0.0#gama表示致死率
        self.theta0=0.0#theta表示治愈率
        

    def get_i(self):#读取感染人数比例i
        return self.i

    def get_s(self):#读取健康人数比例s
        return self.s

    def city_set(self):#设置不同参数，便于对比
        req="q"
        temp=0
        help=(
            "S0:配置初始健康人数（2人以上,默认为10000）\n"
            "I0:配置初始患病人数（1人以上，默认为1）\n"
            "PD:配置人口密度（0-200 人/平方公里，默认为100）\n"
            "CD:配置社交距离（0-750 厘米，默认为120）\n"
            "MP:配置口罩普及率（0-1，默认为0.2）\n"
            "TW:配置市民出行率（0-1，默认为1.0）\n"
            "IR:配置隔离率（0-1，默认为0）\n"
            "Q:结束配置\n"  
            "H:打开帮助菜单\n"     
        )
        print(help)
        print("-------------------------------------")
        while(1):
            req=(input("请输入您希望配置的参数：").strip())
            if(req== "S0"):
                temp=float(input("初始健康人数为："))
                if(temp<2):
                    print("无效的输入")
                else:
                    self.HealthyS0=temp
            elif(req== "I0"):
                temp=float(input("初始感染人数为："))
                if(temp<1 or temp>self.HealthyS0):
                    print("无效的输入")
                else:
                    self.InfectedI0=temp
            elif(req=="PD"):
                temp=float(input("人口密度为："))
                if(temp<=0.0 or temp>200.0):
                    print("无效的输入")
                else:
                    self.PeopleDensity=temp
            elif(req=="CD"):
                temp=float(input("社交距离为："))
                if(temp<0.0 or temp>750.0):
                    print("无效的输入")
                else:
                    self.CommuniDistance=temp
            elif(req=="MP"):
                temp=float(input("口罩普及率为："))
                if(temp<0.0 or temp>1.0):
                    print("无效的输入")
                else:
                    self.MaskPopular=temp
            elif(req=="TW"):
                self.TrafficWill=float(input("市民出行意愿为："))
                if(temp<0.0 or temp>1.0):
                    print("无效的输入")
                else:
                    self.TrafficWill=temp
            elif(req=="IR"):
                temp=float(input("被感染者隔离率为："))
                if(temp<0.0 or temp>1.0):
                    print("无效的输入")
                else:
                    self.IsolatedRate=temp
            elif(req=="H"):
                print(help)
                print("-------------------------------------")
            elif(req=="Q"):
                print("配置已完成\n")
                break
            else:
                print("无效的输入\n")

    def SI_change(self,time):#使用SI模型进行模拟
        self.beta=self.beta0*(1-self.CommuniDistance/750)*(1-self.MaskPopular)
        self.R=self.R0*(self.PeopleDensity/200)*self.TrafficWill
        ##后续补充其它条件,比如各项参数的动态变化,先当常量用着

        #更新每日感染人数
        self.InfectedI=self.PeopleN*self.InfectedI0\
            /(self.InfectedI0+(self.PeopleN-self.InfectedI0)*math.pow(math.e,-(self.beta*self.R*time*(1-self.IsolatedRate))))

        self.HealthyS=self.PeopleN-self.InfectedI
        self.s=self.HealthyS/self.PeopleN
        self.i=self.InfectedI/self.PeopleN
