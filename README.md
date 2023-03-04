# NLTK project
Progetto finale per il corso di linguistica computazionale di informatica umanistica dell'università di Pisa.
Il progetto consiste in un programma python in grado di:
* calcolare il numero totale di frasi e di token;
* calcolare la lunghezza media delle frasi in termini di token e la lunghezza media delle parole in termini di caratteri;
* calcolare la grandezza del vocabolario e la distribuzione degli hapax;
* calcolare la grandezza del vocabolario e la distribuzione degli hapax all'aumentare del corpus per porzioni incrementali di token;
* il rapporto tra categorie grammaticali come Sostantivi e Verbi;
* le PoS (Part-of-Speech) più frequenti;
* estraete ed ordinate i bigrammi di PoS;
* calcolare i bigrammi di POS con la relativa probabilità;
* calcolare i bigrammi di POS con relativa forza associativa (calcolata in termini di Local Mutual Information),
* estrarre  (con possibilità di specificare una stringa che deve essere contenuta nella frase):
    * nomi di persona;
    * luoghi;
    * organizzazioni;
    * date;
    * orari;
    * soldi;
    * percentuali;
    * servizi;
    * strutture.
* la frase più lunga e la frase più breve (con possibilità di specificare una stringa che deve essere contenuta nella frase);
* estrarre le parole appartenenti a categorie grammaticali con relativa frequenza e in ordine decrescente (con possibilità di specificare una stringa che deve essere contenuta nella frase);
* estrarre le date in tutti i formati con espressioni regolari con relativa frequenza e in ordine decrescente (con possibilità di specificare una stringa che deve essere contenuta nella frase) (con possibilità di specificare una stringa che deve essere contenuta nella frase);
* estrarre date in un particolare formato (da specificare) con espressioni regolari;
* estrarre nomi di mesi con espressioni regolari con relativa frequenza e in ordine decrescente (con possibilità di specificare una stringa che deve essere contenuta nella frase) (con possibilità di specificare una stringa che deve essere contenuta nella frase);
* estrarre nomi di giorni della settimana con espressioni regolari con relativa frequenza e in ordine decrescente (con possibilità di specificare una stringa che deve essere contenuta nella frase) (con possibilità di specificare una stringa che deve essere contenuta nella frase);
* calcolare la probabilità delle frasi del corpus con catena di Markov di ordine 0 (con possibilità di specificare una stringa che deve essere contenuta nella frase e la lunghezza minima e/o massima delle frasi).

<hr>

Final project for the computational linguistics course in humanistic computing at the University of Pisa. 
The project consists of a python program capable of:
* calculate the total number of sentences and tokens;
* calculate the average length of sentences in terms of tokens and the average length of words in terms of characters;
* calculate vocabulary size and hapax distribution;
* calculate vocabulary size and hapax distribution as the corpus increases for incremental portions of tokens;
* the relationship between grammatical categories such as Nouns and Verbs;
* the most frequent PoS (Part-of-Speech);
* extract and sort PoS bigrams;
* compute POS bigrams with relative probability;
* compute POS bigrams with relative associative strength (computed in terms of Local Mutual Information),
* extract (with possibility of specifying a string to be contained in the sentence): 
    * person names; 
    * places; 
    * organizations; 
    * dates; 
    * times; 
    * money; 
    * percentages; 
    * services;
    * facilities.
* the longest sentence and the shortest sentence (with the possibility of specifying a string that must be contained in the sentence);
* extract words belonging to grammatical categories with relative frequency and in descending order (with possibility of specifying a string that must be contained in the sentence);
* extract dates in all formats with regular expressions with relative frequency and in descending order (with possibility of specifying a string that must be contained in the sentence) (with possibility of specifying a string that must be contained in the sentence);
* extract dates in a particular format (to be specified) with regular expressions;
* extract names of months with regular expressions with relative frequency and in descending order (with possibility of specifying a string that must be contained in the sentence) (with possibility of specifying a string that must be contained in the sentence);
* extract names of days of the week with regular expressions with relative frequency and in descending order (with possibility of specifying a string that must be contained in the sentence) (with possibility of specifying a string that must be contained in the sentence);
* calculate the probability of the sentences in the corpus with Markov chain of order 0 (with possibility of specifying a string that must be contained in the sentence and the minimum and/or maximum length of the sentences).
