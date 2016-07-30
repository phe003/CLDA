# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:16:13 2016

@author: Ben He
"""

import numpy as np
import pandas as pd
import re
import string

"""
保单 - 营销员或业务员识别号匹配
"""
agentSalesmanNum_table_Policy = table_Policy["销售员工号"]
# 转化成字符型
agentNum1_table_Agent = list(map(str, table_Agent["营销员号"]))
agentNum2_table_Agent = list(map(str, table_Agent["工号"]))
salesmanNum_table_Salesman = table_Salesman["业务员工号"]
# 1. 保单表与营销员表识别号匹配数目查验 - 销售员工号 v.s. 营销员号
count_table_PolicyandAgent1 = 0
# 保单表有682个销售人员
for i in list(set(list(agentSalesmanNum_table_Policy))):
    # 营销员表有838个人, 营销员号是主键
    for j in list(set(agentNum1_table_Agent)):
        # 先对保单表里面的销售员工号做字符串处理, 去掉横杠和空格
        i = i.replace('-', '')
        i = i.replace(' ', '')
        if i == j:
            count_table_PolicyandAgent1 += 1
        else:
            pass
# 结论: 销售员工号 v.s. 营销员号有91个匹配

# 2. 保单表与营销员表识别号匹配数目查验 - 销售员工号 v.s. 工号
count_table_PolicyandAgent2 = 0
# 保单表有682个销售人员
for i in list(set(list(agentSalesmanNum_table_Policy))):
    # 营销员表有838个人, 工号也是主键
    # 工号前面的0都去除掉
    for j in list(set(agentNum2_table_Agent)):
        # 先对保单表里面的销售员工号做字符串处理, 去掉横杠和空格
        i = i.replace('-', '')
        i = i.replace(' ', '')
        if i == j:
            count_table_PolicyandAgent2 += 1
        else:
            pass
# 结论: 销售员工号 v.s. 工号有286个匹配

# 3. 保单表与业务员表识别号匹配数目查验 - 销售员工号 v.s. 业务员工号
count_table_PolicyandSalesman = 0
# 保单表有682个销售人员
for i in list(set(list(agentSalesmanNum_table_Policy))):
    # 业务员表有657个人, 业务员工号是主键
    # 把一些乱码例如"\r\n"去掉
    for j in list(set(salesmanNum_table_Salesman)):
        i = i.replace('-', '')
        i = i.replace(' ', '')
        j = j.replace('\r\n','')
        if i == j:    
            count_table_PolicyandSalesman += 1
        else:
            pass
# 结论: 销售员工号 v.s. 业务员工号有37个匹配


"""
保单 - 客户识别号匹配
"""
applicantNum_table_Policy = list(map(str, table_Policy["投保人客户号"]))
recognizeeNum_table_Policy = list(map(str, table_Policy["被保人客户号"]))
clientNum_table_IndividualClient_combine_uniq = list(map(str, table_IndividualClient_combine_uniq["客户号"]))
# 1. 保单表与个人客户表识别号匹配数目查验 - 投保人客户号 v.s. 客户号
count_table_PolicyandClient1 = 0
# 保单表有9299个客户 - 投保人客户号
for i in list(set(list(applicantNum_table_Policy))):
    # 个人客户表的客户号不是主键, 一共有20502个不重复的客户号
    if i in list(set(clientNum_table_IndividualClient_combine_uniq)):    
        count_table_PolicyandClient1 += 1
    else:
        pass    
# 结论: 投保人客户号 v.s. 客户号有9046个匹配
# 2. 保单表与个人客户表识别号匹配数目查验 - 被保人客户号 v.s. 客户号
count_table_PolicyandClient2 = 0
# 保单表有10700个客户 - 被保人客户号
for i in list(set(list(recognizeeNum_table_Policy))):
    # 个人客户表的客户号不是主键, 一共有20502个不重复的客户号
    if i in list(set(clientNum_table_IndividualClient_combine_uniq)):    
        count_table_PolicyandClient2 += 1
    else:
        pass 
# 结论: 被保人客户号 v.s. 客户号有10463个匹配


"""
保单 - 保全/实收付流水识别号匹配
"""
policyNum_table_Policy = table_Policy["保单号"]
# 实收付流水
policyNum_table_CashJournal_combine_uniq = list(map(str, table_CashJournal_combine_uniq["保单号"]))
# 保全流水
policyNum_table_PolicyMaintenance_combine_uniq = list(map(str, table_PolicyMaintenance_combine_uniq["合同号"]))
# 1. 保单表与实收付流水表识别号匹配数目查验 - 保单号 v.s. 保单号
count_table_PolicyandCashJournal = 0
# 保单表有18234份保单 - 保单号, 保单号是主键
for i in list(set(list(policyNum_table_Policy))):
    # 实收付流水表有26909份保单 - 保单号
    for j in list(set(policyNum_table_CashJournal_combine_uniq)):
        j = j.replace(' ','')
        if i == j:
            count_table_PolicyandCashJournal += 1
        else:
            pass
# 结论: 保单表与实收付流水表通过保单号有12033个匹配
# 2. 保单表与保全流水表识别号匹配数目查验 - 保单号 v.s. 合同号
count_table_PolicyandMaintenance = 0
# 保单表有18234份保单 - 保单号, 保单号是主键
for i in list(set(list(policyNum_table_Policy))):
    # 保全流水表有7891份保单 - 合同号
    for j in list(set(policyNum_table_PolicyMaintenance_combine_uniq)):
        if i == j:
            count_table_PolicyandMaintenance += 1
        else:
            pass
# 结论: 保单表与保全流水表通过保单号-合同号有7814个匹配