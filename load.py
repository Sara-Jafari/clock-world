from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QPoint
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtCore import *
import sys
from PyQt5.QtCore import QDateTime
import pytz
from datetime import datetime


class loading(QMainWindow):
    def __init__(self):
        super(loading,self).__init__()
        uic.loadUi("C:/Users/mmm/Desktop/File/ساعت جهانی/myfile.ui",self)
        home = pytz.timezone("Asia/kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_9.setText(current_time)

        home = pytz.timezone("America/New_york")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_13.setText(current_time)

        home = pytz.timezone("Canada/Atlantic")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_14.setText(current_time)

        home = pytz.timezone("Brazil/Acre")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_12.setText(current_time)

        home = pytz.timezone("Asia/Shanghai")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_2.setText(current_time)

        home = pytz.timezone("europe/Moscow")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_8.setText(current_time)

        home = pytz.timezone("Asia/Tehran")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour.setText(current_time)

        home = pytz.timezone("asia/tokyo")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_10.setText(current_time)

        home = pytz.timezone("Asia/Baku")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_11.setText(current_time)

        home = pytz.timezone("Australia/Eucla")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        self.hour_15.setText(current_time)

        self.show()





app=QApplication(sys.argv)
root=loading()
app.exec()

