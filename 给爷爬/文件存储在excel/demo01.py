import xlwt


# 创建workbook对象
workbook = xlwt.Workbook(encoding='utf-8') # 创建一个workbook对象
worksheet = workbook.add_sheet('sheet1') # 创建工作表
# worksheet.write(0,0,"hello world") # 写入数据，第一个参数表示行，第二个参数表示列，第三个参数表示内容
for i in range(9):
    for j in range(0,i+1):
       worksheet.write(i,j,"{} * {} = {}".format(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')
