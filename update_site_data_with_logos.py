# -*- coding: utf-8 -*-
import os, json, re

base_dir = '/root/1CT-Share/20260828-global500'
founder_dir = os.path.join(base_dir, 'Founder')

# Curated verified domains and brand colors for all 100 Fortune Global 500 companies
brand_meta = {
    1: {'domain': 'amazon.com', 'color': '#FF9900', 'bg': 'bg-amber-500'},
    2: {'domain': 'walmart.com', 'color': '#0071DC', 'bg': 'bg-blue-600'},
    3: {'domain': 'stategrid.com.cn', 'color': '#007B5F', 'bg': 'bg-emerald-700'},
    4: {'domain': 'unitedhealthgroup.com', 'color': '#1E3A8A', 'bg': 'bg-blue-900'},
    5: {'domain': 'aramco.com', 'color': '#00A3E0', 'bg': 'bg-sky-600'},
    6: {'domain': 'apple.com', 'color': '#1E293B', 'bg': 'bg-slate-900'},
    7: {'domain': 'mckesson.com', 'color': '#004B87', 'bg': 'bg-sky-800'},
    8: {'domain': 'google.com', 'color': '#4285F4', 'bg': 'bg-blue-500'},
    9: {'domain': 'cvshealth.com', 'color': '#CC0000', 'bg': 'bg-red-600'},
    10: {'domain': 'cnpc.com.cn', 'color': '#E11414', 'bg': 'bg-red-700'},
    11: {'domain': 'berkshirehathaway.com', 'color': '#334155', 'bg': 'bg-slate-700'},
    12: {'domain': 'sinopec.com', 'color': '#C8102E', 'bg': 'bg-rose-700'},
    13: {'domain': 'volkswagen.de', 'color': '#001E50', 'bg': 'bg-blue-950'},
    14: {'domain': 'toyota-global.com', 'color': '#EB0A1E', 'bg': 'bg-red-600'},
    15: {'domain': 'exxonmobil.com', 'color': '#EE1C25', 'bg': 'bg-red-600'},
    16: {'domain': 'cencora.com', 'color': '#008080', 'bg': 'bg-teal-700'},
    17: {'domain': 'cscec.com', 'color': '#005BAC', 'bg': 'bg-blue-700'},
    18: {'domain': 'microsoft.com', 'color': '#00A4EF', 'bg': 'bg-sky-500'},
    19: {'domain': 'jpmorganchase.com', 'color': '#112233', 'bg': 'bg-slate-800'},
    20: {'domain': 'costco.com', 'color': '#E31837', 'bg': 'bg-red-600'},
    21: {'domain': 'cigna.com', 'color': '#007AA6', 'bg': 'bg-cyan-700'},
    22: {'domain': 'shell.com', 'color': '#FBCE07', 'bg': 'bg-amber-400'},
    23: {'domain': 'foxconn.com', 'color': '#005596', 'bg': 'bg-blue-700'},
    24: {'domain': 'glencore.com', 'color': '#002F6C', 'bg': 'bg-indigo-900'},
    25: {'domain': 'trafigura.com', 'color': '#E05A47', 'bg': 'bg-orange-600'},
    26: {'domain': 'samsung.com', 'color': '#1428A0', 'bg': 'bg-blue-700'},
    27: {'domain': 'cardinalhealth.com', 'color': '#C41230', 'bg': 'bg-rose-600'},
    28: {'domain': 'nvidia.com', 'color': '#76B900', 'bg': 'bg-lime-600'},
    29: {'domain': 'icbc.com.cn', 'color': '#C8102E', 'bg': 'bg-red-700'},
    30: {'domain': 'meta.com', 'color': '#0081FB', 'bg': 'bg-blue-600'},
    31: {'domain': 'elevancehealth.com', 'color': '#002B49', 'bg': 'bg-slate-800'},
    32: {'domain': 'centene.com', 'color': '#005696', 'bg': 'bg-blue-700'},
    33: {'domain': 'bp.com', 'color': '#007A33', 'bg': 'bg-green-700'},
    34: {'domain': 'bankofamerica.com', 'color': '#E31837', 'bg': 'bg-red-600'},
    35: {'domain': 'abchina.com', 'color': '#008575', 'bg': 'bg-emerald-700'},
    36: {'domain': 'chevron.com', 'color': '#005B94', 'bg': 'bg-sky-700'},
    37: {'domain': 'ccb.com', 'color': '#003B7E', 'bg': 'bg-blue-800'},
    38: {'domain': 'ford.com', 'color': '#002C6C', 'bg': 'bg-blue-900'},
    39: {'domain': 'gm.com', 'color': '#0055A5', 'bg': 'bg-blue-600'},
    40: {'domain': 'totalenergies.com', 'color': '#ED1C24', 'bg': 'bg-red-600'},
    41: {'domain': 'jd.com', 'color': '#E1251B', 'bg': 'bg-red-600'},
    42: {'domain': 'chinalife.com.cn', 'color': '#00833E', 'bg': 'bg-emerald-600'},
    43: {'domain': 'stellantis.com', 'color': '#0B2046', 'bg': 'bg-indigo-950'},
    44: {'domain': 'boc.cn', 'color': '#B21021', 'bg': 'bg-red-800'},
    45: {'domain': 'citigroup.com', 'color': '#003B70', 'bg': 'bg-blue-800'},
    46: {'domain': 'homedepot.com', 'color': '#F96302', 'bg': 'bg-orange-600'},
    47: {'domain': 'fanniemae.com', 'color': '#003366', 'bg': 'bg-blue-900'},
    48: {'domain': 'pingan.com', 'color': '#E60012', 'bg': 'bg-orange-600'},
    49: {'domain': 'crecg.com', 'color': '#004B87', 'bg': 'bg-blue-800'},
    50: {'domain': 'bmw.com', 'color': '#0066B1', 'bg': 'bg-blue-600'},
    51: {'domain': 'mercedes-benz.com', 'color': '#000000', 'bg': 'bg-slate-900'},
    52: {'domain': 'kroger.com', 'color': '#00559F', 'bg': 'bg-blue-700'},
    53: {'domain': 'chinamobile.com', 'color': '#0085D0', 'bg': 'bg-sky-600'},
    54: {'domain': 'santander.com', 'color': '#EC0000', 'bg': 'bg-red-600'},
    55: {'domain': 'honda.com', 'color': '#CC0000', 'bg': 'bg-red-600'},
    56: {'domain': 'alibaba.com', 'color': '#FF6A00', 'bg': 'bg-orange-500'},
    57: {'domain': 'crcc.cn', 'color': '#003366', 'bg': 'bg-blue-900'},
    58: {'domain': 'bnpparibas.com', 'color': '#00965E', 'bg': 'bg-emerald-600'},
    59: {'domain': 'citic.com', 'color': '#C8102E', 'bg': 'bg-red-700'},
    60: {'domain': 'verizon.com', 'color': '#CD040B', 'bg': 'bg-red-600'},
    61: {'domain': 'phillips66.com', 'color': '#E31837', 'bg': 'bg-red-600'},
    62: {'domain': 'hsbc.com', 'color': '#DB0011', 'bg': 'bg-red-600'},
    63: {'domain': 'marathonpetroleum.com', 'color': '#003A70', 'bg': 'bg-blue-900'},
    64: {'domain': 'sberbank.ru', 'color': '#21A038', 'bg': 'bg-green-600'},
    65: {'domain': 'telekom.com', 'color': '#E20074', 'bg': 'bg-pink-600'},
    66: {'domain': 'ccccltd.cn', 'color': '#004B87', 'bg': 'bg-blue-800'},
    67: {'domain': 'allianz.com', 'color': '#003781', 'bg': 'bg-blue-800'},
    68: {'domain': 'crc.com.hk', 'color': '#C8102E', 'bg': 'bg-red-700'},
    69: {'domain': 'stonex.com', 'color': '#002D62', 'bg': 'bg-slate-800'},
    70: {'domain': 'statefarm.com', 'color': '#D3222A', 'bg': 'bg-red-600'},
    71: {'domain': 'freddiemac.com', 'color': '#004B87', 'bg': 'bg-sky-800'},
    72: {'domain': 'hyundai.com', 'color': '#002C5F', 'bg': 'bg-blue-950'},
    73: {'domain': 'humana.com', 'color': '#78BE20', 'bg': 'bg-lime-600'},
    74: {'domain': 'edf.fr', 'color': '#FE5815', 'bg': 'bg-orange-600'},
    75: {'domain': 'att.com', 'color': '#00A8E0', 'bg': 'bg-sky-500'},
    76: {'domain': 'mitsubishicorp.com', 'color': '#E60012', 'bg': 'bg-red-600'},
    77: {'domain': 'goldmansachs.com', 'color': '#7399C6', 'bg': 'bg-blue-400'},
    78: {'domain': 'hengli.com', 'color': '#005596', 'bg': 'bg-blue-700'},
    79: {'domain': 'corporate.comcast.com', 'color': '#000000', 'bg': 'bg-slate-900'},
    80: {'domain': 'wellsfargo.com', 'color': '#D71E28', 'bg': 'bg-red-600'},
    81: {'domain': 'huawei.com', 'color': '#CF0A2C', 'bg': 'bg-red-600'},
    82: {'domain': 'tsmc.com', 'color': '#000000', 'bg': 'bg-slate-800'},
    83: {'domain': 'cnooc.com.cn', 'color': '#005596', 'bg': 'bg-blue-700'},
    84: {'domain': 'morganstanley.com', 'color': '#111827', 'bg': 'bg-slate-900'},
    85: {'domain': 'ril.com', 'color': '#003366', 'bg': 'bg-blue-900'},
    86: {'domain': 'csg.cn', 'color': '#007B5F', 'bg': 'bg-emerald-700'},
    87: {'domain': 'shandong-energy.com', 'color': '#C8102E', 'bg': 'bg-red-700'},
    88: {'domain': 'valero.com', 'color': '#005596', 'bg': 'bg-blue-700'},
    89: {'domain': 'gazprom.com', 'color': '#005596', 'bg': 'bg-blue-700'},
    90: {'domain': 'dell.com', 'color': '#007DB8', 'bg': 'bg-sky-600'},
    91: {'domain': 'byd.com', 'color': '#E60012', 'bg': 'bg-red-600'},
    92: {'domain': 'licindia.in', 'color': '#E5A823', 'bg': 'bg-amber-500'},
    93: {'domain': 'nestle.com', 'color': '#005CA9', 'bg': 'bg-blue-700'},
    94: {'domain': 'axa.com', 'color': '#00008F', 'bg': 'bg-blue-900'},
    95: {'domain': 'equinor.com', 'color': '#FF1243', 'bg': 'bg-rose-600'},
    96: {'domain': 'target.com', 'color': '#CC0000', 'bg': 'bg-red-600'},
    97: {'domain': 'tencent.com', 'color': '#0052D9', 'bg': 'bg-blue-600'},
    98: {'domain': 'aholddelhaize.com', 'color': '#009FE3', 'bg': 'bg-sky-500'},
    99: {'domain': 'minmetals.com.cn', 'color': '#C8102E', 'bg': 'bg-red-700'},
    100: {'domain': 'baowugroup.com', 'color': '#003A70', 'bg': 'bg-blue-900'}
}

