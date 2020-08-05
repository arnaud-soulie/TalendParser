""" Parse a Talend project to retrieve all the different job properties

    Raises:
        Exception: Talend root directory not found
        Exception: Talend process directory empty
"""

import glob
import os
import logging
import re
import xml.etree.ElementTree as ET

from reader.job import Job
# from job import Job


class ProjectParser:
    """ Talend project parser retrieves job properties and provide an output prop list
    """

    def __init__(self, _project_path):
        """ Parser init
        Args:
            _project_path (string): path to talend project root directory
        """
        self.logger = logging.getLogger(name='ProjectParser')
        self._project_path = _project_path
        self.job_data_list = []
        self.__check_project()

    def __check_project(self):
        """Check that the talend project contains a non-empty process director

        Raises:
            Exception: Talend root directory not found
            Exception: Talend process directory empty
        """
        self.process_dir = os.path.join(self._project_path, "process")
        if not os.path.exists(self.process_dir):
            self.logger.error("Directory %s does not exist", self.process_dir)
            raise Exception(f"Directory {self.process_dir} does not exist")
        if os.listdir(self.process_dir) == 0:
            self.logger.error("Directory %s is empty.", self.process_dir)
            raise Exception(f"Directory {self.process_dir} is empty")
        self.logger.info("Talend project check OK")

    def parse_jobs(self):
        """ Creates a list of talend jobs available in the project
        """
        job_list = glob.glob(os.path.join(self.process_dir, "**\\*.item"), recursive=True)
        for job in job_list:
            processed_job = self.__process_job_item(job)
            self.job_data_list.append(processed_job)

    def __process_job_item(self, item_path):
        """Process XML content and return Job objects

        Args:
            item_path (string): path to the XML file

        Returns:
            Job: Job object abstraction
        """
        tree = ET.parse(item_path)
        root = tree.getroot()
        try:
            desc = root.findall(".//node/[@componentName='tJava']/elementParameter/" \
                "[@field='MEMO_JAVA']")[0].attrib["value"]
        except (IndexError, KeyError):
            self.logger.warning("tJava/MEMO_JAVA/value not found in the XML tree for %s", item_path)
            return
        table_cible = self.__get_field_value_from_desc(desc, "context.journal_tb_cible")
        table_source = self.__get_field_value_from_desc(desc, "context.journal_tb_source")
        schema_source = self.__get_field_value_from_desc(desc, "context.journal_source")
        zone = self.__get_field_value_from_desc(desc, "context.journal_zone")
        return Job(item_path=item_path, table_cible=table_cible, table_source=table_source,
                   schema_source=schema_source, zone=zone, root_path=self._project_path)


    def __get_field_value_from_desc(self, desc, field):
        """Retrieve a value for a specific field within the MEMO_JAVA value string

        Args:
            desc (string): full MEMO_JAVA value string
            field (string): field to retrieve value for

        Returns:
            string: data value matching the field
        """
        data_list = desc.split("\n")
        for line in data_list:
            line_data = line.split("=")
            if (field == line_data[0].strip()) and (len(line_data) > 1):
                try:
                    value = re.search('"(.+?)"', line_data[1]).group(1)
                    return value
                except AttributeError:
                    self.logger.warning("No data found for field %s inside data %s", field, desc)
                    return ""



if __name__ == "__main__":
    parser = ProjectParser("D:\\Programmation\\Preci\\sari_lot1-v2.0")
    parser.parse_jobs()
    for j in parser.job_data_list:
        print(j)
