# -*- coding: utf-8 -*-
import os

base_dir = '/root/1CT-Share/20260828-global500/Founder'

# --- 051 MERCEDES ---
p51 = os.path.join(base_dir, '051-奔驰集团-MercedesBenz/founder.md')
with open(p51, 'r', encoding='utf-8') as f: c51 = f.read()
extra_51 = """
### 3. 卡尔·本茨的曼海姆车间与第一位顾客法国人罗歇
在获得汽车专利之初，本茨的汽车在德国本土遭遇了长达两年的冷遇：
- 德国各大城市的警察局甚至规定汽车上街必须由专人手持红旗在前面步行引路；
- 1888年巴黎世博会前夕，一位名叫埃米尔·罗歇（Émile Roger）的法国巴黎机械商人偶然见到了本茨的三轮汽车，当场被其精密的机械结构所折服，成为了本茨历史上第一位正式购车的海外客户与巴黎独家代理商；
- 法国市场的热销反向刺激了德国本土，让卡尔·本茨摆脱了破产清算的阴影。
"""
c51 = c51.replace('## 第二章：贝塔·本茨百公里旷世试驾', extra_51 + '\n## 第二章：贝塔·本茨百公里旷世试驾')
with open(p51, 'w', encoding='utf-8') as f: f.write(c51)
print(f"051 Mercedes updated: {len(c51.encode('utf-8'))} bytes")


# --- 055 HONDA ---
p55 = os.path.join(base_dir, '055-本田汽车-Honda/founder.md')
with open(p55, 'r', encoding='utf-8') as f: c55 = f.read()
extra_55 = """
### 3. 东海精机活塞环挫折与中途岛战役空袭
在创办本田摩托之前，本田宗一郎曾于 1937 年创立东海精机公司，专门研发汽车活塞环：
- 当时他把样品送交丰田汽车检验，50 根活塞环中竟然只有 3 根达到丰田标准，其余全部因材质脆弱被退货；
- 宗一郎极度受挫，但他没有放弃，而是以旁听生身份进入滨松高等工业学校苦读冶金金属学，终于攻克了硅铝合金铸造工艺，成为二战期间丰田汽车的核心活塞环供应商；
- 1945年中途岛战役后的美军大轰炸将东海精机厂房夷为平地，宗一郎以 45 万日元将残存设备卖给丰田，随后闭门休整整整一年，为随后的摩托车大创业蓄积力量。
"""
c55 = c55.replace('## 第三章：遇见管家藤泽武夫', extra_55 + '\n## 第三章：遇见管家藤泽武夫')
with open(p55, 'w', encoding='utf-8') as f: f.write(c55)
print(f"055 Honda updated: {len(c55.encode('utf-8'))} bytes")


# --- 056 ALIBABA ---
p56 = os.path.join(base_dir, '056-阿里巴巴-Alibaba/founder.md')
with open(p56, 'r', encoding='utf-8') as f: c56 = f.read()
extra_56 = """
### 4. 2000年互联网泡沫破灭与“延安整风、抗日军政大学”三大运动
在获得软银投资仅仅几个月后，2000年全球互联网泡沫骤然破灭：
- 纳斯达克崩盘，硅谷每天有数十家互联网企业关门破产，阿里在硅谷和香港的分支机构每月疯狂烧钱，现金流只能支撑半年；
- 马云展现出了极具战略定力的危机处置魄力：
  - “回到中国！”他果断关闭硅谷办公室，将海外业务全部收缩撤回杭州本土；
  - 在内部发起了著名的“三大运动”：**延安整风运动（统一价值观与使命）、抗日军政大学（培训干部团队）、南泥湾开荒（推出为中小企业赚钱的‘中国供应商’产品）**；
  - 正是这场绝地大求生，让阿里在泡沫寒冬中率先实现了单日营收 100 万元的自我造血奇迹！
"""
c56 = c56.replace('## 第三章：支付宝担保交易破冰', extra_56 + '\n## 第三章：支付宝担保交易破冰')
with open(p56, 'w', encoding='utf-8') as f: f.write(c56)
print(f"056 Alibaba updated: {len(c56.encode('utf-8'))} bytes")


# --- 059 CITIC ---
p59 = os.path.join(base_dir, '059-中信集团-CITIC/founder.md')
with open(p59, 'r', encoding='utf-8') as f: c59 = f.read()
extra_59 = """
### 3. 荣毅仁与基辛格在和平宾馆的“吃烤鸭定创投”
在 1979 年中信成立前夕，美国前国务卿**亨利·基辛格 (Henry Kissinger)** 率团访华：
- 基辛格特地提出要拜会当时尚未复出的荣毅仁；
- 荣毅仁在全聚德烤鸭店宴请基辛格，两人在席间就中美建交后的投资法律保障、外汇结算进行了长达数小时的深入探讨；
- 基辛格回国后向美国商界领袖极力推荐：“去中国投资，一定要找荣毅仁！”这为中信早期打通西方资本与工业界人脉奠定了极关键的国际声誉基石。
"""
c59 = c59.replace('## 第二章：和平宾馆三间客房创世纪', extra_59 + '\n## 第二章：和平宾馆三间客房创世纪')
with open(p59, 'w', encoding='utf-8') as f: f.write(c59)
print(f"059 CITIC updated: {len(c59.encode('utf-8'))} bytes")

