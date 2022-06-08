class Utils:

    def __init__(self, pyodide, js):
        self.pyodide = pyodide
        self.js = js
        self.document = js.document

    # getHtmlElement
    def getHtmlElement(self, id):
        """
        La funzione torna un elemento selezionato nel DOM con id uguale al valore di id passato.
        """
        return self.document.getElementById(id)

    # writeToHtmlElement
    def writeToHtmlElement(self, element, text):
        """
        La funzione scrive il contenuto di text nell’innerHtml dell’oggetto DOM contenuto in element        
        """
        element.innerHTML = text

    # emptyInputElement
    def emptyInputElement(self, element):
        """
        La funzione pulisce il campo value di un oggetto DOM <input> contenuto in element
        """
        element.value = ''

    # disableInputElement
    def disableInputElement(self, element):
        """
        La funzione setta il flag disabled = true all’oggetto DOM contenuto in element
        """
        element.disabled = True

    # addOnClickEventToHtmlElement
    def addOnClickEventToHtmlElement(self, element, event):
        """
        La funzione aggiunge un evento al onClick dell’oggetto DOM contenuto in element. In event deve essere passato la funzione da associare al click
        """
        element.onclick = event

    # removeOnClickEventFromHtmlElement
    def removeOnClickEventFromHtmlElement(self, element):
        """
        La funzione disabilita eventuali azioni al click dell’elemento DOM contenuto in element, settando onClick = false
        """

        element.onclick = False

    # addKeyupEventToHtmlElement
    def addKeyupEventToHtmlElement(self, element, event):
        """
        La funzione aggiunge l’evento keyup (su tutti i tasti della tastiera) all’oggetto DOM contenuto in element. In event deve essere passato la funzione da associare al keyup 
        """
        element.addEventListener('keyup', self.pyodide.create_proxy(event))

    # writeToConsole
    def writeToConsole(self, value):
        """
        Scrive il contenuto di value in console sul browser.
        """
        self.js.console.log(value)

    # checkIfEventIsEnterKey
    def checkIfEventIsEnterKey(self, event):
        """
        Restituisce vero se l’evento contenuto in event è scatenato dalla pressione del tasto “Enter”. Altrimenti restituisce falso.
        """
        return getattr(event, 'keyCode', 'na') == 13
