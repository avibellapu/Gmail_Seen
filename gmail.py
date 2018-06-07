import imaplib
obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login('username', 'Password') #Enter your Username and Password
obj.select('Inbox')  # <--- it will select inbox
typ ,data = obj.search(None,'UnSeen')
obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')
