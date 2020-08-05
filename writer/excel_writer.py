"""Write job objects inside an excel file

Raises:
    Exception: destination directory not existing
"""


import logging
import os
import time

import xlsxwriter


class ExcelWriter:
    """Creates a new excel file to store jobs information

    Raises:
        Exception: destination directory not existing
    """

    logger = logging.getLogger("ProjectParser")

    def __init__(self, path):
        filename = time.strftime("%Y%m%d-%H%M%S")+"-report.xlsx"
        self.dest = os.path.join(path, filename)
        if not os.path.isdir(os.path.dirname(self.dest)):
            raise Exception(f"{os.path.dirname(self.dest)} directory does not exist")
        self.workbook = xlsxwriter.Workbook(self.dest)
        self.worksheet = self.workbook.add_worksheet()
        self.__init_headers()
        self.row = 1

    def __init_headers(self):
        cell_format = self.workbook.add_format()
        cell_format.set_bold()
        self.worksheet.write('A1', 'Type table', cell_format)
        self.worksheet.write('B1', 'Table', cell_format)
        self.worksheet.write('C1', 'Description', cell_format)
        self.worksheet.write('D1', 'Système et Schéma source', cell_format)
        self.worksheet.write('E1', 'Table source', cell_format)
        self.worksheet.write('F1', 'Périodicité d\'alimentation', cell_format)
        self.worksheet.write('G1', 'Type d\'alimentation', cell_format)
        self.worksheet.write('H1', 'Arborescence Talend', cell_format)
        self.worksheet.write('I1', 'Job Talend', cell_format)
        self.worksheet.write('J1', 'Zone', cell_format)

    def add_job(self, job):
        """Add the job fields inside the worksheet

        Args:
            job (Job): Talend Job object
        """
        self.worksheet.write(self.row, 1, job.table_cible)
        self.worksheet.write(self.row, 3, job.schema_source)
        self.worksheet.write(self.row, 4, job.table_source)
        self.worksheet.write(self.row, 7, job.tree)
        self.worksheet.write(self.row, 8, job.job_name)
        self.worksheet.write(self.row, 9, job.zone)

if __name__ == '__main__':
    e = ExcelWriter("D:\\")
    e.workbook.close()
