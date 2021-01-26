# import pandas as pd
# import openpyxl as xl
# from CBEE_212_Compounds_Enthalpy import *
#
#
# def new_comp(string):
#     string = Compound()
#     return string
#
#
# comp_list = []
#
# df_excel = pd.read_excel('Enthalpy_Data.xlsx', 'Sheet2')
#
# before = df_excel.dtypes
#
#
# df_excel['Component'] = df_excel['Component'].astype(str)
# df_excel['State'] = df_excel['State'].astype(str)
# df_excel['a'] = df_excel['a'].astype(str)
# df_excel['b'] = df_excel['b'].astype(str)
# df_excel['c'] = df_excel['c'].astype(str)
# df_excel['d'] = df_excel['d'].astype(str)
#
# print(df_excel.dtypes)
# print(df_excel)
# print(df_excel['Component'][0])
# print('hi ' + df_excel['Component'][0])
#
# print(df_excel.dtypes)
#
# # for iloc in df_excel.iloc:
# #     if iloc['a'] == '-----':
# #         iloc['a'] = '0'
# #     if iloc['b'] == '-----':
# #         iloc['b'] = '0'
# #     if iloc['c'] == '-----':
# #         iloc['c'] = '0'
# #     if iloc['d'] == '-----':
# #         iloc['d'] = '0'
#
# # print(df_excel)
# # print(new)
#
# # df_excel['a'] = df_excel['a'].astype(float)
# # df_excel['b'] = df_excel['b'].astype(float)
# # df_excel['c'] = df_excel['c'].astype(float)
# # df_excel['d'] = df_excel['d'].astype(float)
# # df_excel['T Unit'] = df_excel['T Unit'].astype(str)
# # df_excel['Low T'] = df_excel['Low T'].astype(float)
# # df_excel['High T'] = df_excel['High T'].astype(float)
#
#
# for iloc in df_excel.iloc:
#     pd_comp = new_comp(iloc['Component'].lower())
#     if iloc['State'] == 'liquid':
#         pd_comp.set_sub_factors(iloc['a'], iloc['b'], iloc['c'], iloc['d'])
#     if iloc['State'] == 'gas':
#         pd_comp.set_super_factors(iloc['a'], iloc['b'], iloc['c'], iloc['d'])
#     comp_list.append(pd_comp)
#
# after = df_excel.dtypes
# print(df_excel['d'])