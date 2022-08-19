import nltk, json, random, pickle
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from tensorflow.keras.models import load_model

class Chat:

    def __init__(self, intents):
        self.intents = intents
        self.lemmatizer = WordNetLemmatizer()
        self.model = load_model('chatbot_model.h5')
        self.words = pickle.load(open('words.pkl','rb'))
        self.classes = pickle.load(open('classes.pkl','rb'))

    # preprocessamento input utente
    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(self, sentence)
        sentence_words = [self, lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    # creazione bag of words
    def bow(self, sentence, words, show_details=True):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0]*len(words)
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))

    def calcola_pred(self, sentence, model):
        p = self.bow(sentence, self.words,show_details=False)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
        return return_list

    def get_response(self, ints, intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tag):

                result = random.choice(i['responses'])
                if(i['responses']== "Le envio el reporte de matriculados"):
                    result += "el numero es 5"
                break
        return result

    def begin(self, msg):
        ints = self.calcola_pred(msg, self.model)
        res = self.getRisposta(ints, self.intents)
        return res