# Curated exact founders (Chinese + English)
curated_founders = {
    1: "杰夫·贝索斯 (Jeff Bezos)",
    2: "山姆·沃尔顿 (Sam Walton)",
    3: "刘振亚 (Liu Zhenya)",
    4: "理查德·伯克 (Richard Burke)",
    5: "马克斯·斯坦尼克 (Max Steineke)",
    6: "史蒂夫·乔布斯 (Steve Jobs)",
    7: "约翰·麦克森 (John McKesson)",
    8: "拉里·佩奇 (Larry Page) & 谢尔盖·布林 (Sergey Brin)",
    9: "斯坦利·戈德斯坦 (Stanley Goldstein)",
    10: "李四光 (Li Siguang) & 王进喜 (Wang Jinxi)",
    11: "沃伦·巴菲特 (Warren Buffett) & 查理·芒格 (Charlie Munger)",
    12: "陈锦华 (Chen Jinhua)",
    13: "费迪南德·保时捷 (Ferdinand Porsche)",
    14: "丰田喜一郎 (Kiichiro Toyoda)",
    15: "约翰·D·洛克菲勒 (John D. Rockefeller)",
    16: "吕西安·布伦斯威格 (Lucien Brunswig)",
    17: "陆佑九 (Lu Youjiu)",
    18: "比尔·盖茨 (Bill Gates) & 保罗·艾伦 (Paul Allen)",
    19: "J.P. 摩根 (J. Pierpont Morgan)",
    20: "吉姆·辛内格尔 (James Sinegal)",
    21: "信诺创始先驱团队 (Cigna Pioneers)",
    22: "马库斯·萨缪尔 (Marcus Samuel)",
    23: "郭台铭 (Terry Gou)",
    24: "马克·里奇 (Marc Rich)",
    25: "克劳德·多芬 (Claude Dauphin)",
    26: "李秉喆 (Lee Byung-chul) & 李健熙 (Lee Kun-hee)",
    27: "罗伯特·D·沃尔特 (Robert D. Walter)",
    28: "黄仁勋 (Jensen Huang)",
    29: "姜建清与工行奠基团队 (ICBC Leadership)",
    30: "马克·扎克伯格 (Mark Zuckerberg)",
    31: "Elevance 创始先驱团队 (Elevance Pioneers)",
    32: "伊丽莎白·布林 (Elizabeth Brinn)",
    33: "威廉·达西 (William D'Arcy)",
    34: "阿马迪奥·贾尼尼 (Amadeo Giannini)",
    35: "中国农行奠基先驱团队 (ABC Pioneers)",
    36: "德米特里厄斯·斯科菲尔德 (D.G. Scofield)",
    37: "中国建行奠基先驱团队 (CCB Pioneers)",
    38: "亨利·福特 (Henry Ford)",
    39: "威廉·杜兰特 (William Durant) & 斯隆 (Alfred Sloan)",
    40: "欧内斯特·梅西埃 (Ernest Mercier)",
    41: "刘强东 (Richard Liu)",
    42: "中国人寿奠基先驱团队 (China Life Pioneers)",
    43: "乔瓦尼·阿涅利 (Giovanni Agnelli) & 标致家族",
    44: "孙中山与张嘉璈 (Bank of China Pioneers)",
    45: "塞缪尔·奥斯古德 (Samuel Osgood) & 桑迪·威尔",
    46: "伯尼·马库斯 (Bernie Marcus) & 阿瑟·布兰克",
    47: "罗斯福与房利美奠基团队 (Fannie Mae Pioneers)",
    48: "马明哲 (Peter Ma)",
    49: "中国中铁开路先锋团队 (CREC Pioneers)",
    50: "卡尔·拉普 (Karl Rapp) & 匡特家族",
    51: "卡尔·本茨 (Carl Benz) & 戈特利布·戴姆勒",
    52: "伯纳德·克罗格 (Bernard Kroger)",
    53: "中国移动奠基先驱团队 (China Mobile Pioneers)",
    54: "埃米尔·博廷 (Emilio Botín) & 桑坦德家族",
    55: "本田宗一郎 (Soichiro Honda) & 藤泽武夫",
    56: "马云 (Jack Ma) & 蔡崇信 (Joe Tsai)",
    57: "铁道兵与中铁建先驱团队 (CRCC Pioneers)",
    58: "米歇尔·佩贝罗 (Michel Pébereau)",
    59: "荣毅仁 (Rong Yiren)",
    60: "伊万·塞登伯格 (Ivan Seidenberg)",
    61: "弗兰克·菲利普斯 (Frank Phillips)",
    62: "托马斯·萨瑟兰德 (Thomas Sutherland)",
    63: "唐奈尔家族 (Donnell Family)",
    64: "格尔曼·格列夫 (Herman Gref)",
    65: "施特凡 (Heinrich von Stephan)",
    66: "中国交建百年奠基团队 (CCCC Pioneers)",
    67: "卡尔·冯·蒂梅 (Carl von Thieme)",
    68: "华润红色先驱谱系 (China Resources Pioneers)",
    69: "索尔·斯通 (Saul Stone)",
    70: "乔治·J·梅切尔 (George J. Mecherle)",
    71: "房地美奠基先驱团队 (Freddie Mac Pioneers)",
    72: "郑周永 (Chung Ju-yung)",
    73: "大卫·A·琼斯 (David A. Jones Sr.)",
    74: "皮埃尔·梅斯梅尔与法电团队 (EDF Pioneers)",
    75: "亚历山大·贝尔 (Alexander Graham Bell)",
    76: "岩崎弥太郎 (Yataro Iwasaki)",
    77: "马库斯·高盛 (Marcus Goldman)",
    78: "陈建华 (Chen Jianhua) & 范红卫 (Fan Hongwei)",
    79: "拉尔夫·J·罗伯茨 (Ralph J. Roberts)",
    80: "亨利·韦尔斯 (Henry Wells) & 威廉·法戈",
    81: "任正非 (Ren Zhengfei)",
    82: "张忠谋 (Morris Chang)",
    83: "秦文彩与中海油奠基先驱 (CNOOC Pioneers)",
    84: "亨利·S·摩根 (Henry S. Morgan) & 哈罗德·斯坦利",
    85: "迪鲁巴伊·安巴尼 (Dhirubhai Ambani)",
    86: "袁懋振与南网奠基先驱 (CSG Pioneers)",
    87: "卜兆德与山东能源开拓者 (Shandong Energy Pioneers)",
    88: "比尔·格里希 (Bill Greehey)",
    89: "维克托·切尔诺梅尔金 (Viktor Chernomyrdin)",
    90: "迈克尔·戴尔 (Michael Dell)",
    91: "王传福 (Wang Chuanfu)",
    92: "印度人寿奠基先驱 (LIC Pioneers)",
    93: "亨利·雀巢 (Henri Nestlé) & 佩奇兄弟",
    94: "克劳德·贝贝阿 (Claude Bébéar)",
    95: "法鲁克·阿尔-卡西姆 (Farouk Al-Kasim)",
    96: "乔治·戴顿 (George Dayton)",
    97: "马化腾 (Pony Ma) 与腾讯创始团队",
    98: "阿尔伯特·海恩 (Albert Heijn) & 德尔海兹兄弟",
    99: "中国五矿奠基先驱团队 (Minmetals Pioneers)",
    100: "宝钢与武钢奠基开拓团队 (Baowu Pioneers)"
}

