from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import password_generator 

#Generating required length password
#Entering the site/app name and the USERNAME
u_pass=password_generator.password
domain=input("ENTER THE NAME OF WEBSITE/APP FOR WHICH YOU HAVE GENERATED PASSWORD:-")
u_name= input("ENTER THE USERNAME/EMAIL/PHONE NO. USED :-")

#connection Details
host="smtp.gmail.com"
port=587
username="email id"#on which you want the mail
password="Password"#password of the above email
from_email=username
to_list=("pyformail@gmail.com","afcafzal98@gmail.com")

#Setting secured connection
email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)

#Mail Formate
the_msg= MIMEMultipart("alternative")
the_msg["Subject"]="GENERATED PASSWORD FOR  " + domain
the_msg["From"]= from_email
the_msg["To"]=to_list[0]
plain_txt="YOUR CREDENTIAL FOR " + domain +":\n\nUSER ID : " +str(u_name) +"\nPASSWORD : " +str(u_pass)
part=MIMEText(plain_txt,"plain")
the_msg.attach(part)
#sending mail
email_conn.sendmail(from_email,the_msg["TO"],the_msg.as_string())
#closing connection
email_conn.quit()
