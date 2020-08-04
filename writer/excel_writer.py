import xlsxwriter
import os

class ExcelWriter:
    
    def __init__(self, path):
        self.workbook = xlsxwriter.Workbook(os.path.join(path,'results.xlsx'))
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.write('A1', 'Type table')
        self.worksheet.write('B1', 'Table')
        self.worksheet.write('C1', 'Description')
        self.worksheet.write('D1', 'Système et Schéma source')
        self.worksheet.write('E1', 'Table source')
        self.worksheet.write('F1', 'Périodicité d\'alimentation')
        self.worksheet.write('G1', 'Type d\'alimentation')
        self.worksheet.write('H1', 'Arborescence Talend')
        self.worksheet.write('I1', 'Job Talend')
        self.worksheet.write('J1', 'Zone')
        self.row = 1

    def add_job(self, job):
        self.worksheet.write(self.row, 1, job.table_cible)
        self.worksheet.write(self.row, 3, job.schema_source)
        self.worksheet.write(self.row, 4, job.table_source)
        self.worksheet.write(self.row, 7, job.tree)
        self.worksheet.write(self.row, 8, job.job_name)
        self.worksheet.write(self.row, 9, job.zone)

if __name__ == '__main__':
    e=ExcelWriter("D:\\")
    e.workbook.close()