# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GuiGraph(object):
    def setupUi(self, GuiGraph):
        GuiGraph.setObjectName("GuiGraph")
        GuiGraph.resize(1200, 900)
        GuiGraph.setMinimumSize(QtCore.QSize(1200, 900))
        self.horizontalLayout = QtWidgets.QHBoxLayout(GuiGraph)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Background = QtWidgets.QFrame(GuiGraph)
        self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(29, 35, 41, 255), stop:1 rgba(64, 75, 88, 255));\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 14pt \"Roboto\";")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleBar = QtWidgets.QFrame(self.Background)
        self.TitleBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.TitleBar.setStyleSheet("font: 85 16pt \"Roboto\";\n"
"font-weight: bold;")
        self.TitleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBar.setObjectName("TitleBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TitleBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.TitleName = QtWidgets.QFrame(self.TitleBar)
        self.TitleName.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.TitleName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleName.setObjectName("TitleName")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.TitleName)
        self.verticalLayout_15.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lb_title = QtWidgets.QLabel(self.TitleName)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_title.setFont(font)
        self.lb_title.setObjectName("lb_title")
        self.verticalLayout_15.addWidget(self.lb_title)
        self.horizontalLayout_2.addWidget(self.TitleName)
        self.TitleButton = QtWidgets.QFrame(self.TitleBar)
        self.TitleButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.TitleButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.TitleButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TitleButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleButton.setObjectName("TitleButton")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.TitleButton)
        self.horizontalLayout_3.setContentsMargins(0, 4, 4, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_maximize = QtWidgets.QPushButton(self.TitleButton)
        self.btn_maximize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_maximize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(85, 255, 127, 200);\n"
"}")
        self.btn_maximize.setText("")
        self.btn_maximize.setObjectName("btn_maximize")
        self.horizontalLayout_3.addWidget(self.btn_maximize)
        self.btn_minimize = QtWidgets.QPushButton(self.TitleButton)
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 219, 10);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 219, 10, 200);\n"
"}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_3.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.TitleButton)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(236, 41, 7);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(236, 41, 7, 200);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout_2.addWidget(self.TitleButton)
        self.verticalLayout.addWidget(self.TitleBar)
        self.ContentSection = QtWidgets.QFrame(self.Background)
        self.ContentSection.setStyleSheet("background-color: none;")
        self.ContentSection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContentSection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContentSection.setObjectName("ContentSection")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContentSection)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PlotLv = QtWidgets.QFrame(self.ContentSection)
        self.PlotLv.setMinimumSize(QtCore.QSize(1182, 190))
        self.PlotLv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlotLv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlotLv.setObjectName("PlotLv")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.PlotLv)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Graph = QtWidgets.QFrame(self.PlotLv)
        self.Graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph.setObjectName("Graph")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Graph)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plot_ = PlotWidget(self.Graph)
        self.plot_.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_.setStyleSheet("background-color: none;")
        self.plot_.setObjectName("plot_")
        self.verticalLayout_3.addWidget(self.plot_)
        self.lbgraph_ = QtWidgets.QLabel(self.Graph)
        self.lbgraph_.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_.setFont(font)
        self.lbgraph_.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_.setObjectName("lbgraph_")
        self.verticalLayout_3.addWidget(self.lbgraph_)
        self.horizontalLayout_5.addWidget(self.Graph)
        self.Graph_1 = QtWidgets.QFrame(self.PlotLv)
        self.Graph_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_1.setObjectName("Graph_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Graph_1)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plot_1 = PlotWidget(self.Graph_1)
        self.plot_1.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_1.setStyleSheet("background-color: none;")
        self.plot_1.setObjectName("plot_1")
        self.verticalLayout_4.addWidget(self.plot_1)
        self.lbgraph_1 = QtWidgets.QLabel(self.Graph_1)
        self.lbgraph_1.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_1.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_1.setFont(font)
        self.lbgraph_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_1.setObjectName("lbgraph_1")
        self.verticalLayout_4.addWidget(self.lbgraph_1)
        self.horizontalLayout_5.addWidget(self.Graph_1)
        self.Graph_2 = QtWidgets.QFrame(self.PlotLv)
        self.Graph_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_2.setObjectName("Graph_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Graph_2)
        self.verticalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.plot_2 = PlotWidget(self.Graph_2)
        self.plot_2.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_2.setStyleSheet("background-color: none;")
        self.plot_2.setObjectName("plot_2")
        self.verticalLayout_5.addWidget(self.plot_2)
        self.lbgraph_2 = QtWidgets.QLabel(self.Graph_2)
        self.lbgraph_2.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_2.setFont(font)
        self.lbgraph_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_2.setObjectName("lbgraph_2")
        self.verticalLayout_5.addWidget(self.lbgraph_2)
        self.horizontalLayout_5.addWidget(self.Graph_2)
        self.Graph_3 = QtWidgets.QFrame(self.PlotLv)
        self.Graph_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_3.setObjectName("Graph_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Graph_3)
        self.verticalLayout_6.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.plot_3 = PlotWidget(self.Graph_3)
        self.plot_3.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_3.setStyleSheet("background-color: none;")
        self.plot_3.setObjectName("plot_3")
        self.verticalLayout_6.addWidget(self.plot_3)
        self.lbgraph_3 = QtWidgets.QLabel(self.Graph_3)
        self.lbgraph_3.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_3.setFont(font)
        self.lbgraph_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_3.setObjectName("lbgraph_3")
        self.verticalLayout_6.addWidget(self.lbgraph_3)
        self.horizontalLayout_5.addWidget(self.Graph_3)
        self.verticalLayout_2.addWidget(self.PlotLv)
        self.PlotLv_2 = QtWidgets.QFrame(self.ContentSection)
        self.PlotLv_2.setMinimumSize(QtCore.QSize(1182, 190))
        self.PlotLv_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlotLv_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlotLv_2.setObjectName("PlotLv_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.PlotLv_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Graph_4 = QtWidgets.QFrame(self.PlotLv_2)
        self.Graph_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_4.setObjectName("Graph_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Graph_4)
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plot_4 = PlotWidget(self.Graph_4)
        self.plot_4.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_4.setStyleSheet("background-color: none;")
        self.plot_4.setObjectName("plot_4")
        self.verticalLayout_7.addWidget(self.plot_4)
        self.lbgraph_4 = QtWidgets.QLabel(self.Graph_4)
        self.lbgraph_4.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_4.setFont(font)
        self.lbgraph_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_4.setObjectName("lbgraph_4")
        self.verticalLayout_7.addWidget(self.lbgraph_4)
        self.horizontalLayout_6.addWidget(self.Graph_4)
        self.Graph_5 = QtWidgets.QFrame(self.PlotLv_2)
        self.Graph_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_5.setObjectName("Graph_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Graph_5)
        self.verticalLayout_8.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.plot_5 = PlotWidget(self.Graph_5)
        self.plot_5.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_5.setStyleSheet("background-color: none;")
        self.plot_5.setObjectName("plot_5")
        self.verticalLayout_8.addWidget(self.plot_5)
        self.lbgraph_5 = QtWidgets.QLabel(self.Graph_5)
        self.lbgraph_5.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_5.setFont(font)
        self.lbgraph_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_5.setObjectName("lbgraph_5")
        self.verticalLayout_8.addWidget(self.lbgraph_5)
        self.horizontalLayout_6.addWidget(self.Graph_5)
        self.Graph_6 = QtWidgets.QFrame(self.PlotLv_2)
        self.Graph_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_6.setObjectName("Graph_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Graph_6)
        self.verticalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.plot_6 = PlotWidget(self.Graph_6)
        self.plot_6.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_6.setStyleSheet("background-color: none;")
        self.plot_6.setObjectName("plot_6")
        self.verticalLayout_9.addWidget(self.plot_6)
        self.lbgraph_6 = QtWidgets.QLabel(self.Graph_6)
        self.lbgraph_6.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_6.setFont(font)
        self.lbgraph_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_6.setObjectName("lbgraph_6")
        self.verticalLayout_9.addWidget(self.lbgraph_6)
        self.horizontalLayout_6.addWidget(self.Graph_6)
        self.Graph_7 = QtWidgets.QFrame(self.PlotLv_2)
        self.Graph_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_7.setObjectName("Graph_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Graph_7)
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.plot_7 = PlotWidget(self.Graph_7)
        self.plot_7.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_7.setStyleSheet("background-color: none;")
        self.plot_7.setObjectName("plot_7")
        self.verticalLayout_10.addWidget(self.plot_7)
        self.lbgraph_7 = QtWidgets.QLabel(self.Graph_7)
        self.lbgraph_7.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_7.setFont(font)
        self.lbgraph_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_7.setObjectName("lbgraph_7")
        self.verticalLayout_10.addWidget(self.lbgraph_7)
        self.horizontalLayout_6.addWidget(self.Graph_7)
        self.verticalLayout_2.addWidget(self.PlotLv_2)
        self.PlotLv_3 = QtWidgets.QFrame(self.ContentSection)
        self.PlotLv_3.setMinimumSize(QtCore.QSize(1182, 190))
        self.PlotLv_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlotLv_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlotLv_3.setObjectName("PlotLv_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.PlotLv_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Graph_8 = QtWidgets.QFrame(self.PlotLv_3)
        self.Graph_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_8.setObjectName("Graph_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.Graph_8)
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.plot_8 = PlotWidget(self.Graph_8)
        self.plot_8.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_8.setStyleSheet("background-color: none;")
        self.plot_8.setObjectName("plot_8")
        self.verticalLayout_11.addWidget(self.plot_8)
        self.lbgraph_8 = QtWidgets.QLabel(self.Graph_8)
        self.lbgraph_8.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_8.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_8.setFont(font)
        self.lbgraph_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_8.setObjectName("lbgraph_8")
        self.verticalLayout_11.addWidget(self.lbgraph_8)
        self.horizontalLayout_7.addWidget(self.Graph_8)
        self.Graph_9 = QtWidgets.QFrame(self.PlotLv_3)
        self.Graph_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_9.setObjectName("Graph_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Graph_9)
        self.verticalLayout_12.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.plot_9 = PlotWidget(self.Graph_9)
        self.plot_9.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_9.setStyleSheet("background-color: none;")
        self.plot_9.setObjectName("plot_9")
        self.verticalLayout_12.addWidget(self.plot_9)
        self.lbgraph_9 = QtWidgets.QLabel(self.Graph_9)
        self.lbgraph_9.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_9.setFont(font)
        self.lbgraph_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_9.setObjectName("lbgraph_9")
        self.verticalLayout_12.addWidget(self.lbgraph_9)
        self.horizontalLayout_7.addWidget(self.Graph_9)
        self.Graph_10 = QtWidgets.QFrame(self.PlotLv_3)
        self.Graph_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_10.setObjectName("Graph_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Graph_10)
        self.verticalLayout_13.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.plot_10 = PlotWidget(self.Graph_10)
        self.plot_10.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_10.setStyleSheet("background-color: none;")
        self.plot_10.setObjectName("plot_10")
        self.verticalLayout_13.addWidget(self.plot_10)
        self.lbgraph_10 = QtWidgets.QLabel(self.Graph_10)
        self.lbgraph_10.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_10.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_10.setFont(font)
        self.lbgraph_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_10.setObjectName("lbgraph_10")
        self.verticalLayout_13.addWidget(self.lbgraph_10)
        self.horizontalLayout_7.addWidget(self.Graph_10)
        self.Graph_11 = QtWidgets.QFrame(self.PlotLv_3)
        self.Graph_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_11.setObjectName("Graph_11")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Graph_11)
        self.verticalLayout_14.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.plot_11 = PlotWidget(self.Graph_11)
        self.plot_11.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_11.setStyleSheet("background-color: none;")
        self.plot_11.setObjectName("plot_11")
        self.verticalLayout_14.addWidget(self.plot_11)
        self.lbgraph_11 = QtWidgets.QLabel(self.Graph_11)
        self.lbgraph_11.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_11.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_11.setFont(font)
        self.lbgraph_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_11.setObjectName("lbgraph_11")
        self.verticalLayout_14.addWidget(self.lbgraph_11)
        self.horizontalLayout_7.addWidget(self.Graph_11)
        self.verticalLayout_2.addWidget(self.PlotLv_3)
        self.PlotLv_4 = QtWidgets.QFrame(self.ContentSection)
        self.PlotLv_4.setMinimumSize(QtCore.QSize(1182, 190))
        self.PlotLv_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PlotLv_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PlotLv_4.setObjectName("PlotLv_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.PlotLv_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Graph_12 = QtWidgets.QFrame(self.PlotLv_4)
        self.Graph_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_12.setObjectName("Graph_12")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.Graph_12)
        self.verticalLayout_19.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.plot_12 = PlotWidget(self.Graph_12)
        self.plot_12.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_12.setStyleSheet("background-color: none;")
        self.plot_12.setObjectName("plot_12")
        self.verticalLayout_19.addWidget(self.plot_12)
        self.lbgraph_12 = QtWidgets.QLabel(self.Graph_12)
        self.lbgraph_12.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_12.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_12.setFont(font)
        self.lbgraph_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_12.setObjectName("lbgraph_12")
        self.verticalLayout_19.addWidget(self.lbgraph_12)
        self.horizontalLayout_8.addWidget(self.Graph_12)
        self.Graph_13 = QtWidgets.QFrame(self.PlotLv_4)
        self.Graph_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_13.setObjectName("Graph_13")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.Graph_13)
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.plot_13 = PlotWidget(self.Graph_13)
        self.plot_13.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_13.setStyleSheet("background-color: none;")
        self.plot_13.setObjectName("plot_13")
        self.verticalLayout_16.addWidget(self.plot_13)
        self.lbgraph_13 = QtWidgets.QLabel(self.Graph_13)
        self.lbgraph_13.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_13.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_13.setFont(font)
        self.lbgraph_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_13.setObjectName("lbgraph_13")
        self.verticalLayout_16.addWidget(self.lbgraph_13)
        self.horizontalLayout_8.addWidget(self.Graph_13)
        self.Graph_14 = QtWidgets.QFrame(self.PlotLv_4)
        self.Graph_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_14.setObjectName("Graph_14")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.Graph_14)
        self.verticalLayout_17.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.plot_14 = PlotWidget(self.Graph_14)
        self.plot_14.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_14.setStyleSheet("background-color: none;")
        self.plot_14.setObjectName("plot_14")
        self.verticalLayout_17.addWidget(self.plot_14)
        self.lbgraph_14 = QtWidgets.QLabel(self.Graph_14)
        self.lbgraph_14.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_14.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_14.setFont(font)
        self.lbgraph_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_14.setObjectName("lbgraph_14")
        self.verticalLayout_17.addWidget(self.lbgraph_14)
        self.horizontalLayout_8.addWidget(self.Graph_14)
        self.Graph_15 = QtWidgets.QFrame(self.PlotLv_4)
        self.Graph_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_15.setObjectName("Graph_15")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Graph_15)
        self.verticalLayout_18.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.plot_15 = PlotWidget(self.Graph_15)
        self.plot_15.setMinimumSize(QtCore.QSize(0, 0))
        self.plot_15.setStyleSheet("background-color: none;")
        self.plot_15.setObjectName("plot_15")
        self.verticalLayout_18.addWidget(self.plot_15)
        self.lbgraph_15 = QtWidgets.QLabel(self.Graph_15)
        self.lbgraph_15.setMinimumSize(QtCore.QSize(0, 20))
        self.lbgraph_15.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbgraph_15.setFont(font)
        self.lbgraph_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lbgraph_15.setObjectName("lbgraph_15")
        self.verticalLayout_18.addWidget(self.lbgraph_15)
        self.horizontalLayout_8.addWidget(self.Graph_15)
        self.verticalLayout_2.addWidget(self.PlotLv_4)
        self.verticalLayout.addWidget(self.ContentSection)
        self.SubtitleBar = QtWidgets.QFrame(self.Background)
        self.SubtitleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.SubtitleBar.setStyleSheet("background-color: none")
        self.SubtitleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SubtitleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SubtitleBar.setObjectName("SubtitleBar")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.SubtitleBar)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.SubtitleText_2 = QtWidgets.QFrame(self.SubtitleBar)
        self.SubtitleText_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SubtitleText_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SubtitleText_2.setObjectName("SubtitleText_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.SubtitleText_2)
        self.horizontalLayout_12.setContentsMargins(24, 0, 24, 12)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lb_subtitle_2 = QtWidgets.QLabel(self.SubtitleText_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lb_subtitle_2.setFont(font)
        self.lb_subtitle_2.setStyleSheet("")
        self.lb_subtitle_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_subtitle_2.setObjectName("lb_subtitle_2")
        self.horizontalLayout_12.addWidget(self.lb_subtitle_2)
        self.horizontalLayout_11.addWidget(self.SubtitleText_2)
        self.frame_grip_2 = QtWidgets.QFrame(self.SubtitleBar)
        self.frame_grip_2.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip_2.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip_2.setObjectName("frame_grip_2")
        self.horizontalLayout_11.addWidget(self.frame_grip_2)
        self.verticalLayout.addWidget(self.SubtitleBar)
        self.horizontalLayout.addWidget(self.Background)

        self.retranslateUi(GuiGraph)
        QtCore.QMetaObject.connectSlotsByName(GuiGraph)

    def retranslateUi(self, GuiGraph):
        _translate = QtCore.QCoreApplication.translate
        GuiGraph.setWindowTitle(_translate("GuiGraph", "Form"))
        self.lb_title.setText(_translate("GuiGraph", "PASSENGER-II Ground Control Station Graph"))
        self.lbgraph_.setText(_translate("GuiGraph", "GRAPH0"))
        self.lbgraph_1.setText(_translate("GuiGraph", "GRAPH1"))
        self.lbgraph_2.setText(_translate("GuiGraph", "GRAPH2"))
        self.lbgraph_3.setText(_translate("GuiGraph", "GRAPH3"))
        self.lbgraph_4.setText(_translate("GuiGraph", "GRAPH4"))
        self.lbgraph_5.setText(_translate("GuiGraph", "GRAPH5"))
        self.lbgraph_6.setText(_translate("GuiGraph", "GRAPH6"))
        self.lbgraph_7.setText(_translate("GuiGraph", "GRAPH7"))
        self.lbgraph_8.setText(_translate("GuiGraph", "GRAPH8"))
        self.lbgraph_9.setText(_translate("GuiGraph", "GRAPH9"))
        self.lbgraph_10.setText(_translate("GuiGraph", "GRAPH10"))
        self.lbgraph_11.setText(_translate("GuiGraph", "GRAPH11"))
        self.lbgraph_12.setText(_translate("GuiGraph", "GRAPH12"))
        self.lbgraph_13.setText(_translate("GuiGraph", "GRAPH13"))
        self.lbgraph_14.setText(_translate("GuiGraph", "GRAPH14"))
        self.lbgraph_15.setText(_translate("GuiGraph", "GRAPH15"))
        self.lb_subtitle_2.setText(_translate("GuiGraph", "SPACE AC 2021"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GuiGraph = QtWidgets.QWidget()
    ui = Ui_GuiGraph()
    ui.setupUi(GuiGraph)
    GuiGraph.show()
    sys.exit(app.exec_())