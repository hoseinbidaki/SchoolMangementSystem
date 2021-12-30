from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
import sys
import json


def printMessWitherr(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(text)
    msg.setWindowTitle("خطا")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QtGui.QIcon("icon.png"))
    msg.exec_()


def printMesswithinf(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setWindowTitle("پیام سیستم")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setWindowIcon(QtGui.QIcon("icon.png"))
    msg.exec_()

def loadData():
    file = open("Data/users.json", "r")
    users = json.load(file)
    file.close()
    return users

def clearInBox(dist):
    try:
        file = open("Data/messages.json", "r")
        users = json.load(file)
        file.close()
        ans = users[dist]
        users[dist] = []
        file = open("Data/messages.json", "w")
        json.dump(users, file)
        file.close()
        return ans
    except:
        return {}
def loadMessageTo(dist):
    try:
        file = open("Data/messages.json", "r")
        users = json.load(file)
        file.close()
        ans = users[dist]
        return ans
    except:
        return {}
def loadClass():
    file = open("Data/classes.json", "r")
    classes = json.load(file)
    file.close()
    return classes

def saveClass(data):
    file = open("Data/classes.json", "w")
    json.dump(data, file)
    file.close()

def saveMessage(data):
    file = open("Data/messages.json", "w")
    json.dump(data, file)
    file.close()
def loadMessage():
    file = open("Data/messages.json", "r")
    mess = json.load(file)
    file.close()
    return mess

def saveData(data):
    file = open("Data/users.json", "w")
    json.dump(data, file)
    file.close()

def exitbtn():
    ex = Exit()
    ex.setModal(True)
    ex.setWindowIcon(QtGui.QIcon("icon.png"))
    ex.setWindowTitle('پیام سیستم')
    ex.exec_()

def classlistbtn():
    cl = ClassList()
    cl.setModal(True)
    cl.setWindowIcon(QtGui.QIcon("icon.png"))
    cl.setWindowTitle('کلاس ها')
    cl.exec_()
def loadStudent():
    users = loadData()
    ans = {}
    for a, b in users.items():
        if b['role'] == 'student':
            ans[a] = b
    return ans
def addclassbtn():
    ac = addClass()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('افزودن کلاس')
    ac.exec_()
def addStudentToClassbtn():
    ac = addStudentToClass()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('افزودن دانش آموز به کلاس')
    ac.exec_()
def StudentInClassViewbtn():
    ac = StudentInClassView()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('دانش آموزان کلاس')
    ac.exec_()

def TeacherClassListbtn():
    ac = TeacherClassList()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle(' کلاس ها')
    ac.exec_()
def TeacherStudentInClassbtn():
    ac = TeacherStudentInClass()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('دانش آموزان کلاس')
    ac.exec_()
def GivingGradebtn():
    ac = GivingGrade()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('نمره دهی به دانش آموزان')
    ac.exec_()
def StudentCoursesbtn():
    ac = StudentCourses()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('دروس')
    ac.exec_()
def savecuruser(txt):
    file = open("Data/courent.txt", "w")
    file.write(txt)
    file.close()
def curUser():
    file = open("Data/courent.txt", "r")
    ans = file.readline()
    file.close()
    return ans

def DeputyListbtn():
    ac = DeputyList()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('مدیریت معاونین')
    ac.exec_()
def MessgeBox():
    ac = Messages()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('پیام ها')
    ac.exec_()
def NewMessbtn():
    ac = NewMessage()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('نوشتن یک پیام')
    ac.exec_()
def Evaluationbtn():
    ac = Evaluation()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('ارزیابی')
    ac.exec_()

def saveEva(data):
    file = open("Data/eva.json", "w")
    json.dump(data, file)
    file.close()
def loadEva():
    file = open("Data/eva.json", "r")
    eva = json.load(file)
    file.close()
    return eva
def ResEvabtn():
    ac = ResEva()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('نتایج ارزیابی')
    ac.exec_()

def EditStudentbtn():
    ac = EditStudent()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('ویرایش دانش آموز')
    ac.exec_()

def EditDeputybtn():
    ac = EditDeputy()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('ویرایش معاون')
    ac.exec_()

def EditSTeacherbtn():
    ac = EditTeacher()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('ویرایش معلم')
    ac.exec_()
def member():
    ac = Members()
    ac.setModal(True)
    ac.setWindowIcon(QtGui.QIcon("icon.png"))
    ac.setWindowTitle('اعضا')
    ac.exec_()

#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------

class Members(QDialog):
    def __init__(self):
        super(Members, self).__init__()
        loadUi("UI Files/members.ui", self)
        self.back.clicked.connect(self.close)
        self.loadData()
    def loadData(self):
        users = loadData()
        row = 0
        size = len(users)
        self.table.setRowCount(size)
        for key, val in users.items():
            if val['role'] == 'admin':
                continue
            str = val['name'] + ' ' + val['family']
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(key))
            role = val['role']
            str = 'معاون'
            if role == 'admin':
                str = 'مدیر'
            elif role == 'teacher':
                str = 'معلم'
            elif role == 'student':
                str = 'دانش آموز'
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str))
            row = row + 1
