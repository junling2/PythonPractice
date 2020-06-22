

def send_mail(text='Email Body', subject ='Test Email', dest_emails=None):
    assert isinstance(dest_emails, list)