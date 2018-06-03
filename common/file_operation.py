import csv 
import xlrd

def get_data(file):
    infos = []
    with open(file,'r') as csvFile:
        csvInfos = csv.reader(csvFile,delimiter = ',')
        next(csvInfos)
        for info in csvInfos:
            infos.append(info)
        return infos

def get_data_xlsx(file):
    rows = []
    book = xlrd.open_workbook(file)
    logsheet = book.sheet_by_index(0)
    postsheet = book.sheet_by_index(1)
    # for row_idx in range(1,sheet.nrows):
    #     rows.append(list(sheet.row_values(row_idx,0)))
    # return rows
    
    # for row_idx in range(1,logsheet.nrows):
    #     val1 = logsheet.cell_value(row_idx,0)
    #     val2 = int(logsheet.cell_value(row_idx,1))
    #     tmp = (val1,str(val2))
    #     rows.append(list(tmp))
    # return rows
    for row_1,row_2 in zip(range(1,logsheet.nrows),range(1,postsheet.nrows)):
            logval1 = logsheet.cell_value(row_1,0)
            logval2 = int(logsheet.cell_value(row_1,1))
            postval1 = postsheet.cell_value(row_2,0)
            postval2 = postsheet.cell_value(row_2,1)
            tmp = (logval1,logval2,postval1,postval2)
            rows.append(list(tmp))
    return rows    