class EditStudent(QDialog):
    def __init__(self):
        super(EditStudent, self).__init__()
        loadUi("UI Files/editstudent.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.subbtn)
        self.rem.clicked.connect(self.rembtn)
    def rembtn(self):
        if self.code.text() == '':
            printMessWitherr('لطفا کد ملی را وارد نمایید')
            return
        users = loadData()
        dict = {}
        for key, val in users.items():
            if key == self.code.text():
                continue
            dict[key] = val
        saveData(dict)
        printMesswithinf('کاربر با موفقیت حذف شد')
        self.close()
    def subbtn(self):
        data = {
            'name': self.name.text(),
            'family': self.family.text(),
            'dad': self.dad.text(),
            'code': self.code.text(),
            'date': self.date.text(),
            'password': self.password.text(),
            'role': 'student'
        }
        for a, b in data.items():
            if b == '':
                printMessWitherr('لطفا فیلد هارا کامل نمایید!')
                return
        users = loadData()
        users[data['code']] = data
        saveData(users)
        text = 'دانش آموز با موفقیت ویرایش شد!\n'
        text += 'نام کاربری: ' + data['code']
        text += '\n'
        text += 'کلمه عبور: ' + data['password']
        printMesswithinf(text)
        self.close()


class EditDeputy(QDialog):
    def __init__(self):
        super(EditDeputy, self).__init__()
        loadUi("UI Files/editDeputy.ui", self)
        self.rem.clicked.connect(self.rembtn)
        self.submit.clicked.connect(self.subbtn)
        self.back.clicked.connect(self.close)
    def subbtn(self):

        name = self.name.text()
        family = self.family.text()
        date = self.date.text()
        code = self.code.text()
        duty = self.duty.text()
        password = self.password.text()
        data = {
            'name' : name,
            'family':family,
            'date' : date,
            'code' : code,
            'duty' : duty,
            'password' : password,
            'role' : "deputy"
        }
        for i in data.values():
            if i == '':
                printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید!')
                return
        users = loadData()
        users[code] = data
        saveData(users)
        printMesswithinf('معاون با موفقیت ویرایش شد')
        self.close()
    def rembtn(self):
        if self.code.text() == '':
            printMessWitherr('لطفا کد ملی را وارد نمایید')
            return
        users = loadData()
        dict = {}
        for key, val in users.items():
            if key == self.code.text():
                continue
            dict[key] = val
        saveData(dict)
        printMesswithinf('کاربر با موفقیت حذف شد')
        self.close()

class EditTeacher(QDialog):
    def __init__(self):
        super(EditTeacher, self).__init__()
        loadUi("UI Files/editTeacher.ui", self)
        self.back.clicked.connect(self.close)
        self.rem.clicked.connect(self.rembtn)
        self.submit.clicked.connect(self.subbtn)
    def subbtn(self):
        data = {
            "name": self.name.text(),
            "family": self.family.text(),
            "birthday": self.date.text(),
            "code": self.code.text(),
            "course": self.course.text(),
            "password": self.password.text(),
            "role": "teacher"
        }
        for i in data.values():
            if i == '':
                printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید')
                return
        username = data['code']
        file = open("Data/users.json", "r")
        users = json.load(file)
        file.close()

        dbfile = open("Data/users.json", "r+")
        users[username] = data
        json.dump(users, dbfile)
        text = 'دبیر با موفقیت ویرایش شد!\n'
        text += 'نام کاربری: ' + username
        text += '\n'
        text +=  'کلمه عبور: ' + data['password']
        printMesswithinf(text)
        self.close()
    def rembtn(self):
        if self.code.text() == '':
            printMessWitherr('لطفا کد ملی را وارد نمایید')
            return
        users = loadData()
        dict = {}
        for key, val in users.items():
            if key == self.code.text():
                continue
            dict[key] = val
        saveData(dict)
        printMesswithinf('کاربر با موفقیت حذف شد')
        self.close()
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------
#-----------------------------------------------------

class ResEva(QDialog):
    def __init__(self):
        super(ResEva, self).__init__()
        loadUi("UI Files/evaluation_result.ui", self)
        self.back.clicked.connect(self.close)
        self.loadData()
    def loadData(self):
        eva = loadEva()
        try:
            res = eva[curUser()]
        except:
            printMessWitherr('کسی ارزیابی انجام نداده است')
            return
        list = []
        for i in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']:
            a = 0
            b = 0
            for s in res:
                if i == 'q6':
                    if s['eva'][i] == 'majazi':
                        b += 1
                    else:
                        a += 1
                else:
                    if s['eva'][i] == 'yes':
                        a += 1
                    else:
                        b += 1
            list.append({'yes' : a, 'no':b})
        print('here')
        a = 0
        b = 0
        c = 0
        for s in res:
            if s['eva']['q7'] == 'low':
                a += 1
            elif s['eva']['q7'] == 'high':
                c += 1
            else:
                b += 1

        self.high.setText(str(c))
        self.med.setText(str(b))
        self.low.setText(str(a))

        a = list[0]['yes']
        b = list[0]['no']
        self.yes1.setText(str(a))
        self.no1.setText(str(b))

        a = list[1]['yes']
        b = list[1]['no']
        self.yes2.setText(str(a))
        self.no2.setText(str(b))

        a = list[2]['yes']
        b = list[2]['no']
        self.yes3.setText(str(a))
        self.no3.setText(str(b))

        a = list[3]['yes']
        b = list[3]['no']
        self.yes4.setText(str(a))
        self.no4.setText(str(b))

        a = list[4]['yes']
        b = list[4]['no']
        self.yes5.setText(str(a))
        self.no5.setText(str(b))

class Evaluation(QDialog):
    def __init__(self):
        super(Evaluation, self).__init__()
        loadUi("UI Files/evaluation.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.submitbtn)
    def submitbtn(self):
        code = self.code.text()
        users = loadData()
        if code not in users:
            printMessWitherr('دبیر یافت نشد')
            return
        classes = loadClass()
        have = []
        for a, b in classes.items():
            if curUser() in b['students']:
                have.append(b['code'])
        if code not in have:
            printMessWitherr('شما مجاز به ارزیابی این دبیر نیستید!')
            return
        eva = loadEva()
        try:
            for teacher in eva[code]:
                if teacher['from'] == curUser():
                    printMessWitherr('شما قبلا ارزیابی را انجام داده اید!')
                    return
        except:
            pass
        data = {}
        if self.yes1.isChecked():
            data['q1'] = 'yes'
        else:
            data['q1'] = 'no'

        if self.yes2.isChecked():
            data['q2'] = 'yes'
        else:
            data['q2'] = 'no'

        if self.yes3.isChecked():
            data['q3'] = 'yes'
        else:
            data['q3'] = 'no'

        if self.yes4.isChecked():
            data['q4'] = 'yes'
        else:
            data['q4'] = 'no'

        if self.yes5.isChecked():
            data['q5'] = 'yes'
        else:
            data['q5'] = 'no'

        if self.majazi.isChecked():
            data['q6'] = 'majazi'
        else:
            data['q6'] = 'hozori'

        if self.low.isChecked():
            data['q7'] = 'low'
        elif self.medium.isChecked():
            data['q7'] = 'medium'
        else:
            data['q7'] = 'high'

        done = False
        try:
            if len(eva[code]) >= 0:
                done = True
                eva[code].append({'from' : curUser(), 'eva' : data})
        except:
            done = True
            eva[code] = [{'from' : curUser(), 'eva' : data}]
        if done ^ 1:
            eva[code] = [{'from': curUser(), 'eva': data}]
        saveEva(eva)
        printMesswithinf('با موفقیت ارزیابی شما انجام شد')
        self.close()
class NewMessage(QDialog):
    def __init__(self):
        super(NewMessage, self).__init__()
        loadUi("UI Files/newmess.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.submitbtn)
        self.member.clicked.connect(member)
    def submitbtn(self):
        rec = self.rec.text()
        text = self.TXT.toPlainText()
        if rec == '' or text == '':
            printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید')
            return
        users = loadData()
        if rec not in users:
            printMessWitherr('گیرنده یافت نشد!')
            return
        mess = loadMessage()
        MESS = {
            'from' : curUser(),
            'text': text
        }
        done = False
        try:
            if len(mess[rec]) >= 0:
                mess[rec].append(MESS)
                done = True
        except:
            mess[rec] = [MESS]
            done = True
        if done ^ 1:
            mess[rec] = [MESS]

        saveMessage(mess)
        printMesswithinf('پیام با موفقیت ارسال شد')
        self.close()
class Messages(QDialog):
    def __init__(self):
        super(Messages, self).__init__()
        loadUi("UI Files/message.ui", self)
        self.table.setColumnWidth(1, 550)
        self.back.clicked.connect(self.close)
        self.newm.clicked.connect(NewMessbtn)
        self.rem.clicked.connect(self.remo)
        self.rem.clicked.connect(self.loadData)
        self.loadData()
    def remo(self):
        clearInBox(curUser())
        printMesswithinf('با موفقیت پیام ها پاک شدند')
    def loadData(self):
        mess = loadMessageTo(curUser())
        row = 0
        size = len(mess)
        users = loadData()
        self.table.setRowCount(size)
        for message in mess:
            str = users[message['from']]['name'] + ' ' + users[message['from']]['family']
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(message['text']))
            row = row + 1
class DeputyPanel(QDialog):
    def __init__(self):
        super(DeputyPanel, self).__init__()
        loadUi("UI Files/deputy_panel.ui", self)
        self.exit.clicked.connect(exitbtn)
        self.message.clicked.connect(MessgeBox)
        self.student.clicked.connect(self.studentbtn)
        txt = 'کاربر: '
        users = loadData()
        txt += users[curUser()]['name'] + ' ' + users[curUser()]['family']
        self.user.setText(txt)
    def studentbtn(self):
        sl = StudentList()
        sl.setModal(True)
        sl.setWindowIcon(QtGui.QIcon("icon.png"))
        sl.setWindowTitle('مدیریت دانش آموزان')
        sl.exec_()
    def student(self):
        ac = StudentList()
        ac.setModal(True)
        ac.setWindowIcon(QtGui.QIcon("icon.png"))
        ac.setWindowTitle('مدیریت دانش آموزان')
class AddDeouty(QDialog):
    def __init__(self):
        super(AddDeouty, self).__init__()
        loadUi("UI Files/addDeputy.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.submitbtn)
    def submitbtn(self):
        name = self.name.text()
        family = self.family.text()
        date = self.date.text()
        code = self.code.text()
        duty = self.duty.text()
        password = self.password.text()
        data = {
            'name' : name,
            'family':family,
            'date' : date,
            'code' : code,
            'duty' : duty,
            'password' : password,
            'role' : "deputy"
        }
        for i in data.values():
            if i == '':
                printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید!')
                return
        users = loadData()
        if code in users:
            printMessWitherr('این کاربر قبلا ثبت شده است!')
            return
        users[code] = data
        saveData(users)
        printMesswithinf('معاون با موفقیت اضافه شد')
        self.close()
class DeputyList(QDialog):
    def __init__(self):
        super(DeputyList, self).__init__()
        loadUi("UI Files/DeputyList.ui", self)
        self.back.clicked.connect(self.close)
        self.add.clicked.connect(self.addbtn)
        self.add.clicked.connect(self.loadData)
        self.edit.clicked.connect(EditDeputybtn)
        self.edit.clicked.connect(loadData)
        self.loadData()
    def addbtn(self):
        ac = AddDeouty()
        ac.setModal(True)
        ac.setWindowIcon(QtGui.QIcon("icon.png"))
        ac.setWindowTitle('اضافه کردن معاون')
        ac.exec_()
    def loadData(self):
        users = loadData()
        deputy = {}
        for a, b in users.items():
            if b['role'] == 'deputy':
                deputy[a] = b
        row = 0
        size = len(deputy)
        self.table.setRowCount(size)
        user = loadData()
        for key, val in deputy.items():
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(user[key]['name']))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(user[key]['family']))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(user[key]['date']))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(user[key]['code']))
            self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(user[key]['duty']))
            row = row + 1
