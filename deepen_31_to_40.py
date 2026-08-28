# -*- coding: utf-8 -*-
import os

base_dir = '/root/1CT-Share/20260828-global500/Founder'

# --- 031 ELEVANCE HEALTH ---
p31 = os.path.join(base_dir, '031-ElevanceHealth/founder.md')
with open(p31, 'r', encoding='utf-8') as f: c31 = f.read()
extra_31 = """
### 3. 1930年代蓝十字与蓝盾的双剑合璧：从住院到医生的全面闭环
随着达拉斯贝勒大学医院“蓝十字”住院预付计划在全美引发狂潮，另一个医疗支付的巨大痛点浮出水面：
- “蓝十字”仅涵盖了病房床位、护士护理与手术室物理使用费用，而主治医生的专业诊疗、开刀与巡诊费用并不包含在内；
- 1939年，在加利福尼亚州，由当地医学会牵头，创立了专门为医生专业诊疗服务提供预付保障的互助计划，并以**“蓝盾 (Blue Shield)”**为标志；
- 从此，“蓝十字（管医院病床）”与“蓝盾（管医生诊疗）”构成了现代美国医疗保险体系最著名的双子星座，为安西姆日后掌控全美数十个州的蓝十字蓝盾独家特许网络奠定了历史根基。
"""
c31 = c31.replace('## 第二章：跨州大兼并', extra_31 + '\n## 第二章：跨州大兼并')
with open(p31, 'w', encoding='utf-8') as f: f.write(c31)
print(f"031 Elevance updated: {len(c31.encode('utf-8'))} bytes")


# --- 032 CENTENE ---
p32 = os.path.join(base_dir, '032-Centene/founder.md')
with open(p32, 'r', encoding='utf-8') as f: c32 = f.read()
extra_32 = """
### 2. 贝蒂·布林克的“一美元互助记账本”与人道温度
在 1984 年创办初期，贝蒂·布林克不仅是管理机构的创办人，更是全密尔沃基数千名贫困母亲的“知心大姐”：
- 很多贫困单亲母亲因拖欠水电费而面临被房东驱逐，贝蒂自掏腰包设立了一个微型互助应急基金；
- 面对那些因自卑而不敢踏入正规私立大医院诊室的黑人和拉美裔流浪家庭，贝蒂亲自陪同他们走进诊室，用她温柔坚定的声音向医生解释：“在疾病面前，每一个生命都同样尊贵，我们计划会为他们全额担保！”
- 贝蒂用纯粹的母性光辉与无私善意，为森特纳注入了延续数十年的“以人为本、守护弱者”的至高企业灵魂。
"""
c32 = c32.replace('## 第二章：迈克尔·奈多夫接棒', extra_32 + '\n## 第二章：迈克尔·奈多夫接棒')
with open(p32, 'w', encoding='utf-8') as f: f.write(c32)
print(f"032 Centene updated: {len(c32.encode('utf-8'))} bytes")


# --- 034 BANK OF AMERICA ---
p34 = os.path.join(base_dir, '034-美国银行-BankOfAmerica/founder.md')
with open(p34, 'r', encoding='utf-8') as f: c34 = f.read()
extra_34 = """
### 3. 加州葡萄园与纳帕谷葡萄酒现代农业的金融天使
在资助好莱坞与金门大桥之外，贾尼尼是拯救与托起加州现代农业（特别是纳帕谷葡萄酒产业）的头号金融功臣：
- 20世纪初，加利福尼亚的农业饱受干旱、病虫害与季节性资金断裂的困扰，华尔街银行家认为农业收成受制于老天爷，极度抗拒向果农贷款；
- 贾尼尼走遍了加州中央山谷的每一个葡萄园、橙子林和奶牛场。他根据不同农作物的成熟生长周期，量身定制了“丰收后还本付息”的柔性农业抵押信贷；
- 当 1920 年代禁酒令颁布沉重打击加州葡萄酒庄时，贾尼尼向陷入绝境的纳帕谷（Napa Valley）意大利酿酒世家提供了长达数十年的无息展期贷款，保住了珍贵的百年老藤葡萄庄园，造就了今天名震全球的加州葡萄酒王国。
"""
c34 = c34.replace('## 第四章：A.P. 贾尼尼与美国银行的八大底层', extra_34 + '\n## 第四章：A.P. 贾尼尼与美国银行的八大底层')
with open(p34, 'w', encoding='utf-8') as f: f.write(c34)
print(f"034 BankOfAmerica updated: {len(c34.encode('utf-8'))} bytes")


# --- 038 FORD ---
p38 = os.path.join(base_dir, '038-福特汽车-Ford/founder.md')
with open(p38, 'r', encoding='utf-8') as f: c38 = f.read()
extra_38 = """
### 4. 彻底粉碎塞尔登垄断专利恶法（Selden Patent）
在福特创立初期，一个由全美传统汽车制造寡头组成的“特许汽车制造商协会 (ALAM)”手握乔治·塞尔登（George Selden）的一项模糊宽泛的内燃机专利，强制要求全美所有汽车厂必须向其缴纳高昂的专利保护费，并企图禁止福特生产平价汽车。

亨利·福特展现出了誓死不屈的硬核反骨：
- 福特拒绝向垄断协会低头缴纳一分钱，他在全美各大报纸刊登整版广告宣告：“福特将为每一位购买福特汽车的顾客提供法律担保，誓与专利流氓抗战到底！”
- 历经长达八年的艰苦诉讼与上百次法庭机械原理辩论，1911年联邦上诉法院最终裁定塞尔登专利对福特无效；
- 福特单枪匹马打破了行业垄断枷锁，彻底扫清了全美汽车工业自由竞争与技术普及的制度障碍。
"""
c38 = c38.replace('## 第三章：1913年流动装配线', extra_38 + '\n## 第三章：1913年流动装配线')
with open(p38, 'w', encoding='utf-8') as f: f.write(c38)
print(f"038 Ford updated: {len(c38.encode('utf-8'))} bytes")


# --- 039 GM ---
p39 = os.path.join(base_dir, '039-通用汽车-GM/founder.md')
with open(p39, 'r', encoding='utf-8') as f: c39 = f.read()
extra_39 = """
### 3. 哈利·厄尔与世界第一款概念车“别克 Y-Job”
在斯隆的力主下，通用汽车于 1927 年成立了全球汽车工业历史上第一个独立的造型设计与色彩部门（Art & Colour Section），由传奇工业设计师**哈利·厄尔 (Harley Earl)** 掌舵：
- 1938年，哈利·厄尔推出了人类汽车历史上**第一款真正意义上的“概念车”——别克 Y-Job (Buick Y-Job)**；
- 首次将隐藏式大灯、流线型瀑布式进气格栅、车身嵌入式门把手与电动升降软顶引入汽车设计；
- 这彻底将汽车从冰冷的机械工业品升华为充满艺术张力与情感荷尔蒙的现代工业艺术品，奠定了底特律作为全球汽车设计之都的黄金地位。
"""
c39 = c39.replace('## 第三章：通用汽车与斯隆的八大底层', extra_39 + '\n## 第三章：通用汽车与斯隆的八大底层')
with open(p39, 'w', encoding='utf-8') as f: f.write(c39)
print(f"039 GM updated: {len(c39.encode('utf-8'))} bytes")

