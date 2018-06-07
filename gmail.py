import imaplib
import getpass

obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
name = raw_input("Username:")
paswd = getpass.getpass("Password:")
obj.login(name,paswd) 
obj.select('Inbox') 
typ ,data = obj.search(None,'UnSeen')
obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')
