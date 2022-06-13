#parte 1 coletar dados
import rpa as r
import pyautogui as p
import pandas as pd

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(2)
p.getActiveWindow().maximize()
dolar= r.read('//*[@id="comercial"]')
r.close()

print(dolar)

# #parte 2 enviar via email # aqui deu ruim fazer viar google services
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # #texto do email
# texto_email =   dolar + 'hoje ' + str(pd.Timestamp)

# # # email remetente, senha, destinatário
# de = 'andremarcinichen@hotmail.com'
# senha = '' # aqui deu ruim fazer viar google services
# para = 'andremarcinichen@hotmail.com'
# #para02 = ''

# # # Setup the MIME
# message = MIMEMultipart()
# message['From'] = de
# message['To'] = para
# #message['To'] = para02
# message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# # # Corpo do E-mail com anexos
# message.attach(MIMEText(texto_email, 'plain'))

# # # Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.office365.com', 587)  # Usuário do Gmail com porta
# session.starttls()  # Habilita a segurança
# session.login(de, senha)  # Login e senha de quem envia o e-mail
# texto = message.as_string()
# session.sendmail(de, para, texto)
# session.quit()