class StudentCourses(QDialog):
    def __init__(self):
        super(StudentCourses, self).__init__()
        loadUi("UI Files/courses.ui", self)
        self.back.clicked.connect(self.close)
        self.eva.clicked.connect(Evaluationbtn)
        self.loadData()
    def loadData(self):
        classes = loadClass()
        have = {}
        for a, b in classes.items():
            if curUser() in b['students']:
                have[a] = b
        size = len(have)
        if size == 0:
            return
        self.table.setRowCount(size)
        row = 0
        user = loadData()
        can = True
        sum = 0
        units = 0
        for id, course in have.items():
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(course['unit']))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(course['course']))
            code_meli_teacher = course['code']
            txt = user[code_meli_teacher]['name'] + ' ' + user[code_meli_teacher]['family']
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(txt))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(code_meli_teacher))
            self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(id))
            self.table.setItem(row, 5, QtWidgets.QTableWidgetItem(classes[id]['grade'][curUser()]))
            row = row + 1
            if can:
                try:
                    sum += float(classes[id]['grade'][curUser()]) * int(course['unit'])
                    units += int(course['unit'])
                except :
                    can = False
        if can:
            txt = 'معدل: '
            txt += str(sum / units)
            txt += ' '
            txt += 'تعداد واحد ها: '
            txt += str(units)
            self.ave.setText(txt)
