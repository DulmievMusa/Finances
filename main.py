import datetime
import sys
import os
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QMessageBox
from PyQt5 import QtCore, QtWidgets
import sqlite3
import pyqtgraph as pg
from playsound import playsound
from project_ui import Ui_MainWindow
from add_form import Ui_Form
from months_form import Ui_Form1
from choose_account import Ui_Form2

db_name = 0

if not os.path.exists('Users.txt'):
    file = open('Users.txt', mode='w', encoding='utf8')
    file.close()

if not os.path.exists('always.txt'):
    file = open('always.txt', mode='w', encoding='utf8')
    file.write('0')
    file.close()


class Choose_account_form(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.fill_layout()
        self.add_user_button.clicked.connect(self.add_user)
        self.remove_user_button.clicked.connect(self.remove_user)
        self.enter_button.clicked.connect(self.open_main_window)
        self.remove_user_button.setEnabled(False)
        self.enter_button.setEnabled(False)
        self.label_2.setText('')
        self.checkBox.hide()

    def users(self):
        with open('Users.txt', mode='r', encoding='utf8') as file:
            return file.read().split('\n')

    def fill_layout(self):
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)

        for user in self.users():
            if user != '':  # Создание кнопки
                self.user_button = QtWidgets.QPushButton()
                self.user_button.setGeometry(QtCore.QRect(520, 30, 211, 61))
                self.user_button.setMinimumSize(QtCore.QSize(211, 58))
                font = QFont()
                font.setPointSize(13)
                self.user_button.setFont(font)
                self.user_button.setObjectName("user_button")
                self.user_button.setText(user)
                self.user_button.clicked.connect(self.choose_user)
                self.verticalLayout.addWidget(self.user_button)

    def add_user(self):
        playsound("button_sound_2.mp3")
        try:
            name = self.enter_name_lineedit.text()
            if len(self.users()) > 7:
                self.error_label.setText('Максимальное количество аккаунтов 7. Прежде чем добавить ещё, удалите один')
                return
            elif name == '':
                self.error_label.setText('Впишите текст')
                return
            elif ' ' in name:
                self.error_label.setText('Впишите текст без пробелов')
                return
            elif name in self.users():
                self.error_label.setText('Пользователь с таким именем уже создан')
                return
            elif name.isdigit():
                self.error_label.setText('Нельзя дать имя только из цифр')
                return
            elif len(name) > 10:
                self.error_label.setText('Слишком много символов. Максимум - 10')
                return
            elif name[0].isdigit():
                self.error_label.setText('Первый символ должна быть буква')
                return
            elif not name.isalnum():
                self.error_label.setText('Название должно содержать только буквы и цифры')
                return
            with open('Users.txt', mode='a', encoding='utf8') as file:
                if len(self.users()) == 0:
                    file.write(name)
                else:
                    file.write('\n' + name)
            self.fill_layout()
            self.enter_name_lineedit.setText('')
        except Exception:
            self.error_label.setText('Ошибка')

    def remove_user(self):
        playsound("button_sound_2.mp3")
        with open('always.txt', mode='r', encoding='utf8') as alwaysf:
            always_user = alwaysf.read().strip()
        users = self.users()
        answer = QMessageBox.question(self, f'Удалить пользователя {self.user}?',
                                      f'Вы уверены что хотите удалить пользователя {self.user}?\n'
                                      'Удалится вся инфромация за всё время', QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if answer == QMessageBox.No:
            return
        users.remove(self.user)
        try:
            if os.path.exists(self.user + '.sqlite'):
                os.remove(self.user + '.sqlite')
        except Exception:
            self.error_label.setText('Этого пользователя можно удалить только после перезапуска программы')
            self.remove_user_button.setText('Удалить пользователя')
            return
        if self.user == always_user:
            alwaysf = open('always.txt', mode='w', encoding='utf8')
            alwaysf.write('0')
            alwaysf.close()
        with open('Users.txt', mode='w', encoding='utf8') as file:
            file.write('\n'.join(users))
        self.fill_layout()
        self.remove_user_button.setEnabled(False)
        self.enter_button.setEnabled(False)
        self.remove_user_button.setText('Удалить пользователя')
        self.label_2.setText('')
        self.error_label.setText('')
        self.checkBox.hide()

    def choose_user(self):
        playsound("button_sound_2.mp3")
        self.checkBox.show()
        self.user = self.sender().text()
        self.label_2.setText(f'При открытии всегда выбирать пользователя {self.user}')
        self.remove_user_button.setText(f'Удалить пользователя {self.user}')
        self.remove_user_button.setEnabled(True)
        self.enter_button.setEnabled(True)
        self.error_label.setText('')

    def open_main_window(self):
        playsound("button_sound_2.mp3")
        global db_name
        db_name = self.user + '.sqlite'
        with open('always.txt', mode='w', encoding='utf8') as file:
            if self.checkBox.isChecked():
                file.write(db_name)
            else:
                file.write('0')
        self.main_form = MyWidget()
        self.main_form.show()
        self.close()


class NegativeNumber(Exception):
    pass


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, colors=[(93, 135, 130), (242, 154, 22), (117, 221, 235),
                               (127, 117, 235), (113, 166, 104), (240, 77, 77),
                               (0, 166, 143), (255, 144, 144), (205, 111, 255)]):
        super().__init__()
        self.setupUi(self)
        global db_name
        self.category_comboBox.currentIndexChanged.connect(self.category_comboBox_changed)
        self.show_last_month_button.clicked.connect(self.show_last_month)
        self.button_add_summ_to_income.clicked.connect(self.add_summ_to_income)
        self.button_edit_income.clicked.connect(self.add_summ_to_income)
        self.edit_expenses_button.clicked.connect(self.open_add_form)
        self.show_statistics_for_months_button.clicked.connect(self.open_statistics_for_months_form)
        self.change_user_button.clicked.connect(self.change_user)
        self.db = db_name
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()
        self.colors = colors
        tables = [i[0] for i in self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        self.t1 = tables.copy()
        if 'days' not in tables:
            self.cur.execute("""CREATE TABLE days (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                                    Еда INTEGER)""")
            self.cur.execute("""INSERT INTO days(Еда) VALUES(0)""")
            self.con.commit()
        if 'months' not in tables:
            self.cur.execute("""CREATE TABLE months (id STRING UNIQUE NOT NULL)""")
            self.main_table = 'days'
            self.new_month(first=True)
            self.con.commit()
        if 'last_month_days' not in tables:
            self.show_last_month_button.setEnabled(False)
        else:
            self.show_last_month_button.setEnabled(True)
        if 'incomes' not in tables:
            self.cur.execute("""CREATE TABLE incomes (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                                      income INTEGER)""")
            # self.cur.execute("""INSERT INTO incomes(income) VALUES(0)""")
            self.con.commit()
        if 'last_month_incomes' not in tables:
            self.cur.execute("""CREATE TABLE last_month_incomes(id INTEGER, income INTEGER)""")
            self.con.commit()
        if 'incomes_months' not in tables:
            self.cur.execute("""CREATE TABLE incomes_months(id STRING, income INTEGER)""")
            self.con.commit()
        self.con.commit()
        self.init_all()

    def init_all(self, main_table='days'):
        self.square_graph_pixmap = QPixmap(101, 485)
        self.pix_label.setPixmap(self.square_graph_pixmap)

        if len(self.cur.execute("""SELECT id FROM months""").fetchall()) < 3:
            self.show_statistics_for_months_button.setEnabled(False)
        else:
            years = list([i[0].split()[0] for i in self.cur.execute(f"""SELECT id FROM months""").fetchall()])
            flag = True
            for year in years:
                if years.count(year) >= 2:
                    self.show_statistics_for_months_button.setEnabled(True)
                    flag = False
            if flag:
                self.show_statistics_for_months_button.setEnabled(False)
        self.main_table = main_table
        if self.main_table == 'days':
            self.income_table = 'incomes'
            self.day = datetime.datetime.today().day
        else:
            self.income_table = 'last_month_incomes'
            self.day = int(self.cur.execute("""SELECT id FROM last_month_incomes""").fetchall()[-1][0])
        for _ in range(len(self.most_spending_categories_sort()) - len(self.colors)):  # Добавление новых цветов
            self.colors.append((randint(1, 255), randint(1, 255), randint(1, 255)))
        self.do_paint = True
        self.paint()
        self.add_labels()
        months = [i[0] for i in self.cur.execute("""SELECT id FROM months""").fetchall()]
        if main_table == 'days':
            months = sorted(months, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
            month = int(months[-1].split()[-1])
        else:
            months = sorted(months, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
            month = int(months[-2].split()[-1])
        self.months_dict = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
                       7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
        self.month = self.months_dict[month]
        if main_table == 'days' and datetime.datetime.today().month != month:  # Новый месяц
            self.new_month()
        days = [sum(tup[1:]) for tup in
                self.cur.execute(f"""SELECT * FROM {self.main_table}""")]  # Список сумм потраченых в каждый день месяца
        today = datetime.datetime.today().day
        self.con.commit()
        if today > len(days) and self.main_table == 'days':  # Если пользователь зашёл в новый день
            columns = [tup[1] for tup in
                       self.cur.execute(f"""pragma table_info({self.main_table})""")]  # Названия полей
            for i in range(today - len(days)):  # Добавление строк с нулями для новых дней
                # print(f"""INSERT INTO {self.main_table}{tuple(columns[1:])} VALUES{tuple(len(columns[1:]) * [0])}""")
                if len(tuple(columns[1:])) == 1:
                    col = '(' + str(columns[1:][0]) + ')'
                else:
                    col = tuple(columns[1:])
                if len(len(columns[1:]) * [0]) == 1:
                    col2 = '(0)'
                else:
                    col2 = tuple(len(columns[1:]) * [0])
                self.cur.execute(f"""INSERT INTO {self.main_table}{col}
                                                        VALUES{col2}""")
                self.cur.execute(f"""INSERT INTO incomes(income)VALUES(0)""")
            self.con.commit()
            days += [0] * (today - len(days))
        self.repaint_graph(days, self.widget)
        most_spending_categories = self.most_spending_categories_sort()
        self.refill_category_comboBox(most_spending_categories)
        self.category_comboBox_changed()
        if self.main_table == 'days':
            self.show_day_statistics(day=datetime.datetime.today().day)
        else:
            last_day = self.cur.execute("""SELECT id FROM last_month_days""").fetchall()[-1][0]
            self.show_day_statistics(day=last_day)
        self.change_labels()
        self.repaint_graph([i[0] for i in self.cur.execute(f"""SElECT income FROM {self.income_table}""").fetchall()],
                           self.graph_about_income)

    def new_month(self, first=False):
        tables = [i[0] for i in self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        # start last_month_days
        if 'last_month_days' in tables:
            self.cur.execute("""DROP TABLE last_month_days""")
            self.con.commit()
        if not first:
            columns = [tup[1] + ' INTEGER' for tup in
                       self.cur.execute(f"""pragma table_info({self.main_table})""")]  # Названия полей в таблице дней
            self.cur.execute(f"""CREATE TABLE last_month_days({', '.join(columns)})""")
            all_info_about_days = self.cur.execute("""SELECT * FROM days""").fetchall()
            columns = ', '.join([i.split()[0] for i in columns])
            for tup in all_info_about_days:
                self.cur.execute(
                    f"""INSERT INTO last_month_days({columns}) VALUES{tup}""")  # Добавление значений в lm_days
            self.con.commit()
            self.show_last_month_button.show()
        # start incomes
        if 'incomes' in self.t1 and not first:
            all_info_about_incomes = self.cur.execute("""SELECT * FROM incomes""").fetchall()
            self.cur.execute("""DELETE FROM last_month_incomes""")
            for tup in all_info_about_incomes:  # Заполнение доходов за прошлый месяц
                self.cur.execute(f"""INSERT INTO last_month_incomes(id, income) VALUES{tup}""")
            self.cur.execute(f"""DELETE FROM incomes""")
            self.cur.execute("""UPDATE SQLITE_SEQUENCE SET seq = 0""")  # Установка счёта id с 1
            self.con.commit()
        # end incomes
        columns = [tup[1] for tup in
                   self.cur.execute(f"""pragma table_info({self.main_table})""")]  # Названия полей в таблице дней
        date = f'{datetime.datetime.today().year} {datetime.datetime.today().month}'
        # Добавление информации о доходах за месяц
        if 'last_month_incomes' in self.t1 and not first:
            all_income = sum([sum(i[1:]) for i in self.cur.execute('''SELECT * FROM last_month_incomes''').fetchall()])
            if len(self.cur.execute(f'''SELECT id FROM months''').fetchall()) >= 2:
                months = [i[0] for i in self.cur.execute("""SELECT id FROM months""").fetchall()]
                months = sorted(months, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
                month = months[-1].split()[-1]
                date1 = f'{datetime.datetime.today().year} {month}'
            else:
                if datetime.datetime.today().month == 1:
                    date1 = f'{datetime.datetime.today().year} {12}'
                else:
                    date1 = f'{datetime.datetime.today().year} {datetime.datetime.today().month - 1}'
            self.cur.execute(f"""INSERT INTO incomes_months(id, income) VALUES {tuple((date1, all_income))}""")
        sum_each_categories = []
        columns_in_months = [tup[1] for tup in
                             self.cur.execute("""pragma table_info(months)""")]  # Названия полей в таблице месяцев
        for name_of_column in columns[1:]:
            if name_of_column not in columns_in_months:  # Добавление новых столбцов в таблицу months
                self.cur.execute(f"""ALTER TABLE months ADD COLUMN {name_of_column} INTEGER""")
                for name in columns_in_months:
                    if name != date:
                        self.cur.execute(
                            f"""UPDATE months SET {name_of_column} = 0""")  # Добавление нулей в в новый столбик
            sum_of_category = sum([tup[0] for tup in self.cur.execute(f"""SELECT {name_of_column}
                                    from {self.main_table}""").fetchall()])  # Сумма трат по данной категории за месяц
            sum_each_categories.append(sum_of_category)
        # if len(list(self.cur.execute(f'''SELECT * FROM months''').fetchall())) != 0:
            # self.cur.execute(f"""DELETE FROM months WHERE id = '{self.cur.execute(f'''SELECT id from months''').fetchall()[-1][0]}'""")
        if len(self.cur.execute(f'''SELECT id FROM months''').fetchall()) >= 2:
            months = [i[0] for i in self.cur.execute("""SELECT id FROM months""").fetchall()]
            months = sorted(months, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
            month = months[-1].split()[-1]
            date1 = f'{datetime.datetime.today().year} {month}'
        else:
            if datetime.datetime.today().month == 1:
                date1 = f'{datetime.datetime.today().year} {12}'
            else:
                date1 = f'{datetime.datetime.today().year} {datetime.datetime.today().month - 1}'
        for i, name in enumerate(columns[1:]):
            self.cur.execute(f'''UPDATE months SET {name} = {sum_each_categories[i]} WHERE id = "{date1}"''')
            self.con.commit()
        self.cur.execute(f"""INSERT INTO months{tuple(['id'] + columns[1:])} 
                                    VALUES{tuple([date] + len(sum_each_categories) * [0])}""")
        self.con.commit()
        for name in columns_in_months[1:]:
            self.cur.execute(
                f"""UPDATE months SET {name} = 0 WHERE {name} IS NULL""")  # Добавление нулей в пустые места
        self.cur.execute(f"""DELETE FROM {self.main_table}""")
        self.cur.execute("""UPDATE SQLITE_SEQUENCE SET seq = 0""")  # Установка счёта id с 1
        self.con.commit()

    def change_user(self):
        playsound("button_sound_2.mp3")
        with open('always.txt', mode='w', encoding='utf8') as alwaysf:
            alwaysf.write('0')
        self.choose_account_form = Choose_account_form()
        self.choose_account_form.show()
        self.close()

    def change_labels(self):
        all_expenses = sum([sum(i[1:]) for i in self.cur.execute(f"SELECT * FROM {self.main_table}").fetchall()])
        all_income = sum([i[0] for i in self.cur.execute(f"SELECT income FROM {self.income_table}").fetchall()])
        self.expenses_per_month.setText(f'Расходы за месяц: {all_expenses}')
        self.income_per_month.setText(f'Доходы за месяц: {all_income}')
        self.total.setText(f'Итог: {"+" if all_income - all_expenses > 0 else ""}{all_income - all_expenses}')
        self.income_per_day.setText(
            f'''Доход за {self.day} {self.month}: {self.cur.execute(f"""SELECT income FROM {self.income_table} 
                                                                    WHERE id = {self.day}""").fetchall()[0][0]}''')

    def add_day_buttons(self, amount_of_days):  # Добавление кнопок над графиком №1
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        for num in range(1, amount_of_days + 1):
            self.day_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
            self.day_btn.setMinimumSize(QtCore.QSize(0, 50))
            self.day_btn.setMaximumSize(QtCore.QSize(1000, 1000))
            self.day_btn.setText(str(num))
            self.day_btn.clicked.connect(self.show_day_statistics)
            self.horizontalLayout.addWidget(self.day_btn)

    def add_labels(self):  # добавления labels разных цветов около квадратного графика
        self.scrollArea_category_labels.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_category_labels.setWidgetResizable(True)
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        most_spent = self.most_spending_categories_sort()
        for name in most_spent:
            index = most_spent.index(name)
            self.lab = QtWidgets.QLabel(' ' + name)
            self.lab.setMinimumSize(100, 41)
            self.lab.setMaximumSize(16777215, 1000)
            self.lab.setStyleSheet(f'background-color: rgb{self.colors[index]}')
            font = QFont()
            font.setPointSize(11)
            self.lab.setFont(font)
            self.verticalLayout_2.addWidget(self.lab)

    def show_day_statistics(self, day=0):  # Добавление статистики в виде синих labels в scrollarea
        self.scrollarea_day_statistics.setWidgetResizable(True)
        self.scrollarea_day_statistics.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        if day:
            today = day
        else:
            self.day, today = int(self.sender().text()), self.sender().text()
            self.income_per_day.setText(
                f'''Доход за {self.day} {self.month}: {self.cur.execute(f"""SELECT income FROM {self.income_table} 
                                                                        WHERE id = {self.day}""").fetchall()[0][0]}''')
            playsound("button_sound_2.mp3")

        self.day_statistics_label.setText(f"Подробная статистика за {today} {self.month}")
        for name in [tup[1] for tup in self.cur.execute(f"""pragma table_info({self.main_table})""")][1:]:
            spent_money = self.cur.execute(f"""SELECT {name} FROM {self.main_table} WHERE id = {today}""").fetchone()[0]
            self.category_label = QLabel(self.scrollAreaWidgetContents)
            self.category_label.setMinimumSize(QtCore.QSize(0, 50))
            self.category_label.setMaximumSize(QtCore.QSize(16777215, 150))
            self.category_label.setStyleSheet("""background-color: #4CAAFD; font-size: 20px""")
            self.category_label.setText(f" {name}: {spent_money}")
            self.verticalLayout.addWidget(self.category_label)
        self.category_label = QLabel(self.scrollAreaWidgetContents)
        self.category_label.setMinimumSize(QtCore.QSize(0, 50))
        self.category_label.setMaximumSize(QtCore.QSize(16777215, 150))
        self.category_label.setStyleSheet("""background-color: #4CAAFD; font-size: 20px""")
        self.category_label.setText(
            f""" Доход: {self.cur.execute(f'''SELECT income FROM {self.income_table} 
                                                            WHERE id = {self.day}''').fetchall()[0][0]}""")
        self.verticalLayout.addWidget(self.category_label)

    def repaint_graph(self, days, widget, pen_color='yellow', background_color='white', clear=True, width=5):  # График
        if clear:
            widget.clear()
        widget.setBackground(background_color)
        if len(days) != 1:  # Фикс ошибки первого дня месяца
            widget.plot([i for i in range(1, len(days) + 1)], [i for i in days], pen=pg.mkPen(pen_color, width=width))
        else:
            widget.plot([i for i in range(0, len(days) + 1)], [i for i in [0] + days],
                        pen=pg.mkPen(pen_color, width=width))
        if widget == self.widget:
            self.add_day_buttons(len((self.cur.execute(f"""SELECT id FROM {self.main_table}""").fetchall())))

    def most_spending_categories_sort(self):  # Возвращает список категории отсортированных по сумме трат за месяц
        column_names = [tup[1] for tup in self.cur.execute(f"""pragma table_info({self.main_table})""")][1:]
        sp = []
        for name in column_names:
            summ = sum([tup[0] for tup in self.cur.execute(f"""SELECT {name} FROM {self.main_table}""").fetchall()])
            sp.append((name, summ))
        sp = sorted(sp, key=lambda tup: -tup[1])
        return [tup[0] for tup in sp]

    def refill_category_comboBox(self, categories):
        self.category_comboBox.clear()
        self.category_comboBox.addItem('Все')
        self.category_comboBox.addItems(categories)

    def category_comboBox_changed(self):  # Перерисовка графа в зависимости от выбранной категории
        text = self.category_comboBox.currentText()
        if text == 'Все':
            self.widget_2.clear()
            columns = self.most_spending_categories_sort()
            for index, name in enumerate(columns):
                most_spending_sp = [tup[0] for tup in self.cur.execute(f"""SELECT {name}
                                                                                FROM {self.main_table}""").fetchall()]
                self.repaint_graph(most_spending_sp, self.widget_2, clear=False, pen_color=self.colors[index], width=5)
        else:
            if text:
                most_spent = self.most_spending_categories_sort()
                index = most_spent.index(text)

                most_spending_sp = [tup[0] for tup in self.cur.execute(f"""SELECT {text} 
                                                                                FROM {self.main_table}""").fetchall()]
                self.repaint_graph(most_spending_sp, self.widget_2, pen_color=self.colors[index])

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self.pix_label.pixmap())
            qp.begin(self)
            self.draw_square_graph(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_square_graph(self, qp):  # Рисование квадратного графика
        most_spent = self.most_spending_categories_sort()
        amounts = {}
        for name in most_spent:  # Создание словаря: категория: сумма
            if name not in amounts.keys():
                amounts[name] = sum(
                    [i[0] for i in self.cur.execute(f"""SELECT {name} FROM {self.main_table}""").fetchall()])
        all_summ = sum([amounts[name] for name in amounts.keys()])  # Общая сумма
        height = 0
        if all_summ == 0:
            qp.setBrush(QColor(200, 200, 200))
            qp.drawRect(0, height, 100, 500)
        for index, name in enumerate(most_spent):
            if amounts[name] != 0:
                percent = amounts[name] * 100 // all_summ
                length = percent * 500 // 100
                qp.setBrush(QColor(*self.colors[index]))
                qp.drawRect(0, height, 100, length)
                height += length

    def add_summ_to_income(self):  # Добавление дохода
        playsound("button_sound_2.mp3")
        try:
            summ = int(self.incomes_edit.text())
            if summ < 0:
                raise NegativeNumber
            if self.sender().text() == 'Добавить':
                self.cur.execute(f"""UPDATE {self.income_table} SET income = income + {summ} 
                                                                WHERE id = {self.day}""")
            else:
                self.cur.execute(f"""UPDATE {self.income_table} SET income = {summ} 
                                                                WHERE id = {self.day}""")
            self.con.commit()
            self.change_labels()
            self.income_error_label.setText('')
            self.category_label.setText(
                f"""Доход: {self.cur.execute(f'''SELECT income FROM {self.income_table} 
                                                                        WHERE id = {self.day}''').fetchall()[0][0]}""")
            self.incomes_edit.setText('')
            self.repaint_graph(
                [i[0] for i in self.cur.execute(f"""SElECT income FROM {self.income_table}""").fetchall()],
                self.graph_about_income)
        except NegativeNumber:
            self.income_error_label.setText('Вводите положительное число')
        except Exception:
            self.income_error_label.setText('Вводите число')

    def show_last_month(self):  # Открытие окна связанного с прошлым месяцем
        playsound("button_sound_2.mp3")
        if self.show_last_month_button.text() == 'Показать статистику за прошлый месяц':
            self.show_last_month_button.setText('Показать статистику за нынешний месяц')
            self.init_all(main_table='last_month_days')
        elif self.show_last_month_button.text() == 'Показать статистику за нынешний месяц':
            self.show_last_month_button.setText('Показать статистику за прошлый месяц')
            self.init_all(main_table='days')

    def open_add_form(self):
        playsound("button_sound_2.mp3")
        self.add_form = Add_form(self.db, self.most_spending_categories_sort, self.colors, self.main_table, self.month)
        self.add_form.show()
        self.close()

    def open_statistics_for_months_form(self):
        playsound("button_sound_2.mp3")
        self.months_form = Months_form(self.db, self.colors)
        self.months_form.show()
        self.close()


class Add_form(QWidget, Ui_Form):  # форма для редактирования трат и их категории
    def __init__(self, db_name, categories, colors, main_table, month):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.categories, self.colors, self.main_table, self.month = categories, colors, main_table, month
        self.initUI()

    def initUI(self):
        self.back_to_main_window_button.clicked.connect(self.back_to_main_window)
        self.add_button.clicked.connect(self.change_value_of_category)
        self.subtract_button.clicked.connect(self.change_value_of_category)
        self.edit_button.clicked.connect(self.change_value_of_category)
        self.category_remove_button.clicked.connect(self.remove_category)
        self.category_add_button.clicked.connect(self.add_category)
        self.add_buttons()
        self.refill_combobox()
        self.category = self.categories()[0]
        date = f'{self.choose_day_comboBox.currentText()} {self.month}'
        exp = self.cur.execute(f'''SELECT {self.category} FROM {self.main_table}
                                                WHERE id = {self.choose_day_comboBox.currentText()}''').fetchone()[0]
        self.label_show_category.setText(f"""Категория '{self.category}', {date}, Потрачено: {exp}""")
        self.choose_day_comboBox.currentTextChanged.connect(self.select_day)

    def back_to_main_window(self):
        playsound("button_sound_2.mp3")
        self.main_form = MyWidget(colors=self.colors)
        self.main_form.show()
        self.close()

    def refill_combobox(self):
        days = [str(i[0]) for i in self.cur.execute(f"""SELECT id FROM {self.main_table}""").fetchall()][::-1]
        self.choose_day_comboBox.addItems(days)

    def select_category(self):
        playsound("button_sound_2.mp3")
        self.category = self.sender().text()
        date = f'{self.choose_day_comboBox.currentText()} {self.month}'
        exp = self.cur.execute(f'''SELECT {self.category} FROM {self.main_table}
                                                    WHERE id = {self.choose_day_comboBox.currentText()}''').fetchone()[0]
        self.label_show_category.setText(f"""Категория '{self.category}', {date}, Потрачено: {exp}""")
        self.category_remove_button.setText(f'Удалить категорию {self.category}')

    def select_day(self):
        date = f'{self.choose_day_comboBox.currentText()} {self.month}'
        exp = self.cur.execute(f'''SELECT {self.category} FROM {self.main_table}
                                                WHERE id = {self.choose_day_comboBox.currentText()}''').fetchone()[0]
        self.label_show_category.setText(f"""Категория '{self.category}', {date}, Потрачено: {exp}""")

    def add_buttons(self):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        names = self.categories()
        positions = [(i, j) for i in range(len(names)) for j in range(3)]
        for i, tup in enumerate(zip(positions, names)):
            position, name = tup
            self.category_button = QPushButton(name)
            self.category_button.setGeometry(QtCore.QRect(680, 550, 189, 111))
            self.category_button.setMinimumSize(QtCore.QSize(160, 111))
            self.category_button.setMaximumSize(QtCore.QSize(1000, 120))
            self.category_button.setStyleSheet(f'background-color: rgb{self.colors[i]}; '
                                               f'border-radius: 15px; '
                                               f'border: 2px solid #094065')
            self.category_button.clicked.connect(self.select_category)
            self.gridLayout.addWidget(self.category_button, *position)

    def change_value_of_category(self):
        playsound("button_sound_2.mp3")
        if self.sender().text() == 'Добавить':
            symbol = '+'
        elif self.sender().text() == 'Вычесть':
            symbol = '-'
        else:
            symbol = '='
        try:
            day = self.choose_day_comboBox.currentText()
            new_summ = int(self.add_summ_lineedit.text())
            if new_summ < 0:
                self.error_label.setText('Нельзя вводить отрицательное число')
                return
            saved_summ = int(self.cur.execute(f"""SELECT {self.category} 
                                                            FROM {self.main_table} WHERE id = {day}""").fetchone()[0])
            if symbol == '+':
                total = saved_summ + new_summ
            elif symbol == '-':
                total = saved_summ - new_summ
            elif symbol == '=':
                total = new_summ
            if total < 0:
                raise NegativeNumber
            self.cur.execute(f"""UPDATE {self.main_table} SET {self.category} = {total} WHERE id = {day}""")
            self.con.commit()
            self.error_label.setText('')
            self.add_summ_lineedit.setText('')
            date = f'{self.choose_day_comboBox.currentText()} {self.month}'
            exp = self.cur.execute(f'''SELECT {self.category} FROM {self.main_table}
                                                WHERE id = {self.choose_day_comboBox.currentText()}''').fetchone()[0]
            self.label_show_category.setText(f"""Категория '{self.category}', {date}, Потрачено: {exp}""")
        except NegativeNumber:
            self.error_label.setText('Итог: отрицательное число')
        except Exception:
            self.error_label.setText('Введите число')

    def remove_category(self):
        column_names = [tup[1] for tup in self.cur.execute(f"""pragma table_info({self.main_table})""")][1:]
        if len(column_names) == 1:
            self.label_add_category_error.setText('Нельзя удалять последний элемент')
            return
        answer = QMessageBox.question(self, f'Удалить категорию {self.category}?',
                                      f'Вы уверены что хотите удалить категорию {self.category}?\n'
                                      'Удалится вся инфромация за месяц', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer == QMessageBox.No:
            return
        index = column_names.index(self.category) + 1
        column_names.remove(self.category)
        column_names2 = [name + ' INTEGER NOT NULL' for name in column_names]
        self.cur.execute(f"""ALTER TABLE {self.main_table} RENAME TO {self.main_table}_old""")
        self.cur.execute(f"""CREATE TABLE {self.main_table}(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL
        , {', '.join(column_names2)});""")
        for tup in self.cur.execute(f"""SELECT * FROM {self.main_table}_old""").fetchall():
            sp = list(tup)
            del sp[index]
            tup = tuple(sp)
            self.cur.execute(f"""INSERT INTO {self.main_table}({', '.join(['id'] + column_names)}) VALUES{tup}""")
        self.cur.execute(f"""DROP TABLE {self.main_table}_old""")
        self.con.commit()
        self.add_buttons()
        self.category = self.categories()[-1]
        self.select_day()
        self.category_remove_button.setText(f'Удалить категорию {self.category}')

    def add_category(self):
        try:
            name = self.name_of_category_lineedit.text()
            if name == '':
                self.label_add_category_error.setText('Впишите текст')
                return
            elif ' ' in name:
                self.label_add_category_error.setText('Впишите текст без пробелов')
                return
            elif name in self.categories():
                self.label_add_category_error.setText('Категория уже создана')
                return
            elif name.isdigit():
                self.label_add_category_error.setText('Нельзя дать имя только из цифр')
                return
            elif len(name) > 15:
                self.label_add_category_error.setText('Слишком много символов')
                return
            elif name[0].isdigit():
                self.label_add_category_error.setText('Первый символ - буква')
                return
            self.cur.execute(f"""ALTER TABLE {self.main_table} ADD {name} INTEGER""")
            self.cur.execute(f"""UPDATE {self.main_table} SET {name} = 0""")
            self.con.commit()
            self.label_add_category_error.setText('')
            for i in range(len(self.categories()) - len(self.colors)):
                self.colors.append((randint(1, 255), randint(1, 255), randint(1, 255)))
            self.add_buttons()
            self.category = self.categories()[-1]
            self.select_day()
            self.name_of_category_lineedit.clear()
        except Exception:
            self.label_add_category_error.setText('Ошибка')


class Months_form(QWidget, Ui_Form1):  # Форма для отображения информации за прошлые месяцы
    def __init__(self, db_name, colors):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.colors = colors
        self.initUI()

    def initUI(self):
        self.go_back_button.clicked.connect(self.go_back_to_main_window)

        months = [i[0] for i in self.cur.execute("""SELECT id FROM months""").fetchall()]
        self.months = sorted(months, key=lambda x: (int(x.split()[0]), int(x.split()[1])), reverse=True)[1:]
        self.comboBox_choose_month.addItems(self.months)
        self.comboBox_choose_month.currentTextChanged.connect(self.changed_month)

        self.categories = [tup[1] for tup in self.cur.execute(f"""pragma table_info(months)""")][1:]
        self.comboBox_choose_category.addItems(['Сумма', 'Все'])
        self.comboBox_choose_category.addItems(self.categories)
        self.comboBox_choose_category.setCurrentText('Сумма')
        self.comboBox_choose_category.currentTextChanged.connect(self.changed_category_or_year_categories)

        ys = list([i[0].split()[0] for i in self.cur.execute(f"""SELECT id FROM months""").fetchall()])
        years = []
        for year in ys:
            if ys.count(year) >= 2:
                years.append(year)
        self.comboBox_choose_year.addItems(sorted(list(set(years)), reverse=True))
        self.comboBox_choose_year.setCurrentText(years[-1])
        self.comboBox_choose_year.currentTextChanged.connect(self.changed_category_or_year_categories)

        for i in range(len(self.categories) - len(self.colors)):
            self.colors.append((randint(1, 255), randint(1, 255), randint(1, 255)))
        year = self.comboBox_choose_year.currentText()
        self.label_stat_for_categories.setText(f"Статистика по выбранной категории за {year} год")
        self.fill_statistics_per_month(first=True)
        self.repaint_graph(self.graph_categories)
        self.draw_graph_about_incomes()

    def draw_graph_about_incomes(self):
        year = self.comboBox_choose_year.currentText()
        sp = []
        dates_for_graph = []
        for date in self.months:
            if year == date.split()[0]:
                sp.append(date)
                dates_for_graph.append(int(date.split()[1]))
        sp = sorted(sp, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
        sp = sp[::-1]
        incomes = []
        for date in sp:
            income = self.cur.execute(f"""SELECT income FROM incomes_months WHERE id = '{date}'""").fetchone()[0]
            incomes.append(income)
        dates_for_graph, incomes = self.edit_dates_and_numbers(dates_for_graph, incomes)
        self.repaint_graph2(dates_for_graph, incomes, self.graph_incomes)

    def create_category_label(self, summ, color=(255, 220, 0), title='Общие расходы'):
        self.category_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.category_label.setMinimumSize(QtCore.QSize(0, 71))
        self.category_label.setMaximumSize(QtCore.QSize(16777215, 71))
        self.category_label.setStyleSheet(f"""background-color: rgb{color}; font-size: 14px""")
        self.category_label.setText(f" {title}: {summ}")
        self.verticalLayout.addWidget(self.category_label)

    def fill_statistics_per_month(self, first=False):
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)
        if first:
            date = self.months[0]
        else:
            date = self.comboBox_choose_month.currentText()
        info = self.cur.execute(f"SELECT * FROM months WHERE id = '{date}'").fetchall()[0][1:]
        self.create_category_label(sum(info))
        income = self.cur.execute(f"SELECT income FROM incomes_months WHERE id = '{date}'").fetchone()[0]
        self.create_category_label(income, title='Общие Доходы')
        if income - sum(info) > 0:
            summ = '+' + str(income - sum(info))
        else:
            summ = income - sum(info)
        self.create_category_label(summ, title='Итог')

        for index, infik in enumerate(zip(self.categories, info)):
            category, summ = infik
            self.create_category_label(summ, color=self.colors[index], title=category)
        self.label_stat_per_month.setText(f'Статистика за {date}')

    def changed_month(self):
        self.fill_statistics_per_month(first=False)

    def changed_category_or_year_categories(self):
        self.repaint_graph(self.graph_categories)
        year = self.comboBox_choose_year.currentText()
        self.label_stat_for_categories.setText(f"Статистика по выбранной категории за {year} год")
        self.draw_graph_about_incomes()

    def edit_dates_and_numbers(self, dates, numbers):
        numbers_true = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dates_true = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for index, date in enumerate(dates):
            index_of_value = dates_true.index(date)
            num = numbers[index]
            del numbers_true[index_of_value]
            numbers_true.insert(index_of_value, num)
        return dates_true, numbers_true

    def repaint_graph2(self, x, y, widget, pen_color='yellow', background_color='white', clear=True, width=5):
        if clear:
            widget.clear()
        widget.setBackground(background_color)
        if len(x) != 1:
            widget.plot([i for i in x], [i for i in y], pen=pg.mkPen(pen_color, width=width))
        else:
            widget.plot([i for i in x], [i for i in [0] + y],
                        pen=pg.mkPen(pen_color, width=width))

    def repaint_graph(self, widget, pen_color='yellow',
                      background_color='white', clear=True, width=5):
        year = self.comboBox_choose_year.currentText()
        text = self.comboBox_choose_category.currentText()
        sp = []
        dates_for_graph = []
        for date in self.months:
            if year == date.split()[0]:
                sp.append(date)
                dates_for_graph.append(int(date.split()[1]))
        sp = sorted(sp, reverse=True)
        numbers = []
        if text == 'Сумма':
            for date in sp:
                summ = sum(list(self.cur.execute(f"""SELECT * FROM months WHERE id = '{date}'""").fetchall()[0][1:]))
                numbers.append(summ)
            numbers = sorted(numbers, reverse=True)
        elif text == 'Все':
            self.graph_categories.clear()
            sp = sorted(sp, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
            for i, category in enumerate(self.categories):
                index = self.categories.index(category)
                numbers = []
                for date in sp[::-1]:
                    summ = list(self.cur.execute(f"""SELECT * FROM months WHERE id = '{date}'""").fetchall()[0][1:])[
                        index]
                    numbers.append(summ)
                dates_for_graph1, numbers = self.edit_dates_and_numbers(dates_for_graph, numbers)
                self.repaint_graph2(dates_for_graph1, numbers, self.graph_categories,
                                    pen_color=self.colors[i], clear=False)
            return
        elif text != 'Все' and text != 'Сумма':
            index = self.categories.index(text)
            sp = sorted(sp, key=lambda x: (int(x.split()[0]), int(x.split()[1])))
            for date in sp[::-1]:
                summ = list(self.cur.execute(f"""SELECT * FROM months WHERE id = '{date}'""").fetchall()[0][1:])[index]
                numbers.append(summ)
            pen_color = self.colors[index]
        dates_for_graph, numbers = self.edit_dates_and_numbers(dates_for_graph, numbers)
        if clear:
            widget.clear()
        widget.setBackground(background_color)
        if len(dates_for_graph) != 1:
            widget.plot([i for i in dates_for_graph], [i for i in numbers], pen=pg.mkPen(pen_color, width=width))
        else:
            widget.plot([i for i in dates_for_graph], [i for i in [0] + numbers],
                        pen=pg.mkPen(pen_color, width=width))

    def go_back_to_main_window(self):
        playsound("button_sound_2.mp3")
        self.main_form = MyWidget(colors=self.colors)
        self.main_form.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('always.txt', mode='r', encoding='utf8') as file:
        text = file.read().strip()
        if text == '0':
            ex = Choose_account_form()
        else:
            db_name = text
            ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())