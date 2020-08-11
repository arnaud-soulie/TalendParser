# Talend Doc Generator

This programs takes a Talend project as input and generates some excel documentation based on some specific predefined in-code comments.

## Tree

Here are the main interesting files: 

```
|   .gitignore
|   README.md
|   requirements.txt               --> pip requirements
|   
+---.github
|   \---workflows
|           python-app.yml         --> Github CI configuration
|           
+---.vscode
\---src
    |       
    \---main
        +---icons
        |       
        \---python
            |   gui.ui             --> QT5 UI file
            |   main.py            --> main python file
            |   qtgen.py           --> generated QT GUI
            |   
            +---reader             --> Talend project parser
            |   |   job.py
            |   |   project_parser.py
            |   |   __init__.py
            |   | 
            +---writer             --> Excel report writer
            |   |   excel_writer.py
            |   |   __init__.py


 ```

## Automatic package generation

Each commit or pull-request triggers a new build. If successful, new Artifacts are created linked to the build page here: [https://github.com/arnaud-soulie/TalendParser/actions](https://github.com/arnaud-soulie/TalendParser/actions).

The zip Artifact contains a stand-alone TalendParser.exe file.

## How to use as a simple script

You can use the reader and writer classes inside a simple script without any GUI, for example:
``` python
from reader.project_parser import ProjectParser
from writer.excel_writer import ExcelWriter

parser = ProjectParser("D:\\mytalendproject")
parser.parse_jobs()

e=ExcelWriter("D:\\")
for job in parser.job_data_list:
    if job != None:
        e.add_job(job)
        e.row+=1
e.workbook.close()
```

## Development environment setup

### Basic setup

- Create a ew virtual environment and activate it:
``` bash 
python -m venv venv
venv\Scripts\activate
```
- Install the minimum dependencies
``` bash
pip install -r requirements.txt
```
- You should be able to launch the program with:
``` bash
python src\main\python\main.py
```

### Update the GUI

The UI has been created using QT5. You can use QTDesigner to modify the gui.ui file:
- Install QTDesigner
``` bash
pip install PyQt5Designer
```
- Run the designer and open the gui.ui file
``` bash
designer %cd%\src\main\python\gui.ui
```
- When you are done the modification, regenerate the pygen.py file:
``` bash
cd src\main\python & pyuic5 -x gui.ui -o qtgen.py
```
- You should have a fresh new qtgen.py file
- Patch the generated files to handle logs display inside the QTextEditor:
    - Add an import at the begining: 
    ```
    from texteditlogger import QTextEditLogger
    ```
    - Change the logbrowser declaration by:
    ```
    self.logsBrowser = QTextEditLogger(self.centralwidget)
    ```




