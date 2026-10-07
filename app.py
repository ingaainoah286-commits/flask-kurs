from flask import Flask, render_template
app = Flask(__name__)

#Øve på 7.Templates
#"Templates is being used before it's defines."

#Må jeg kanskje lage templates folder vedsiden av eller inni
# (vis det går skulle gå ann) app.py?
#   flask-kurs/
#   ├── app.py
#   └── templates/
#       └── index.html

#Egentlig det viser: Lage templates/ og filen templates/index.html. 
# Lage index.html, endre koden som viser next i app.py,
#  og da skal systeme operere slik:
#route/ -> index() -> render_template("index.html")
# ->templates/index.html
# ->nettleser

@app.route("/")
def index():
    return render_template(
        "index.html",
          navn="Amir",
          klasse="VG2",
          fag="Informasjonsteknologi",
          navn2="Aurora",
          alder="17",
          favorittspråk="norsk",
          skole="Kuben",
          #Oppgave6
          poeng="50",
    )   

#Å tilsette navn som er lik elevnavn in til h1 i index.html, funka ikke :(





@app.route("/om")
def om():
    return "Om oss"

@app.route("/kontakt")
def kontakt():
    return "Kontakt oss"

@app.route("/profil")
def profil():
    return "Kaja Ainoah"


    
#Søke på hvorfor {##} ikke funker i app.py.
#Flask run: For å søke etter link, få en side i VSCode, og kopiere selve linken til nettside.
#Teste med / etterpå som andre app.routes har.



@app.route("/prosjekter")
def prosjekter():
    return "Våre Prosjekter"

@app.route("/fag")
def fag():
    fagliste = ["Python", "Flask", "HTML", "CSS"]
    return render_template("fag.html", fag=fagliste)


if __name__ == "__main__":
    app.run(debug=True)





