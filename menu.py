import sys
from forms.tela_menu import *
from ponto import TelaPonto
from cad_empresa import TelaEmpresa
from cad_funcionario import TelaFuncionario
from funcao_padrao import grava_erro_banco, trata_excecao, lanca_tabela
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
import inspect
import os
import requests
from collections import defaultdict
from datetime import datetime
import bs4


def mensagem_temperatura(temp, descr_clima):
    try:
        if descr_clima == "ensolarado":
            if temp > 30:
                mensagem = f"Dia quente e ensolarado com {temp}ºC!\n" \
                           f"Não se esqueça do protetor solar. Use roupas leves, como shorts e camisetas."
            elif temp > 20:
                mensagem = f"Dia ensolarado agradável com {temp}ºC!\n" \
                           f"Perfeito para atividades ao ar livre. " \
                           f"Vista roupas confortáveis, como calças leves e camisas de manga curta."
            else:
                mensagem = f"Dia ensolarado, mas um pouco fresco com {temp}ºC!\n" \
                           f"Vista-se adequadamente com roupas de manga longa ou uma jaqueta leve."
        elif descr_clima == "nublado":
            if temp > 25:
                mensagem = f"Dia nublado, mas ainda bastante quente com {temp}ºC!\n" \
                           f"Aproveite! Vista roupas frescas e confortáveis."
            elif temp > 15:
                mensagem = f"Céu nublado, temperatura amena com {temp}ºC!\n" \
                           f"Um bom dia para passeios. Vista-se com roupas leves e tenha uma jaqueta por precaução."
            else:
                mensagem = f"Dia nublado e fresco com {temp}ºC!\n" \
                           f"Considere vestir uma jaqueta leve e roupas confortáveis."
        elif descr_clima == "chuvoso":
            if temp > 20:
                mensagem = f"Chuva esperada com {temp}ºC!\n" \
                           f"Não esqueça seu guarda-chuva. Use roupas à prova d'água e botas impermeáveis."
            else:
                mensagem = f"Dia chuvoso e fresco com {temp}ºC!\n" \
                           f"Vista-se com roupas à prova d'água e tenha um guarda-chuva."
        elif descr_clima == "chuva leve":
            if temp > 18:
                mensagem = f"Chuva leve esperada com {temp}ºC!\n" \
                           f"Tenha um guarda-chuva à mão. Vista roupas impermeáveis se possivel."
            else:
                mensagem = f"Chuva leve e fresca com {temp}ºC!\n" \
                           f"Considere vestir uma jaqueta impermeável e roupas confortáveis."
        elif descr_clima == "chuva moderada":
            if temp > 22:
                mensagem = f"Chuva moderada esperada com {temp}ºC!\n" \
                           f"Leve um guarda-chuva e vista roupas impermeáveis."
            else:
                mensagem = f"Chuva moderada e fresca com {temp}ºC!\n" \
                           f"Considere vestir uma jaqueta impermeável e roupas confortáveis."
        else:
            mensagem = f"{descr_clima} com {temp}ºC!"

        return mensagem

    except Exception as e:
        nome_funcao = inspect.currentframe().f_code.co_name
        nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
        nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
        trata_excecao(nome_funcao, str(e), nome_arquivo)
        grava_erro_banco(nome_funcao, e, nome_arquivo)


