import sys
import datetime
import utils
import corpus


def exec(file_name1, file_name2):
    corpus1 = corpus.Corpus(file_name1)
    corpus2 = corpus.Corpus(file_name2)
    # Output file
    output = open("output_prj2" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".txt", "w+", encoding='utf8')
    # estrarre i 10 nomi propri di persona più frequenti con relative informazioni:
    corpus1.human_name()
    #   restituire la frase più lunga e più corta
    #   i 10 luoghi più frequenti (ordine decrescente)
    #   le 10 persone più frequenti (ordine decrescente)
    #   i 10 verbi più frequenti (ordine decrescente)
    #   date, mesi, giorni della settimana (con espressioni regolari) (ordine decrescente)
    #   frase lunga minimo 8 e massimo 12 token conprobabilità più alta (Markovv di ordine 0, che usa la distribuzione di frequenza estratte dall'intero libro)
    output.close()


exec(sys.argv[1], sys.argv[2])
