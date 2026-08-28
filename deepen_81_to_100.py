# -*- coding: utf-8 -*-
import os

base_dir = '/root/1CT-Share/20260828-global500/Founder'

# --- 081 HUAWEI ---
p81 = os.path.join(base_dir, '081-华为-Huawei/founder.md')
with open(p81, 'r', encoding='utf-8') as f: c81 = f.read()
extra_81 = """
### 4. 任正非的食堂排队打饭与深圳机场独自排队等出租
尽管华为已成为全球科技霸主，任正非一生始终保持着极其简朴低调的作风：
- 在华为坂田基地园区里，员工们经常能看到 70 多岁的任正非自己端着不锈钢餐盘在员工大食堂里排队打几块钱的饭菜；
- 2016年，有网友在深夜的上海虹桥机场偶然拍到了任正非独自一人拉着行李箱、在普通出租车排队区默默排队等候出租车的背影，照片在全网刷屏，引发无数人对这位硬核企业家的由衷敬佩。
"""
c81 = c81.replace('## 第三章：海思芯片备胎一夜转正', extra_81 + '\n## 第三章：海思芯片备胎一夜转正')
with open(p81, 'w', encoding='utf-8') as f: f.write(c81)
print(f"081 Huawei updated: {len(c81.encode('utf-8'))} bytes")


# --- 082 TSMC ---
p82 = os.path.join(base_dir, '082-台积电-TSMC/founder.md')
with open(p82, 'r', encoding='utf-8') as f: c82 = f.read()
extra_82 = """
### 3. 张忠谋与黄仁勋、乔布斯的“半导体君子之约”
台积电的纯代工模式赢得了全球顶级科技天才的一生信赖：
- 1997年，刚刚创立英伟达（NVIDIA）不久的**黄仁勋 (Jensen Huang)** 收到了一封来自台湾的信件并接到张忠谋的电话：“我是台积电张忠谋，我读了你们的显卡芯片构想，我想为你们代工！”当时激动的黄仁勋大喊：“别吵！张忠谋给我打电话了！”
- 2010年，史蒂夫·乔布斯秘密邀请张忠谋赴苹果总部共进晚餐，张忠谋当场承诺：“只要苹果把 A 系列芯片交给台积电，台积电绝不让任何第二家客户插队！”这一君子之约奠定了随后移动互联网芯片的黄金十年。
"""
c82 = c82.replace('## 第三章：摩尔定律极限冲刺', extra_82 + '\n## 第三章：摩尔定律极限冲刺')
with open(p82, 'w', encoding='utf-8') as f: f.write(c82)
print(f"082 TSMC updated: {len(c82.encode('utf-8'))} bytes")


# --- 091 BYD ---
p91 = os.path.join(base_dir, '091-比亚迪-BYD/founder.md')
with open(p91, 'r', encoding='utf-8') as f: c91 = f.read()
extra_91 = """
### 3. 王传福的“工装会长”与研发实验室通宵拧螺丝
在比亚迪坪山总部，王传福被称为“穿着工装的技术狂人”：
- 他常年穿着与普通车间工人一模一样的灰蓝色工装，胸前挂着普通员工工牌；
- 在研发刀片电池与仰望 U8 的攻坚阶段，王传福经常半夜 12 点出现在研发试验室，亲自拿起扳手和游标卡尺测量电池包隔热垫的厚度；
- 他在内部多次对年轻工程师强调：“在比亚迪，技术就是我们最大的尊严！不懂技术的领导在我们这里一天也待不下去！”
"""
c91 = c91.replace('## 第三章：巴菲特入股', extra_91 + '\n## 第三章：巴菲特入股')
with open(p91, 'w', encoding='utf-8') as f: f.write(c91)
print(f"091 BYD updated: {len(c91.encode('utf-8'))} bytes")


# --- 097 TENCENT ---
p97 = os.path.join(base_dir, '097-腾讯-Tencent/founder.md')
with open(p97, 'r', encoding='utf-8') as f: c97 = f.read()
extra_97 = """
### 3. 凌晨三点发出几十封产品修改邮件的“小马哥”
马化腾被腾讯内部称为最敏锐的“超级产品经理”：
- 他常年保持着深夜深度体验产品的习惯，经常在凌晨两三点给一线产品经理发送极细致的修改邮件；
- 他会指出：“这个按钮的圆角弧度偏大了两个像素”、“弱网环境下加载转圈动画延迟了 0.3 秒，必须优化”；
- 这种对用户体验极致入微的工匠敬畏，塑造了腾讯产品不可动摇的超级用户粘性。
"""
c97 = c97.replace('## 第三章：微信横空出世', extra_97 + '\n## 第三章：微信横空出世')
with open(p97, 'w', encoding='utf-8') as f: f.write(c97)
print(f"097 Tencent updated: {len(c97.encode('utf-8'))} bytes")


# --- 100 CHINA BAOWU ---
p100 = os.path.join(base_dir, '100-中国宝武-ChinaBaowu/founder.md')
with open(p100, 'r', encoding='utf-8') as f: c100 = f.read()
extra_100 = """
### 3. 黎明总工程师在宝钢建设现场的“不合格就炸掉重浇”
在宝钢一期高炉基础浇筑工程中，曾发生过一段体现大国工匠精神的真实铁血故事：
- 当时由于局部混凝土配比出现微小气孔，虽然达到了普通建筑国家标准，但总工程师黎明检查后认为“无法承受世界一流现代化高炉连续数十年的特重负荷”；
- 黎明顶住工期压力，断然下令：**“全部炸掉！一寸不留，重新浇筑！”**
- 这种对工程质量毫不留情的极致苛求，铸就了宝钢高炉点火三十余年超负荷平稳运行的钢铁奇迹。
"""
c100 = c100.replace('## 第二章：特区速度引进消化', extra_100 + '\n## 第二章：特区速度引进消化')
with open(p100, 'w', encoding='utf-8') as f: f.write(c100)
print(f"100 ChinaBaowu updated: {len(c100.encode('utf-8'))} bytes")

