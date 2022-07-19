# Music Theory Stuff
NoteArr =   [0   ,  1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ,  9  ,  10 , 11]
SharpsArr = ['C ', 'C#', 'D ', 'D#', 'E ', 'F ', 'F#', 'G ', 'G#', 'A ', 'A#', 'B ']
FlatArr =   ['C ', 'Db', 'D ', 'Eb', 'E ', 'F ', 'Gb', 'G ', 'Ab', 'A ', 'Bb', 'B ']
majorScale = [0, 2, 4, 5, 7, 9, 11, 0]
minorScale = [0, 2, 3, 5, 7, 8, 10, 0]
majorDegrees = ["I", 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
minorDegrees = ["i", 'ii°', 'III', 'iv', 'V', 'VI', 'vii°']
"""
   0                     3             5             7             9                    12                   15            17            19            21
|------||------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
|------||------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
|------||------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
|------||------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
|------||------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
|------||------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
   0                     3             5             7             9                    12                   15            17            19            21
"""
eString = [4 , 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1]
BString = [11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8]
GString = [7 , 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4]
DString = [2 , 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
AString = [9 ,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6]
EString = [4 , 5, 6, 7, 8, 9,10,11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11, 0, 1]
markers = "   0                     3             5             7             9                    12                   15            17            19            21"
class Key:
    def __init__(self, root, k):
        self.root = int(root)
        self.key = k

        ## Major/Relative Major
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


        ## Triads
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

    def TriadConvert(self, t):
        return [SharpsArr[t[0]], SharpsArr[t[1]], SharpsArr[t[2]]]

    def TriadString(self, t):
        s = ""
        for i in t:
            s += i +" "
        return s

    def printMajor(self):
        if(self.key == 'M'):
            print(SharpsArr[self.root], " Major Scale Degrees:")
            print("I:    ", SharpsArr[self.majorScale[0]])
            print("ii:   ", SharpsArr[self.majorScale[1]])
            print("iii:  ", SharpsArr[self.majorScale[2]])
            print("IV:   ", SharpsArr[self.majorScale[3]])
            print("V:    ", SharpsArr[self.majorScale[4]])
            print("vi:   ", SharpsArr[self.majorScale[5]])
            print("vii°: ", SharpsArr[self.majorScale[6]])
        elif(self.key =='m'):
            print(SharpsArr[self.root], "Minor relative ", SharpsArr[self.relMajor], " Major Scale Degrees:")
            print("I:    ", SharpsArr[self.relMajorScale[0]])
            print("ii:   ", SharpsArr[self.relMajorScale[1]])
            print("iii:  ", SharpsArr[self.relMajorScale[2]])
            print("IV:   ", SharpsArr[self.relMajorScale[3]])
            print("V:    ", SharpsArr[self.relMajorScale[4]])
            print("vi:   ", SharpsArr[self.relMajorScale[5]])
            print("vii°: ", SharpsArr[self.relMajorScale[6]])

    def printMinor(self):
        if(self.key == 'm'):
            print(SharpsArr[self.root], " Minor Scale Degrees:")
            print("i:    ", SharpsArr[self.minorScale[0]])
            print("ii°:  ", SharpsArr[self.minorScale[1]])
            print("III:  ", SharpsArr[self.minorScale[2]])
            print("iv:   ", SharpsArr[self.minorScale[3]])
            print("V:    ", SharpsArr[self.minorScale[4]])
            print("VI:   ", SharpsArr[self.minorScale[5]])
            print("vii°: ", SharpsArr[self.minorScale[6]])
        elif(self.key =='M'):
            print(SharpsArr[self.root], "Major relative ", SharpsArr[self.relMinor], " Minor Scale Degrees:")
            print("i:    ", SharpsArr[self.relMinorScale[0]])
            print("ii°:  ", SharpsArr[self.relMinorScale[1]])
            print("III:  ", SharpsArr[self.relMinorScale[2]])
            print("iv:   ", SharpsArr[self.relMinorScale[3]])
            print("V:    ", SharpsArr[self.relMinorScale[4]])
            print("VI:   ", SharpsArr[self.relMinorScale[5]])
            print("vii°: ", SharpsArr[self.relMinorScale[6]])

    def printTriads(self):
        if(self.key == 'M'):
            print(SharpsArr[self.root], " Major Triads:")
            print("I:    ", self.TriadString(self.TriadConvert(self.triads[0])))
            print("ii:   ", self.TriadString(self.TriadConvert(self.triads[1])))
            print("iii:  ", self.TriadString(self.TriadConvert(self.triads[2])))
            print("IV:   ", self.TriadString(self.TriadConvert(self.triads[3])))
            print("V:    ", self.TriadString(self.TriadConvert(self.triads[4])))
            print("vi:   ", self.TriadString(self.TriadConvert(self.triads[5])))
            print("vii°: ", self.TriadString(self.TriadConvert(self.triads[6])))
        if(self.key == 'm'):
            print(SharpsArr[self.root], " Minor Triads:")
            print("I:    ", self.TriadString(self.TriadConvert(self.triads[0])))
            print("ii°:  ", self.TriadString(self.TriadConvert(self.triads[1])))
            print("III:  ", self.TriadString(self.TriadConvert(self.triads[2])))
            print("iv:   ", self.TriadString(self.TriadConvert(self.triads[3])))
            print("V:    ", self.TriadString(self.TriadConvert(self.triads[4])))
            print("VI:   ", self.TriadString(self.TriadConvert(self.triads[5])))
            print("vii°: ", self.TriadString(self.TriadConvert(self.triads[6])))

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
        print(markers)
        print(first)
        print(second)
        print(third)
        print(fourth)
        print(fifth)
        print(sixth)




def main():
    for i in NoteArr:
        print(i, ':', SharpsArr[i])
    print("Input a key numer:")
    k = input()
    print("Input Major/Minor (M/m):")
    km = input()
    currKey = Key(k,km)
    currKey.boardBuilder([None])
    chord = ""
    while(chord != "exit"):
        print("What chord do you want to hit? (1-7)")
        chord = input();
        if chord == 'exit':
            break
        chordNum = int(chord) - 1
        if(currKey.key == 'M'):
            print(currKey.keyname, "Scale, focus on ", majorDegrees[chordNum])
        if(currKey.key == 'm'):
            print(currKey.keyname, "Scale, focus on ", minorDegrees[chordNum])
        currKey.boardBuilder(currKey.triads[chordNum])



if __name__=="__main__":
    main()
