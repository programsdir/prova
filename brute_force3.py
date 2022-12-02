import os
import random, pyautogui
import sys, pkg_resources
if __name__ == '__main__':
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    list_alfabeto = list(alfabeto)
    passw = pyautogui.password("Inserisci la password da Testare")
    passwo = ""
    count = 0
    while(passwo != passw):
        passwo = random.choices(list_alfabeto, k=len(passw))
        print("Password Testata ----->" + str(passwo) + "<------")
        count += 1
        if(passwo == list(passw)):
            print("Password Trovata dopo " + str(count) + " tentativi")
            os.system("pause")
            sys.exit(0)