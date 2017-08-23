# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
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

class Ui_SmartMT_MainWindow(object):
    def setupUi(self, SmartMT_MainWindow):
        SmartMT_MainWindow.setObjectName(_fromUtf8("SmartMT_MainWindow"))
        SmartMT_MainWindow.resize(1024, 768)
        SmartMT_MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Application-x-pcb.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SmartMT_MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(SmartMT_MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setViewMode(QtGui.QMdiArea.SubWindowView)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.horizontalLayout.addWidget(self.mdiArea)
        SmartMT_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SmartMT_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartMT_MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(SmartMT_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        SmartMT_MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(SmartMT_MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        SmartMT_MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Project = QtGui.QAction(SmartMT_MainWindow)
        self.actionNew_Project.setObjectName(_fromUtf8("actionNew_Project"))
        self.actionOpen_Project = QtGui.QAction(SmartMT_MainWindow)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionClose_Project = QtGui.QAction(SmartMT_MainWindow)
        self.actionClose_Project.setEnabled(False)
        self.actionClose_Project.setObjectName(_fromUtf8("actionClose_Project"))
        self.actionOpen_edi_File = QtGui.QAction(SmartMT_MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Text-x-generic_with_pencil.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_edi_File.setIcon(icon1)
        self.actionOpen_edi_File.setObjectName(_fromUtf8("actionOpen_edi_File"))
        self.actionOpen_edi_Folder = QtGui.QAction(SmartMT_MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Document-open.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_edi_Folder.setIcon(icon2)
        self.actionOpen_edi_Folder.setObjectName(_fromUtf8("actionOpen_edi_Folder"))
        self.actionSave_as_Project = QtGui.QAction(SmartMT_MainWindow)
        self.actionSave_as_Project.setEnabled(False)
        self.actionSave_as_Project.setObjectName(_fromUtf8("actionSave_as_Project"))
        self.actionSave_Project = QtGui.QAction(SmartMT_MainWindow)
        self.actionSave_Project.setEnabled(False)
        self.actionSave_Project.setObjectName(_fromUtf8("actionSave_Project"))
        self.actionExit = QtGui.QAction(SmartMT_MainWindow)
        self.actionExit.setStatusTip(_fromUtf8(""))
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExport = QtGui.QAction(SmartMT_MainWindow)
        self.actionExport.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Image-x-generic.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon3)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionShow_Data_Collection = QtGui.QAction(SmartMT_MainWindow)
        self.actionShow_Data_Collection.setCheckable(True)
        self.actionShow_Data_Collection.setChecked(True)
        self.actionShow_Data_Collection.setEnabled(False)
        self.actionShow_Data_Collection.setObjectName(_fromUtf8("actionShow_Data_Collection"))
        self.actionFind_Action = QtGui.QAction(SmartMT_MainWindow)
        self.actionFind_Action.setObjectName(_fromUtf8("actionFind_Action"))
        self.actionHelp = QtGui.QAction(SmartMT_MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(SmartMT_MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOptions = QtGui.QAction(SmartMT_MainWindow)
        self.actionOptions.setMenuRole(QtGui.QAction.PreferencesRole)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionPlot = QtGui.QAction(SmartMT_MainWindow)
        self.actionPlot.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Icon_Mathematical_Plot.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot.setIcon(icon4)
        self.actionPlot.setObjectName(_fromUtf8("actionPlot"))
        self.actionShow_Station_Summary = QtGui.QAction(SmartMT_MainWindow)
        self.actionShow_Station_Summary.setCheckable(True)
        self.actionShow_Station_Summary.setChecked(True)
        self.actionShow_Station_Summary.setEnabled(False)
        self.actionShow_Station_Summary.setObjectName(_fromUtf8("actionShow_Station_Summary"))
        self.actionCascade_Windows = QtGui.QAction(SmartMT_MainWindow)
        self.actionCascade_Windows.setObjectName(_fromUtf8("actionCascade_Windows"))
        self.actionTile_Windows = QtGui.QAction(SmartMT_MainWindow)
        self.actionTile_Windows.setObjectName(_fromUtf8("actionTile_Windows"))
        self.actionWindowed_View = QtGui.QAction(SmartMT_MainWindow)
        self.actionWindowed_View.setCheckable(True)
        self.actionWindowed_View.setChecked(True)
        self.actionWindowed_View.setEnabled(False)
        self.actionWindowed_View.setObjectName(_fromUtf8("actionWindowed_View"))
        self.actionTabbed_View = QtGui.QAction(SmartMT_MainWindow)
        self.actionTabbed_View.setCheckable(True)
        self.actionTabbed_View.setObjectName(_fromUtf8("actionTabbed_View"))
        self.actionClose_All_Images = QtGui.QAction(SmartMT_MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Edit-clear.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_All_Images.setIcon(icon5)
        self.actionClose_All_Images.setObjectName(_fromUtf8("actionClose_All_Images"))
        self.actionExport_ModEM_Data = QtGui.QAction(SmartMT_MainWindow)
        self.actionExport_ModEM_Data.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Tango/resources/icons/Tango/Package-x-generic.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_ModEM_Data.setIcon(icon6)
        self.actionExport_ModEM_Data.setObjectName(_fromUtf8("actionExport_ModEM_Data"))
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionClose_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_edi_File)
        self.menuFile.addAction(self.actionOpen_edi_Folder)
        self.menuFile.addAction(self.actionSave_as_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExport_ModEM_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionShow_Data_Collection)
        self.menuView.addAction(self.actionShow_Station_Summary)
        self.menuWindow.addAction(self.actionWindowed_View)
        self.menuWindow.addAction(self.actionTabbed_View)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionTile_Windows)
        self.menuWindow.addAction(self.actionCascade_Windows)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionClose_All_Images)
        self.menuWindow.addSeparator()
        self.menuHelp.addAction(self.actionFind_Action)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionPlot)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionOptions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen_edi_File)
        self.toolBar.addAction(self.actionOpen_edi_Folder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlot)
        self.toolBar.addAction(self.actionClose_All_Images)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addAction(self.actionExport_ModEM_Data)

        self.retranslateUi(SmartMT_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(SmartMT_MainWindow)

    def retranslateUi(self, SmartMT_MainWindow):
        SmartMT_MainWindow.setWindowTitle(_translate("SmartMT_MainWindow", "SmartMT", None))
        self.menuFile.setTitle(_translate("SmartMT_MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("SmartMT_MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("SmartMT_MainWindow", "View", None))
        self.menuWindow.setTitle(_translate("SmartMT_MainWindow", "Window", None))
        self.menuHelp.setTitle(_translate("SmartMT_MainWindow", "Help", None))
        self.menuTools.setTitle(_translate("SmartMT_MainWindow", "Tools", None))
        self.toolBar.setWindowTitle(_translate("SmartMT_MainWindow", "toolBar", None))
        self.actionNew_Project.setText(_translate("SmartMT_MainWindow", "New Project...", None))
        self.actionNew_Project.setShortcut(_translate("SmartMT_MainWindow", "Alt+N", None))
        self.actionOpen_Project.setText(_translate("SmartMT_MainWindow", "Open Project...", None))
        self.actionClose_Project.setText(_translate("SmartMT_MainWindow", "Close Project", None))
        self.actionOpen_edi_File.setText(_translate("SmartMT_MainWindow", "Open .edi File...", None))
        self.actionOpen_edi_Folder.setText(_translate("SmartMT_MainWindow", "Open .edi Folder...", None))
        self.actionSave_as_Project.setText(_translate("SmartMT_MainWindow", "Save as Project...", None))
        self.actionSave_Project.setText(_translate("SmartMT_MainWindow", "Save Project...", None))
        self.actionExit.setText(_translate("SmartMT_MainWindow", "Exit", None))
        self.actionExport.setText(_translate("SmartMT_MainWindow", "Export Image...", None))
        self.actionShow_Data_Collection.setText(_translate("SmartMT_MainWindow", "Show Data Collection", None))
        self.actionFind_Action.setText(_translate("SmartMT_MainWindow", "Find Action...", None))
        self.actionHelp.setText(_translate("SmartMT_MainWindow", "Help", None))
        self.actionAbout.setText(_translate("SmartMT_MainWindow", "About", None))
        self.actionOptions.setText(_translate("SmartMT_MainWindow", "Options...", None))
        self.actionPlot.setText(_translate("SmartMT_MainWindow", "Plot...", None))
        self.actionShow_Station_Summary.setText(_translate("SmartMT_MainWindow", "Show Station Summary", None))
        self.actionCascade_Windows.setText(_translate("SmartMT_MainWindow", "Cascade Windows", None))
        self.actionTile_Windows.setText(_translate("SmartMT_MainWindow", "Tile Windows", None))
        self.actionWindowed_View.setText(_translate("SmartMT_MainWindow", "Windowed View", None))
        self.actionTabbed_View.setText(_translate("SmartMT_MainWindow", "Tabbed View", None))
        self.actionClose_All_Images.setText(_translate("SmartMT_MainWindow", "Close All Images", None))
        self.actionExport_ModEM_Data.setText(_translate("SmartMT_MainWindow", "Generate ModEM Input Files...", None))

import icons_rc
