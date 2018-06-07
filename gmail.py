import imaplib
import getpass

func = imaplib.IMAP4_SSL('imap.gmail.com', '993')
name = raw_input("Username:")
paswd = getpass.getpass("Password:")
func.login(name,paswd) 
func.select('Inbox') 

typ ,data = func.search(None,'UnSeen')
func.store(data[0].replace(' ',','),'+FLAGS','\Seen')
