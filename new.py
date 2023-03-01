from phonebook import *
def phonebook(name,no):
    global contact
    
    # contact={}
    contact.update({name:no})
    return contact

contact={}
phonebook("HG","2")

phonebook("cuw","12358558")
print(contact)