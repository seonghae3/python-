long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

list1 = []
rs = long_text.split('.')       # 以'.'分割字符串
for r in rs:
    list1.append(r.split('\n')) # 以换行符分割字符串

head = list1.pop(0)             # 弹出带有name和lei的列表
name = head[1]
lei = head[2]

tmp_dict = {}       # 临时储存title和isin的字典
sub_fund_list = []  # 'sub_fund'

for i in list1:
    i = i[0:-1]         # 去掉列表中无用项
    title = i.pop(0)    # 弹出列表第一个元素接收  作为title
    isin = i            # 其余列表项即为 isin
    tmp_dict = {'title': title, 'isin': isin}   # 临时储存在字典中
    sub_fund_list.append(tmp_dict)

final_dict = {
    'name': name,
    'lei': lei,
    'sub_fund': sub_fund_list
}
print(final_dict)