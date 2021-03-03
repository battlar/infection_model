# -
使用SI模型模拟新冠疫情传播过程
代码思路：  
  1.使用SI传染模型对病毒传播过程进行模拟，明确模型中影响传播效果的因素，包括一个时间周期内接触的人数R，传染率beta。  
  2.考虑区域人口密度，人们出行意愿，口罩普及度，社交距离，隔离率对R和beta的影响。为简化模型，这些因素都为固定值。  
  3.通过对照实验，每次只调整一个因素，观察该改变对模型效果的影响。

实验数据：  
  见文件夹datas/

实验代码：  
  见文件夹code/

实验结论：  
  在SI模型下，所有人最终都会被传染，只是时间早晚问题。但如下条件下，传染达到峰值的时间会被推迟：  
  1.人口密度小的地区  
  2.人们出行意愿低  
  3.口罩普及率高  
  4.较大的社交距离  
  5.较高的隔离率  
  通过如上措施，可以将传染峰值的到来向后推迟，从而得到宝贵的时间来进行治疗方案的升级。  


可以改进的方向：  
  1.模型中未考虑感染者者被治愈的情况，考虑治愈可以使用SIS模型表示。  
  2.模型中未考虑感染者死亡的情况，病患的死亡可以使用SIR模型表示。  
  3.模型中人们出行意愿，口罩普及率，社交距离三个因素实际上会随着疫情的发展情况变动。以人们出行意愿为例，疫情严重时人们出行意愿会下降，不严重时会上升，这一点在模型中没有反映出来。
  4.代码本身还有需要改进的地方，主要包括一些输入判定，以及用户体验方面
