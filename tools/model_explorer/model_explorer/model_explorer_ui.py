# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_explorer_ui.ui'
#
# Created: Tue Feb 04 19:36:34 2014
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ModelExplorer(object):
    def setupUi(self, ModelExplorer):
        ModelExplorer.setObjectName(_fromUtf8("ModelExplorer"))
        ModelExplorer.resize(1314, 897)
        ModelExplorer.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(ModelExplorer)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.verticalLayout_4.addWidget(self.mplwidget)
        ModelExplorer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ModelExplorer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1314, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ModelExplorer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ModelExplorer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ModelExplorer.setStatusBar(self.statusbar)
        self.dock_saved_params = QtGui.QDockWidget(ModelExplorer)
        self.dock_saved_params.setMinimumSize(QtCore.QSize(259, 200))
        self.dock_saved_params.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dock_saved_params.setObjectName(_fromUtf8("dock_saved_params"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.list_saved_params = QtGui.QListWidget(self.dockWidgetContents_3)
        self.list_saved_params.setObjectName(_fromUtf8("list_saved_params"))
        self.verticalLayout.addWidget(self.list_saved_params)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_save_params = QtGui.QPushButton(self.dockWidgetContents_3)
        self.button_save_params.setFlat(False)
        self.button_save_params.setObjectName(_fromUtf8("button_save_params"))
        self.horizontalLayout_2.addWidget(self.button_save_params)
        self.button_delete_params = QtGui.QPushButton(self.dockWidgetContents_3)
        self.button_delete_params.setObjectName(_fromUtf8("button_delete_params"))
        self.horizontalLayout_2.addWidget(self.button_delete_params)
        self.button_delete_all_params = QtGui.QPushButton(self.dockWidgetContents_3)
        self.button_delete_all_params.setObjectName(_fromUtf8("button_delete_all_params"))
        self.horizontalLayout_2.addWidget(self.button_delete_all_params)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.dock_saved_params.setWidget(self.dockWidgetContents_3)
        ModelExplorer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_saved_params)
        self.dock_params = QtGui.QDockWidget(ModelExplorer)
        self.dock_params.setMinimumSize(QtCore.QSize(200, 200))
        self.dock_params.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dock_params.setObjectName(_fromUtf8("dock_params"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scroll_area_params = QtGui.QScrollArea(self.dockWidgetContents_4)
        self.scroll_area_params.setWidgetResizable(True)
        self.scroll_area_params.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_params.setObjectName(_fromUtf8("scroll_area_params"))
        self.scroll_area_params_contents = QtGui.QWidget()
        self.scroll_area_params_contents.setGeometry(QtCore.QRect(0, 0, 254, 323))
        self.scroll_area_params_contents.setObjectName(_fromUtf8("scroll_area_params_contents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scroll_area_params_contents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scroll_area_params.setWidget(self.scroll_area_params_contents)
        self.verticalLayout_2.addWidget(self.scroll_area_params)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.combobox_plot_style = QtGui.QComboBox(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_plot_style.sizePolicy().hasHeightForWidth())
        self.combobox_plot_style.setSizePolicy(sizePolicy)
        self.combobox_plot_style.setObjectName(_fromUtf8("combobox_plot_style"))
        self.horizontalLayout.addWidget(self.combobox_plot_style)
        self.progress_bar = QtGui.QProgressBar(self.dockWidgetContents_4)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.horizontalLayout.addWidget(self.progress_bar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.dock_params.setWidget(self.dockWidgetContents_4)
        ModelExplorer.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_params)

        self.retranslateUi(ModelExplorer)
        QtCore.QObject.connect(self.combobox_plot_style, QtCore.SIGNAL(_fromUtf8("activated(QString)")), ModelExplorer.change_plot_style)
        QtCore.QObject.connect(self.button_save_params, QtCore.SIGNAL(_fromUtf8("clicked()")), ModelExplorer.save_parameters)
        QtCore.QObject.connect(self.list_saved_params, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), ModelExplorer.clicked_saved_parameters)
        QtCore.QObject.connect(self.button_delete_params, QtCore.SIGNAL(_fromUtf8("clicked()")), ModelExplorer.delete_parameters)
        QtCore.QObject.connect(self.button_delete_all_params, QtCore.SIGNAL(_fromUtf8("clicked()")), ModelExplorer.delete_all_parameters)
        QtCore.QMetaObject.connectSlotsByName(ModelExplorer)

    def retranslateUi(self, ModelExplorer):
        ModelExplorer.setWindowTitle(QtGui.QApplication.translate("ModelExplorer", "Model Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.dock_saved_params.setWindowTitle(QtGui.QApplication.translate("ModelExplorer", "Saved parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save_params.setText(QtGui.QApplication.translate("ModelExplorer", "Save params", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete_params.setText(QtGui.QApplication.translate("ModelExplorer", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete_all_params.setText(QtGui.QApplication.translate("ModelExplorer", "Delete all", None, QtGui.QApplication.UnicodeUTF8))
        self.dock_params.setWindowTitle(QtGui.QApplication.translate("ModelExplorer", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.progress_bar.setFormat(QtGui.QApplication.translate("ModelExplorer", "%p%", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget