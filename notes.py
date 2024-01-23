from enum import Enum

LOWER_LIMIT_FREQ = 15
UPPER_LIMIT_FREQ = 8300

# Note Spectrum
notes = (
   [ 16.35, 32.70, 65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01 ], # C
   [ 17.32, 34.65, 69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92 ], # C#
   [ 18.35, 36.71, 73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.63 ], # D
   [ 19.45, 38.89, 77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03 ], # D#/Eb
   [ 20.60, 41.20, 82.41, 164.81, 329.63, 659.25, 1318.51, 2637.02, 5274.04 ], # E
   [ 21.83, 43.65, 87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65 ], # F
   [ 23.12, 46.25, 92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91 ], # F#/Gb
   [ 24.50, 49.00, 98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93 ], # G
   [ 25.96, 51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88 ], # G#/Ab
   [ 27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00 ], # A
   [ 29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62 ], # A#/Bb,
   [ 30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13 ] # B
)

class Notes(Enum):
    C = 0
    C_SHARP = 1
    D = 2
    D_SHARP = 3
    F = 4
    F_SHARP = 5
    G = 6
    G_SHARP = 7
    A = 8
    A_SHARP = 9
    B = 10
    ERR = 11

class Octave(Enum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3
    FIFTH = 4
    SIXTH = 5
    SEVENTH = 6
    EIGHTH = 7
    ERR = 8

def get_note_octave(freq):
    if ((freq >= notes[Notes.C.value][0]) and (freq <= notes[Notes.B.value][0])):
        return Octave.FIRST
    elif ((freq >= notes[Notes.C.value][1]) and (freq <= notes[Notes.B.value][1])):
        return Octave.SECOND
    elif ((freq >= notes[Notes.C.value][2]) and (freq <= notes[Notes.B.value][2])):
        return Octave.THIRD        
    elif ((freq >= notes[Notes.C.value][3]) and (freq <= notes[Notes.B.value][3])):
        return Octave.FOURTH    
    elif ((freq >= notes[Notes.C.value][4]) and (freq <= notes[Notes.B.value][4])):
        return Octave.FIFTH
    elif ((freq >= notes[Notes.C.value][5]) and (freq <= notes[Notes.B.value][5])):
        return Octave.SIXTH
    elif ((freq >= notes[Notes.C.value][6]) and (freq <= notes[Notes.B.value][6])):
        return Octave.SEVENTH
    elif ((freq >= notes[Notes.C.value][7]) and (freq <= notes[Notes.B.value][7])):
        return Octave.EIGHTH
    else:
        return Octave.ERR
    
def get_note_from_freq(freq):
    octave = get_note_octave(freq).value
    if(octave != Octave.ERR):
        if ((freq <= (notes[Notes.C.value][octave] + (notes[Notes.C_SHARP.value][octave]-notes[Notes.C.value][octave])/2)) and (freq >= LOWER_LIMIT_FREQ)):
            return Notes.C
        elif (freq <= (notes[Notes.C_SHARP.value][octave] + (notes[Notes.D.value][octave]-notes[Notes.C_SHARP.value][octave])/2)):
            return Notes.C_SHARP
        elif (freq <= (notes[Notes.D.value][octave] + (notes[Notes.D_SHARP.value][octave]-notes[Notes.D.value][octave])/2)):
            return Notes.D
        elif (freq <= (notes[Notes.D_SHARP.value][octave] + (notes[Notes.F.value][octave]-notes[Notes.D_SHARP.value][octave])/2)):
            return Notes.D_SHARP
        elif (freq <= (notes[Notes.F.value][octave] + (notes[Notes.F_SHARP.value][octave]-notes[Notes.F.value][octave])/2)):
            return Notes.F
        elif (freq <= (notes[Notes.F_SHARP.value][octave] + (notes[Notes.G.value][octave]-notes[Notes.F_SHARP.value][octave])/2)):
            return Notes.F_SHARP
        elif (freq <= (notes[Notes.G.value][octave] + (notes[Notes.G_SHARP.value][octave]-notes[Notes.G.value][octave])/2)):
            return Notes.G
        elif (freq <= (notes[Notes.G_SHARP.value][octave] + (notes[Notes.A.value][octave]-notes[Notes.G_SHARP.value][octave])/2)):
            return Notes.G_SHARP
        elif (freq <= (notes[Notes.A.value][octave] + (notes[Notes.A_SHARP.value][octave]-notes[Notes.A.value][octave])/2)):
            return Notes.A       
        elif (freq <= (notes[Notes.A_SHARP.value][octave] + (notes[Notes.B.value][octave]-notes[Notes.A_SHARP.value][octave])/2)):
            return Notes.A_SHARP
        elif (freq <= (notes[Notes.B.value][octave] + (UPPER_LIMIT_FREQ-notes[Notes.B.value][octave]))):
            return Notes.B 
        else:
            return Notes.ERR
    else:
        print("Octave error out of range")
        return Notes.ERR