import sys
import datetime
import utils
import corpus


def exec(file_name1, file_name2):
    corpus1 = corpus.Corpus(file_name1)
    corpus2 = corpus.Corpus(file_name2)
    # Output file
    output = open("output_prj1" + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S") + ".txt", "w+", encoding='utf8')
    # Number of sentence
    utils.print_var_file(output, "Number of sentence in " + corpus1.get_name(), corpus1.get_n_sentences())
    utils.print_var_file(output, "Number of sentence in " + corpus2.get_name(), corpus2.get_n_sentences())
    # Number of tokens
    utils.print_var_file(output, "Number of tokens in " + corpus1.get_name(), corpus1.get_n_token())
    utils.print_var_file(output, "Number of tokens in " + corpus2.get_name(), corpus2.get_n_token())
    # Mean of number of token in the sentences
    utils.print_var_file(output, "Mean of number of tokens in the sentences of " + corpus1.get_name(),
                         corpus1.mean_sentences())
    utils.print_var_file(output, "Mean of number of tokens in the sentences of " + corpus2.get_name(),
                         corpus2.mean_sentences())
    # Mean of number of letters in the tokens
    utils.print_var_file(output, "Mean of number of letter in the tokens of " + corpus1.get_name(),
                         corpus1.mean_token())
    utils.print_var_file(output, "Mean of number of letter in the tokens of " + corpus2.get_name(),
                         corpus2.mean_token())
    # Vocabulary incremental length
    utils.print_dict_file(output, "Vocabulary incremental length in " + corpus1.get_name(),
                          corpus1.incremental_vocabulary_length())
    utils.print_dict_file(output, "Vocabulary incremental length in " + corpus2.get_name(),
                          corpus2.incremental_hapax_distribution())
    # Hapax incremental distribution
    utils.print_dict_file(output, "Hapax incremental distribution in " + corpus1.get_name(),
                          corpus1.incremental_hapax_distribution())
    utils.print_dict_file(output, "Hapax incremental distribution in " + corpus2.get_name(),
                          corpus2.incremental_hapax_distribution())
    # Ratio between nouns and verbs
    utils.print_var_file(output, "Ration between NOUN and VERB in " + corpus1.get_name(), corpus1.ratio("NOUN", "VERB"))
    utils.print_var_file(output, "Ration between NOUN and VERB in " + corpus2.get_name(), corpus2.ratio("NOUN", "VERB"))
    # 10 most common POS tag
    utils.print_array_file(output, "10 most Common POS-tag in " + corpus1.get_name(), corpus1.most_frequent_pos()[:10])
    utils.print_array_file(output, "10 most Common POS-tag in " + corpus2.get_name(), corpus2.most_frequent_pos()[:10])
    # 10 bigrams with highest conditional probability
    utils.print_array_file(output, "10 bigrams with highest conditional probability in " + corpus1.get_name(),
                           corpus1.conditioned_probability()[:10])
    utils.print_array_file(output, "10 bigrams with highest conditional probability in " + corpus2.get_name(),
                           corpus2.conditioned_probability()[:10])
    # 10 bigrams with highest local mutual information
    utils.print_array_file(output, "10 bigrams with highest local mutual information in " + corpus1.get_name(),
                           corpus1.collocations()[:10])
    utils.print_array_file(output, "10 bigrams with highest local mutual information in " + corpus2.get_name(),
                           corpus2.collocations()[:10])
    output.close()


exec(sys.argv[1], sys.argv[2])
