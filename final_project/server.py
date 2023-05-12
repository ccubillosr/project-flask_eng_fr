from flask import Flask,render_template,request
from machinetranslation import translator
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    #texttranslated= translator.englishtofrench(textToTranslate)
    texttranslated="French"
    return texttranslated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    #texttranslated= translator.frenchtoenglish(textToTranslate)
    texttranslated="English"
    return texttranslated

@app.route("/")
def renderIndexPage():
     return render_template("index.html")
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)