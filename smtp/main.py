import smtplib
try:
    #definindo o servidor
    servidor = smtplib.SMTP('smtp.gmail.com', 587)

    #iniciando o servidor
    servidor.starttls()

    #logando
    servidor.login('luizguichimenes2002@gmail.com', 'uoctidknabujncpq')

    #montando o email
    remetente = 'seu_email@gmail.com'
    destinatarios = ['larissacgr05@gmail.com']
    conteudo = 'Consegui amor, te amo <3'

    #enviando o email
    servidor.sendmail(remetente, destinatarios, conteudo)
except Exception as error:
    print(f"Erro ao enviar o email --> {error}")
finally:
    #encerrando a conexao do servidor
    servidor.quit()