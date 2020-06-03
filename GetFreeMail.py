# -*- coding: UTF-8 -*-

# author : Tom Eureka Newton
import xlrd
import xlwt

# fnm = input("Input the file's name:")
fnm = "fxxkcd.xls"
src = xlrd.open_workbook(fnm)
# inm = input("Input the Inference's name:")
inm = "infer.xls"
infr = xlrd.open_workbook(inm)

sht = src.sheet_by_name('Sheet1')
rsht = infr.sheet_by_name('Sheet1')

dst = xlwt.Workbook()
dsht = dst.add_sheet('passwd')
dsht1 = dst.add_sheet('ID')


dsht1.col(0).width = 256 * 8
dsht1.col(1).width = 256 * 20
dsht1.col(2).width = 256 * 40
dsht1.col(3).width = 256 * 10
dsht1.col(4).width = 256 * 35
dsht1.col(5).width = 256 *28

dsht.col(0).width = 256 * 8
dsht.col(1).width = 256 * 40
dsht.col(2).width = 256 * 10

dsht1.write(0, 0, "Name")
dsht1.write(0, 1, "Id")
dsht1.write(0, 2, "Mail")
dsht1.write(0, 3, "Passwd")
dsht1.write(0, 4, "StudentId")
dsht1.write(0, 5, "Class")

dsht.write(0, 0, "Name")
dsht.write(0, 1, "Mail")
dsht.write(0, 2, "Passwd")

for i in range(sht.nrows)[1:]:
	Id = sht.cell_value(i, 1)
	passwd = Id[-7:-1]
	Nm = sht.cell_value(i, 2)
	stdid = "NULL"
	for j in range(rsht.nrows)[1:]:
		if rsht.cell_value(j, 2) == Nm  and int(rsht.cell_value(j, 1)) == int(sht.cell_value(i, 10)) :
			stdid = rsht.cell_value(j, 0)
			if stdid % 1 == 0 :
				stdid = int(stdid)
			stdid = str(stdid)
			break


	if 'NULL' == stdid :
		mail = stdid
	else:
		mail= stdid+"@std.uestc.edu.cn"

	dsht1.write(i, 0, Nm)
	dsht1.write(i, 1, Id)
	dsht1.write(i, 2, mail)
	dsht1.write(i, 3, passwd)
	dsht1.write(i, 4, stdid)
	dsht1.write(i, 5, sht.cell_value(i, 10))

	dsht.write(i, 0, Nm)
	dsht.write(i, 1, mail)
	dsht.write(i, 2, passwd)

dst.save('onepiece.xls')