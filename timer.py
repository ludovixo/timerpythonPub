import os
import time
import subprocess

print(
    "sono il Timer\n"
    "istruzioni: inserisci questo bot nella cartella dove è presente il file da eseguire "
    "e ricordati di rispondere a tutte le domande del bot\n\n")

print("da quanti secondi vuoi impostare il timer?")
timer = input()
print("inserisci il percorso per eseguire un file")
nome = input()
print("bene, sono pronto! il tuo file verrà avviato alla fine del timer")

time.sleep(int(timer))
#os.startfile("pippo.txt")
#os.system("cd Desktop/codici/timerpython/pippo.txt")
subprocess.run(['notepad.exe', str(nome)])