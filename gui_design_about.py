# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_design_about.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_aboutForm(object):
    def setupUi(self, aboutForm):
        aboutForm.setObjectName(_fromUtf8("aboutForm"))
        aboutForm.setWindowModality(QtCore.Qt.WindowModal)
        aboutForm.resize(688, 592)
        self.gridLayout = QtGui.QGridLayout(aboutForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.aboutTextBrowser = QtGui.QTextBrowser(aboutForm)
        self.aboutTextBrowser.setObjectName(_fromUtf8("aboutTextBrowser"))
        self.gridLayout.addWidget(self.aboutTextBrowser, 0, 0, 1, 1)

        self.retranslateUi(aboutForm)
        QtCore.QMetaObject.connectSlotsByName(aboutForm)

    def retranslateUi(self, aboutForm):
        aboutForm.setWindowTitle(_translate("aboutForm", "About - Manga Downloader", None))
        self.aboutTextBrowser.setHtml(_translate("aboutForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Manga Downloader v1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Copyright (c) 2017 mackGH. All rights reserved.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Check some of my mini projects at </span><a href=\"https://github.com/mackGH\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://github.com/mackGH</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">1. Terms</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">By accessing this program, you are agreeing to be bound by these program\'s Terms and Conditions of Use, all applicable laws and regulations, and agree that you are responsible for compliance with any applicable local laws. If you do not agree with any of these terms, you are prohibited from using this program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">2. Use License</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">1. Permission is granted to use the Manga Downloader program for personal, non-commercial use only. This is the grant of a license, not a transfer of title, and under this license you may not:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">     • Sell or promote this software with the intention of profiting in any form.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">     • Remove any copyright or other notations from materials downloaded from mangareader.net. Mangareader.net reserves all the rights of the CONTENT(S) downloaded using this program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">2. This license shall automatically terminate if you violate any of these restrictions and may be terminated by the author at any time. Upon terminating your use of the program or upon the termination of this license, you must destroy any downloaded materials in your possession whether in electronic or printed format.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">3. You may copy and distribute verbatim copies of this software as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice and disclaimer of warranty; keep intact all the notices that refer to this License and to the absence of any warranty; and give any other recipients of the Program a copy of this License along with the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">3. Disclaimer</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">1. </span><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; color:#000000; background-color:#ffffff;\">NO WARRANTY.</span><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\"> Manga Downloader is provided &quot;as is&quot;. Because the program is licensed free of charge, the author makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties, including without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">4. Limitations</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'source_sans_proregular\'; font-size:10pt; color:#000000; background-color:#ffffff;\">1. In no event shall the Author be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption,) arising out of the use or inability to use the program even if authorized representative has been notified orally or in writing of the possibility of such damage. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'source_sans_proregular\'; font-size:10pt; font-weight:600; text-decoration: underline; color:#000000;\"><br /></p></body></html>", None))

