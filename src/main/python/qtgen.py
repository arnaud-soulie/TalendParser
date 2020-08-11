# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TalendDocGenerator(object):
    def setupUi(self, TalendDocGenerator):
        TalendDocGenerator.setObjectName("TalendDocGenerator")
        TalendDocGenerator.resize(541, 439)
        self.centralwidget = QtWidgets.QWidget(TalendDocGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 381))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.projectRootPath = QtWidgets.QTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectRootPath.sizePolicy().hasHeightForWidth())
        self.projectRootPath.setSizePolicy(sizePolicy)
        self.projectRootPath.setMinimumSize(QtCore.QSize(0, 0))
        self.projectRootPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.projectRootPath.setInputMethodHints(QtCore.Qt.ImhNone)
        self.projectRootPath.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.projectRootPath.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.projectRootPath.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.projectRootPath.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.projectRootPath.setAcceptRichText(False)
        self.projectRootPath.setPlaceholderText("")
        self.projectRootPath.setObjectName("projectRootPath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.projectRootPath)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.reportPath = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.reportPath.setMinimumSize(QtCore.QSize(0, 0))
        self.reportPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.reportPath.setInputMethodHints(QtCore.Qt.ImhNone)
        self.reportPath.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reportPath.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.reportPath.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.reportPath.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.reportPath.setAcceptRichText(False)
        self.reportPath.setPlaceholderText("")
        self.reportPath.setObjectName("reportPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reportPath)
        self.GenerateButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.GenerateButton.setMinimumSize(QtCore.QSize(0, 40))
        self.GenerateButton.setObjectName("GenerateButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.GenerateButton)
        self.logsBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget)
        self.logsBrowser.setObjectName("logsBrowser")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.logsBrowser)
        self.ReportButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.ReportButton.setMinimumSize(QtCore.QSize(0, 40))
        self.ReportButton.setObjectName("ReportButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.ReportButton)
        TalendDocGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TalendDocGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 22))
        self.menubar.setObjectName("menubar")
        TalendDocGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TalendDocGenerator)
        self.statusbar.setObjectName("statusbar")
        TalendDocGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(TalendDocGenerator)
        QtCore.QMetaObject.connectSlotsByName(TalendDocGenerator)

    def retranslateUi(self, TalendDocGenerator):
        _translate = QtCore.QCoreApplication.translate
        TalendDocGenerator.setWindowTitle(_translate("TalendDocGenerator", "Talend Doc Generator"))
        self.label.setText(_translate("TalendDocGenerator", "Talend project root path:"))
        self.projectRootPath.setHtml(_translate("TalendDocGenerator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("TalendDocGenerator", "Report Directory:"))
        self.reportPath.setHtml(_translate("TalendDocGenerator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">D:\\</p></body></html>"))
        self.GenerateButton.setText(_translate("TalendDocGenerator", "Generate"))
        self.ReportButton.setText(_translate("TalendDocGenerator", "Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TalendDocGenerator = QtWidgets.QMainWindow()
    ui = Ui_TalendDocGenerator()
    ui.setupUi(TalendDocGenerator)
    TalendDocGenerator.show()
    sys.exit(app.exec_())
