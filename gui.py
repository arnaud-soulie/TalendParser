import logging
import subprocess
from io import StringIO

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from reader.project_parser import ProjectParser
from writer.excel_writer import ExcelWriter

log_stream = StringIO()
log = logging.getLogger('ProjectParser')

class Screen(BoxLayout):
    line = StringProperty()
    last_report_path = ""

    def _update_logs(self, *args):
        self.line = log_stream.getvalue()

    def _generate(self, *args):
        self.ids['open_button'].disabled = True
        self.ids['generate_button'].disabled = True
        Clock.schedule_interval(self._update_logs, 0.5)
        try:
            parser = ProjectParser(args[0])
            parser.parse_jobs()
            e = ExcelWriter(self.ids['report_path'].text)
            for job in parser.job_data_list:
                if job is not None:
                    e.add_job(job)
                    e.row += 1
            e.workbook.close()
            self.last_report_path = e.dest
            self.ids['open_button'].disabled = False
        except Exception as ex:
            log.error(str(ex))
        self.ids['generate_button'].disabled = False

    def _open_report(self):
        print(self.last_report_path)
        subprocess.Popen([self.last_report_path], shell=True)

class MainApp(App):
    def build(self):
        return Screen()


def __configure_logs():
    fh = logging.FileHandler(filename='logs.log', mode='w')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s : %(asctime)s : %(message)s')
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    sh=logging.StreamHandler(stream=log_stream)
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    log.addHandler(fh)
    log.addHandler(ch)
    log.addHandler(sh)



if __name__ == '__main__':
    Config.set('graphics', 'width', '600')
    Config.set('graphics', 'height', '500')
    __configure_logs()
    MainApp().run()
