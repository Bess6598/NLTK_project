import sys
import datetime
import utils
import corpus


def exec(file_name1, file_name2):
    corpus1 = corpus.Corpus(file_name1)
    corpus2 = corpus.Corpus(file_name2)
    # Output file
    output = open("output_prj2" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".txt", "w+", encoding='utf8')
    # 10 most frequent person's name:
    utils.print_array_file(output, "10 more frequent person's name in " + corpus1.get_name(),
                           corpus1.find_category("PERSON")[:10])
    utils.print_array_file(output, "10 more frequent person's name in " + corpus2.get_name(),
                           corpus2.find_category("PERSON")[:10])
    # Iterating the 10 most frequent person's name of corpus1
    for key, value in corpus1.sentence_containing_name(10).items():
        # True is used to print the sentences without punctuation symbols
        # All the sentences that contains the 10 most frequent person's name
        utils.print_array_file(output, "Sentences that contain " + key + " in " + corpus1.get_name(), value, True)
        # Shortest and longest sentence that contains the key (name)
        utils.print_var_file(output, "Shortest sentence that contain " + key + " in " + corpus1.get_name(),
                             corpus1.min_max_sentence(key)[0], True)
        utils.print_var_file(output, "Longest sentence that contain " + key + " in " + corpus1.get_name(),
                             corpus1.min_max_sentence(key)[1], True)
        # Places contained in sentences that also contain key (name)
        utils.print_array_file(output, "Places contained in sentences that also contain " + key + " in " + corpus1.get_name(), corpus1.find_category("GPE", key), True)
    # Iterating the 10 most frequent person's name of corpus2
    for key, value in corpus2.sentence_containing_name(10).items():
        # True is used to print the sentences without punctuation symbols
        # All the sentences that contains the 10 most frequent person's name
        utils.print_array_file(output, "Sentences that contain " + key + " in " + corpus2.get_name(), value, True)
        # Shortest and longest sentence that contains the key (name)
        utils.print_var_file(output, "Shortest sentence that contain " + key + " in " + corpus2.get_name(),
                             corpus2.min_max_sentence(key)[0], True)
        utils.print_var_file(output, "Longest sentence that contain " + key + " in " + corpus2.get_name(),
                             corpus2.min_max_sentence(key)[1], True)
        # Places contained in sentences that also contain key (name)
        utils.print_array_file(output, "Places contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_category("GPE", key), True)

    #   i 10 luoghi più frequenti (ordine decrescente)
    #   le 10 persone più frequenti (ordine decrescente)
    #   i 10 verbi più frequenti (ordine decrescente)
    #   date, mesi, giorni della settimana (con espressioni regolari) (ordine decrescente)
    #   frase lunga minimo 8 e massimo 12 token conprobabilità più alta (Markovv di ordine 0, che usa la distribuzione di frequenza estratte dall'intero libro)
    output.close()


exec(sys.argv[1], sys.argv[2])