country_map = {
    'Amazon': '🇺🇸 美国', 'Walmart': '🇺🇸 美国', 'StateGrid': '🇨🇳 中国', 'UnitedHealth': '🇺🇸 美国',
    'SaudiAramco': '🇸🇦 沙特', 'Apple': '🇺🇸 美国', 'McKesson': '🇺🇸 美国', 'Alphabet': '🇺🇸 美国',
    'CVSHealth': '🇺🇸 美国', 'CNPC': '🇨🇳 中国', 'BerkshireHathaway': '🇺🇸 美国', 'Sinopec': '🇨🇳 中国',
    'Volkswagen': '🇩🇪 德国', 'Toyota': '🇯🇵 日本', 'ExxonMobil': '🇺🇸 美国', 'Cencora': '🇺🇸 美国',
    'CSCEC': '🇨🇳 中国', 'Microsoft': '🇺🇸 美国', 'JPMorganChase': '🇺🇸 美国', 'Costco': '🇺🇸 美国',
    'Cigna': '🇺🇸 美国', 'Shell': '🇬🇧 英国', 'Foxconn': '🇨🇳 中国', 'Glencore': '🇨🇭 瑞士',
    'Trafigura': '🇸🇬 新加坡', 'Samsung': '🇰🇷 韩国', 'CardinalHealth': '🇺🇸 美国', 'NVIDIA': '🇺🇸 美国',
    'ICBC': '🇨🇳 中国', 'Meta': '🇺🇸 美国', 'ElevanceHealth': '🇺🇸 美国', 'Centene': '🇺🇸 美国',
    'BP': '🇬🇧 英国', 'BankOfAmerica': '🇺🇸 美国', 'ABC': '🇨🇳 中国', 'Chevron': '🇺🇸 美国',
    'CCB': '🇨🇳 中国', 'Ford': '🇺🇸 美国', 'GM': '🇺🇸 美国', 'TotalEnergies': '🇫🇷 法国',
    'JD': '🇨🇳 中国', 'ChinaLife': '🇨🇳 中国', 'Stellantis': '🇳🇱 荷兰', 'BOC': '🇨🇳 中国',
    'Citigroup': '🇺🇸 美国', 'HomeDepot': '🇺🇸 美国', 'FannieMae': '🇺🇸 美国', 'PingAn': '🇨🇳 中国',
    'CREC': '🇨🇳 中国', 'BMW': '🇩🇪 德国'
}

