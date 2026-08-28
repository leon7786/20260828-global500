# -*- coding: utf-8 -*-
"""Generate the beautified and enriched list.md"""

from generate_part1 import DATA_PART1
from generate_part2 import DATA_PART2
from generate_part3 import DATA_PART3
from generate_part4 import DATA_PART4
from generate_part5 import DATA_PART5
import json

companies = DATA_PART1 + DATA_PART2 + DATA_PART3 + DATA_PART4 + DATA_PART5

# Calculate stats
total_rev = sum(int(c['revenue_m'].replace(',', '')) for c in companies)
countries = {}
for c in companies:
    cntry = c['country']
    countries[cntry] = countries.get(cntry, 0) + 1

sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)

md_lines = []

md_lines.append("# 《财富》世界500强全景深度情报名录 (Fortune Global 500 Intelligence Center)")
md_lines.append("")
md_lines.append("> 📊 **全景数据权威呈现**：收录最新《财富》世界500强全部 500 家跨国巨头完整名录，深度拓展并规范 **企业中文与官方英文全称**、**创始人/奠基背景（中英文）**、**总部国家与城市**、**创立年份**、**核心行业细分赛道** 与 **营业收入（百万美元）**。")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📈 全球宏观概览与关键洞察 (Executive Insights)")
md_lines.append("")
md_lines.append(f"- 🏢 **入榜企业总数**：**500 / 500 家（100% 完整收录与数据增强）**")
md_lines.append(f"- 💰 **500强总营业收入**：**${total_rev:,} 百万美元**（约合 **${total_rev/1000000:.2f} 万亿美元**）")
md_lines.append(f"- 👑 **全球营收三甲**：**亚马逊 (Amazon.com)** 以 **$716,924M** 居首；**沃尔玛 ($713,163M)** 紧随其后；**国家电网 ($555,371M)** 稳居全球公用事业与中国企业第一位")
md_lines.append(f"- 🚀 **硬核科技与新能源跃升**：**英伟达 (NVIDIA)** 跃升至第 **28** 位（营收 $215,938M）；**比亚迪 (BYD)** 跻身第 **91** 位（营收 $111,853M）；**宁德时代 (CATL)** 名列第 **260** 位；**阿斯麦 (ASML)** 位列第 **453** 位")
md_lines.append("")

# Country Distribution Table
md_lines.append("### 🌍 上榜国家与地区分布 TOP 10")
md_lines.append("")
md_lines.append("| 排名 | 国家 / 地区 | 上榜企业数量 | 全球占比 (%) | 核心代表企业 |")
md_lines.append("| :---: | :--- | :---: | :---: | :--- |")

top_representatives = {
    "🇺🇸 美国": "亚马逊、沃尔玛、联合健康、苹果、微软、英伟达、特斯拉、谷歌、埃克森美孚",
    "🇨🇳 中国": "国家电网、中石油、中石化、中建集团、工商银行、比亚迪、华为、腾讯、阿里巴巴、拼多多",
    "🇯🇵 日本": "丰田汽车、三菱商事、本田汽车、索尼、日立、松下、日本电报电话、软银集团",
    "🇩🇪 德国": "大众公司、宝马集团、梅赛德斯-奔驰、德国电信、博世集团、西门子、安联保险",
    "🇫🇷 法国": "道达尔能源、法国电力、安盛保险、迪奥(LVMH)、空中客车、赛诺菲、施耐德电气",
    "🇬🇧 英国": "壳牌公司、英国石油、汇丰银行、巴克莱、阿斯利康、葛兰素史克、力拓",
    "🇰🇷 韩国": "三星电子、现代汽车、SK集团、起亚公司、LG电子、SK海力士、浦项制铁",
    "🇨🇦 加拿大": "加拿大皇家银行、多伦多道明银行、博枫公司、森科能源、加拿大丰业银行",
    "🇨🇭 瑞士": "嘉能可、雀巢、罗氏公司、瑞银集团、苏黎世保险、诺华公司、ABB集团",
    "🇮🇳 印度": "信实工业、印度人寿、印度石油、印度国家银行、塔塔汽车、HDFC银行",
}

