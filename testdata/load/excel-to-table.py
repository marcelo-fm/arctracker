import os
import xlrd
import openpyxl
import arcpy

def importallsheets(in_excel, out_gdb):
    if in_excel.endswith(".xlsx"):
        workbook = openpyxl.load_workbook(in_excel)
        sheets = workbook.sheetnames
    elif in_excel.endswith(".xls"):
        workbook = xlrd.open_workbook(in_excel)
        sheets = [sheet.name for sheet in workbook.sheets()]
    else:
        print("An Excel Workbook of format .xls or .xlsx is required.")
        return

    print('{} sheets found: {}'.format(len(sheets), ','.join(sheets)))
    for sheet in sheets:
        # The out_table is based on the input Excel file name
        # an underscore (_) separator followed by the sheet name
        out_table = os.path.join(
            out_gdb,
            arcpy.ValidateTableName(
                "{0}_{1}".format(os.path.basename(in_excel), sheet),
                out_gdb))

        print('Converting {} to {}'.format(sheet, out_table))

        # Perform the conversion
        arcpy.conversion.ExcelToTable(in_excel, out_table, sheet)

if __name__ == '__main__':
    importallsheets('c:/data/data.xls',
                    'c:/data/outgdb.gdb')