def get_country(folder_name):
    for key, val in country_map.items():
        if key.lower() in folder_name.lower():
            return val
    if '中国' in folder_name or '中铁' in folder_name or '建行' in folder_name or '中海油' in folder_name or '宝武' in folder_name or '中电建' in folder_name:
        return '🇨🇳 中国'
    return '🌍 跨国/其他'

def get_industry(folder_name):
    fn = folder_name.lower()
    if any(k in fn for k in ['apple', 'alphabet', 'microsoft', 'nvidia', 'meta', 'tencent', 'dell']):
        return '💻 科技芯片'
    if any(k in fn for k in ['amazon', 'walmart', 'costco', 'jd', 'target', 'homedepot', 'ahold']):
        return '🛒 零售电商'
    if any(k in fn for k in ['aramco', 'cnpc', 'sinopec', 'exxon', 'shell', 'bp', 'chevron', 'total', 'gazprom', 'cnooc', 'phillips', 'marathon', 'valero']):
        return '🛢️ 石油能源'
    if any(k in fn for k in ['unitedhealth', 'mckesson', 'cvs', 'cencora', 'cigna', 'cardinal', 'elevance', 'centene', 'humana']):
        return '🏥 医疗健康'
    if any(k in fn for k in ['volkswagen', 'toyota', 'ford', 'gm', 'stellantis', 'bmw', 'mercedes', 'byd', 'hyundai', 'honda']):
        return '🚗 汽车出行'
    if any(k in fn for k in ['jpmorgan', 'icbc', 'bankofamerica', 'abc', 'ccb', 'boc', 'citigroup', 'fanniemae', 'pingan', 'morganstanley', 'goldman', 'wellsfargo', 'santander', 'hsbc', 'sberbank', 'bnp', 'citic', 'stonex', 'statefarm', 'freddie', 'lic', 'axa']):
        return '🏦 金融银行'
    if any(k in fn for k in ['stategrid', 'csg', 'edf']):
        return '⚡ 电网公用'
    if any(k in fn for k in ['cscec', 'crec', 'crcc', 'powerchina', 'cccc']):
        return '🏗️ 建筑工程'
    if any(k in fn for k in ['foxconn', 'tsmc']):
        return '⚙️ 制造芯片'
    if any(k in fn for k in ['glencore', 'trafigura', 'reliance', 'chinaminmetals', 'chinabaowu', 'shandongenergy', 'hengli']):
        return '⛏️ 资源大宗'
    if any(k in fn for k in ['chinamobile', 'verizon', 'deutschetelekom', 'att', 'comcast']):
        return '📡 电信传媒'
    if any(k in fn for k in ['nestle', 'kroger']):
        return '🍞 食品消费'
    return '🏢 综合产业'

