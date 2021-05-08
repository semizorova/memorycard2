#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,QGroupBox,QRadioButton,QButtonGroup
from random import shuffle,randint
#создание приложения и главного окна
app = QApplication([])#Создать приложение
main_win = QWidget()#создать 
#создание виджетов главного окна
main_win.setWindowTitle("Memory Card")
text = QLabel('Самый сложный вопрос в мире?')#надпись
btn = QPushButton('Ответить')
RadioGroupBox = QGroupBox("Варианты ответов" )
rbtn_1 = QRadioButton( 'Вариант 1' )
rbtn_2 = QRadioButton( 'Вариант 2' )
rbtn_3 = QRadioButton( 'Вариант 3' )
rbtn_4 = QRadioButton(' Вариант 4' )
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnswerGroupBox = QGroupBox("Результат теста" )
rbtne_1 = QLabel( 'Правильно/Неправильно' )
rbtne_2 = QLabel( 'Правильный ответ' )
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(rbtne_1)
layout_ans4.addWidget(rbtne_2)
#расположение виджетов по лэйаутам
layout_main = QVBoxLayout() 
line1 = QHBoxLayout()#разметка
line2 = QHBoxLayout()
line3 = QHBoxLayout()
#Группа по лэйаутам
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3 =QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox. setLayout (layout_ans1)
AnswerGroupBox. setLayout (layout_ans4)
line1.addWidget(text, alignment = Qt.AlignCenter)
line2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
line2.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
line3.addWidget(btn)
layout_main.addLayout(line1)
layout_main.addLayout(line2)
layout_main.addLayout(line3)
#обработка нажатий на переключатели
def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    btn.setText("Следующий вопрос")
def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    btn.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if btn.text()=="Ответить":
        show_result()
    else:
        show_question()
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2= wrong2
        self.wrong3 = wrong3
answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    rbtne_2.setText(q.right_answer)
    show_question()
q = Question('Импровизация?','ТНТ','СТС','Пятница','Первый')
ask(q)
question_list = []
q1 = Question(
    'Верховный Бог из скандинавской мифологии?','Один',
    'Зевс','Геркулес','Аид')
q2 = Question(
    'Сколько раз земля пройдёт вокруг своей оси за 1440 минут','1',
    '3','5','2')
q3 = Question(
    'Сколько персонажей погибли в саге "Игра Престолов"?','6887',
    '7886','6886','7000')
q4 = Question(
    'Самая длинная клавиша клавиша на клавиатуре?','Space',
    'Enter','Shift','Backspase')
q5 = Question(
    'Фамилия Атоса?','Граф Де Ла Фэр',
    'Барон Дю Валлон',"Шевалье Д'Эрбле",'Констанций Бонасье')
q6 = Question(
    'Сколько клавиш у стандвртного пианино?','88',
    '82',"85",'80')
q7 = Question(
    'Какую страну называют туманным альбионом?','Великобритания',
    'Лондон','Нью-Йорк','США')
q8 = Question(
    'Сколько длится фильм Братьев Люмьер "Прибытие поезда на вокзал Ля-Сьота"?','50',
    '60','120','110')
q9 = Question(
    'Сколько лет Микки Маусу?','92',
    '100','95','90')
q10 = Question(
    'Сколько автомобилей в Японии приходится на 1000 человек в 2020?','649',
    '1000','700','756')    
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)
def show_correct(res):
    rbtne_1.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
def click_ok():
    if btn.text()=="Ответить":
        check_answer()
    else:
        next_question()
def next_question():
    main_win.total += 1
    cur_question = randint(0,len(question_list) - 1)
    ask(question_list[cur_question])
    print('Статистика')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:',main_win.score)
    print('-Рейтинг:',(main_win.score/main_win.total)*100,'%')
btn.clicked.connect(click_ok)
main_win.total = 0 
main_win.score = 0 
#отображение окна приложения
main_win.setLayout(layout_main)
main_win.show()
AnswerGroupBox.hide()
app.exec_()