import xlrd  
import xlwt  
from datetime import date,datetime  
  

data = xlrd.open_workbook(r'Correlation.xlsx')
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('Sheet1')

table = data.sheets()[0]

nrows = table.nrows #行数
ncols = table.ncols #列数
print(nrows,ncols)


for j in range(1,270):
    sum=0
    for i in range(19*(j-1)+1,19*j+1):
        rowValues= table.row_values(i) 
        sum=sum+(rowValues[4]**1.112)/(rowValues[3]**0.888)

    for i in range(19*(j-1)+1,19*j+1):
        n=i-19*(j-1)
        p=0
        rowValues= table.row_values(i) 
        p=((rowValues[4]**1.112)/(rowValues[3]**0.888))/sum
        worksheet.write(19*(j-1)+n, 1, p)
        workbook.save('Huff(主观-归).xls')
        print(p)

