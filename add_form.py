# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1173, 888)
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 204, 153);\n"
"border: 2px solid #094065")
        self.scrollArea_of_categories = QtWidgets.QScrollArea(Form)
        self.scrollArea_of_categories.setGeometry(QtCore.QRect(50, 90, 531, 601))
        self.scrollArea_of_categories.setMinimumSize(QtCore.QSize(531, 601))
        self.scrollArea_of_categories.setMaximumSize(QtCore.QSize(1000, 1000))
        self.scrollArea_of_categories.setStyleSheet("border-color: rgb(255, 204, 153);\n"
"color: rgb(0, 0, 0);")
        self.scrollArea_of_categories.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_of_categories.setWidgetResizable(True)
        self.scrollArea_of_categories.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_of_categories.setObjectName("scrollArea_of_categories")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 527, 597))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_test = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_test.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 2px solid #094065")
        self.label_test.setText("")
        self.label_test.setObjectName("label_test")
        self.gridLayout.addWidget(self.label_test, 0, 0, 1, 1)
        self.scrollArea_of_categories.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(255, 204, 153);\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.add_summ_lineedit = QtWidgets.QLineEdit(Form)
        self.add_summ_lineedit.setGeometry(QtCore.QRect(660, 160, 481, 31))
        self.add_summ_lineedit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.add_summ_lineedit.setObjectName("add_summ_lineedit")
        self.subtract_button = QtWidgets.QPushButton(Form)
        self.subtract_button.setGeometry(QtCore.QRect(910, 210, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.subtract_button.setFont(font)
        self.subtract_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(224, 32, 32);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.subtract_button.setObjectName("subtract_button")
        self.edit_button = QtWidgets.QPushButton(Form)
        self.edit_button.setGeometry(QtCore.QRect(660, 290, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.edit_button.setFont(font)
        self.edit_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.edit_button.setObjectName("edit_button")
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(660, 210, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(120, 183, 140);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.add_button.setObjectName("add_button")
        self.choose_day_comboBox = QtWidgets.QComboBox(Form)
        self.choose_day_comboBox.setGeometry(QtCore.QRect(660, 420, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choose_day_comboBox.setFont(font)
        self.choose_day_comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;\n"
"border: 2px solid #094065")
        self.choose_day_comboBox.setObjectName("choose_day_comboBox")
        self.label_show_category = QtWidgets.QLabel(Form)
        self.label_show_category.setGeometry(QtCore.QRect(660, 110, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_show_category.setFont(font)
        self.label_show_category.setStyleSheet("border-color: rgb(255, 204, 153);\n"
"color: rgb(0, 0, 0);")
        self.label_show_category.setText("")
        self.label_show_category.setObjectName("label_show_category")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(920, 300, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("border-color: rgb(255, 204, 153);\n"
"color: rgb(0, 0, 0);")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.name_of_category_lineedit = QtWidgets.QLineEdit(Form)
        self.name_of_category_lineedit.setGeometry(QtCore.QRect(40, 760, 251, 31))
        self.name_of_category_lineedit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.name_of_category_lineedit.setObjectName("name_of_category_lineedit")
        self.category_add_button = QtWidgets.QPushButton(Form)
        self.category_add_button.setGeometry(QtCore.QRect(310, 760, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.category_add_button.setFont(font)
        self.category_add_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.category_add_button.setObjectName("category_add_button")
        self.category_remove_button = QtWidgets.QPushButton(Form)
        self.category_remove_button.setGeometry(QtCore.QRect(310, 810, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.category_remove_button.setFont(font)
        self.category_remove_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.category_remove_button.setObjectName("category_remove_button")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(660, 391, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color: rgb(255, 204, 153);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.back_to_main_window_button = QtWidgets.QPushButton(Form)
        self.back_to_main_window_button.setGeometry(QtCore.QRect(20, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.back_to_main_window_button.setFont(font)
        self.back_to_main_window_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 15px;\n"
"border: 2px solid #094065")
        self.back_to_main_window_button.setObjectName("back_to_main_window_button")
        self.label_add_category_error = QtWidgets.QLabel(Form)
        self.label_add_category_error.setGeometry(QtCore.QRect(40, 810, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_add_category_error.setFont(font)
        self.label_add_category_error.setStyleSheet("border-color: rgb(255, 204, 153);\n"
"color: rgb(0, 0, 0);")
        self.label_add_category_error.setText("")
        self.label_add_category_error.setObjectName("label_add_category_error")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Категории"))
        self.subtract_button.setText(_translate("Form", "Вычесть"))
        self.edit_button.setText(_translate("Form", "Изменить"))
        self.add_button.setText(_translate("Form", "Добавить"))
        self.category_add_button.setText(_translate("Form", "Добавить категорию"))
        self.category_remove_button.setText(_translate("Form", "Удалить категорию"))
        self.label_2.setText(_translate("Form", "Выбрать день"))
        self.back_to_main_window_button.setText(_translate("Form", "Вернуться к главному окну"))