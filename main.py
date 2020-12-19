import os
import shutil
import sys
# import numpy as np
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QFileDialog
import CHOICE
import CODE
import CREAT
import GANWU
import LAST
import LOGIN
import MUDI
import UP
import WORD
import auto


# 登录界面：用于记录登录者的姓名、学号和班级
class Login(QtWidgets.QMainWindow, LOGIN.Ui_MainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.choice = Choice(self)

    def queding(self):
        stu_name = self.lineEdit.text()
        stu_id = self.lineEdit_2.text()
        stu_class = self.lineEdit_3.text()
        # 保存信息
        with open("stu_message.txt", 'w') as f:
            f.write(stu_name + '\n')
            f.write(stu_id + '\n')
            f.write(stu_class + '\n')
            f.close()
        self.choice.show()  # 选择实验界面
        self.close()


# 实验选择界面
class Choice(QtWidgets.QMainWindow, CHOICE.Ui_MainWindow):
    def __init__(self, last_form):
        super(Choice, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form
        self.index = -1
        self.code = Code(self)

    # 设置下个界面
    def enter(self):
        self.index = self.comboBox.currentIndex()
        self.code.index = self.index
        self.code.label.setText(QtCore.QCoreApplication.translate("MainWindow",
                                                                  "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">实验：" + auto.get_name(
                                                                      self.index) + "</span></p></body></html>"))
        self.code.textEdit.setText('')
        self.code.textBrowser_2.setText('')
        self.code.textBrowser_2.ensureCursorVisible()
        self.code.show()
        self.close()


# 实验界面
class Code(QtWidgets.QMainWindow, CODE.Ui_MainWindow):
    def __init__(self, last_form):
        super(Code, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form
        self.last = Last(self)
        self.mudi = Mudi(self)
        self.ganwu = Ganwu(self)
        self.creat = Creat(self)
        self.up = Up(self)
        self.index = -1
        self.textEdit.setText('')
        self.textBrowser_2.setText('')
        self.textBrowser_2.ensureCursorVisible()
        self.name = 'zhd'

    # 观看教学视频
    def view(self):
        try:
            watch = '.\\视频讲解\\' + auto.get_name(self.index) + '.mp4'
            # print(watch)
            os.system(watch)
        except:
            pass

    # 下载示范代码
    def download(self):

        try:
            n_name = auto.get_mname(self.index)
            with open(n_name, 'r') as f:
                f1 = open('codes1.txt', 'w')
                txt = f.read()
                f1.write(txt)
                f1.close()
                f.close()
            os.system('codes1.txt')
        except:
            pass

    # 创建自定义函数
    def creatcode(self):
        self.creat.index = self.index
        self.creat.name = self.name
        self.creat.textEdit.setText('')
        self.creat.show()
        self.close()

    # 添加实验目的
    def add_mudi(self):
        self.mudi.show()
        self.close()

    # 添加实验感悟
    def add_ganwu(self):
        self.ganwu.show()
        self.close()

    # 添加算法推导
    def suanfa(self):
        file = auto.get_name(self.index) + '.png'
        try:
            os.startfile(file)
        except:
            pass

    # 上传照片
    def upload(self):
        self.up.index = self.index
        self.up.textEdit.setText('')
        self.up.show()

    # 提交并进入下一个界面
    def submit(self):
        # print(self.name)
        try:
            os.remove('./实验代码/' + str(self.name) + '.m')
        except:
            pass
        self.last.index = self.index
        self.last.show()
        self.close()

    # 运行
    def run(self):
        codes = self.textEdit.toPlainText()
        if codes != '':
            with open('./实验代码/temp_code.txt', 'w') as f:
                f.write(codes)
                f.close()
            with open('codes.txt', 'a') as f:
                f.write('实验' + auto.get_name(self.index) + '的调用：\n')
                f.write(codes)
                f.write('\n\n\n')
                f.close()
            os.rename('./实验代码/temp_code.txt', './实验代码/temp_code.m')

            # engine = matlab.engine.start_matlab()
            # engine.temp_code(nargout=0)
            cmd = 'cd 实验代码&&python zhd.py'
            res = os.popen(cmd)
            output_str = res.read()  # 获得输出字符串
            self.textBrowser_2.setText(str(output_str))
            with open('answer.txt', 'a') as f:
                f.write('实验' + auto.get_name(self.index) + ':\n')
                f.write(output_str)
                f.write('\n\n\n')
                f.close()
            os.remove('./实验代码/temp_code.m')
        else:
            pass


# 二级菜单
class Last(QtWidgets.QMainWindow, LAST.Ui_MainWindow):
    def __init__(self, last_form):
        super(Last, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form
        self.index = -1
        self.word = Word(self)

    # 选择其他实验
    def choice(self):
        self.last_form.last_form.show()
        self.close()

    # 生成实验报告
    def toword(self):
        auto.auto_word(self.index)
        self.word.show()
        self.close()


# 查看word实验报告
class Word(QtWidgets.QMainWindow, WORD.Ui_MainWindow):
    def __init__(self, last_form):
        super(Word, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form

    def open(self):
        os.system('Matlab_Experimental_report.doc')

    def reset(self):
        # noinspection PyBroadException
        try:
            os.remove('codes1.txt')
            os.remove('codes.txt')
            os.remove('answer.txt')
            os.remove('stu_message.txt')
            os.remove('ganwu.txt')
            os.remove('mudi.txt')
        except:
            pass
        self.close()


# 实验目的界面
class Mudi(QtWidgets.QMainWindow, MUDI.Ui_MainWindow):
    def __init__(self, last_form):
        super(Mudi, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form
        self.textEdit.setText('')

    def save(self):
        text = self.textEdit.toPlainText()
        # print(text)
        with open('mudi.txt', 'w') as f:
            f.write(text)
            f.close()
        self.last_form.show()
        self.close()


# 创建自定义函数
class Creat(QtWidgets.QMainWindow, CREAT.Ui_MainWindow):
    def __init__(self, last_form):
        super(Creat, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form
        self.textEdit.setText('')
        self.lineEdit.setText('')
        self.index = -1
        self.name = 'zhd'

    def save(self):
        name = self.lineEdit.text()
        if name != '':
            self.name = name
            text = self.textEdit.toPlainText()
            with open('./实验代码/' + str(name) + '.txt', 'w') as f:
                f1 = open('codes.txt', 'a')
                f1.write('实验' + auto.get_name(self.index) + ':\n')
                f1.write(text)
                f1.write('\n\n\n')
                f1.close()
                f.write(text)
                f.close()
            # cmd = 'copy ' + str(name) + '.txt ' + 'codes.txt'
            # os.system(cmd)
            auto.bianyi('./实验代码/' + name)
            self.last_form.name = self.name
            self.last_form.show()
            self.close()
        else:
            self.last_form.show()
            self.close()


# 实验感悟界面
class Ganwu(QtWidgets.QMainWindow, GANWU.Ui_MainWindow):
    def __init__(self, last_form):
        super(Ganwu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.last_form = last_form
        self.textEdit.setText('')

    def save(self):
        text = self.textEdit.toPlainText()
        # print(text)
        with open('ganwu.txt', 'w') as f:
            f.write(text)
            f.close()
        self.last_form.show()
        self.close()


# 上传照片界面
class Up(QtWidgets.QMainWindow, UP.Ui_MainWindow):
    def __init__(self, last_form):
        super(Up, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('数值分析实验教学系统')
        self.last_form= last_form
        self.setWindowIcon(QIcon('./image/title.jpg'))
        self.textEdit.setAcceptDrops(True)
        self.index = -1

    def con(self):
        # self.textEdit.textChanged.connect(self.editchange)
        try:
            if 0 == self.textEdit.toPlainText().find('file:///'):
                self.textEdit.setText(self.textEdit.toPlainText().replace('file:///', ''))
            a = self.textEdit.toPlainText()
        except:
            pass
        try:
            os.remove(auto.get_name(self.index) + '.png')
        except:
            pass
        try:
            b = auto.get_name(self.index) + '.png'
            shutil.copy(a, b)
        except:
            pass
        self.close()


'''
    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '')
        print(openfile_name[0])
'''

# 开始
if __name__ == '__main__':
    auto.init()
    app = QtWidgets.QApplication(sys.argv)
    ui = Login()
    ui.show()
    sys.exit(app.exec_())