class StudentPanel(QDialog):
    def __init__(self):
        super(StudentPanel, self).__init__()
        loadUi("UI Files/student_panel.ui", self)
        self.course.clicked.connect(StudentCoursesbtn)
        self.exit.clicked.connect(exitbtn)
        self.mess.clicked.connect(MessgeBox)
        self.setUser()
    def setUser(self):
        users = loadData()
        str = 'کاربر: '
        str += users[curUser()]['name'] + ' ' + users[curUser()]['family']
        self.user.setText(str)
class GivingGrade(QDialog):
    def __init__(self):
        super(GivingGrade, self).__init__()
        loadUi("UI Files/giving_grade.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.submitbtn)
    def submitbtn(self):
        code = self.code.text()
        g = self.g.text()
        id = self.id.text()
        g = float(g)
        if code == '' or g == '' or id == '':
            printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید!')
            return
        students = loadStudent()
        classes = loadClass()
        if code not in students:
            printMessWitherr('دانش آموز یافت نشد!')
            return
        if id not in classes:
            printMessWitherr('کلاس یاقت نشد')
            return
        if classes[id]['code'] != curUser() :
            printMessWitherr('شما مجاز به این عملیات نیستید!')
            return
        if g < 0 or g > 20:
            printMessWitherr('نمره در بازه 0 تا 20 باید باشد')
            return
        g = str(g)
        classes[id]['grade'][code] = g
        txt = 'نمره '
        txt += g
        txt += ' برای درس '
        txt += classes[id]['course']
        txt += ' برای '
        txt += students[code]['name'] + ' ' + students[code]['family']
        txt += ' ثبت شد!'
        saveClass(classes)
        printMesswithinf(txt)
        self.close()

class TeacherStudentInClass(QDialog):
    def __init__(self):
        super(TeacherStudentInClass, self).__init__()
        loadUi("UI Files/teacher_student_in_class.ui", self)
        self.back.clicked.connect(self.close)
        self.view.clicked.connect(self.viewbtn)
        self.grade.clicked.connect(GivingGradebtn)
        self.grade.clicked.connect(self.viewbtn)
    def viewbtn(self):
        id = self.id.text()
        if id == '':
            printMessWitherr('لطفا کد کلاس را وارد نمایید')
            return
        classes = loadClass()
        if id not in classes:
            printMessWitherr('کلاس یافت نشد!')
            return
        if classes[id]['code'] != curUser():
            printMessWitherr('شما مجاز به مشاهده این کلاس نیستید!')
            return
        user = loadData()
        row = 0
        size = len(classes[id]['students'])
        self.student_table.setRowCount(size)
        for student in classes[id]['students']:

            self.student_table.setItem(row, 0, QtWidgets.QTableWidgetItem(user[student]['name'] + ' ' + user[student]['family']))
            self.student_table.setItem(row, 1, QtWidgets.QTableWidgetItem(user[student]['code']))
            code_meli_teacher = classes[id]['code']
            str = user[code_meli_teacher]['name'] + ' ' + user[code_meli_teacher]['family']
            self.student_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str))
            self.student_table.setItem(row, 3, QtWidgets.QTableWidgetItem(classes[id]['course']))
            self.student_table.setItem(row, 4, QtWidgets.QTableWidgetItem(id))
            try:
                gr = classes[id]['grade'][student]
            except:
                gr = '-'
            self.student_table.setItem(row, 5, QtWidgets.QTableWidgetItem(gr))
            row = row + 1
