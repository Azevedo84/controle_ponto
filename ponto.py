import sys
from forms.tela_ponto import *
from conexao_teste import conectar_banco
from funcao_padrao import grava_erro_banco, trata_excecao, mensagem_alerta, extrair_tabela, \
    transforma_string_2pontos, verifica_formato_horario, limpa_tabela, meses_do_ano, lanca_tabela, \
    transforma_hora_para_float, tranforma_float_para_hora
from PyQt5.QtWidgets import QMainWindow, QApplication, QAbstractItemView, QDesktopWidget
from PyQt5.QtCore import QDate
from datetime import date, datetime, timedelta
import inspect
import os


class TelaPonto(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.cad_empresa = []
        self.cad_funcionario = []

        self.definir_tamanho_aplicacao()

        self.check_Banco.setChecked(True)

        self.combo_Empresa.activated.connect(self.inicio_lanca_combo_funcionario)

        self.check_Extra.stateChanged.connect(self.check_extra_mostrar_extra)

        self.check_Banco.stateChanged.connect(self.check_banco_desliga_atestado)
        self.check_Atestado.stateChanged.connect(self.check_atestado_desliga_banco)
        self.check_Feriado.stateChanged.connect(self.check_feriado_zera_horas)

        self.line_Ini_Manha.editingFinished.connect(self.manha_ver_hora_ini)
        self.line_Fim_Manha.editingFinished.connect(self.manha_ver_hora_fim)
        self.line_Ini_Tarde.editingFinished.connect(self.tarde_ver_hora_ini)
        self.line_Fim_Tarde.editingFinished.connect(self.tarde_ver_hora_fim)
        self.line_Ini_Extra.editingFinished.connect(self.extra_ver_hora_ini)
        self.line_Fim_Extra.editingFinished.connect(self.extra_ver_hora_fim)
        self.date_Ponto.editingFinished.connect(self.date_verifica_data)
        self.processando = False

        self.btn_Adicionar.clicked.connect(self.manual_verifica_campos)
        self.btn_Buscar.clicked.connect(self.busca_verifica_campos)
        self.combo_Func.activated.connect(self.busca_verifica_campos)

        self.btn_Salvar.clicked.connect(self.salvar_verifica_salvamento)

        self.btn_ExcluirItem.clicked.connect(self.excluir_item)
        self.btn_ExcluirTudo.clicked.connect(self.excluir_tudo)

        self.widget_Extra.setHidden(True)

        self.inicio_definir_layout_tabela_ponto()
        self.inicio_lanca_combo_empresa()
        self.inicio_lanca_data_mes_ano_atual()

        self.combo_Empresa.setFocus()

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

    def inicio_definir_layout_tabela_ponto(self):
        try:
            qtable_widget = self.table_Ponto

            qtable_widget.setColumnWidth(0, 70)
            qtable_widget.setColumnWidth(1, 70)
            qtable_widget.setColumnWidth(2, 70)
            qtable_widget.setColumnWidth(3, 70)
            qtable_widget.setColumnWidth(4, 70)
            qtable_widget.setColumnWidth(5, 70)
            qtable_widget.setColumnWidth(6, 70)
            qtable_widget.setColumnWidth(7, 70)
            qtable_widget.setColumnWidth(8, 70)
            qtable_widget.setColumnWidth(9, 70)
            qtable_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

            qtable_widget.horizontalHeader().setStyleSheet(
                "QHeaderView::section { background-color:#6b6b6b; font-weight: bold; }")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def inicio_lanca_combo_empresa(self):
        conecta = conectar_banco()
        try:
            self.combo_Empresa.clear()

            nova_lista = [""]

            cursor = conecta.cursor()
            cursor.execute('SELECT id, descricao FROM cadastro_empresa order by descricao;')
            lista_completa = cursor.fetchall()
            for ides, descr in lista_completa:
                dd = f"{ides} - {descr}"
                nova_lista.append(dd)

            self.combo_Empresa.addItems(nova_lista)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def inicio_lanca_combo_funcionario(self):
        conecta = conectar_banco()
        try:
            cursor = conecta.cursor()
            cursor.execute(f'SELECT id, descricao '
                           f'FROM cadastro_funcionario '
                           f'where id = 1 '
                           f'order by descricao;')
            lista_completa = cursor.fetchall()

            self.combo_Func.clear()

            nova_lista = [""]

            grupo = self.combo_Empresa.currentText()
            if grupo:
                grupotete = grupo.find(" - ")
                id_empresa = grupo[:grupotete]

                cursor = conecta.cursor()
                cursor.execute(f'SELECT id, descricao '
                               f'FROM cadastro_funcionario '
                               f'where id_empresa = {id_empresa} '
                               f'order by descricao;')
                lista_completa = cursor.fetchall()
                if lista_completa:
                    for ides, descr in lista_completa:
                        dd = f"{ides} - {descr}"
                        nova_lista.append(dd)

                self.combo_Func.addItems(nova_lista)
            else:
                self.combo_Empresa.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def inicio_lanca_data_mes_ano_atual(self):
        try:
            data_hoje = date.today()

            data_atual = QDate.currentDate()
            data_primeiro_dia_mes = QDate(data_atual.year(), data_atual.month(), 1)
            self.date_Ponto.setDate(data_primeiro_dia_mes)

            self.line_Ano.setText(str(data_hoje.year))

            mes_atual = data_atual.month()
            self.combo_Mes.setCurrentIndex(mes_atual - 1)

            self.inicio_lanca_dia_da_semana()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def inicio_lanca_dia_da_semana(self):
        try:
            data_selecionada = self.date_Ponto.date()
            dia_semana = data_selecionada.dayOfWeek()
            dias_da_semana = ["SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA",
                              "SEXTA-FEIRA", "SÁBADO", "DOMINGO"]
            nome_dia = dias_da_semana[dia_semana - 1]
            self.line_semana.setText(nome_dia)

            if nome_dia == "SÁBADO":
                self.line_Horas.setText("04:00")
            elif nome_dia == "DOMINGO":
                self.line_Horas.setText("00:00")
            else:
                self.line_Horas.setText("08:00")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def manha_ver_hora_ini(self):
        if not self.processando:
            try:
                self.processando = True

                ini_manha = self.line_Ini_Manha.text()
                if ini_manha:
                    valor = transforma_string_2pontos(ini_manha)
                    self.line_Ini_Manha.setText(valor)

                    ini_manha_alterado = self.line_Ini_Manha.text()

                    if verifica_formato_horario(ini_manha_alterado):
                        self.line_Fim_Manha.setFocus()
                    else:
                        mensagem_alerta("Formato de hora inválido.")
                        self.line_Ini_Manha.clear()
                        self.line_Ini_Manha.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def manha_ver_hora_fim(self):
        if not self.processando:
            try:
                self.processando = True

                fim_manha = self.line_Fim_Manha.text()
                if fim_manha:
                    valor = transforma_string_2pontos(fim_manha)
                    self.line_Fim_Manha.setText(valor)

                    fim_manha_alterado = self.line_Fim_Manha.text()

                    if verifica_formato_horario(fim_manha_alterado):
                        self.line_Ini_Tarde.setFocus()
                    else:
                        mensagem_alerta("Formato de hora inválido.")
                        self.line_Fim_Manha.clear()
                        self.line_Fim_Manha.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def tarde_ver_hora_ini(self):
        if not self.processando:
            try:
                self.processando = True

                ini_tarde = self.line_Ini_Tarde.text()
                if ini_tarde:
                    valor = transforma_string_2pontos(ini_tarde)
                    self.line_Ini_Tarde.setText(valor)

                    ini_tarde_alterado = self.line_Ini_Tarde.text()

                    if verifica_formato_horario(ini_tarde_alterado):
                        self.line_Fim_Tarde.setFocus()
                    else:
                        mensagem_alerta("Formato de hora inválido.")
                        self.line_Ini_Tarde.clear()
                        self.line_Ini_Tarde.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def tarde_ver_hora_fim(self):
        if not self.processando:
            try:
                self.processando = True

                fim_tarde = self.line_Fim_Tarde.text()
                if fim_tarde:
                    valor = transforma_string_2pontos(fim_tarde)
                    self.line_Fim_Tarde.setText(valor)

                    fim_tarde_alterado = self.line_Fim_Tarde.text()

                    if verifica_formato_horario(fim_tarde_alterado):
                        ini_tarde = self.line_Ini_Tarde.text()
                        if ini_tarde:
                            self.tarde_verifica_se_lanca_extra()
                    else:
                        mensagem_alerta("Formato de hora inválido.")
                        self.line_Fim_Tarde.clear()
                        self.line_Fim_Tarde.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def tarde_verifica_se_lanca_extra(self):
        try:
            if self.check_Extra.isChecked():
                self.line_Ini_Extra.setFocus()
            else:
                self.manual_pronto_lancar_tabela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def extra_ver_hora_ini(self):
        if not self.processando:
            try:
                self.processando = True

                ini_extra = self.line_Ini_Extra.text()
                if ini_extra:
                    valor = transforma_string_2pontos(ini_extra)
                    self.line_Ini_Extra.setText(valor)

                    ini_extra_alterado = self.line_Ini_Extra.text()

                    if verifica_formato_horario(ini_extra_alterado):
                        self.line_Fim_Extra.setFocus()
                    else:
                        mensagem_alerta("Formato de hora inválido.")
                        self.line_Ini_Extra.clear()
                        self.line_Ini_Extra.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def extra_ver_hora_fim(self):
        if not self.processando:
            try:
                self.processando = True

                fim_extra = self.line_Fim_Extra.text()
                if fim_extra:
                    valor = transforma_string_2pontos(fim_extra)
                    self.line_Fim_Extra.setText(valor)

                    fim_extra_alterado = self.line_Fim_Extra.text()

                    if verifica_formato_horario(fim_extra_alterado):
                        ini_extra = self.line_Ini_Extra.text()
                        if ini_extra:
                            self.manual_pronto_lancar_tabela()
                    else:
                        mensagem_alerta("Formato de hora inválido.")
                        self.line_Fim_Extra.clear()
                        self.line_Fim_Extra.setFocus()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def busca_verifica_campos(self):
        try:
            empresa = self.combo_Empresa.currentText()
            func = self.combo_Func.currentText()
            mes = self.combo_Mes.currentText()
            ano = self.line_Ano.text()

            if not empresa:
                mensagem_alerta(f'O campo "Empresa" não pode estar vazio!')
            elif not func:
                mensagem_alerta(f'O campo "Funcionário" não pode estar vazio!')
            elif not mes:
                mensagem_alerta(f'O campo "Mês" não pode estar vazio!')
            elif not ano:
                mensagem_alerta(f'O campo "Ano" não pode estar vazio!')
            else:
                self.busca_manipula_horarios_banco()
                self.limpa_dados_horarios()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def busca_manipula_horarios_banco(self):
        conecta = conectar_banco()
        try:
            limpa_tabela(self.table_Ponto)

            tabela_nova = []

            funcionario = self.combo_Func.currentText()
            funcionariotete = funcionario.find(" - ")
            id_funcionario = funcionario[:funcionariotete]

            mes = self.combo_Mes.currentText()
            meses = meses_do_ano()
            numero_mes = meses.get(mes.upper())
            ano = int(self.line_Ano.text())

            cursor = conecta.cursor()
            cursor.execute(f"SELECT DATA, ID_FUNCIONARIO, UM_INI, UM_FIM, DOIS_INI, DOIS_FIM, "
                           f"EXTRA_INI, EXTRA_FIM, PADRAO, TRABALHADAS , SALDO, TIPO "
                           f"FROM horarios "
                           f"WHERE ID_FUNCIONARIO = {id_funcionario} "
                           f"AND EXTRACT(MONTH FROM DATA) = {numero_mes} "
                           f"AND EXTRACT(YEAR FROM DATA) = {ano} "
                           f"ORDER BY DATA;")
            extrair_horas = cursor.fetchall()
            if extrair_horas:
                for i in extrair_horas:
                    data, id_fu, um_ini, um_fim, doi_ini, doi_fim, extr_ini, extr_fim, padrao, trab, saldo, tipo = i

                    emissao = data.strftime('%d/%m/%Y')

                    dia_semana = data.weekday()
                    dias_da_semana = ["SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA",
                                      "SEXTA-FEIRA", "SÁBADO", "DOMINGO"]
                    nome_dia = dias_da_semana[dia_semana]

                    dados = (emissao, nome_dia, um_ini, um_fim, doi_ini, doi_fim, extr_ini, extr_fim,
                             padrao, trab, saldo, tipo)
                    tabela_nova.append(dados)

            if tabela_nova:
                lista_de_listas_ordenada = sorted(tabela_nova, key=lambda x: x[0])
                lanca_tabela(self.table_Ponto, lista_de_listas_ordenada)
                self.totais_somar_tudo()
                self.busca_verifica_dias_lancados()

            else:
                self.ativar_campos_manual()
                self.busca_verifica_dias_lancados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()

    def busca_verifica_dias_lancados(self):
        try:
            mes = self.combo_Mes.currentText()
            meses = meses_do_ano()
            numero_mes = meses.get(mes.upper())
            ano = int(self.line_Ano.text())

            extraido_dados = extrair_tabela(self.table_Ponto)

            primeiro_dia_mes = datetime(ano, numero_mes, 1)
            ultimo_dia_mes = datetime(ano, numero_mes + 1, 1) - timedelta(days=1)
            datas_mes = [primeiro_dia_mes + timedelta(days=x) for x in
                         range((ultimo_dia_mes - primeiro_dia_mes).days + 1)]

            datas_tabela = [datetime.strptime(i[0], "%d/%m/%Y") for i in extraido_dados]

            datas_faltando = [data for data in datas_mes if data not in datas_tabela]

            if not datas_faltando:
                msg = f"Todos os dias do mês\nde {mes} de {ano} já foram lançados"
                self.label_3.setText(msg)
                self.inativar_campos_manual()
                self.btn_Buscar.setFocus()
            else:
                msg = 'Estas são as datas faltando na\ntabela "Relatório do Ponto":\n\n'
                for datin in datas_faltando:
                    self.date_Ponto.setDate(datin)
                    self.inicio_lanca_dia_da_semana()
                    break

                for datin in datas_faltando:
                    emissao = datin.strftime('%d/%m/%Y')

                    msg += f"- {emissao}\n"

                self.label_3.setText(msg)

                self.ativar_campos_manual()
                self.date_Ponto.setFocus()

            if extraido_dados:
                self.busca_manipula_cabecalho_com_dados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def busca_manipula_cabecalho_com_dados(self):
        try:
            extraido_dados = extrair_tabela(self.table_Ponto)

            data_mais_recente = None

            if extraido_dados:
                for i in extraido_dados:
                    data, sem, man_ini, man_fim, tar_ini, tar_fim, ext_ini, ext_fim, padrao, trab, saldo, tipo = i

                    data_formatada = datetime.strptime(data, '%d/%m/%Y')

                    if data_mais_recente is None or data_formatada > data_mais_recente:
                        data_mais_recente = data_formatada

            if not data_mais_recente:
                mensagem_alerta("Não foi possível encontrar uma data válida na tabela.")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def manual_verifica_campos(self):
        try:
            empresa = self.combo_Empresa.currentText()
            func = self.combo_Func.currentText()
            mes = self.combo_Mes.currentText()
            ano = self.line_Ano.text()

            if not empresa:
                mensagem_alerta(f'O campo "Empresa" não pode estar vazio!')
            elif not func:
                mensagem_alerta(f'O campo "Funcionário" não pode estar vazio!')
            elif not mes:
                mensagem_alerta(f'O campo "Mês" não pode estar vazio!')
            elif not ano:
                mensagem_alerta(f'O campo "Ano" não pode estar vazio!')
            else:
                self.manual_pronto_lancar_tabela()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def manual_pronto_lancar_tabela(self):
        try:
            tipo = self.manual_define_tipo()

            data = self.date_Ponto.date()
            data_formatada = data.toString("dd/MM/yyyy")

            dia_s = self.line_semana.text()

            if self.check_Feriado.isChecked():
                padrao = "00:00"
            else:
                padrao = self.line_Horas.text()
            total_padrao_float = transforma_hora_para_float(padrao)

            ini_1 = self.line_Ini_Manha.text()
            ini_1_float = transforma_hora_para_float(ini_1)

            fim_1 = self.line_Fim_Manha.text()
            fim_1_float = transforma_hora_para_float(fim_1)

            total_1 = fim_1_float - ini_1_float
            total_1_arred = round(total_1, 2)

            ini_2 = self.line_Ini_Tarde.text()
            ini_2_float = transforma_hora_para_float(ini_2)

            fim_2 = self.line_Fim_Tarde.text()
            fim_2_float = transforma_hora_para_float(fim_2)

            total_2 = fim_2_float - ini_2_float
            total_2_arred = round(total_2, 2)

            ini_3 = self.line_Ini_Extra.text()
            ini_3_float = transforma_hora_para_float(ini_3)

            fim_3 = self.line_Fim_Extra.text()
            fim_3_float = transforma_hora_para_float(fim_3)

            total_3 = fim_3_float - ini_3_float
            total_3_arred = round(total_3, 2)

            total_geral = total_1_arred + total_2_arred + total_3_arred
            trab = tranforma_float_para_hora(total_geral)

            dif_float = total_geral - total_padrao_float
            dif_hora = tranforma_float_para_hora(dif_float)
            if dif_hora:
                if self.check_Atestado.isChecked():
                    saldo = "00:00"
                else:
                    saldo = dif_hora
            else:
                saldo = "00:00"

            extraido_dados = extrair_tabela(self.table_Ponto)

            dados = [data_formatada, dia_s, ini_1, fim_1, ini_2, fim_2, ini_3, fim_3, padrao, trab, saldo, tipo]
            extraido_dados.append(dados)

            if extraido_dados:
                lista_de_listas_ordenada = sorted(extraido_dados, key=lambda x: x[0])
                lanca_tabela(self.table_Ponto, lista_de_listas_ordenada)
                self.totais_somar_tudo()

            self.busca_verifica_dias_lancados()
            self.limpa_dados_horarios()
            self.inicio_lanca_dia_da_semana()
            self.check_Extra.setChecked(False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def totais_somar_tudo(self):
        try:
            extraido_dados = extrair_tabela(self.table_Ponto)

            padrazao_float = 0
            trabzao_float = 0
            saldozao_float = 0

            if extraido_dados:
                for i in extraido_dados:
                    data, sem, man_ini, man_fim, tar_ini, tar_fim, ext_ini, ext_fim, padrao, trab, saldo, tipo = i

                    padrao_float = transforma_hora_para_float(padrao)
                    padrazao_float += padrao_float

                    trab_float = transforma_hora_para_float(trab)
                    trabzao_float += trab_float

                    saldo_float = transforma_hora_para_float(saldo)
                    saldozao_float += saldo_float

            padrao_final = tranforma_float_para_hora(padrazao_float)
            self.line_Total_Padrao.setText(padrao_final)

            trab_final = tranforma_float_para_hora(trabzao_float)
            self.line_Total_Trabalhado.setText(trab_final)

            saldo_final = tranforma_float_para_hora(saldozao_float)
            self.line_Saldo.setText(saldo_final)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def manual_define_tipo(self):
        try:
            if self.check_Feriado.isChecked():
                tipo = "FERIADO"
            elif self.check_Atestado.isChecked():
                tipo = "ATESTADO"
            else:
                tipo = "BANCO"

            return tipo

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def check_extra_mostrar_extra(self, state):
        if state == 2:
            self.widget_Extra.setHidden(False)
            self.limpa_dados_horarios()
            self.line_Ini_Manha.setFocus()
        else:
            self.widget_Extra.setHidden(True)

    def check_banco_desliga_atestado(self, state):
        if state == 2:
            self.check_Atestado.setChecked(False)
        else:
            self.check_Atestado.setChecked(True)

    def check_atestado_desliga_banco(self, state):
        if state == 2:
            self.check_Banco.setChecked(False)
        else:
            self.check_Banco.setChecked(True)

    def check_feriado_zera_horas(self, state):
        if state == 2:
            self.line_Horas.setText("00:00")
        else:
            self.inicio_lanca_dia_da_semana()

    def date_verifica_data(self):
        if not self.processando:
            try:
                self.processando = True

                self.date_verifica_data_fora_do_mes()

            except Exception as e:
                nome_funcao = inspect.currentframe().f_code.co_name
                nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
                nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
                trata_excecao(nome_funcao, str(e), nome_arquivo)
                grava_erro_banco(nome_funcao, e, nome_arquivo)

            finally:
                self.processando = False

    def date_verifica_data_fora_do_mes(self):
        try:
            self.processando = True

            data_lancada = self.date_Ponto.date()
            ano_data_lancada = data_lancada.year()
            mes_data_lancada = data_lancada.month()

            mes_ref = self.combo_Mes.currentText()
            meses = meses_do_ano()
            numero_mes_ref = meses.get(mes_ref.upper())
            ano_ref = int(self.line_Ano.text())

            if ano_data_lancada == ano_ref and mes_data_lancada == numero_mes_ref:
                data_formatada = data_lancada.toString("dd/MM/yyyy")

                ano = data_lancada.year()
                mes = data_lancada.month()
                dia = data_lancada.day()
                data_normal = date(ano, mes, dia)

                data_repetida = 0

                extraido_dados = extrair_tabela(self.table_Ponto)
                if extraido_dados:
                    for i in extraido_dados:
                        data_str = i[0]

                        data_date = datetime.strptime(data_str, "%d/%m/%Y").date()

                        if data_normal == data_date:
                            data_repetida += 1

                if data_repetida > 0:
                    mensagem_alerta(f"A data {data_formatada} já está lançada na tabela!")
                    self.limpa_tudo()
                else:
                    self.date_seleciona_dia_da_semana()
            else:
                mensagem_alerta("Não pode ser lançado data fora do mês de referência!")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def date_seleciona_dia_da_semana(self):
        try:
            data_selecionada = self.date_Ponto.date()
            dia_semana = data_selecionada.dayOfWeek()
            dias_da_semana = ["SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA",
                              "SEXTA-FEIRA", "SÁBADO", "DOMINGO"]
            nome_dia = dias_da_semana[dia_semana - 1]
            self.line_semana.setText(nome_dia)

            if nome_dia == "SÁBADO":
                self.line_Horas.setText("04:00")
            elif nome_dia == "DOMINGO":
                self.line_Horas.setText("00:00")
            else:
                self.line_Horas.setText("08:00")

            self.line_Ini_Manha.setFocus()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def inativar_campos_manual(self):
        try:
            self.date_Ponto.setReadOnly(True)
            self.date_Ponto.setEnabled(False)

            self.line_semana.setEnabled(False)
            self.line_Horas.setEnabled(False)

            self.check_Banco.setEnabled(False)
            self.check_Feriado.setEnabled(False)
            self.check_Atestado.setEnabled(False)
            self.check_Extra.setEnabled(False)

            self.line_Ini_Manha.setEnabled(False)
            self.line_Fim_Manha.setEnabled(False)
            self.line_Ini_Tarde.setEnabled(False)
            self.line_Fim_Tarde.setEnabled(False)
            self.line_Ini_Extra.setEnabled(False)
            self.line_Fim_Extra.setEnabled(False)
            self.btn_Adicionar.setEnabled(False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def ativar_campos_manual(self):
        try:
            self.date_Ponto.setReadOnly(False)
            self.date_Ponto.setEnabled(True)

            self.line_semana.setEnabled(True)
            self.line_Horas.setEnabled(True)

            self.check_Banco.setEnabled(True)
            self.check_Feriado.setEnabled(True)
            self.check_Atestado.setEnabled(True)
            self.check_Extra.setEnabled(True)

            self.line_Ini_Manha.setEnabled(True)
            self.line_Fim_Manha.setEnabled(True)
            self.line_Ini_Tarde.setEnabled(True)
            self.line_Fim_Tarde.setEnabled(True)
            self.line_Ini_Extra.setEnabled(True)
            self.line_Fim_Extra.setEnabled(True)
            self.btn_Adicionar.setEnabled(True)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def limpa_dados_horarios(self):
        try:
            self.line_Ini_Manha.clear()
            self.line_Fim_Manha.clear()

            self.line_Ini_Tarde.clear()
            self.line_Fim_Tarde.clear()

            self.line_Ini_Extra.clear()
            self.line_Fim_Extra.clear()

            self.check_Banco.setChecked(True)
            self.check_Feriado.setChecked(False)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def limpa_dados_totais(self):
        try:
            self.line_Total_Padrao.clear()
            self.line_Total_Trabalhado.clear()
            self.line_Saldo.clear()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def limpa_tudo(self):
        try:
            self.limpa_dados_horarios()
            self.limpa_dados_totais()

            self.combo_Empresa.setCurrentText("")
            self.combo_Func.setCurrentText("")
            self.table_Ponto.setRowCount(0)

            self.inicio_definir_layout_tabela_ponto()
            self.inicio_lanca_combo_empresa()
            self.inicio_lanca_data_mes_ano_atual()

            self.combo_Empresa.setFocus()

            self.label_3.setText("")

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def excluir_item(self):
        try:
            extrai_recomendados = extrair_tabela(self.table_Ponto)
            if not extrai_recomendados:
                mensagem_alerta(f'A tabela "Relatório do Ponto" está vazia!')
            else:
                linha_selecao = self.table_Ponto.currentRow()
                if linha_selecao >= 0:
                    self.table_Ponto.removeRow(linha_selecao)

                self.ativar_campos_manual()
                self.busca_verifica_dias_lancados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def excluir_tudo(self):
        try:
            extrai_estrutura = extrair_tabela(self.table_Ponto)
            if not extrai_estrutura:
                mensagem_alerta(f'A tabela "Relatório do Ponto" está vazia!')
            else:
                self.table_Ponto.setRowCount(0)
                self.busca_verifica_dias_lancados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def salvar_verifica_salvamento(self):
        try:
            empresa = self.combo_Empresa.currentText()
            func = self.combo_Func.currentText()
            mes = self.combo_Mes.currentText()
            ano = self.line_Ano.text()

            if not empresa:
                mensagem_alerta(f'O campo "Empresa" não pode estar vazio!')
            elif not func:
                mensagem_alerta(f'O campo "Funcionário" não pode estar vazio!')
            elif not mes:
                mensagem_alerta(f'O campo "Mês" não pode estar vazio!')
            elif not ano:
                mensagem_alerta(f'O campo "Ano" não pode estar vazio!')
            else:
                self.salvar_excluir_dados()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def salvar_excluir_dados(self):
        conecta = conectar_banco()
        try:
            datas_excluidas = []

            extraido_dados = extrair_tabela(self.table_Ponto)

            funcionario = self.combo_Func.currentText()
            funcionariotete = funcionario.find(" - ")
            id_funcionario = funcionario[:funcionariotete]

            mes = self.combo_Mes.currentText()
            meses = meses_do_ano()
            numero_mes = meses.get(mes.upper())
            ano = int(self.line_Ano.text())

            cursor = conecta.cursor()
            cursor.execute(f"SELECT ID, DATA, ID_FUNCIONARIO, TIPO "
                           f"FROM horarios "
                           f"WHERE ID_FUNCIONARIO = {id_funcionario} "
                           f"AND EXTRACT(MONTH FROM DATA) = {numero_mes} "
                           f"AND EXTRACT(YEAR FROM DATA) = {ano} "
                           f"ORDER BY DATA;")
            extrair_horas = cursor.fetchall()
            if extrair_horas:
                for i in extrair_horas:
                    id_mov, data, id_funcy, tipo = i

                    emissao = data.strftime('%d/%m/%Y')

                    encontrado = any(emissao in i for i in extraido_dados)

                    if not encontrado:
                        cursor = conecta.cursor()
                        cursor.execute(f"DELETE from horarios where id = {id_mov};")

                        cece = (emissao, id_funcy)
                        datas_excluidas.append(cece)

            if datas_excluidas:
                msg = "Foram excluídas datas com sucesso!"
                conecta.commit()
                mensagem_alerta(msg)

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
            extraido_dados = extrair_tabela(self.table_Ponto)
            if extraido_dados:
                funcionario = self.combo_Func.currentText()
                funcionariotete = funcionario.find(" - ")
                id_funcionario = funcionario[:funcionariotete]
                nome_funcionario = funcionario[funcionariotete:]

                for i in extraido_dados:
                    data, sem, man_ini, man_fim, tar_ini, tar_fim, ext_ini, ext_fim, padrao, trab, saldo, tipo = i

                    date_entr = datetime.strptime(data, '%d/%m/%Y').date()
                    data_entr_certa = str(date_entr)

                    cursor = conecta.cursor()
                    cursor.execute(f"SELECT DATA, ID_FUNCIONARIO, UM_INI, UM_FIM, DOIS_INI, DOIS_FIM, "
                                   f"EXTRA_INI, EXTRA_FIM, TIPO "
                                   f"FROM horarios "
                                   f"WHERE ID_FUNCIONARIO = {id_funcionario} "
                                   f"AND DATA = '{date_entr}';")
                    registro_data = cursor.fetchall()

                    if registro_data:
                        cursor = conecta.cursor()
                        cursor.execute(f"UPDATE horarios SET UM_INI = '{man_ini}', "
                                       f"UM_FIM = '{man_fim}', "
                                       f"DOIS_INI = '{tar_ini}', "
                                       f"DOIS_FIM = '{tar_fim}', "
                                       f"EXTRA_INI = '{ext_ini}', "
                                       f"EXTRA_FIM = '{ext_fim}', "
                                       f"PADRAO = '{padrao}', "
                                       f"TRABALHADAS = '{trab}', "
                                       f"SALDO = '{saldo}', "
                                       f"TIPO = '{tipo}' "
                                       f"WHERE ID_FUNCIONARIO = {id_funcionario} "
                                       f"AND DATA = '{date_entr}';")

                    else:
                        cursor = conecta.cursor()
                        cursor.execute(f"Insert into horarios "
                                       f"(data, id_funcionario, um_ini, um_fim, dois_ini, dois_fim, "
                                       f"extra_ini, extra_fim, padrao, trabalhadas, saldo, tipo) "
                                       f"values ('{data_entr_certa}', {id_funcionario}, '{man_ini}', '{man_fim}', "
                                       f"'{tar_ini}', '{tar_fim}', '{ext_ini}', '{ext_fim}', "
                                       f"'{padrao}', '{trab}', '{saldo}', '{tipo}');")

                conecta.commit()
                mensagem_alerta(f'O horários de {nome_funcionario} foram salvos com sucesso!')

            self.limpa_tudo()

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

        finally:
            if 'conexao' in locals():
                conecta.close()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaPonto()
    tela.show()
    qt.exec_()
