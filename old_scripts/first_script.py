import requests

API_KEY=''

#estrae i synsets
def get_synset_ids_hyp(word):
    # Definisci l'URL dell'API di BabelNet
    url = "https://babelnet.io/v6/getSynsetIds"

    # Parametri della richiesta
    params = {"lemma": word, "searchLang": "IT", "key":API_KEY}

    # Effettua la richiesta per ottenere gli ID dei synset per la parola
    response = requests.get(url, params=params)
    # Restituisci gli ID dei synset
    return response.json()

def get_synset_ids_syn(word):
    # Definisci l'URL dell'API di BabelNet
    url = "https://babelnet.io/v6/getSynsetIds"

    # Parametri della richiesta
    params = {"word": word, "lang": "IT"}

    # Effettua la richiesta per ottenere gli ID dei synset per la parola
    response = requests.get(url, params=params)

    # Restituisci gli ID dei synset
    return response.json()

#controlla se sono sinonimi
def are_synonyms(word1, word2):
    # Ottieni gli ID dei synset per entrambe le parole
    synset_ids_word1 = set(get_synset_ids_syn(word1))
    synset_ids_word2 = set(get_synset_ids_syn(word2))

    # Controlla se ci sono synset in comune
    if synset_ids_word1.intersection(synset_ids_word2):
        return True
    else:
        return False

#meronym, aponym e hypernym
def get_hypernyms(word):
    # Ottieni gli ID dei synset per la parola
    synset_ids = get_synset_ids_hyp(word)

    # Se non ci sono synset per la parola, restituisci una lista vuota
    if not synset_ids:
        return []
    id=synset_ids[0]["id"]
    # Definisci l'URL dell'API di BabelNet per ottenere gli iperonimi
    url = f"https://babelnet.io/v6/getOutgoingEdges?id={id}&key={API_KEY}&filter=HYPERNYM"
    # Effettua la richiesta per ottenere gli iperonimi
    response = requests.get(url)
    #for edge in response.json():
    #    print(edge)
    # Estrai gli iperonimi dalle risposte
    hypernyms = [edge["target"] for edge in response.json()]
    return hypernyms

def is_hypernym(word1, word2):
    # Ottieni gli iperonimi per entrambe le parole
    hypernyms_word1 = set(get_hypernyms(word1))
    hypernyms_word2 = set(get_hypernyms(word2))

    # Controlla se una delle parole è un iperonimo dell'altra
    if hypernyms_word1 & hypernyms_word2:
        return True
    else:
        return False

# Esempio di utilizzo
word1 = "animale"
word2 = "cane"

if is_hypernym(word1, word2):
    print(f"{word1} è un iperonimo di {word2} o viceversa.")
else:
    print(f"{word1} non è un iperonimo di {word2} e viceversa.")


print(is_hypernym(word1,word2) or are_synonyms(word1, word2))
