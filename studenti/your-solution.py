'''
REPO: pyckathon

PREMESSA:
L’esercizio serve ad allontanare le paure che ci possono affliggere all’idea di dover imparare da zero un nuovo linguaggio.
Se non ve ne siete accorti, negli ultimi mesi ne abbiamo imparati già due. Oggi però farete tutto da soli.

SCOPO DEL GIOCO:
Sicuramente avrete già giocato al gioco dell’impiccato sui banchi di scuola, nei momenti morti di alcune lezioni con il vostro vicino.
Uno dei giocatori pensa una parola e aggiunge su un foglio un numero di trattini pari al numero di lettere che la compongono.
L’altro giocatore dovrà indovinare la parola tentando di indovinare le lettere che la compongono.
Ogni tentativo sbagliato verrà contato come errore.

TECNOLOGIE:
Oggi si lavora con Python, per questo motivo dovete concentrarvi solo sul file YOUR_SOLUTION.py, non curatevi degli altri file.
Se volete poi dopo le 18.00 potrete sbirciare il resto del codice.
Ma l’escamotage che abbiamo usato per farvi lavorare tranquilli è solo un modo semplice e comodo per permettervi di lavorare senza distrazioni

CONSEGNA:
I giocatori sono l'utente e il computer.
Il computer sceglie casualmente una parola e l'utente la dovrà indovinare.
Ha a disposizione 5 tentativi.

L'utente potrà provare ad indovinare una sola lettera per volta.
Ad ogni inserimento (sia che avvenga tramite tasto INVIO oppure tramite CLICK su apposito pulsante) il computer deve controllare
se quella lettera è presente nella parola da indovinare.

Se la lettera è presente, deve apparire al posto giusto, sostituendo il trattino (o i trattini) corrispondente.
Se la lettera non è presente, l'utente deve essere avvisato dell'errore con un messaggio che mostra anche quanti tentativi sono rimasti.
Se la lettera è già stata usata, l'utente deve essere avvisato con un messaggio, ma i tentativi a disposizione non devono diminuire.

Nella parte sottostante il campo di input saranno mostrate tutte le lettere già utilizzate dall'utente (sia quelle corrette che quelle errate).

Il gioco termina quando l'utente esaurisce i tentativi a disposizione oppure se indovina la parola.
In entrambi i casi si deve mostrare un messaggio adatto alla situazione.
'''

# CONSIGLI:
# - occhio alla indentazione

#------------------------------------------LIBRERIE-------------------------------------------------------

import random   #libreria per usare un valore casuale
import pyodide  #libreria per pyscript
import js       #libreria per javascript
from utils import Utils #libreria per utilizzare funzioni JS

custom_utils = Utils(pyodide, js) #istanza della libreria - ripensate all'esercizio di PHP con Movie ;)

#---------------------------------------ELEMENTI DAL DOM------------------------------------------------------

# questi elementi sono già stati catturati per te, 
# ti serviranno per prendere il valore inserito e catturare l'evento di invio

user_letter = custom_utils.getHtmlElement("user-letter")

add_letter_btn = custom_utils.getHtmlElement("add-letter-btn")

# questo elemento conterrà il testo segnaposto per la parola da indovinare
word_html_container = custom_utils.getHtmlElement('word')
error_count = custom_utils.getHtmlElement('errors')
solution_html = custom_utils.getHtmlElement('solution')
result_html = custom_utils.getHtmlElement('result')

#----------------------------------------------------------------------------------------------------

def main():

    #le variabili sono definite come esempi, non siete obbligati ad utilizzarle tutte o solo queste

    global words
    global count
    global length
    global word
    global display
    global already_guessed
    global limit
    global wordList
 
    words = ['matto', 'gatto', 'pazzo'] # array con le parole da indovinare
    count = 5
    already_guessed = []

    # inserisco la stringa segnaposto dentro il contenitore HTML
    display = "___" # da modificare
    display = random.choice(words)
    word = display
    wordList = list(word)
    display = display.replace(display,'_',len(display))*len(display)
    # print(word)
    # print(wordList)
    custom_utils.writeToHtmlElement(word_html_container, '%s' % (display))

    
def checkLetters(event):
    # custom_utils.writeToConsole(user_letter.value) 
        global count
        global display 
        letteraUtente = user_letter.value
        user_letter.value = ""
        if (letteraUtente in wordList):
            display = transformString(letteraUtente, display)
            custom_utils.writeToHtmlElement(word_html_container, '%s' % (display))
        # custom_utils.writeToConsole('daje')
            for letter in wordList:
                custom_utils.writeToConsole(wordList.index(letteraUtente))
        else:
            count -= 1
            custom_utils.writeToHtmlElement(error_count, 'Tentativi rimasti: %s' % (count)) 
            if (count == 0):
                custom_utils.writeToHtmlElement(error_count, 'Tentativi esauriti, hai perso!')
                custom_utils.writeToHtmlElement(solution_html, "La parola da indovinare era: <span>%s</span>" % (word))
                custom_utils.disableInputElement(user_letter)
                custom_utils.removeOnClickEventFromHtmlElement (add_letter_btn)

        # custom_utils.writeToConsole(len(wordList))    
def transformString(letteraUtente, display):
    for index, currentLetter in enumerate(wordList):

        if currentLetter == letteraUtente:
            displayList = list(display)
            displayList[index] = letteraUtente
            display = "".join(displayList)
        if display.lower() == word.lower():
            custom_utils.writeToHtmlElement(result_html, "Hai VINTO!!!")
            custom_utils.disableInputElement(user_letter)
            custom_utils.removeOnClickEventFromHtmlElement (add_letter_btn)
    return display
custom_utils.addOnClickEventToHtmlElement (add_letter_btn, checkLetters)
    
# custom_utils.addKeyupEventToHtmlElement (user_letter, checkLetters)
    

main()