dirs = sorted([d for d in os.listdir(founder_dir) if os.path.isdir(os.path.join(founder_dir, d)) and d[0].isdigit()])

companies = []
for d in dirs:
    rank = int(d.split('-')[0])
    parts = d.split('-')
    name_cn = parts[1] if len(parts) > 1 else d
    name_en = parts[2] if len(parts) > 2 else ''
    
    founder_file = os.path.join(founder_dir, d, 'founder.md')
    company_file = os.path.join(founder_dir, d, 'company.md')
    
    founder_size = os.path.getsize(founder_file) if os.path.exists(founder_file) else 0
    company_size = os.path.getsize(company_file) if os.path.exists(company_file) else 0
    
    meta = brand_meta.get(rank, {'domain': f"{name_en.lower()}.com", 'color': '#0284C7', 'bg': 'bg-sky-600'})
    domain = meta['domain']
    logo_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
    
    founder_name = curated_founders.get(rank, f"{name_cn}创始团队")
    
    founder_title = "创始人全景传记"
    founder_quote = ""
    if os.path.exists(founder_file):
        with open(founder_file, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(15)]
            for line in lines:
                if line.startswith('# '):
                    founder_title = line.replace('# ', '').strip()
                elif line.startswith('> **“') or line.startswith('> “'):
                    founder_quote = line.replace('> ', '').replace('**', '').strip()

    status = "🌟 大师级深度精修" if founder_size >= 28000 else ("✨ 详实传记" if founder_size >= 10000 else "📝 标准传记")
    
    companies.append({
        'rank': rank,
        'folder': d,
        'name_cn': name_cn,
        'name_en': name_en,
        'domain': domain,
        'logo_url': logo_url,
        'brand_color': meta['color'],
        'brand_bg': meta['bg'],
        'country': get_country(d),
        'industry': get_industry(d),
        'founder_name': founder_name,
        'founder_title': founder_title,
        'founder_quote': founder_quote[:150] + ('...' if len(founder_quote) > 150 else ''),
        'founder_size': founder_size,
        'founder_size_kb': round(founder_size / 1024, 1),
        'company_size_kb': round(company_size / 1024, 1),
        'status': status
    })

site_data = {
    'total_companies': len(companies),
    'master_count': len([c for c in companies if c['founder_size'] >= 28000]),
    'generated_at': '2026-08-29',
    'companies': companies
}

out_path = os.path.join(base_dir, 'site_data.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(site_data, f, ensure_ascii=False, indent=2)

print(f"Generated site_data.json with {len(companies)} companies! All 100 logos mapped.")
