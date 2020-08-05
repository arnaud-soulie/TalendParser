import logging
from reader.project_parser import ProjectParser
from writer.excel_writer import ExcelWriter
log = logging.getLogger()
fh = logging.FileHandler(filename='logs.log', mode='w')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(name)s : %(message)s')
fh.setFormatter(formatter)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)
log.addHandler(fh)
log.addHandler(ch)

parser = ProjectParser("D:\\Programmation\\Preci\\sari_lot1-v2.0")
parser.parse_jobs()

e = ExcelWriter("D:\\")
for job in parser.job_data_list:
    if job is not None:
        e.add_job(job)
        e.row += 1
e.workbook.close()
