import sys
import datetime
import utils
import corpus


def exec(file_name1, file_name2):
    corpus1 = corpus.Corpus(file_name1)
    corpus2 = corpus.Corpus(file_name2)
    # Output file
    output = open("output_prj2" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".txt", "w+", encoding='utf8')

    # 10 most frequent person's name in Corpus1:
    utils.print_array_file(output, "10 more frequent person's name in " + corpus1.get_name(),
                           corpus1.find_pos_category("PERSON")[:10])
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
        utils.print_array_file(output,
                               "Places contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_pos_category("GPE", key)[:10], True)
        # Other name contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Other person's name contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_pos_category("PERSON", key)[:10], True)
        # Noun contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Nouns contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_grammar_category("NOUN", key)[:10], True)
        # Verbs contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Verbs contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_grammar_category("VERB", key)[:10], True)
        # Dates contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Dates contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_all_date_regex(key), True)
        # Months names contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Months names contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_month_regex(key))
        # Months names contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Day of the week contained in sentences that also contain " + key + " in " + corpus1.get_name(),
                               corpus1.find_day_week_regex(key))

    # 10 most frequent person's name in corpus 2:
    utils.print_array_file(output, "10 more frequent person's name in " + corpus2.get_name(),
                           corpus2.find_pos_category("PERSON")[:10])
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
        utils.print_array_file(output,
                               "Places contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_pos_category("GPE", key)[:10], True)
        # Other name contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Other person's name contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_pos_category("PERSON", key)[:10], True)
        # Noun contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Nouns contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_grammar_category("NOUN", key)[:10], True)
        # Verbs contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Verbs contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_grammar_category("VERB", key)[:10], True)
        # Dates contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Dates contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_all_date_regex(key), True)
        # Months names contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Months names contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_month_regex(key))
        # Months names contained in sentences that also contain key (name)
        utils.print_array_file(output,
                               "Day of the week contained in sentences that also contain " + key + " in " + corpus2.get_name(),
                               corpus2.find_day_week_regex(key))

    #   frase lunga minimo 8 e massimo 12 token con probabilità più alta (Markovv di ordine 0, che usa la distribuzione di frequenza estratte dall'intero libro)find_category
    output.close()


exec(sys.argv[1], sys.argv[2])
