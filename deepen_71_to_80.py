# -*- coding: utf-8 -*-
import os

base_dir = '/root/1CT-Share/20260828-global500/Founder'

# --- 072 HYUNDAI ---
p72 = os.path.join(base_dir, '072-现代汽车-Hyundai/founder.md')
with open(p72, 'r', encoding='utf-8') as f: c72 = f.read()
extra_72 = """
### 4. 严冬露宿工地的草鞋会长与晨间五点全家早餐会
郑周永一生保持着极度苛刻而朴素的生活作风：
- 哪怕在成为韩国首富之后，他依然常年住在汉城清云洞一栋没有奢华装修的老宅里，脚上穿着补了又补的旧皮鞋与粗布袜子；
- 每天清晨 5 点整，郑周永会召集所有儿子和核心高管一起吃大酱汤早餐，一边吃一边逐一盘问前一天工地的每一个施工细节；
- 在承建沙特朱拜勒工业港超级工程期间，60多岁的郑周永直接搬进沙特沙漠工地的集装箱铁皮屋里，顶着 50 度的高温与一线工人同吃同住长达数月，以身作则树立了令人震撼的现代韩国企业精神。
"""
c72 = c72.replace('## 第三章：五百元龟船借款神话', extra_72 + '\n## 第三章：五百元龟船借款神话')
with open(p72, 'w', encoding='utf-8') as f: f.write(c72)
print(f"072 Hyundai updated: {len(c72.encode('utf-8'))} bytes")


# --- 076 MITSUBISHI ---
p76 = os.path.join(base_dir, '076-三菱商事-MitsubishiCorp/founder.md')
with open(p76, 'r', encoding='utf-8') as f: c76 = f.read()
extra_76 = """
### 3. 岩崎弥太郎与坂本龙马的土佐同志情谊
在幕末动荡岁月里，岩崎弥太郎与明治维新最著名的传奇志士**坂本龙马 (Ryoma Sakamoto)** 同为土佐藩乡士：
- 坂本龙马在长崎创立了日本历史上第一个现代股份制商贸政治团体“海援队”；
- 岩崎弥太郎当时担任土佐藩长崎商会的主管，负责为海援队调配枪支弹药与远洋帆船的财务账目；
- 坂本龙马遇刺后，岩崎弥太郎继承了海援队“以海外贸易强盛日本”的遗志，将这种打破封建门阀、向大洋进军的雄心壮志，彻底熔铸进了三菱的骨髓深处。
"""
c76 = c76.replace('## 第二章：西南战争大发国难财', extra_76 + '\n## 第二章：西南战争大发国难财')
with open(p76, 'w', encoding='utf-8') as f: f.write(c76)
print(f"076 Mitsubishi updated: {len(c76.encode('utf-8'))} bytes")


# --- 078 HENGLI ---
p78 = os.path.join(base_dir, '078-恒力集团-Hengli/founder.md')
with open(p78, 'r', encoding='utf-8') as f: c78 = f.read()
extra_78 = """
### 3. 2008年全球金融危机逆势豪赌织机
在 2008 年全球金融海啸爆发时，江浙纺织业遭遇大面积倒闭潮：
- 当所有同行都在恐慌抛售设备、关停生产线时，陈建华与范红卫做出了惊人的逆向决策；
- 两人趁欧洲机械制造巨头陷入困境、大幅降价的千载难逢良机，以骨折价一次性订购了上千台世界顶级的德国进口喷气织机；
- 次年全球经济复苏、纺织订单报复性爆发时，恒力集团凭借全行业最庞大、最先进的现成产能瞬间吃下海量高端面料订单，产值直接翻番！
"""
c78 = c78.replace('## 第二章：引入进口喷气织机', extra_78 + '\n## 第二章：引入进口喷气织机')
with open(p78, 'w', encoding='utf-8') as f: f.write(c78)
print(f"078 Hengli updated: {len(c78.encode('utf-8'))} bytes")


# --- 080 WELLS FARGO ---
p80 = os.path.join(base_dir, '080-富国银行-WellsFargo/founder.md')
with open(p80, 'r', encoding='utf-8') as f: c80 = f.read()
extra_80 = """
### 3. 1906年旧金山大地震大火中的金库营救传奇
1906年4月18日清晨，旧金山发生里氏 7.8 级大地震并引发三天三夜的毁灭性大火：
- 当整条蒙哥马利金融街被烈火包围时，富国银行的员工冒死用湿棉被包裹着金库账本与装满金条的重型铁箱，用两辆防弹马车抢运至海湾码头装船避难；
- 大火熄灭后，在满城瓦砾废墟中，富国银行在一间搭着帆布帐篷的临时木桌前贴出告示：“所有客户的黄金与存款分文不差，即时全额兑付！”
- 这一在火海废墟中的绝对兑现奇迹，让富国银行在全美加州人民心中升华为不可动摇的信任圣殿。
"""
c80 = c80.replace('## 第二章：从驿站马车到全美社区银行霸主', extra_80 + '\n## 第二章：从驿站马车到全美社区银行霸主')
with open(p80, 'w', encoding='utf-8') as f: f.write(c80)
print(f"080 WellsFargo updated: {len(c80.encode('utf-8'))} bytes")

