import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo, quantidade):
    # Configurar informações do remetente
    remetente = 'seu_email'
    senha = 'senha_do_seu_email'
    
    # Configurar o servidor SMTP do Outlook
    # ===== se for google colocar smpt@gmail.com =====
    servidor_smtp = 'smtp.office365.com'
    porta_smtp = 587
    
    for _ in range(quantidade):
        mensagem = MIMEText(corpo)
        mensagem['Subject'] = assunto
        mensagem['From'] = remetente
        mensagem['To'] = destinatario
        
        # Iniciar a conexão com o servidor SMTP do Outlook
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        
        # Logar no servidor
        servidor.login(remetente, senha)
        
        # Enviar e-mail
        servidor.sendmail(remetente, destinatario, mensagem.as_string())
        
        # Fechar a conexão
        servidor.quit()

# Exemplo de uso com uma lista de destinatários e quantidade de e-mails
destinatarios = ['email_Aqui', '', '']
assunto = 'Sr Otarioooo'
corpo = 'senhor otario va mandar golpe para a puta q te pariuuuuu'
quantidade_de_emails = 200  # Altere este valor para a quantidade desejada

for destinatario in destinatarios:
    enviar_email(destinatario, assunto, corpo, quantidade_de_emails)
