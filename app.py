from bottle import route,run,template,request,static_file
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

    return template("textview",listT=listT,posttext=posttext,t=t,token=token)


@route('/static/<file_path:path>')
def static(file_path):

    return static_file(file_path, root="./static")


run(host='localhost', port=8080, debug=True)
