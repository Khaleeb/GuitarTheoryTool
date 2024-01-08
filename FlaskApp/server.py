# Caleb Davis
# Guitar Theory Tool

from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__, template_folder="templates")
app.secret_key = "1337"

@app.route('/display/')
def display():
    return render_template('display.html', scaleNoteOutput="<p>testing</p>")

#@app.route('/display/', methods=['POST'])
#def displayRet():
   #return redirect(url_for('welcome'))


@app.route('/')
def welcome():
    return render_template('welcome_form.html')

@app.route('/', methods=['POST'])
def processKeyID():
    keyID = int(request.form['key_id'])
    scaleShape = request.form['scale_shape']
    trgtChordsInput = request.form.getlist('trgt_chords')
    trgtChords = []
    for item in trgtChordsInput:
        trgtChords.append(int(item))
    session['keyID'] = keyID
    session['scaleShape'] = scaleShape
    session['trgtChords'] = trgtChords
    return redirect(url_for('display'))
    #return "%i %s %s" % (keyID, scaleShape, ''.join(trgtChords))


if __name__ == '__main__':
    app.run(debug=True)