class TeacherClassList(QDialog):
    def __init__(self):
        super(TeacherClassList, self).__init__()
        loadUi("UI Files/teacher_class_list.ui", self)
        self.back.clicked.connect(self.close)
        self.view.clicked.connect(TeacherStudentInClassbtn)
        self.loadData()
    def loadData(self):
        classes = loadClass()
        row = 0
        size = 0
        for a, b in classes.items():
            if b['code'] == curUser():
                size = size + 1
        self.class_table.setRowCount(size)
        for code, inf in classes.items():
            if inf['code'] != curUser():
                continue
            self.class_table.setItem(row, 0, QtWidgets.QTableWidgetItem(inf['id']))
            self.class_table.setItem(row, 1, QtWidgets.QTableWidgetItem(inf['course']))
            self.class_table.setItem(row, 2, QtWidgets.QTableWidgetItem(inf['date']))
            self.class_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(len(inf['students']))))
            row = row + 1
class StudentInClassView(QDialog):
    def __init__(self):
        super(StudentInClassView, self).__init__()
        loadUi("UI Files/student_class_view.ui", self)
        self.back.clicked.connect(self.close)
        self.view.clicked.connect(self.viewbtn)
    def viewbtn(self):
        id = self.id.text()
        classes = loadClass()
        if id not in classes:
            printMessWitherr('کلاس یافت نشد!')
            return
        row = 0
        size = len(classes[id]['students'])
        self.student_table.setRowCount(size)
        user = loadData()
        for student in classes[id]['students']:
            self.student_table.setItem(row, 0, QtWidgets.QTableWidgetItem(user[student]['name']))
            self.student_table.setItem(row, 1, QtWidgets.QTableWidgetItem(user[student]['family']))
            code_meli_teacher = classes[id]['code']
            str = user[code_meli_teacher]['name'] + ' ' + user[code_meli_teacher]['family']
            self.student_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str))
            self.student_table.setItem(row, 3, QtWidgets.QTableWidgetItem(classes[id]['course']))
            self.student_table.setItem(row, 4, QtWidgets.QTableWidgetItem(i))
            row = row + 1
