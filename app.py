from bottle import route,run,template,request
from janome.tokenizer import Tokenizer


@route('/add')
def add_text():

    return template("index")


@route('/textstream',method=["POST"])
def textstream():

    posttext = request.POST.getunicode("example1")

    listT = []
    t = Tokenizer()
    for token in t.tokenize(posttext):
        listT = token.surface

    return template("textview",listT=listT,posttext=posttext,t=t)

run(host='localhost', port=8080, debug=True)
