def send_emails_via_Outlook_with_attachment(from_who, to_who, subject , body, files_dir, files_with_extension, password):
        msg = MIMEMultipart()

        msg['To'] = ", ".join(to_who)
        msg['From'] = from_who
        msg['Subject'] = subject

        body = MIMEText(body, 'html', 'utf-8')  
        msg.attach(body)  # add message body (text or html)


        for f in files_with_extension:  # add files to the message
                file_path = os.path.join(files_dir, f)
                attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
                attachment.add_header('Content-Disposition','attachment', filename=f)
                msg.attach(attachment)

        Outlook_server = smtplib.SMTP('smtp.office365.com:587')
        Outlook_server.starttls()
        Outlook_server.login(from_who,password)
        Outlook_server.sendmail(msg['From'], to_who, msg.as_string())
        Outlook_server.close()
        print("finished sending emails")
