from qtgen import *
import sys

import logging
import subprocess
import threading
from io import StringIO

from reader.project_parser import ProjectParser
from writer.excel_writer import ExcelWriter
from fbs_runtime.application_context.PyQt5 import ApplicationContext


project_path = ""
log_stream = StringIO()
log = logging.getLogger('ProjectParser')
last_report_path = ""

def _generate():
    ui.GenerateButton.setEnabled(False)
    ui.ReportButton.setEnabled(False)
    threading.Thread(target=__thread).start()


def _open_report(self):
    """Open the excel report
    """
    global last_report_path
    subprocess.Popen([last_report_path], shell=True)

def __thread():
        try:
            global last_report_path
            parser = ProjectParser(ui.projectRootPath.toPlainText())
            parser.parse_jobs()
            e = ExcelWriter(ui.reportPath.toPlainText())
            for job in parser.job_data_list:
                if job is not None:
                    e.add_job(job)
                    e.row += 1
            e.workbook.close()
            last_report_path = e.dest
            ui.ReportButton.setEnabled(True)
        except Exception as ex:
            log.error(str(ex))
        ui.GenerateButton.setEnabled(True)
        print("finish")

def __configure_logs():
    fh = logging.FileHandler(filename='logs.log', mode='w')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    sh = logging.StreamHandler(stream=log_stream)
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    log.addHandler(fh)
    log.addHandler(ch)
    log.addHandler(sh)

__configure_logs()
#app = QtWidgets.QApplication(sys.argv)
appctxt = ApplicationContext()
MainWindow = QtWidgets.QMainWindow()
ui = Ui_TalendDocGenerator()
ui.setupUi(MainWindow)
ui.GenerateButton.clicked.connect(_generate)
ui.ReportButton.clicked.connect(_open_report)
MainWindow.show()
sys.exit(appctxt.app.exec_())