class addStudentToClass(QDialog):
    def __init__(self):
        super(addStudentToClass, self).__init__()
        loadUi("UI Files/add_student_to_class.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.submitbtn)
        self.loadData()
    def submitbtn(self):
        code = self.code.text()
        id = self.id.text()
        if code == '' or id == '':
            printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید!')
            return
        classes = loadClass()
        if id not in classes:
            printMessWitherr('کلاس یافت نشد!')
            return
        students = loadStudent()
        if code not in students:
            printMessWitherr('دانش آموز یافت نشد!')
            return
        for i in classes[id]['students']:
            if i == code:
                printMessWitherr('این دانش آموز قبلا اضافه شده است!')
                return
        classes[id]['students'].append(code)
        classes[id]['grade'][code] = '-'
        saveClass(classes)
        printMesswithinf('دانش آموز با موفقیت به کلاس اضافه شد.')
        self.close()
    def loadData(self):
        users = loadData()
        row = 0
        size = 0
        for name, user in users.items():
            if user['role'] == 'student':
                size = size + 1
        self.student_table.setRowCount(size)
        for name, user in users.items():
            if user['role'] != 'student':
                continue
            self.student_table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['name']))
            self.student_table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['family']))
            self.student_table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['dad']))
            self.student_table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['code']))
            self.student_table.setItem(row, 4, QtWidgets.QTableWidgetItem(user['date']))
            row = row + 1
class addClass(QDialog):
    def __init__(self):
        super(addClass, self).__init__()
        loadUi("UI Files/add_class.ui", self)
        self.back.clicked.connect(self.close)
        self.submit.clicked.connect(self.addclasssubbtn)
    def addclasssubbtn(self):
        classes = loadClass()
        newclass = {
            'code':self.code.text(),
            'id':self.id.text(),
            'course': '$',
            'date':self.date.text(),
            'unit' : self.unit.text(),
            'students':[],
            'grade':{}
        }
        for j, i in newclass.items():
            if i == '':
                printMessWitherr('لطفا تمامی فیلد هارا کامل نمایید!')
                return
        code = self.code.text()
        users = loadData()
        find = False
        for user, val in users.items():
            if val['role'] == 'teacher':
                if val['code'] == code:
                    find = True
                    break
        if find ^ 1:
            printMessWitherr('دبیر یافت نشد!')
            return
        if self.id.text() in classes:
            printMessWitherr('این کد کلاس قبلا ثبت شده است!')
            return
        newclass['course'] = users[code]['course']
        classes[self.id.text()] = newclass
        saveClass(classes)
        txt = 'کلاس با موفقیت ایجاد شد.'
        printMesswithinf(txt)
        self.close()
class ClassList(QDialog) :
    def __init__(self):
        super(ClassList, self).__init__()
        loadUi("UI Files/class_list.ui", self)
        self.return_2.clicked.connect(self.close)
        self.add_class.clicked.connect(addclassbtn)
        self.add_class.clicked.connect(self.loadtable)
        self.addsc.clicked.connect(addStudentToClassbtn)
        self.view.clicked.connect(StudentInClassViewbtn)
        self.loadtable()
    def loadtable(self):
        classes = loadClass()
        row = 0
        size = len(classes)
        users = loadData()
        self.class_table.setRowCount(size)
        self.class_table.setColumnWidth(2, 150)
        self.class_table.setColumnWidth(0, 70)
        for code, inf in classes.items():
            teachername = users[inf['code']]['name']
            teachername += ' '
            teachername += users[inf['code']]['family']
            self.class_table.setItem(row, 0, QtWidgets.QTableWidgetItem(inf['unit']))
            self.class_table.setItem(row, 2, QtWidgets.QTableWidgetItem(teachername))
            self.class_table.setItem(row, 3, QtWidgets.QTableWidgetItem(inf['code']))
            self.class_table.setItem(row, 1, QtWidgets.QTableWidgetItem(inf['id']))
            self.class_table.setItem(row, 4, QtWidgets.QTableWidgetItem(inf['course']))
            self.class_table.setItem(row, 5, QtWidgets.QTableWidgetItem(inf['date']))
            row = row + 1


