from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        """Эта функция является аналогом конструктора для нашего окна"""

        # Далее идёт создание нашего окна
        # setObjectName позволяет задать название класса нашего объекта,
        # чтобы потом его стиль можно было изсенять с помощью CSS
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 350)

        # Далее создаём шрифт, настраиваем его стиль, размер и жирность
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)

        # Создаём виджет главного окна, в котором будут размещаться все объекты
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # После чего создаём объекты нашего класса
        # В Первой строке всегда будет создание объекта класса
        # В следующей строчке будет настраиваться геометрия объекта
        # И далее будут настроенны другие особенности, как шрифт м т.д.
        # Повторяю, setObjectName нужен для стилей CSS
        # <editor-fold desc="ResultOfCalculationLabel lcdNumber">
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 190, 260, 80))
        self.lcdNumber.setObjectName("lcdNumber")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel lcdNumber_2">
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(40, 60, 260, 80))
        self.lcdNumber_2.display("00:00")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelNowTime">
        self.LabelNowTime = QtWidgets.QLabel(self.centralwidget)
        self.LabelNowTime.setGeometry(QtCore.QRect(60, 160, 230, 20))
        self.LabelNowTime.setFont(font)
        self.LabelNowTime.setObjectName("LabelNowTime")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelClockTime">
        self.LabelClockTime = QtWidgets.QLabel(self.centralwidget)
        self.LabelClockTime.setGeometry(QtCore.QRect(60, 30, 230, 20))
        self.LabelClockTime.setFont(font)
        self.LabelClockTime.setObjectName("LabelClockTime")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel SpinBoxClockHours">
        self.SpinBoxClockHours = QtWidgets.QSpinBox(self.centralwidget)
        self.SpinBoxClockHours.setGeometry(QtCore.QRect(350, 60, 51, 31))
        self.SpinBoxClockHours.setMinimum(0)
        self.SpinBoxClockHours.setMaximum(23)
        self.SpinBoxClockHours.setFont(font)
        self.SpinBoxClockHours.setObjectName("SpinBoxClockHours")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel SpinBoxClockMinutes">
        self.SpinBoxClockMinutes = QtWidgets.QSpinBox(self.centralwidget)
        self.SpinBoxClockMinutes.setGeometry(QtCore.QRect(350, 110, 51, 31))
        self.SpinBoxClockHours.setMinimum(0)
        self.SpinBoxClockHours.setMaximum(59)
        self.SpinBoxClockMinutes.setFont(font)
        self.SpinBoxClockMinutes.setObjectName("SpinBoxClockMinutes")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelSetClockTime">
        self.LabelSetClockTime = QtWidgets.QLabel(self.centralwidget)
        self.LabelSetClockTime.setGeometry(QtCore.QRect(330, 30, 261, 20))
        self.LabelSetClockTime.setFont(font)
        self.LabelSetClockTime.setObjectName("LabelSetClockTime")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelClockHours">
        self.LabelClockHours = QtWidgets.QLabel(self.centralwidget)
        self.LabelClockHours.setGeometry(QtCore.QRect(410, 60, 71, 31))
        self.LabelClockHours.setFont(font)
        self.LabelClockHours.setObjectName("LabelClockHours")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelClockMinutes">
        self.LabelClockMinutes = QtWidgets.QLabel(self.centralwidget)
        self.LabelClockMinutes.setGeometry(QtCore.QRect(410, 110, 81, 31))
        self.LabelClockMinutes.setFont(font)
        self.LabelClockMinutes.setObjectName("LabelClockHours_2")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel CheckBoxClockActivity">
        self.CheckBoxClockActivity = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBoxClockActivity.setGeometry(QtCore.QRect(470, 70, 220, 50))
        self.CheckBoxClockActivity.setFont(font)
        self.CheckBoxClockActivity.setTristate(False)
        self.CheckBoxClockActivity.setChecked(True)
        self.CheckBoxClockActivity.setObjectName("CheckBoxClockActivity")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel TextBrowserAfterClockMessage">
        self.TextBrowserAfterClockMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.TextBrowserAfterClockMessage.setGeometry(QtCore.QRect(340, 200, 340, 40))
        self.TextBrowserAfterClockMessage.setFont(font)
        self.TextBrowserAfterClockMessage.setObjectName("TextBrowserAfterClockMessage")
        self.TextBrowserAfterClockMessage.setText("Дарова, отец")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelSetClockMessage">
        self.LabelSetClockMessage = QtWidgets.QLabel(self.centralwidget)
        self.LabelSetClockMessage.setGeometry(QtCore.QRect(340, 150, 301, 41))
        self.LabelSetClockMessage.setFont(font)
        self.LabelSetClockMessage.setObjectName("LabelSetClockMessage")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButtonOfClockSettingsSave">
        self.PushButtonOfClockSettingsSave = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonOfClockSettingsSave.setGeometry(QtCore.QRect(350, 250, 320, 65))
        self.PushButtonOfClockSettingsSave.setFont(font)
        self.PushButtonOfClockSettingsSave.clicked.connect(self.set_clock_parametrs)
        self.PushButtonOfClockSettingsSave.setObjectName("PushButtonOfClockSettingsSave")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_1">
        self.PushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_1.setGeometry(QtCore.QRect(730, 90, 70, 60))
        self.PushButton_1.setFont(font)
        self.PushButton_1.setObjectName("PushButton_1")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_2">
        self.PushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_2.setGeometry(QtCore.QRect(800, 90, 70, 60))
        self.PushButton_2.setFont(font)
        self.PushButton_2.setObjectName("PushButton_2")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_3">
        self.PushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_3.setGeometry(QtCore.QRect(870, 90, 70, 60))
        self.PushButton_3.setFont(font)
        self.PushButton_3.setObjectName("PushButton_3")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_4">
        self.PushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_4.setGeometry(QtCore.QRect(730, 150, 70, 60))
        self.PushButton_4.setFont(font)
        self.PushButton_4.setObjectName("PushButton_4")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_5">
        self.PushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_5.setGeometry(QtCore.QRect(800, 150, 70, 60))
        self.PushButton_5.setFont(font)
        self.PushButton_5.setObjectName("PushButton_5")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_6">
        self.PushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_6.setGeometry(QtCore.QRect(870, 150, 70, 60))
        self.PushButton_6.setFont(font)
        self.PushButton_6.setObjectName("PushButton_6")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_7">
        self.PushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_7.setGeometry(QtCore.QRect(730, 210, 70, 60))
        self.PushButton_7.setFont(font)
        self.PushButton_7.setObjectName("PushButton_7")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_8">
        self.PushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_8.setGeometry(QtCore.QRect(800, 210, 70, 60))
        self.PushButton_8.setFont(font)
        self.PushButton_8.setObjectName("PushButton_8")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_9">
        self.PushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_9.setGeometry(QtCore.QRect(870, 210, 70, 60))
        self.PushButton_9.setFont(font)
        self.PushButton_9.setObjectName("PushButton_9")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButton_0">
        self.PushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.PushButton_0.setGeometry(QtCore.QRect(730, 270, 110, 60))
        self.PushButton_0.setFont(font)
        self.PushButton_0.setObjectName("PushButton_0")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButtonExecuteCalculations">
        self.PushButtonExecuteCalculations = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonExecuteCalculations.setGeometry(QtCore.QRect(840, 270, 100, 60))
        self.PushButtonExecuteCalculations.setFont(font)
        self.PushButtonExecuteCalculations.setObjectName("PushButtonExecuteCalculations")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButtonPlus">
        self.PushButtonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonPlus.setGeometry(QtCore.QRect(940, 90, 51, 60))
        self.PushButtonPlus.setFont(font)
        self.PushButtonPlus.setObjectName("PushButtonPlus")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButtonMinus">
        self.PushButtonMinus = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonMinus.setGeometry(QtCore.QRect(940, 150, 51, 60))
        self.PushButtonMinus.setFont(font)
        self.PushButtonMinus.setObjectName("PushButtonMinus")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButtonMultipliy">
        self.PushButtonMultipliy = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonMultipliy.setGeometry(QtCore.QRect(940, 210, 51, 60))
        self.PushButtonMultipliy.setFont(font)
        self.PushButtonMultipliy.setObjectName("PushButtonMultipliy")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel PushButtonDiv">
        self.PushButtonDiv = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonDiv.setGeometry(QtCore.QRect(940, 270, 51, 60))
        self.PushButtonDiv.setFont(font)
        self.PushButtonDiv.setObjectName("PushButtonDiv")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelCalculator">
        self.LabelCalculator = QtWidgets.QLabel(self.centralwidget)
        self.LabelCalculator.setGeometry(QtCore.QRect(790, 20, 121, 20))
        self.LabelCalculator.setFont(font)
        self.LabelCalculator.setObjectName("LabelCalculator")
        # </editor-fold>

        # <editor-fold desc="ResultOfCalculationLabel LabelResultOfCalculations">
        self.LabelResultOfCalculations = QtWidgets.QLabel(self.centralwidget)
        self.LabelResultOfCalculations.setGeometry(QtCore.QRect(730, 50, 261, 31))
        self.LabelResultOfCalculations.setFont(font)
        self.LabelResultOfCalculations.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.LabelResultOfCalculations.setObjectName("LabelResultOfCalculations")
        # </editor-fold>

        # Задаём в нашем окне центральный виджет
        MainWindow.setCentralWidget(self.centralwidget)

        # И далее ретранслируем информацию в GUI
        # Т.е. Если мы хотим задать какието названия на кнопках, то чтобы они отобразились, надо вызвать эту функцию
        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Создаём таймер и говорим, чтобы он менял время в будильнике
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.set_time)
        self.timer.start()

        # Так же создаём время в которое будильник прозвучит и создаёт таймер,
        # который с каждым тиком будет проверять нужно ли включить будильник
        self.alarm_time = QtCore.QTime(0, 0)
        self.check_alarm = QtCore.QTimer(MainWindow)
        self.check_alarm.timeout.connect(self.create_alarm)
        self.check_alarm.start()

        # Добавляем функции для калькулятора
        self.add_functions()

    def retranslateUi(self, MainWindow):
        """Эта функция позволяет задать надписи на кнопках в GUI"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Будильник Смирнов И.М. 3-41хх 2022"))
        self.LabelNowTime.setText(_translate("MainWindow", "Сколько сейчас времени"))
        self.LabelClockTime.setText(_translate("MainWindow", "Время будильника"))
        self.LabelSetClockTime.setText(_translate("MainWindow", "Задайте время будильника"))
        self.LabelClockHours.setText(_translate("MainWindow", "Часы"))
        self.LabelClockMinutes.setText(_translate("MainWindow", "Минуты"))
        self.CheckBoxClockActivity.setText(_translate("MainWindow", "Вкл./Выкл. Будильник"))
        self.LabelSetClockMessage.setText(_translate("MainWindow", "Сообщение после срабатывания "))
        self.PushButtonOfClockSettingsSave.setText(_translate("MainWindow", "Сохранить настройки будильника"))
        self.PushButton_1.setText(_translate("MainWindow", "1"))
        self.PushButton_2.setText(_translate("MainWindow", "2"))
        self.PushButton_3.setText(_translate("MainWindow", "3"))
        self.PushButton_4.setText(_translate("MainWindow", "4"))
        self.PushButton_5.setText(_translate("MainWindow", "5"))
        self.PushButton_6.setText(_translate("MainWindow", "6"))
        self.PushButton_7.setText(_translate("MainWindow", "7"))
        self.PushButton_8.setText(_translate("MainWindow", "8"))
        self.PushButton_9.setText(_translate("MainWindow", "9"))
        self.PushButton_0.setText(_translate("MainWindow", "0"))
        self.PushButtonExecuteCalculations.setText(_translate("MainWindow", "="))
        self.PushButtonPlus.setText(_translate("MainWindow", "+"))
        self.PushButtonMinus.setText(_translate("MainWindow", "-"))
        self.PushButtonMultipliy.setText(_translate("MainWindow", "*"))
        self.PushButtonDiv.setText(_translate("MainWindow", "/"))
        self.LabelCalculator.setText(_translate("MainWindow", "Калькулятор"))
        self.LabelResultOfCalculations.setText(_translate("MainWindow", "0"))

    def set_time(self):
        """Эта функция устанавливает наше время"""
        self.global_time = QtCore.QTime.currentTime()
        text = self.global_time.toString("HH:mm")
        self.lcdNumber.display(text)

    def set_clock_parametrs(self):
        """Эта функция устанавливает время в которое звонок должен сработать"""
        self.alarm_time = QtCore.QTime(int(self.SpinBoxClockHours.value()), int(self.SpinBoxClockMinutes.value()))
        print(f"{self.global_time.hour()} {self.alarm_time.hour()} {self.global_time.minute()} {self.alarm_time.minute()}")
        alarm_time_text = self.alarm_time.toString("HH:mm")
        self.lcdNumber_2.display(alarm_time_text)

    def create_alarm(self):
        """Эта функция вызывает тревогу при срабатывании будильника"""
        if ((self.global_time.hour() == self.alarm_time.hour()) and
            (self.global_time.minute() == self.alarm_time.minute()) and
            (self.CheckBoxClockActivity.isChecked())):
            print(f"{self.global_time.hour()} {self.alarm_time.hour()} {self.global_time.minute()} {self.alarm_time.minute()}")

            self.CheckBoxClockActivity.setChecked(False)

            # Создаём тревожное окошко
            alarm_message = QMessageBox()
            alarm_message.setWindowTitle("Тревога!")

            alarm_message.setText(self.TextBrowserAfterClockMessage.toPlainText())
            alarm_message.setIcon(QMessageBox.Warning)
            alarm_message.setStandardButtons(QMessageBox.Ok)

            alarm_message.exec_()

    def add_functions(self):
        """Эта функция добавляет функционал для калькуляторв"""
        self.PushButton_0.clicked.connect(lambda: self.write_number(self.PushButton_0.text()))
        self.PushButton_1.clicked.connect(lambda: self.write_number(self.PushButton_1.text()))
        self.PushButton_2.clicked.connect(lambda: self.write_number(self.PushButton_2.text()))
        self.PushButton_3.clicked.connect(lambda: self.write_number(self.PushButton_3.text()))
        self.PushButton_4.clicked.connect(lambda: self.write_number(self.PushButton_4.text()))
        self.PushButton_5.clicked.connect(lambda: self.write_number(self.PushButton_5.text()))
        self.PushButton_6.clicked.connect(lambda: self.write_number(self.PushButton_6.text()))
        self.PushButton_7.clicked.connect(lambda: self.write_number(self.PushButton_7.text()))
        self.PushButton_8.clicked.connect(lambda: self.write_number(self.PushButton_8.text()))
        self.PushButton_9.clicked.connect(lambda: self.write_number(self.PushButton_9.text()))

        self.PushButtonPlus.clicked.connect(lambda: self.write_number(self.PushButtonPlus.text()))
        self.PushButtonMinus.clicked.connect(lambda: self.write_number(self.PushButtonMinus.text()))
        self.PushButtonMultipliy.clicked.connect(lambda: self.write_number(self.PushButtonMultipliy.text()))
        self.PushButtonDiv.clicked.connect(lambda: self.write_number(self.PushButtonDiv.text()))

        self.PushButtonExecuteCalculations.clicked.connect(self.result)


    def write_number(self, number):
        """Эта функция позволяет писать символ в строку калькулятора"""
        if (self.LabelResultOfCalculations.text() == "0"):
            self.LabelResultOfCalculations.setText(number)
        else:
            self.LabelResultOfCalculations.setText(self.LabelResultOfCalculations.text() + number)
        print(number)

    def result(self):
        """Эта функция подсчитывает результат
            Если не получается подсчитать результат, то выводится окно с ошибкой
            И какльклятор выдаёт информацию об ошибке"""
        try:
            res = eval(self.LabelResultOfCalculations.text())
            self.LabelResultOfCalculations.setText(str(res))
        except:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Невозможео выполнить данное действие")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            error.exec_()
            self.LabelResultOfCalculations.setText(str(0))

if __name__ == "__main__":
    import sys
    # Создаём объект отвечающий за контроль GUI и передаём туда настройки нашей системы
    app = QtWidgets.QApplication(sys.argv)
    # Создаём класс главного окна
    MainWindow = QtWidgets.QMainWindow()
    # После чего создаём наш GUI и говорим, что этот GUI будет главным окном
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # И выводим наше окно
    MainWindow.show()
    # Приложение закончит свою работу, когда главный интерфейс будет выключен
    sys.exit(app.exec_())
