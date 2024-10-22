def code(c,m):
    cle = c
    Messageacrypter = m
    acrypter=Messageacrypter.upper()
    lg=len(acrypter)
    MessageCrypte=""

    for i in range(lg):
        if acrypter[i]==' ':
            MessageCrypte+=' '
        else:
            asc= ord(acrypter[i])+cle
        if asc >90:
                asc-=26
        MessageCrypte += chr(asc)

    print (MessageCrypte)
code(2,"bonjour tout le monde")