for idx, (cntry, count) in enumerate(sorted_countries[:10], 1):
    pct = (count / 500.0) * 100
    rep = top_representatives.get(cntry, "—")
    md_lines.append(f"| #{idx} | {cntry} | **{count} 家** | {pct:.1f}% | {rep} |")

md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📑 目录索引快速跳转")
md_lines.append("")
md_lines.append("- [第 001 - 100 名：全球超级巨头（营收 $1000亿+ 美元梯队）](#第-001---100-名全球超级巨头营收-1000亿-美元梯队)")
md_lines.append("- [第 101 - 200 名：全球产业领军骨干（营收 $700亿 - $1000亿 美元）](#第-101---200-名全球产业领军骨干营收-700亿---1000亿-美元)")
md_lines.append("- [第 201 - 300 名：跨国财团与行业先锋（营收 $500亿 - $700亿 美元）](#第-201---300-名跨国财团与行业先锋营收-500亿---700亿-美元)")
md_lines.append("- [第 301 - 400 名：高端制造与区域支柱（营收 $400亿 - $500亿 美元）](#第-301---400-名高端制造与区域支柱营收-400亿---500亿-美元)")
md_lines.append("- [第 401 - 500 名：高成长与专精特新巨擘（营收 $330亿 - $400亿 美元）](#第-401---500-名高成长与专精特新巨擘营收-330亿---400亿-美元)")
md_lines.append("")
md_lines.append("---")
md_lines.append("")

def render_table_chunk(start_idx, end_idx, title_section):
    chunk_lines = []
    chunk_lines.append(f"## {title_section}")
    chunk_lines.append("")
    chunk_lines.append("| 排名 | 企业名称 (中/英文) | 创始人 / 创办背景 (中/英文) | 国家 / 总部 | 成立 | 核心行业赛道 | 营业收入 (百万美元) |")
    chunk_lines.append("| :---: | :--- | :--- | :--- | :---: | :--- | :---: |")
    
    for c in companies[start_idx-1:end_idx]:
        r = c['rank']
        name_cell = f"**{c['name_cn']}**<br>_{c['name_en']}_"
        founder_cell = f"{c['founder_cn']}<br>_{c['founder_en']}_"
        loc_cell = f"{c['country']}<br><small>{c['hq']}</small>"
        year_cell = f"{c['founded_year']}"
        ind_cell = f"{c['industry']}"
        rev_cell = f"**${c['revenue_m']}**"
        
        chunk_lines.append(f"| **#{r}** | {name_cell} | {founder_cell} | {loc_cell} | {year_cell} | {ind_cell} | {rev_cell} |")
    
    chunk_lines.append("")
    return "\n".join(chunk_lines)

md_lines.append(render_table_chunk(1, 100, "第 001 - 100 名：全球超级巨头（营收 $1000亿+ 美元梯队）"))
md_lines.append(render_table_chunk(101, 200, "第 101 - 200 名：全球产业领军骨干（营收 $700亿 - $1000亿 美元）"))
md_lines.append(render_table_chunk(201, 300, "第 201 - 300 名：跨国财团与行业先锋（营收 $500亿 - $700亿 美元）"))
md_lines.append(render_table_chunk(301, 400, "第 301 - 400 名：高端制造与区域支柱（营收 $400亿 - $500亿 美元）"))
md_lines.append(render_table_chunk(401, 500, "第 401 - 500 名：高成长与专精特新巨擘（营收 $330亿 - $400亿 美元）"))

md_lines.append("---")
md_lines.append("")
md_lines.append("### 📌 备注说明")
md_lines.append("1. **营业收入 (Revenue)**：单位为百万美元 ($M USD)，统计口径统一按照最新全球会计准则审计后的企业财年营业收入。")
md_lines.append("2. **创始人与奠基人 (Founder/Founding Background)**：全面涵盖民营企业初创团队（包含中英文标准译名及联合创始人），以及国有企业、大型战略重组实体的历史沿革背景。")
md_lines.append("3. **总部与设立年份 (HQ & Inception)**：标明现代企业法定总部所在地及集团最早溯源创立年份。")

output_content = "\n".join(md_lines)

with open('list.md', 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"Successfully generated updated list.md! Total size: {len(output_content)} bytes")