'''
 
class Class:
    teacher = ''
    students = []
    ClassID = int
    course = ''
    date = ''
    def __init__(self, teacher, id, course, date):
        self.teacher = teacher
        self.ClassID = id
        self.course = course
        self.date = date
    def addStudent(self, studen):
        self.students.append(studen)
'''


class addStudent(QDialog):
    def __init__(self):
        super(addStudent, self).__init__()
        loadUi("UI Files/addstudent.ui", self)
        self.closebtn.clicked.connect(self.close)
        self.submit.clicked.connect(self.subbtn)
    def subbtn(self):
        data = {
            'name':self.name.text(),
            'family' : self.family.text(),
            'dad':self.dad.text(),
            'code': self.code.text(),
            'date':self.date.text(),
            'password' : self.password.text(),
            'role': 'student'
        }
        for a, b in data.items():
            if b == '':
                printMessWitherr('لطفا فیلد هارا کامل نمایید!')
                return
        users = loadData()
        if data['code'] in users:
            printMessWitherr('این کد ملی قبلا ثبت شده است!')
            return
        users[data['code']] = data
        saveData(users)
        text = 'دانش آموز با موفقیت اضافه شد!\n'
        text += 'نام کاربری: ' + data['code']
        text += '\n'
        text +=  'کلمه عبور: ' + data['password']
        printMesswithinf(text)
        self.close()
class TeacherPanel(QDialog):
    def __init__(self):
        super(TeacherPanel, self).__init__()
        loadUi("UI Files/teacher_panel.ui", self)
        self.exit.clicked.connect(exitbtn)
        self.classes.clicked.connect(TeacherClassListbtn)
        self.evaluation_result.clicked.connect(ResEvabtn)
        self.mess.clicked.connect(MessgeBox)
        users = loadData()
        txt = 'کاربر: ' + users[curUser()]['name'] + ' ' + users[curUser()]['family']
        self.user.setText(txt)

class Exit(QDialog):
    def __init__(self):
        super(Exit, self).__init__()
        loadUi("UI Files/exit.ui", self)
        self.yes.clicked.connect(exit)
        self.no.clicked.connect(self.btnno)
    def btnno(self):
        self.close()

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("UI Files/login_form.ui", self)
        self.submit.clicked.connect(self.SubmitButton)
        #self.submit.clicked.connect(self.gotoTeacherPanel)
        #self.submit.clicked.connect(self.gotoAdminPanel)
        #self.submit.clicked.connect(self.gotoStudentPanel)
        self.exit.clicked.connect(exitbtn)


    def SubmitButton(self):
        user = self.username.text()
        password = self.password.text()
        file = open("Data/users.json", "r")
        users = json.load(file)
        if users == '' or password == '':
            printMessWitherr('لطفا فیلد ها را کامل نمایید!')
        elif user not in users:
            printMessWitherr('نام کاربری یا رمز عبور صحیح نیست!')
        elif users[user]['password'] != password:
            printMessWitherr('نام کاربری یا رمز عبور صحیح نیست!')
        else:
            Role = users[user]['role']
            printMesswithinf('با موفقیت وارد شدید!')
            if Role == 'admin':
                savecuruser(user)
                self.gotoAdminPanel()
            elif Role == 'teacher':
                savecuruser(user)
                self.gotoTeacherPanel()
            elif Role == 'deputy':
                savecuruser(user)
                self.gotoDeoutyPanel()
            else:
                savecuruser(user)
                self.gotoStudentPanel()

    def gotoAdminPanel(self):
        adminpanel = AdminPanel()
        wid.setFixedWidth(543)
        wid.setFixedHeight(268)
        wid.addWidget(adminpanel)
        wid.setWindowTitle('پنل مدیر')
        wid.setCurrentIndex(wid.currentIndex() + 1)

    def gotoTeacherPanel(self):
        tp = TeacherPanel()
        wid.setFixedWidth(491)
        wid.setFixedHeight(289)
        wid.addWidget(tp)
        wid.setWindowTitle('پنل دبیر')
        wid.setCurrentIndex(wid.currentIndex() + 1)
    def gotoStudentPanel(self):
        tp = StudentPanel()
        wid.setFixedWidth(397)
        wid.setFixedHeight(228)
        wid.addWidget(tp)
        wid.setWindowTitle('پنل دانش آموز')
        wid.setCurrentIndex(wid.currentIndex() + 1)
    def gotoDeoutyPanel(self):
        tp = DeputyPanel()
        wid.setFixedWidth(420)
        wid.setFixedHeight(264)
        wid.addWidget(tp)
        wid.setWindowTitle('پنل معاون')
        wid.setCurrentIndex(wid.currentIndex() + 1)
