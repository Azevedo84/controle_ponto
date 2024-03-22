import sys
from forms.tela_funcionario import *
from conexao import conectar_banco
from funcao_padrao import grava_erro_banco, trata_excecao, mensagem_alerta, lanca_tabela
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QApplication, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from datetime import date
import inspect
import os


class TelaFuncionario(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.definir_tamanho_aplicacao()

        self.btn_Salvar.clicked.connect(self.verifica_salvamento)
        self.btn_Limpar.clicked.connect(self.reiniciando_tela)
        self.btn_Excluir.clicked.connect(self.excluir_cadastro)

        self.combo_Consulta_Empresa.activated.connect(self.procura_por_empresa)

        self.table_Lista.viewport().installEventFilter(self)

        self.layout_inicial_tabela()
        self.lanca_numero()
        self.line_Num.setReadOnly(True)
        self.data_emissao()
        self.lanca_combo_empresa()

    def definir_tamanho_aplicacao(self):
        try:
            monitor = QDesktopWidget().screenGeometry()
            monitor_width = monitor.width()
            monitor_height = monitor.height()

            if monitor_width > 1199 and monitor_height > 809:
                interface_width = 1100
                interface_height = 720

            elif monitor_width > 1365 and monitor_height > 767:
                interface_width = 900
                interface_height = 585
            else:
                interface_width = monitor_width - 165
                interface_height = monitor_height - 90

            x = (monitor_width - interface_width) // 2
            y = (monitor_height - interface_height) // 2

            self.setGeometry(x, y, interface_width, interface_height)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def lanca_numero(self):
        conecta = conectar_banco()
        try:
            cursor = conecta.cursor()
            cursor.execute("SELECT MAX(id) as id FROM cadastro_funcionario;")
            dados = cursor.fetchall()

            if not dados or dados[0][0] is None:
                self.line_Num.setText("1")
                self.line_Descricao.setFocus()
            else:
                num = dados[0]
                num_escolha = num[0]
                num_plano_int = int(num_escolha) + 1
                num_plano_str = str(num_plano_int)
                self.line_Num.setText(num_plano_str)
                self.line_Descricao.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def data_emissao(self):
        try:
            data_hoje = date.today()
            self.date_Emissao.setDate(data_hoje)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def layout_inicial_tabela(self):
        try:
            self.table_Lista.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.table_Lista.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.table_Lista.horizontalHeader().setStyleSheet("QHeaderView::section { background-color:#6b6b6b }")

            font = QFont()
            font.setBold(True)
            self.table_Lista.horizontalHeader().setFont(font)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def lanca_combo_empresa(self):
        conecta = conectar_banco()
        try:
            self.combo_Empresa.clear()
            self.combo_Consulta_Empresa.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute('SELECT id, descricao FROM cadastro_empresa order by descricao;')
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Empresa.addItems(nova_lista)
            self.combo_Consulta_Empresa.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def procura_por_empresa(self):
        conecta = conectar_banco()
        try:
            tabela_nova = []

            empresa = self.combo_Consulta_Empresa.currentText()
            if empresa:
                tete = empresa.find(" - ")
                id_empresa = empresa[:tete]

                cursor = conecta.cursor()
                cursor.execute(f"SELECT func.id, func.criacao, empr.descricao, func.descricao, "
                               f"COALESCE(func.obs, '') "
                               f"FROM cadastro_funcionario as func "
                               f"INNER JOIN cadastro_empresa as empr ON func.id_empresa = empr.id "
                               f"where func.id_empresa = '{id_empresa}' "
                               f"order by func.descricao;")
                lista_completa = cursor.fetchall()

                if not lista_completa:
                    mensagem_alerta(f'Não foi encontrado nenhum item com Empresa:\n "{empresa}"!')
                    self.reiniciando_tela()
                else:
                    for i in lista_completa:
                        id_func, data, empresa, descricao, obs = i

                        formato_brasileiro = "%d/%m/%Y"
                        data_brasileira = data.strftime(formato_brasileiro)

                        dados = (id_func, data_brasileira, empresa, descricao, obs)
                        tabela_nova.append(dados)

                    lanca_tabela(self.table_Lista, tabela_nova)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def reiniciando_tela(self):
        try:
            self.line_Num.clear()
            self.line_Descricao.clear()
            self.combo_Empresa.setCurrentText("")
            self.combo_Consulta_Empresa.setCurrentText("")
            self.plain_Obs.clear()
            self.table_Lista.setRowCount(0)

            self.layout_inicial_tabela()
            self.lanca_numero()
            self.data_emissao()
            self.lanca_combo_empresa()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def eventFilter(self, source, event):
        try:
            if (event.type() == QtCore.QEvent.MouseButtonDblClick and
                    event.buttons() == QtCore.Qt.LeftButton and
                    source is self.table_Lista.viewport()):
                item = self.table_Lista.currentItem()

                dados = self.extrair_tabela_funcionario()
                selecao = dados[item.row()]
                ids, criacao, grupo, descr, obs = selecao

                item_count = self.combo_Empresa.count()
                for i in range(item_count):
                    item_text = self.combo_Empresa.itemText(i)
                    if grupo in item_text:
                        self.combo_Empresa.setCurrentText(item_text)

                self.line_Num.setText(ids)
                self.line_Descricao.setText(descr)
                self.plain_Obs.setPlainText(obs)

            return super(QMainWindow, self).eventFilter(source, event)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def extrair_tabela_funcionario(self):
        row_count = self.table_Lista.rowCount()
        column_count = self.table_Lista.columnCount()
        lista_final_itens = []
        linha = []
        for row in range(row_count):
            for column in range(column_count):
                widget_item = self.table_Lista.item(row, column)
                lista_item = widget_item.text()
                linha.append(lista_item)
                if len(linha) == column_count:
                    lista_final_itens.append(linha)
                    linha = []
        return lista_final_itens

    def excluir_cadastro(self):
        conecta = conectar_banco()
        try:
            codigo = self.line_Num.text()
            descricao = self.line_Descricao.text()

            if not descricao:
                mensagem_alerta('O campo "Descrição:" não pode estar vazio!')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            elif descricao == "0":
                mensagem_alerta('O campo "Descrição:" não pode ser "0"!')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            elif not codigo:
                mensagem_alerta('O campo "Código:" não pode estar vazio!')
                self.line_Descricao.clear()
                self.line_Num.setFocus()
            elif codigo == "0":
                mensagem_alerta('O campo "Código:" não pode ser "0"!')
                self.line_Descricao.clear()
                self.line_Num.setFocus()
            else:
                cursor = conecta.cursor()
                cursor.execute(f"SELECT * from cadastro_funcionario where id = {codigo};")
                registro_id = cursor.fetchall()

                if registro_id:
                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT DATA, ID_FUNCIONARIO "
                                   f"FROM horarios "
                                   f"WHERE ID_FUNCIONARIO = {codigo};")
                    registro_mov = cursor.fetchall()

                    if registro_mov:
                        mensagem_alerta(f'O Funcionário(a) {descricao} não pode ser excluído(a)\n'
                                        f'pois possui registros de cartão ponto!!')
                        self.reiniciando_tela()
                    else:
                        cursor = conecta.cursor()
                        cursor.execute(f"DELETE from cadastro_funcionario where id = {codigo};")
                        conecta.commit()

                        mensagem_alerta(f'O Funcionário {descricao} foi excluído com sucesso!')
                        self.reiniciando_tela()

                else:
                    mensagem_alerta(f'O código {codigo} do Funcionário não existe!')
                    self.reiniciando_tela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def verifica_salvamento(self):
        try:
            descricao = self.line_Descricao.text()
            empresa = self.combo_Empresa.currentText()

            if not descricao:
                mensagem_alerta('O campo "Descrição:" não pode estar vazio!')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            elif descricao == "0":
                mensagem_alerta('O campo "Descrição:" não pode ser "0"!')
                self.line_Descricao.clear()
                self.line_Descricao.setFocus()
            elif not empresa:
                mensagem_alerta('O campo "Empresa:" não pode estar vazio!')
                self.combo_Empresa.setCurrentText("")
                self.combo_Empresa.setFocus()
            else:
                self.verifica_nome_funcionario()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def verifica_nome_funcionario(self):
        conecta = conectar_banco()
        try:
            descricao = self.line_Descricao.text()
            descr_maiuscula = descricao.upper()

            empresa = self.combo_Empresa.currentText()
            tete = empresa.find(" - ")
            id_empresa = empresa[:tete]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT func.id, func.criacao, empr.descricao, func.descricao, "
                           f"COALESCE(func.obs, '') "
                           f"FROM cadastro_funcionario as func "
                           f"INNER JOIN cadastro_empresa as empr ON func.id_empresa = empr.id "
                           f"where func.id_empresa = '{id_empresa}' "
                           f"and func.descricao = '{descr_maiuscula}' "
                           f"order by func.descricao;")
            lista_completa = cursor.fetchall()

            if lista_completa:
                mensagem_alerta("Este nome de Funcionário já foi cadastrado nesta empresa!")
            else:
                self.salvar_dados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def salvar_dados(self):
        conecta = conectar_banco()
        try:
            codigo = self.line_Num.text()

            descricao = self.line_Descricao.text()
            descr_maiuscula = descricao.upper()

            obs = self.plain_Obs.toPlainText()
            if not obs:
                obs_maiusculo = ""
            else:
                obs_maiusculo = obs.upper()

            empresa = self.combo_Empresa.currentText()
            tete = empresa.find(" - ")
            id_empresa = empresa[:tete]

            cursor = conecta.cursor()
            cursor.execute(f"SELECT * from cadastro_funcionario where id = {codigo};")
            registro_id = cursor.fetchall()

            if registro_id:
                cursor = conecta.cursor()
                cursor.execute(f"UPDATE cadastro_funcionario SET descricao = '{descr_maiuscula}', "
                               f"id_empresa = {id_empresa}, obs = '{obs_maiusculo}' "
                               f"where id = {codigo};")

                mensagem_alerta(f'O Funcionário {descr_maiuscula}\nfoi alterada com sucesso!')
                self.reiniciando_tela()
            else:
                cursor = conecta.cursor()
                cursor.execute(f'Insert into cadastro_funcionario '
                               f'(descricao, id_empresa, obs) '
                               f'values ("{descr_maiuscula}", {id_empresa}, "{obs_maiusculo}");')

                mensagem_alerta(f'O Funcionário {descr_maiuscula} foi criado com sucesso!')
                self.reiniciando_tela()

            conecta.commit()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaFuncionario()
    tela.show()
    qt.exec_()
