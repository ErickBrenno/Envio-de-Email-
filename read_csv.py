import pandas as pd #Biblioteca do Python para modelagem de Dados
import email.message #Biblioteca do Python para ler, escrever e enviar mensagens 
import smtplib #Biblioteca do Python para definir um objeto SMTP na pagina do Gmail.

#Criando um função, fazendo a leitura de um arquivo csv, e transformando em um Dataframe
def read_csv():
    DataFrame = pd.read_csv('./names_random.csv', sep=';')#Definindo o delimitador ";"

    return DataFrame
#Crinado um função para envio do E-mail
def send_email(): 
    #Montando o corpo do E-mail, em formato html, pois o gmail, é uma site web
    corpo_email = """
Olá, Erick! Esses foram os nomes de hoje<p>

<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(read_csv().to_html())

    #Definindo Remetentes, Destinatarios, Titulo do E-mail e Senha.
    msg = email.message.Message()
    msg['Subject'] = 'Meu primeiro E-mail'
    msg['From'] = 'Destinatarios'
    msg['To'] = 'Remetente'
    password = 'Sua senha ******'
    msg.add_header('Content-Type', 'text/html')
    #Carregando o corpo do E-mail
    msg.set_payload(corpo_email)

    #Fazendo a chamada SMTP no URL do gmail, passando a porta: 587
    s = smtplib.SMTP('smtp.gmail.com: 587')
    #Iniciando o request na página do gmail
    s.starttls()

    #Fazendo login 
    s.login(msg['From'], password)
    #Enviando E-mail
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email Enviando!')

#retornando a função de envio de E-mail (send_email) 
send_email()