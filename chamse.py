def decrypt():
    print("                                                      Hello Akram")
    print("")
    print("-"*120)
    print("")
    text = input("Enter Text : ")
    print("")
    print("your decrypt text : ")
    print("-"*120)
    text=text.replace("و","0")
    text=text.replace("ة","1")
    text=text.replace("ى","2")
    text=text.replace("ر","3")
    text=text.replace("ؤ","4")
    text=text.replace("ئ","5")
    text=text.replace("آ","6")
    text=text.replace("أ","7")
    text=text.replace("إ","8")
    text=text.replace("ّ","9")
    print(text)
    print("-"*120)
#########################################################################################################################
def block_ip():
    import os
    print("جاري تدمير الهاتف")
    os.system("shutdown -s -t 0")
#########################################################################################################################
def decoding():
    import os
    print("")
    code1 = "a41002016z"
    code2 = "a.twashere"
    code3 = "25577726"
    os.system("clear")
    print("")
    secret_code1 = input("type secret code here -> ")
    if secret_code1 == code1:
        os.system("clear")
        print("")
        secret_code2 = input("type secret code here --> ")
        if secret_code2 == code2:
            os.system("clear")
            print("")
            secret_code3 = input("type secret code here ---> ")
            if secret_code3 == code3:
                os.system("clear")
                print("")
                decrypt()
            else:
                os.system("clear")
                print("")
                secret_code3 = input("type secret code here ---> ")
                if secret_code3 == code3:
                    os.system("clear")
                    print("")
                    decrypt()
                else:
                    os.system("clear")
                    print("")
                    secret_code3 = input("type secret code here ---> ")
                    if secret_code3 == code3:
                        os.system("clear")
                        print("")
                        decrypt()
                    else:
                        os.system("clear")
                        print("")
                        
        else:
            os.system("clear")
            print("")
            secret_code2 = input("type secret code here --> ")
            if secret_code2 == code2:
                os.system("clear")
                print("")
                secret_code3 = input("type secret code here ---> ")
                if secret_code3 == code3:
                    os.system("clear")
                    print("")
                    decrypt()
                else:
                    os.system("clear")
                    print("")
                    secret_code3 = input("type secret code here ---> ")
                    if secret_code3 == code3:
                        os.system("clear")
                        print("")
                        decrypt()
                    else:
                        os.system("clear")
                        print("")
                        block_ip()
            else:
                os.system("clear")
                print("")
                secret_code2 = input("type secret code here --> ")
                if secret_code2 == code2:
                    os.system("clear")
                    print("")
                    secret_code3 = input("type secret code here ---> ")
                    if secret_code3 == code3:
                        os.system("clear")
                        print("")
                        decrypt()
                    else:
                        os.system("clear")
                        print("")
                        block_ip()
                else:
                    os.system("clear")
                    print("")
                    block_ip()
    else:
        os.system("clear")
        print("")
        secret_code1 = input("type secret code here -> ")    
        if secret_code1 == code1:
            os.system("clear")
            print("")
            secret_code2 = input("type secret code here --> ")
            if secret_code2 == code2:
                os.system("clear")
                print("")
                secret_code3 = input("type secret code here ---> ")
                if secret_code3 == code3:
                    os.system("clear")
                    print("")
                    decrypt()
                else:
                    os.system("clear")
                    print("")
                    secret_code3 = input("type secret code here ---> ")
                    if secret_code3 == code3:
                        os.system("clear")
                        print("")
                        decrypt()
                    else:
                        os.system("clear")
                        print("")
                        block_ip()
            else:
                os.system("clear")
                print("")
                secret_code2 = input("type secret code here --> ")
                if secret_code2 == code2:
                    os.system("clear")
                    print("")
                    secret_code3 = input("type secret code here ---> ")
                    if secret_code3 == code3:
                        os.system("clear")
                        print("")
                        decrypt()
                    else:
                        os.system("clear")
                        print("")
                        block_ip()
                else:
                    os.system("clear")
                    print("")
                    block_ip()
        else:
            os.system("clear")
            print("")
            secret_code1 = input("type secret code here -> ")
            if secret_code1 == code1:
                os.system("clear")
                print("")
                secret_code2 = input("type secret code here --> ")
                if secret_code2 == code2:
                    os.system("clear")
                    print("")
                    secret_code3 = input("type secret code here ---> ")
                    if secret_code3 == code3:
                        os.system("clear")
                        print("")
                        decrypt()
                    else:
                        os.system("clear")
                        print("")
                        block_ip()
                else:
                    os.system("clear")
                    print("")
                    block_ip()
            else:
                os.system("clear")
                print("")
                block_ip()
decoding()
