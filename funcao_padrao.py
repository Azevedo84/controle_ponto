from PyQt5.QtWidgets import QTableWidget, QHeaderView
from PyQt5.QtGui import QColor
import re
from conexao import conectar_banco
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox
from PyQt5 import QtCore, QtWidgets
import traceback
import inspect
import os


def grava_erro_banco(nome_funcao, e, nome_arquivo):
    msg_editada = str(e).replace("'", "*")
    msg_editada1 = msg_editada.replace('"', '*')
    print(nome_funcao, nome_arquivo, msg_editada1)

    """
    cursor = conecta.cursor()
    cursor.execute(f"Insert into ZZZ_ERROS (id, arquivo, funcao, mensagem) "
                   f"values (GEN_ID(GEN_ZZZ_ERROS_ID,1), '{nome_arquivo}', '{nome_funcao}', '{msg_editada1}');")
    conecta.commit()
    """


def mensagem_alerta(mensagem):
    alert = QMessageBox()
    alert.setIcon(QMessageBox.Warning)
    alert.setText(mensagem)
    alert.setWindowTitle("Atenção")
    alert.setStandardButtons(QMessageBox.Ok)
    alert.exec_()


def pergunta_confirmacao(mensagem):
    confirmacao = QMessageBox()
    confirmacao.setIcon(QMessageBox.Question)
    confirmacao.setText(mensagem)
    confirmacao.setWindowTitle("Confirmação")

    sim_button = confirmacao.addButton("Sim", QMessageBox.YesRole)
    nao_button = confirmacao.addButton("Não", QMessageBox.NoRole)

    confirmacao.setDefaultButton(nao_button)

    confirmacao.exec_()

    if confirmacao.clickedButton() == sim_button:
        return True
    else:
        return False


def trata_excecao(nome_funcao, mensagem, arquivo):
    try:
        traceback.print_exc()
        print(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')
        mensagem_alerta(f'Houve um problema no arquivo: {arquivo} na função: "{nome_funcao}":\n{mensagem}')

    except Exception as e:
        print(e)


def verifica_formato_horario(string):
    return bool(re.match(r'^\d{1,2}:\d{2}$', string))


def transforma_string_2pontos(string):
    try:
        if string:
            if "." in string:
                string_com_virgula = string.replace('.', ':')
            elif "," in string:
                # Divide a string nos elementos antes e depois da vírgula
                partes = string.split(',')
                # Formata as horas e minutos para terem sempre dois dígitos
                horas = partes[0].rjust(2, '0')
                minutos = partes[1].ljust(2, '0')
                string_com_virgula = f"{horas}:{minutos}"
            elif ":" not in string:
                if len(string) <= 2:
                    # Se o usuário digitou apenas a hora, acrescenta ":00"
                    string_com_virgula = f"{string.rjust(2, '0')}:00"
                elif len(string) == 4:
                    # Formata as horas e minutos para terem sempre dois dígitos
                    horas = string[:2].rjust(2, '0')
                    minutos = string[2:].ljust(2, '0')
                    string_com_virgula = f"{horas}:{minutos}"
                else:
                    # Formata os minutos para terem sempre dois dígitos
                    minutos = string[-2:].ljust(2, '0')
                    string_com_virgula = string[:-2] + ":" + minutos
            else:
                string_com_virgula = string
        else:
            string_com_virgula = ""

        return string_com_virgula

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
        trata_excecao(nome_funcao, str(e), nome_arquivo)
        grava_erro_banco(nome_funcao, e, nome_arquivo)


def lanca_tabela(qtable_widget, nova_tabela):
    try:
        linhas_est = (len(nova_tabela))
        colunas_est = (len(nova_tabela[0]))
        qtable_widget.setRowCount(linhas_est)
        qtable_widget.setColumnCount(colunas_est)
        for i in range(0, linhas_est):
            qtable_widget.setRowHeight(i, 25)
            for j in range(0, colunas_est):
                alinha_cetralizado = AlignDelegate(qtable_widget)
                qtable_widget.setItemDelegateForColumn(j, alinha_cetralizado)
                qtable_widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(nova_tabela[i][j])))

        qtable_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        qtable_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        qtable_widget.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color:#6b6b6b; font-weight: bold; }")
        qtable_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        for row in range(qtable_widget.rowCount()):
            if row % 2 == 0:
                for col in range(qtable_widget.columnCount()):
                    item = qtable_widget.item(row, col)
                    item.setBackground(QColor(220, 220, 220))

        qtable_widget.scrollToBottom()

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
        trata_excecao(nome_funcao, str(e), nome_arquivo)
        grava_erro_banco(nome_funcao, e, nome_arquivo)


