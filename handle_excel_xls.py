
# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
 
 
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

def write_excel_xls_append(path, value):
    index = len(value)
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old,j,value[i][j])
    new_workbook.save(path)
    print("xls格式表格【追加】写入数据成功")

def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_names()
    worksheet =  workbook.sheet_by_name(sheet[0])
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i,j), "\t", end="")
        print() 

 

 
 

 
 
book_name_xls = 'xls格式测试工作簿.xls'
 
sheet_name_xls = 'xls格式测试表'
 
value_title = [["姓名", "性别", "年龄", "城市", "职业"],]
 

value1 = [["张三", "男", "19", "杭州", "研发工程师"],
          ["李四", "男", "22", "北京", "医生"],
          ["王五", "女", "33", "珠海", "出租车司机"],]
 

 
 
#write_excel_xls(book_name_xls, sheet_name_xls, value_title)

write_excel_xls_append(book_name_xls, value1)
read_excel_xls(book_name_xls)