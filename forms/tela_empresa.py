# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_empresa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(15, 5, 15, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(60, 0))
        self.label_4.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.line_Num = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Num.sizePolicy().hasHeightForWidth())
        self.line_Num.setSizePolicy(sizePolicy)
        self.line_Num.setMinimumSize(QtCore.QSize(95, 25))
        self.line_Num.setMaximumSize(QtCore.QSize(95, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.line_Num.setFont(font)
        self.line_Num.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Num.setInputMask("")
        self.line_Num.setText("")
        self.line_Num.setFrame(True)
        self.line_Num.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_Num.setAlignment(QtCore.Qt.AlignCenter)
        self.line_Num.setDragEnabled(False)
        self.line_Num.setPlaceholderText("")
        self.line_Num.setObjectName("line_Num")
        self.horizontalLayout.addWidget(self.line_Num)
        self.label_titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.horizontalLayout.addWidget(self.label_titulo)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.date_Emissao = QtWidgets.QDateEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_Emissao.sizePolicy().hasHeightForWidth())
        self.date_Emissao.setSizePolicy(sizePolicy)
        self.date_Emissao.setMinimumSize(QtCore.QSize(90, 25))
        self.date_Emissao.setMaximumSize(QtCore.QSize(90, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.date_Emissao.setFont(font)
        self.date_Emissao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_Emissao.setObjectName("date_Emissao")
        self.horizontalLayout.addWidget(self.date_Emissao)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(350, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.widget_5.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.widget_5.setObjectName("widget_5")
        self.formLayout = QtWidgets.QFormLayout(self.widget_5)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_titulo_2 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo_2.setFont(font)
        self.label_titulo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo_2.setObjectName("label_titulo_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_titulo_2)
        self.label_24 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.line_Descricao = QtWidgets.QLineEdit(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_Descricao.setFont(font)
        self.line_Descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Descricao.setText("")
        self.line_Descricao.setMaxLength(45)
        self.line_Descricao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_Descricao.setObjectName("line_Descricao")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_Descricao)
        self.label_28 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.plain_Obs = QtWidgets.QPlainTextEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plain_Obs.sizePolicy().hasHeightForWidth())
        self.plain_Obs.setSizePolicy(sizePolicy)
        self.plain_Obs.setMinimumSize(QtCore.QSize(0, 100))
        self.plain_Obs.setMaximumSize(QtCore.QSize(16777215, 100))
        self.plain_Obs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plain_Obs.setObjectName("plain_Obs")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plain_Obs)
        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_6.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(15, 5, 15, 5)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_Excluir = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Excluir.sizePolicy().hasHeightForWidth())
        self.btn_Excluir.setSizePolicy(sizePolicy)
        self.btn_Excluir.setMinimumSize(QtCore.QSize(90, 30))
        self.btn_Excluir.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Excluir.setFont(font)
        self.btn_Excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Excluir.setObjectName("btn_Excluir")
        self.horizontalLayout_2.addWidget(self.btn_Excluir)
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.btn_Limpar = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Limpar.sizePolicy().hasHeightForWidth())
        self.btn_Limpar.setSizePolicy(sizePolicy)
        self.btn_Limpar.setMinimumSize(QtCore.QSize(90, 30))
        self.btn_Limpar.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Limpar.setFont(font)
        self.btn_Limpar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Limpar.setObjectName("btn_Limpar")
        self.horizontalLayout_2.addWidget(self.btn_Limpar)
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.btn_Salvar = QtWidgets.QPushButton(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Salvar.sizePolicy().hasHeightForWidth())
        self.btn_Salvar.setSizePolicy(sizePolicy)
        self.btn_Salvar.setMinimumSize(QtCore.QSize(90, 30))
        self.btn_Salvar.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Salvar.setFont(font)
        self.btn_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Salvar.setObjectName("btn_Salvar")
        self.horizontalLayout_2.addWidget(self.btn_Salvar)
        self.gridLayout_2.addWidget(self.widget_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_7.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        self.label_6.setMinimumSize(QtCore.QSize(110, 0))
        self.label_6.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.line_Consulta = QtWidgets.QLineEdit(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_Consulta.sizePolicy().hasHeightForWidth())
        self.line_Consulta.setSizePolicy(sizePolicy)
        self.line_Consulta.setMinimumSize(QtCore.QSize(250, 25))
        self.line_Consulta.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_Consulta.setFont(font)
        self.line_Consulta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_Consulta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_Consulta.setObjectName("line_Consulta")
        self.horizontalLayout_3.addWidget(self.line_Consulta)
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.btn_Consulta = QtWidgets.QPushButton(self.widget_7)
        self.btn_Consulta.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_Consulta.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Consulta.setFont(font)
        self.btn_Consulta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_Consulta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Consulta.setAutoFillBackground(False)
        self.btn_Consulta.setCheckable(False)
        self.btn_Consulta.setAutoDefault(False)
        self.btn_Consulta.setDefault(False)
        self.btn_Consulta.setFlat(False)
        self.btn_Consulta.setObjectName("btn_Consulta")
        self.horizontalLayout_3.addWidget(self.btn_Consulta)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget_8)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.table_Lista = QtWidgets.QTableWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_Lista.sizePolicy().hasHeightForWidth())
        self.table_Lista.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.table_Lista.setFont(font)
        self.table_Lista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_Lista.setObjectName("table_Lista")
        self.table_Lista.setColumnCount(4)
        self.table_Lista.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Lista.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Lista.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Lista.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_Lista.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.table_Lista)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.gridLayout.addWidget(self.widget_4, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Empresas"))
        self.label_4.setText(_translate("MainWindow", "Código:"))
        self.label_titulo.setText(_translate("MainWindow", "Cadastro de Empresas"))
        self.label.setText(_translate("MainWindow", "Emissão:"))
        self.label_titulo_2.setText(_translate("MainWindow", "Dados para Cadastro"))
        self.label_24.setText(_translate("MainWindow", "Empresa:"))
        self.label_28.setText(_translate("MainWindow", "Observação:"))
        self.btn_Excluir.setText(_translate("MainWindow", "EXCLUIR"))
        self.btn_Limpar.setText(_translate("MainWindow", "LIMPAR"))
        self.btn_Salvar.setText(_translate("MainWindow", "SALVAR"))
        self.label_6.setText(_translate("MainWindow", "Consulta Empresa:"))
        self.btn_Consulta.setText(_translate("MainWindow", "Consulta"))
        self.label_5.setText(_translate("MainWindow", "Lista de Empresas"))
        item = self.table_Lista.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_Lista.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CRIACAO"))
        item = self.table_Lista.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.table_Lista.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "OBSERVAÇÃO"))