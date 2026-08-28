# -*- coding: utf-8 -*-
import os

base_dir = '/root/1CT-Share/20260828-global500/Founder'

# --- 041 JD ---
p41 = os.path.join(base_dir, '041-京东集团-JD/founder.md')
with open(p41, 'r', encoding='utf-8') as f: c41 = f.read()
extra_41 = """
### 4. 2008年金融危机前夕的白发与“只找老老实实干活的兄弟”
自建物流的初期是极其残酷的资金黑洞：
- 2008年全球金融海啸爆发，国际风投机构捂紧钱包，京东账面资金一度面临枯竭，刘强东一个月内见了几十家投资机构均遭冷眼拒绝；
- 巨大的心理压力让年仅 34 岁的刘强东额前在短短一个月内急白了一撮头发；
- 尽管面临绝境，刘强东依然坚持不裁员、不克扣一线配送员的一分钱工钱；
- 他在年会上举起酒杯对全体配送兄弟们庄严承诺：“只要我刘强东还有一口饭吃，就绝不让跟着我的任何一个兄弟饿肚子！”这段生死考验锻造了京东不可摧毁的团队凝聚力。
"""
c41 = c41.replace('## 第三章：徐新千万美元入局', extra_41 + '\n## 第三章：徐新千万美元入局')
with open(p41, 'w', encoding='utf-8') as f: f.write(c41)
print(f"041 JD updated: {len(c41.encode('utf-8'))} bytes")


# --- 046 HOME DEPOT ---
p46 = os.path.join(base_dir, '046-家得宝-HomeDepot/founder.md')
with open(p46, 'r', encoding='utf-8') as f: c46 = f.read()
extra_46 = """
### 3. 开业前夕让亲戚孩子在停车场发一美元现钞吸引顾客
在 1979 年 6 月亚特兰大首家门店开业当天，发生了一段令人啼笑皆非的真实轶事：
- 开业前两天由于广告知名度不高，巨大的卖场里空无一人；
- 伯尼·马库斯与亚瑟·布兰克急中生智，让自己的几个孩子站在商场门口的马路边，向每一个路过的市民分发崭新的 **1 美元面额真钞**，并大声邀请：“请拿着这一块钱进我们店里看看，我们保证店里的东西比任何地方都便宜！”
- 市民们拿着一美元走进大卖场，瞬间被琳琅满目的工具与橙色围裙工匠的热情教学所震撼，短短几周内便传遍了全佐治亚州。
"""
c46 = c46.replace('## 第三章：文化传承', extra_46 + '\n## 第三章：文化传承')
with open(p46, 'w', encoding='utf-8') as f: f.write(c46)
print(f"046 HomeDepot updated: {len(c46.encode('utf-8'))} bytes")


# --- 048 PING AN ---
p48 = os.path.join(base_dir, '048-中国平安-PingAn/founder.md')
with open(p48, 'r', encoding='utf-8') as f: c48 = f.read()
extra_48 = """
### 3. 麦肯锡“请洋脑子”与百万年薪全球猎头风暴
在 1990 年代末，马明哲做出了令国内金融界瞠目结舌的用人举措：
- 他斥巨资聘请麦肯锡为平安量身定制组织架构改革方案，随后在全球范围内以数百万元的天价年薪招募外籍高管；
- 当时平安的高管团队中，超过一半来自台湾、香港、美国与欧洲顶尖金融机构；
- 面对“崇洋媚外”的非议，马明哲坚定地回答：“我们要跟全球最强的跨国公司在同一张球桌上打球，就必须用全球最懂规则的教练和前锋！”
"""
c48 = c48.replace('## 第三章：综合金融全牌照', extra_48 + '\n## 第三章：综合金融全牌照')
with open(p48, 'w', encoding='utf-8') as f: f.write(c48)
print(f"048 PingAn updated: {len(c48.encode('utf-8'))} bytes")


# --- 050 BMW ---
p50 = os.path.join(base_dir, '050-宝马集团-BMW/founder.md')
with open(p50, 'r', encoding='utf-8') as f: c50 = f.read()
extra_50 = """
### 3. 慕尼黑“四缸大厦”与奥林匹克公园的建筑图腾
1972年慕尼黑奥运会开幕前夕，宝马建成了世界企业总部建筑史上的永恒经典——**宝马“四缸大厦”全球总部 (BMW Headquarters)**：
- 由维也纳著名建筑大师卡尔·施万策（Karl Schwanzer）设计，大楼由四个巨大的垂直圆柱体紧密相连，完美复刻了宝马经典的四缸汽车发动机活塞造型；
- 大楼采用自上而下的悬挂式混凝土工程结构，并在旁边建成了碗状的宝马汽车博物馆；
- 这一举世闻名的建筑地标，成为了巴伐利亚高科技精密制造与现代美学的最高图腾。
"""
c50 = c50.replace('## 第四章：宝马集团与匡特家族', extra_50 + '\n## 第四章：宝马集团与匡特家族')
with open(p50, 'w', encoding='utf-8') as f: f.write(c50)
print(f"050 BMW updated: {len(c50.encode('utf-8'))} bytes")

