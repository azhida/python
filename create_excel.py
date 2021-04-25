import openpyxl
wb = openpyxl.Workbook()
#利用openpyxl.Workbook()函数创建新的workbook（工作薄）对象，就是创建新的空的Excel文件。
sheet = wb.active
sheet.title = 'test file'
sheet['A1'] = '漫威宇宙12111'
rows = [['美国队长','钢铁侠','冷霜凝'],['是','漫威','宇宙', '经典','人物']]
#先把要写入的多行内容写成列表，再放进大列表里，赋值给rows。
for i in rows:
    sheet.append(i)
#遍历rows，同时把遍历的内容添加到表格里，这样就实现了多行写入。
print(rows)
#保存到指定的路径
wb.save("test.xlsx")
print('ok')
