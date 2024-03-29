from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import sys


class Gui(object):
    def __init__(self):
        self.lockfile = QtCore.QLockFile(QtCore.QDir.tempPath() + '/mygui.lock')

    def setupUi(self, Form):

        pg.setConfigOption('background', (40, 40, 40))
        pg.setConfigOption('foreground', 'w')
        pg.mkPen(width=10)

        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);")
        self.widget_temp2 = PlotWidget(Form)
        self.widget_temp2.setGeometry(QtCore.QRect(540, 110, 401, 201))
        self.widget_temp2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_temp2.setObjectName("widget_temp2")
        self.lb_sys_time_9 = QtWidgets.QLabel(Form)
        self.lb_sys_time_9.setGeometry(QtCore.QRect(120, 820, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_9.setFont(font)
        self.lb_sys_time_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_9.setObjectName("lb_sys_time_9")
        self.lb_sys_time_13 = QtWidgets.QLabel(Form)
        self.lb_sys_time_13.setGeometry(QtCore.QRect(1400, 820, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_13.setFont(font)
        self.lb_sys_time_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_13.setObjectName("lb_sys_time_13")
        self.widget_lon = PlotWidget(Form)
        self.widget_lon.setGeometry(QtCore.QRect(1400, 860, 401, 131))
        self.widget_lon.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_lon.setObjectName("widget_lon")
        self.widget_accy = PlotWidget(Form)
        self.widget_accy.setGeometry(QtCore.QRect(980, 360, 401, 201))
        self.widget_accy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_accy.setObjectName("widget_accy")
        self.widget_vol = PlotWidget(Form)
        self.widget_vol.setGeometry(QtCore.QRect(120, 860, 401, 131))
        self.widget_vol.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_vol.setObjectName("widget_vol")
        self.lb_title = QtWidgets.QLabel(Form)
        self.lb_title.setGeometry(QtCore.QRect(460, 30, 1001, 41))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet("")
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_title.setObjectName("lb_title")
        self.widget_pm102 = PlotWidget(Form)
        self.widget_pm102.setGeometry(QtCore.QRect(980, 610, 401, 201))
        self.widget_pm102.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_pm102.setObjectName("widget_pm102")
        self.lb_sys_time_15 = QtWidgets.QLabel(Form)
        self.lb_sys_time_15.setGeometry(QtCore.QRect(1400, 1000, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_15.setFont(font)
        self.lb_sys_time_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_15.setObjectName("lb_sys_time_15")
        self.widget_alt2 = PlotWidget(Form)
        self.widget_alt2.setGeometry(QtCore.QRect(540, 360, 401, 201))
        self.widget_alt2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_alt2.setObjectName("widget_alt2")
        self.widget_pm101 = PlotWidget(Form)
        self.widget_pm101.setGeometry(QtCore.QRect(540, 610, 401, 201))
        self.widget_pm101.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_pm101.setObjectName("widget_pm101")
        self.lb_sys_time_12 = QtWidgets.QLabel(Form)
        self.lb_sys_time_12.setGeometry(QtCore.QRect(540, 820, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_12.setFont(font)
        self.lb_sys_time_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_12.setObjectName("lb_sys_time_12")
        self.lb_sys_time_16 = QtWidgets.QLabel(Form)
        self.lb_sys_time_16.setGeometry(QtCore.QRect(980, 1000, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_16.setFont(font)
        self.lb_sys_time_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_16.setObjectName("lb_sys_time_16")
        self.lb_sys_time_11 = QtWidgets.QLabel(Form)
        self.lb_sys_time_11.setGeometry(QtCore.QRect(120, 1000, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_11.setFont(font)
        self.lb_sys_time_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_11.setObjectName("lb_sys_time_11")
        self.lb_sys_time_3 = QtWidgets.QLabel(Form)
        self.lb_sys_time_3.setGeometry(QtCore.QRect(980, 320, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_3.setFont(font)
        self.lb_sys_time_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_3.setObjectName("lb_sys_time_3")
        self.widget_hum = PlotWidget(Form)
        self.widget_hum.setGeometry(QtCore.QRect(120, 610, 401, 201))
        self.widget_hum.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_hum.setObjectName("widget_hum")
        self.widget_alt1 = PlotWidget(Form)
        self.widget_alt1.setGeometry(QtCore.QRect(120, 360, 401, 201))
        self.widget_alt1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_alt1.setObjectName("widget_alt1")
        self.lb_subtitle = QtWidgets.QLabel(Form)
        self.lb_subtitle.setGeometry(QtCore.QRect(460, 70, 1001, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_subtitle.setFont(font)
        self.lb_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_subtitle.setObjectName("lb_subtitle")
        self.lb_sys_time_14 = QtWidgets.QLabel(Form)
        self.lb_sys_time_14.setGeometry(QtCore.QRect(540, 1000, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_14.setFont(font)
        self.lb_sys_time_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_14.setObjectName("lb_sys_time_14")
        self.lb_sys_time_5 = QtWidgets.QLabel(Form)
        self.lb_sys_time_5.setGeometry(QtCore.QRect(120, 570, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_5.setFont(font)
        self.lb_sys_time_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_5.setObjectName("lb_sys_time_5")
        self.widget_pm103 = PlotWidget(Form)
        self.widget_pm103.setGeometry(QtCore.QRect(1400, 610, 401, 201))
        self.widget_pm103.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_pm103.setObjectName("widget_pm103")
        self.widget_lat = PlotWidget(Form)
        self.widget_lat.setGeometry(QtCore.QRect(980, 860, 401, 131))
        self.widget_lat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_lat.setObjectName("widget_lat")
        self.lb_sys_time_4 = QtWidgets.QLabel(Form)
        self.lb_sys_time_4.setGeometry(QtCore.QRect(1400, 320, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_4.setFont(font)
        self.lb_sys_time_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_4.setObjectName("lb_sys_time_4")
        self.lb_sys_time = QtWidgets.QLabel(Form)
        self.lb_sys_time.setGeometry(QtCore.QRect(120, 320, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time.setFont(font)
        self.lb_sys_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time.setObjectName("lb_sys_time")
        self.widget_temp1 = PlotWidget(Form)
        self.widget_temp1.setGeometry(QtCore.QRect(120, 110, 401, 201))
        self.widget_temp1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_temp1.setObjectName("widget_temp1")
        self.lb_sys_time_2 = QtWidgets.QLabel(Form)
        self.lb_sys_time_2.setGeometry(QtCore.QRect(540, 320, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_2.setFont(font)
        self.lb_sys_time_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_2.setObjectName("lb_sys_time_2")
        self.lb_sys_time_8 = QtWidgets.QLabel(Form)
        self.lb_sys_time_8.setGeometry(QtCore.QRect(1400, 570, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_8.setFont(font)
        self.lb_sys_time_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_8.setObjectName("lb_sys_time_8")
        self.widget_mpxv = PlotWidget(Form)
        self.widget_mpxv.setGeometry(QtCore.QRect(540, 860, 401, 131))
        self.widget_mpxv.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_mpxv.setObjectName("widget_mpxv")
        self.lb_sys_time_7 = QtWidgets.QLabel(Form)
        self.lb_sys_time_7.setGeometry(QtCore.QRect(980, 570, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_7.setFont(font)
        self.lb_sys_time_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_7.setObjectName("lb_sys_time_7")
        self.widget_gyry = PlotWidget(Form)
        self.widget_gyry.setGeometry(QtCore.QRect(1400, 360, 401, 201))
        self.widget_gyry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_gyry.setObjectName("widget_gyry")
        self.lb_sys_time_6 = QtWidgets.QLabel(Form)
        self.lb_sys_time_6.setGeometry(QtCore.QRect(540, 570, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_6.setFont(font)
        self.lb_sys_time_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_6.setObjectName("lb_sys_time_6")
        self.widget_accx = PlotWidget(Form)
        self.widget_accx.setGeometry(QtCore.QRect(980, 110, 401, 201))
        self.widget_accx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_accx.setObjectName("widget_accx")
        self.widget_gyrx = PlotWidget(Form)
        self.widget_gyrx.setGeometry(QtCore.QRect(1400, 110, 401, 201))
        self.widget_gyrx.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_gyrx.setObjectName("widget_gyrx")
        self.lb_sys_time_10 = QtWidgets.QLabel(Form)
        self.lb_sys_time_10.setGeometry(QtCore.QRect(980, 820, 401, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lb_sys_time_10.setFont(font)
        self.lb_sys_time_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sys_time_10.setObjectName("lb_sys_time_10")
        self.lb_update = QtWidgets.QLabel(Form)
        self.lb_update.setGeometry(QtCore.QRect(30, 30, 351, 20))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_update.setFont(font)
        self.lb_update.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lb_update.setObjectName("lb_update")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PASSENGER-I GCS (Graph)"))
        self.lb_sys_time_9.setText(_translate("Form", "PKT - INTERNAL HUMIDITY (%)"))
        self.lb_sys_time_13.setText(_translate("Form", "PKT - PM10 (3)"))
        self.lb_title.setText(_translate("Form", "PASSENGER-I GCS"))
        self.lb_sys_time_15.setText(_translate("Form", "PKT - LONGITUDE"))
        self.lb_sys_time_12.setText(_translate("Form", "PKT - PM10 (1)"))
        self.lb_sys_time_16.setText(_translate("Form", "PKT - LATITUDE"))
        self.lb_sys_time_11.setText(_translate("Form", "PKT - BATTERY VOLTAGE (mV)"))
        self.lb_sys_time_3.setText(_translate("Form", "PKT - ACC_X"))
        self.lb_subtitle.setText(_translate("Form", "CHANNEL 1/2/3"))
        self.lb_sys_time_14.setText(_translate("Form", "PKT - MPXV"))
        self.lb_sys_time_5.setText(_translate("Form", "PKT - GPS ALTITUDE (M)"))
        self.lb_sys_time_4.setText(_translate("Form", "PKT - GYR_X"))
        self.lb_sys_time.setText(_translate("Form", "PKT - INTERNAL TEMPERATURE (DEG C)"))
        self.lb_sys_time_2.setText(_translate("Form", "PKT - EXTERNAL TEMPERATURE (DEG C)"))
        self.lb_sys_time_8.setText(_translate("Form", "PKT - GYR_Y"))
        self.lb_sys_time_7.setText(_translate("Form", "PKT - ACC_Y"))
        self.lb_sys_time_6.setText(_translate("Form", "PKT - BAROMETRIC ALTITUDE (M)"))
        self.lb_sys_time_10.setText(_translate("Form", "PKT - PM10 (2)"))
        self.lb_update.setText(_translate("Form", "NOT READY"))

    def isRunning(self):

        if self.lockfile.tryLock(100):
            self._isRunning = False
        else:
            self._isRunning = True
        return self._isRunning

def mystart():
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui2 = Gui()
    ui2.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    mystart()