def extrair_tabela(qtable_widget):
    try:
        lista_final_itens = []

        total_linhas = qtable_widget.rowCount()
        if total_linhas:
            total_colunas = qtable_widget.columnCount()
            lista_final_itens = []
            linha = []
            for row in range(total_linhas):
                for column in range(total_colunas):
                    widget_item = qtable_widget.item(row, column)
                    if widget_item is not None:
                        lista_item = widget_item.text()
                        linha.append(lista_item)
                        if len(linha) == total_colunas:
                            lista_final_itens.append(linha)
                            linha = []
        return lista_final_itens

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
        trata_excecao(nome_funcao, e, nome_arquivo)
        grava_erro_banco(nome_funcao, e, nome_arquivo)


def limpa_tabela(qtable_widget):
    try:
        qtable_widget.setRowCount(0)

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
        trata_excecao(nome_funcao, str(e), nome_arquivo)
        grava_erro_banco(nome_funcao, e, nome_arquivo)


def transforma_hora_para_float(string):
    num_float = 0

    if string:
        ponto_divisao = string.find(":")
        inteiro = int(string[:ponto_divisao])
        minutos = int(string[(ponto_divisao + 1):])

        decimal = (minutos / 60) * 100

        if inteiro < 10:
            num = "{:02d}.{:02d}".format(inteiro, int(decimal))
        else:
            num = "{:d}.{:02d}".format(inteiro, int(decimal))

        num_float = float(num)

        # Verifica se o tempo é negativo e ajusta o sinal da saída
        if string.startswith("-"):
            if num_float > 0:
                num_float *= -1

    return num_float


def tranforma_float_para_hora(valor):
    if valor:
        e_negativo = False

        if valor < 0:
            e_negativo = True

            valor2 = valor * -1
        else:
            valor2 = valor

        inteiro = int(valor2)

        parte_decimal = valor2 - inteiro
        parte_decimal_inteira = parte_decimal * 100
        decimal = (parte_decimal_inteira * 60) / 100
        decimal_arred = int(round(decimal, 0))

        if inteiro < 10:
            if decimal_arred < 10:
                num = f"0{inteiro}:0{decimal_arred}"
            else:
                num = f"0{inteiro}:{decimal_arred}"
        else:
            if decimal_arred < 10:
                num = f"{inteiro}:0{decimal_arred}"
            else:
                num = f"{inteiro}:{decimal_arred}"

        if e_negativo:
            valor_final = "-" + num
        else:
            valor_final = num

    else:
        valor_final = "00:00"

    return valor_final


def meses_do_ano():
    meses = {'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5, 'JUNHO': 6, 'JULHO': 7,
             'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10, 'NOVEMBRO': 11, 'DEZEMBRO': 12}

    return meses


def obter_dados_empresa(palavra_chave):
    conecta = conectar_banco()
    try:
        cursor = conecta.cursor()
        cursor.execute(f'SELECT id, criacao, descricao, COALESCE(obs, "") '
                       f'FROM cadastro_empresa WHERE descricao LIKE "%{palavra_chave}%";')
        lista_completa = cursor.fetchall()

        return lista_completa

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
        trata_excecao(nome_funcao, str(e), nome_arquivo)
        grava_erro_banco(nome_funcao, e, nome_arquivo)

    finally:
        if 'conexao' in locals():
            conecta.close()


def obter_dados_funcionario(palavra_chave):
    conecta = conectar_banco()
    try:
        cursor = conecta.cursor()
        cursor.execute(f'SELECT id, criacao, descricao, COALESCE(obs, "") '
                       f'FROM cadastro_empresa WHERE descricao LIKE "%{palavra_chave}%";')
        lista_completa = cursor.fetchall()

        return lista_completa

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