class AdminPanel(QDialog):
    def __init__(self):
        super(AdminPanel, self).__init__()
        loadUi("UI Files/admin_panel.ui", self)
        self.exit.clicked.connect(exitbtn)
        self.Teachers.clicked.connect(self.teachersbtn)
        self.Student.clicked.connect(self.studentbtn)
        self.classification.clicked.connect(classlistbtn)
        self.Deputy.clicked.connect(DeputyListbtn)
        self.mess.clicked.connect(MessgeBox)
    def studentbtn(self):
        sl = StudentList()
        sl.setModal(True)
        sl.setWindowIcon(QtGui.QIcon("icon.png"))
        sl.setWindowTitle('مدیریت دانش آموزان')
        sl.exec_()
    def teachersbtn(self):
        tp = TeacherList()
        tp.setModal(True)
        tp.setWindowIcon(QtGui.QIcon("icon.png"))
        tp.setWindowTitle('دبیران')
        tp.exec_()

class Addteacher(QDialog):
    def __init__(self):
        super(Addteacher, self).__init__()
        loadUi("UI Files/addTeacher.ui", self)
        self.Closebtn.clicked.connect(self.closebtn)
        self.submit.clicked.connect(self.submitbtn)
    def submitbtn(self):
        data = {
            "name": self.name.text(),
            "family": self.family.text(),
            "birthday": self.date.text(),
            "code": self.code.text(),
            "course": self.course.text(),
            "password": self.password.text(),
            "role": "teacher"
        }
        for i in data.values():
            if i == '':
                printMessWitherr('لطفا تمامی فیلد ها را کامل نمایید')
                return
        username = data['code']
        file = open("Data/users.json", "r")
        users = json.load(file)
        file.close()
        if data['code'] in users:
            printMessWitherr('این شخص قبلا در سیستم ثبت شده است!')
        dbfile = open("Data/users.json", "r+")
        users[username] = data
        json.dump(users, dbfile)
        text = 'دبیر با موفقیت اضافه شد!\n'
        text += 'نام کاربری: ' + username
        text += '\n'
        text +=  'کلمه عبور: ' + data['password']
        printMesswithinf(text)
        self.close()
    def closebtn(self):
        self.close()
class TeacherList(QDialog):
    def __init__(self):
        super(TeacherList, self).__init__()
        loadUi("UI Files/teacher_list.ui", self)
        self.return_2.clicked.connect(self.close)
        self.addTeacher.clicked.connect(self.gotoAddteacher)
        self.addTeacher.clicked.connect(self.loadData)
        self.ed.clicked.connect(EditSTeacherbtn)
        self.ed.clicked.connect(loadData)
        self.loadData()

    def gotoAddteacher(self):
        at = Addteacher()
        at.setModal(True)
        at.setWindowIcon(QtGui.QIcon("icon.png"))
        at.setWindowTitle('اضافه کردن دبیر')
        at.exec_()

    def loadData(self):
        users = loadData()
        row = 0
        size = 0
        for name, user in users.items():
            if user['role'] == 'teacher':
                size = size + 1
        self.teacher_table.setRowCount(size)
        for name, user in users.items():
            if user['role'] != 'teacher':
                continue
            self.teacher_table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['name']))
            self.teacher_table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['family']))
            self.teacher_table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['birthday']))
            self.teacher_table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['code']))
            self.teacher_table.setItem(row, 4, QtWidgets.QTableWidgetItem(user['course']))
            row = row + 1
class StudentList(QDialog):
    def __init__(self):
        super(StudentList, self).__init__()
        loadUi("UI Files/student_list.ui", self)
        self.return_2.clicked.connect(self.close)
        self.addStudent.clicked.connect(self.addStudentbtn)
        self.addStudent.clicked.connect(self.loadData)
        self.edit.clicked.connect(EditStudentbtn)
        self.edit.clicked.connect(loadData)
        self.loadData()

    def addStudentbtn(self):
        ast = addStudent()
        ast.setModal(True)
        ast.setWindowIcon(QtGui.QIcon("icon.png"))
        ast.setWindowTitle('اضافه کردن دانش آموز')
        ast.exec_()
    def loadData(self):
        users = loadData()
        row = 0
        size = 0
        for name, user in users.items():
            if user['role'] == 'student':
                size = size + 1
        self.student_table.setRowCount(size)
        for name, user in users.items():
            if user['role'] != 'student':
                continue
            self.student_table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['name']))
            self.student_table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['family']))
            self.student_table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['dad']))
            self.student_table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['code']))
            self.student_table.setItem(row, 4, QtWidgets.QTableWidgetItem(user['date']))
            row = row + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = QtWidgets.QStackedWidget()
    main_w = Login()
    wid.addWidget(main_w)
    wid.setFixedWidth(374)
    wid.setFixedHeight(176)
    wid.setWindowIcon(QtGui.QIcon("icon.png"))
    wid.setWindowTitle('Login')
    wid.show()
    app.exec_()