class TelaMenu(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.label_Versao.setText("VERSÃO 1.01.004 - 22/03/2024")

        self.cartao_ponto = []
        self.cad_empresa = []
        self.cad_funcionario = []

        self.definir_tamanho_aplicacao()

        self.btn_Ponto.clicked.connect(self.chama_ponto)
        self.btn_Empresa.clicked.connect(self.chama_cad_empresa)
        self.btn_Func.clicked.connect(self.chama_cad_funcionario)

        self.inicio_temperatura()
        self.inicio_previsao_temp()
        self.inicio_noticia1()
        self.inicio_noticia2()

    def chama_ponto(self):
        self.cartao_ponto = TelaPonto()
        self.cartao_ponto.show()

    def chama_cad_empresa(self):
        self.cad_empresa = TelaEmpresa()
        self.cad_empresa.show()

    def chama_cad_funcionario(self):
        self.cad_funcionario = TelaFuncionario()
        self.cad_funcionario.show()

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

    def inicio_temperatura(self):
        try:
            # link do open_weather: https://openweathermap.org/

            api_key = "94f1bd23041ee6db0bdf444cfff72e43"
            cidade = "Estância Velha"
            link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br"

            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()
            descricao_clima = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp'] - 273.15
            temperatura_celsius = int(round(temperatura, 0))

            mensagem = mensagem_temperatura(temperatura_celsius, descricao_clima)
            self.label_Temp.setText(mensagem)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def inicio_previsao_temp(self):
        try:
            api_key = "94f1bd23041ee6db0bdf444cfff72e43"
            cidade = "ivoti"
            link = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={api_key}&lang=pt_br"

            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()

            previsoes = requisicao_dic['list']

            previsoes_por_dia = defaultdict(list)

            for previsao in previsoes:
                data = previsao['dt_txt'].split(' ')[0]
                descricao = previsao['weather'][0]['description']
                temperatura = previsao['main']['temp'] - 273.15
                temperatura_celsius = int(round(temperatura, 0))
                previsoes_por_dia[data].append((descricao, temperatura_celsius))

            mensagem_previsao = ""
            tabelas = []
            for dia, previsoes_do_dia in previsoes_por_dia.items():
                data_formato_original = datetime.strptime(dia, '%Y-%m-%d')
                data_formatada = data_formato_original.strftime('%d/%m/%Y')

                dia_semana = data_formato_original.weekday()
                dias_da_semana = ["SEGUNDA-FEIRA", "TERÇA-FEIRA", "QUARTA-FEIRA", "QUINTA-FEIRA",
                                  "SEXTA-FEIRA", "SÁBADO", "DOMINGO"]
                nome_dia = dias_da_semana[dia_semana]
                espacos = " " * (15 - len(nome_dia))

                media_temperatura = sum([temp for _, temp in previsoes_do_dia]) / len(previsoes_do_dia)
                media_arred = int(round(media_temperatura, 0))

                mensagem_previsao += f'- {data_formatada} {nome_dia}:{espacos} {media_arred}ºC - ' \
                                     f'{previsoes_do_dia[0][0]}\n'
                dados = (data_formatada, nome_dia, f"{media_arred}ºC", previsoes_do_dia[0][0])
                tabelas.append(dados)

            if mensagem_previsao:
                lanca_tabela(self.table, tabelas)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def inicio_noticia1(self):
        try:
            noticias1 = ''
            noticias2 = ''

            url = 'https://globoesporte.globo.com/futebol/times/gremio/'

            requisicao = requests.get(url)

            pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")

            lista_noticias = pagina.find_all("a", class_="feed-post-link")

            for noticia in lista_noticias:
                noti = noticia.text
                link = noticia.get("href")

                noticias1 += noti
                noticias2 += f'Clique <a href="{link}">aqui</a> para visitar o site.'

                break

            self.label_Not1.setText(noticias1)
            self.label_Not2.setOpenExternalLinks(True)
            self.label_Not2.setText(noticias2)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)

    def inicio_noticia2(self):
        try:
            noticias1 = ''
            noticias2 = ''

            url = 'https://www.abcmais.com/ultimas-noticias/'

            requisicao = requests.get(url)

            pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")

            lista_noticias = pagina.find_all("a", class_="wp-block-latest-posts__post-title")

            for noticia in lista_noticias:
                noti = noticia.text
                link = noticia.get("href")

                noticias1 += noti
                noticias2 += f'Clique <a href="{link}">aqui</a> para visitar o site.'

                break

            self.label_Not3.setText(noticias1)
            self.label_Not4.setOpenExternalLinks(True)
            self.label_Not4.setText(noticias2)

        except Exception as e:
            nome_funcao = inspect.currentframe().f_code.co_name
            nome_arquivo_com_caminho = inspect.getframeinfo(inspect.currentframe()).filename
            nome_arquivo = os.path.basename(nome_arquivo_com_caminho)
            trata_excecao(nome_funcao, str(e), nome_arquivo)
            grava_erro_banco(nome_funcao, e, nome_arquivo)


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tela = TelaMenu()
    tela.show()
    qt.exec_()
