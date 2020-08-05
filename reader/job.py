""" Talend job abstraction
"""
import os

class Job:
    """ Talend single job abstraction
    Provides methods to read items files to retrieve job properties
    """

    def __init__(self, *, item_path, table_cible, table_source, schema_source,
                 zone, root_path):
        self.item_path = item_path
        self.table_cible = table_cible
        self.table_source = table_source
        self.schema_source = schema_source
        self.root_path = root_path
        self.tree = self.__get_tree_from_path()
        self.job_name = self.get_name_from_path()
        self.zone = zone

    def get_name_from_path(self):
        """Get the job name from job filepath

        Returns:
            string: job name
        """
        assert self.item_path != ""
        #Removes the _0 at the end of each filename
        return os.path.basename(self.item_path).split('.')[0][:-2]

    def __get_tree_from_path(self):
        assert self.item_path != ""
        rel_path = os.path.relpath(self.item_path, start=os.path.join(self.root_path, "process"))
        return os.path.dirname(rel_path)


    def __str__(self):
        return f"Job: {self.job_name}, TB_Cible: {self.table_cible}, "\
            f"TB_Source: {self.table_source}, Schema: {self.schema_source}, "\
                f"Zone: {self.zone}, Tree: {self.tree}"
