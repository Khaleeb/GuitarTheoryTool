# Caleb Davis
# Guitar Theory Tool

from flask import Flask, redirect, url_for, request, render_template, session

# Flask stuff
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "1337"

# music theory stuff
NoteArr =   [0   ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ,  9  ,  10 , 11]
SharpsArr = ['C ', 'C#', 'D ', 'D#', 'E ', 'F ', 'F#', 'G ', 'G#', 'A ', 'A#', 'B ']
FlatArr =   ['C ', 'Db', 'D ', 'Eb', 'E ', 'F ', 'Gb', 'G ', 'Ab', 'A ', 'Bb', 'B ']
majorScale = [0, 2, 4, 5, 7, 9, 11, 0]
minorScale = [0, 2, 3, 5, 7, 8, 10, 0]
majorDegrees = ["I", 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
minorDegrees = ["i", 'ii°', 'III', 'iv', 'V', 'VI', 'vii°']
eString = [4 , 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1]
BString = [11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8]
GString = [7 , 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4]
DString = [2 , 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
AString = [9 ,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6]
EString = [4 , 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1]
markers = "   0                     3             5             7             9                    12                   15            17            19            21"


# render resulting display page
@app.route('/display/')
def display():
    snippet = renderScales(session['keyID'], session['scaleShape'], session['trgtChords'])
    return render_template('display.html', scaleNoteOutput=snippet)

#@app.route('/display/', methods=['POST'])
#def displayRet():
   #return redirect(url_for('welcome'))


# render request forms 
@app.route('/')
def welcome():
    return render_template('welcome_form.html')


# get information from request forms
@app.route('/', methods=['POST'])
def processKeyID():
    keyID = int(request.form['key_id'])   # Number 0-11 representing root note
    scaleShape = request.form['scale_shape']   # M/m for Major or minor
    trgtChordsInput = request.form.getlist('trgt_chords')  # list of digits 1-7 representing target chords within scale
    trgtChords = []
    for item in trgtChordsInput:
        trgtChords.append(int(item))
    session['keyID'] = keyID
    session['scaleShape'] = scaleShape
    session['trgtChords'] = trgtChords
    return redirect(url_for('display'))
    #return "%i %s %s" % (keyID, scaleShape, ''.join(trgtChords))


# Key Class     root=keyID k = scaleShape
class Key: 
    def __init__(self, root, k):
        self.root =root
        self.key = k

        # Mjor/Relate Major
        if(self.key == 'M'):
                self.keyname = SharpsArr[self.root] + " Major"
                self.majorScale = [None] * 7
                for i in range(0,7):
                    self.majorScale[i] = (self.root + majorScale[i]) % 12
        elif(self.key == 'm'):
            self.keyname = SharpsArr[self.root] + " Minor"
            self.relMajorScale = [None] * 7
            self.relMajor = (self.root + 3 ) % 12
            for i in range(0,7):
                self.relMajorScale[i] = (self.relMajor + majorScale[i]) % 12
        ## Minor/Relative Minor
        if(self.key == 'm'):
            self.minorScale = [None] * 7
            for i in range(0,7):
                self.minorScale[i] = (self.root + minorScale[i]) % 12
        elif(self.key == 'M'):
            self.relMinorScale = [None] * 7
            self.relMinor = (self.root - 3) % 12
            for i in range(0,7):
                self.relMinorScale[i] = (self.relMinor + minorScale[i]) % 12
        ## Build triads array
        if(self.key == 'M'):
            self.triads = [None] * 7
            for i in range(0,7):
                t=[]
                t.append(self.majorScale[i])
                t.append(self.majorScale[(i+2) % 7])
                t.append(self.majorScale[(i+4)% 7])
                self.triads[i] = t
        if(self.key == 'm'):
            self.triads = [None] * 7
            for i in range(0,7):
                t=[]
                t.append(self.minorScale[i])
                t.append(self.minorScale[(i+2) % 7])
                t.append(self.minorScale[(i+4)% 7])
                self.triads[i] = t
    

    # return specified triad array for key object, takes triad from triads[]
    def TriadConvert(self, t):
        return [SharpsArr[t[0]], SharpsArr[t[1]], SharpsArr[t[2]]]

    
    # return specified triad string for key object, specified by arr from TriadConvert
    def TriadString(self, t):
        s = ""
        for i in t:
            s += i +" "
        return s


    # return HTML snippet for specified target chord in Key object
    def boardBuilder(self, chord):
        if(self.key == 'M'):
            currScale = self.majorScale
        if(self.key == 'm'):
            currScale = self.minorScale
        eOut = [None] * 22
        BOut = [None] * 22
        GOut = [None] * 22
        DOut = [None] * 22
        AOut = [None] * 22
        EOut = [None] * 22

        for i in range(0,22):
            if(eString[i] in currScale):
                if(eString[i] in chord):
                    eOut[i] = '<' + str(currScale.index(eString[i])+1) + '>'
                else:
                    eOut[i] = '-' + str(currScale.index(eString[i])+1) + '-'
            else:
                eOut[i] = '---'
            if(BString[i] in currScale):
                if(BString[i] in chord):
                    BOut[i] = '<' + str(currScale.index(BString[i])+1) + '>'
                else:
                    BOut[i] = '-' + str(currScale.index(BString[i])+1) + '-'
            else:
                BOut[i] = '---'
            if(GString[i] in currScale):
                if(GString[i] in chord):
                    GOut[i] = '<' + str(currScale.index(GString[i])+1) + '>'
                else:
                    GOut[i] = '-' +  str(currScale.index(GString[i])+1) + '-'
            else:
                GOut[i] = '---'
            if(DString[i] in currScale):
                if(DString[i] in chord):
                    DOut[i] = '<' + str(currScale.index(DString[i])+1) + '>'
                else:
                    DOut[i] =  '-' + str(currScale.index(DString[i])+1) + '-'
            else:
                DOut[i] = '---'
            if(AString[i] in currScale):
                if(AString[i] in chord):
                    AOut[i] = '<' + str(currScale.index(AString[i])+1) + '>'
                else:
                    AOut[i] =  '-' + str(currScale.index(AString[i])+1) + '-'
            else:
                AOut[i] = '---'
            if(EString[i] in currScale):
                if(EString[i] in chord):
                    EOut[i] = '<' + str(currScale.index(EString[i])+1) + '>'
                else:
                    EOut[i] =  '-' + str(currScale.index(EString[i])+1) + '-'
            else:
                EOut[i] = '---'
        first = "|-" + eOut[0] + "--||"
        second = "|-" + BOut[0] + "--||"
        third = "|-" + GOut[0] + "--||"
        fourth = "|-" + DOut[0] + "--||"
        fifth = "|-" + AOut[0] + "--||"
        sixth = "|-" + EOut[0] + "--||"
        for i in range(0,21):
            first += "-" + eOut[i+1] + "--|"
            second += "-" + BOut[i+1] + "--|"
            third += "-" + GOut[i+1] + "--|"
            fourth += "-" + DOut[i+1] + "--|"
            fifth += "-" + AOut[i+1] + "--|"
            sixth += "-" + EOut[i+1] + "--|"
        snippet = "<pre>" + markers + "<br>" + first + "<br>" + second + "<br>" + third + "<br>" + fourth + "<br>" + fifth + "<br>" + sixth + "<br>" + "</pre>"
        return snippet
        
        #print(markers)
        #print(first)
        #print(second)
        #print(third)
        #print(fourth)
        #print(fifth)
        #print(sixth)


# Build scaleNoteOutput
def renderScales(keyID, scaleShape, trgtChords):
    snippet = "<h4>Scale notes:</h4>"
    currKey = Key(keyID, scaleShape)
    snippet += currKey.boardBuilder([None])
    return snippet


if __name__ == '__main__':
    app.run(debug=True)