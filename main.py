from reader.project_parser import ProjectParser
from writer.excel_writer import ExcelWriter

parser = ProjectParser("D:\\Programmation\\Preci\\sari_lot1-v2.0")
parser.parse_jobs()
# for j in parser.job_data_list:
#     print(j)
e=ExcelWriter("D:\\")
for job in parser.job_data_list:
    if job != None:
        e.add_job(job)
        e.row+=1
e.workbook.close()