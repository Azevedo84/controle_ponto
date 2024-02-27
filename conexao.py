import mysql.connector
from mysql.connector import errorcode

try:
    conecta = mysql.connector.connect(
        host='controle-ponto.mysql.uhserver.com',
        user='ivania_ruckert',
        password='1@Xkb9{l36',
        database='controle_ponto')

    print("eu aqui")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        msgerro = "Usuário ou senha incorretos!"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        msgerro = "Banco de Dados não existe!"
    elif err.errno == errorcode.CR_CONN_HOST_ERROR:
        msgerro = "Endereço TCP/IP não encontrado!"
    else:
        msgerro = err
