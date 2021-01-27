import sys

DELTA = 30
defaultF = 50
defaultX = -75
defaultY = 200
defaultZ = -103
defaultW = 10
defaultH = 20
defaultSpace = 5

#A
def A(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2)  + " y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/5) + " y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) +  "\n"
    gcode += "g1 x" + str(x+w*4/5) + " y" + str(y+h/2) + " f" + str(f) + "\n"
    return gcode

#B
def B(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x) + "y" + str(y+h/2) + "I0 J" + str(-h/4) + " f " + str(f) + "\n"
    gcode += "g2 x" + str(x) + "y" + str(y) + "I0 J" + str(-h/4) + " f " + str(f) + "\n"
    return gcode

#C
def C(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g3 x" + str(x+w) + "y" + str(y) + "I0" + " J" + str(-h/2) + " f " + str(f) + "\n"
    return gcode

#D
def D(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x) + "y" + str(y) + "I" + str(-(h/2-w/2)) + " J" + str(-h/2) + " f " + str(f) + "\n"
    return gcode
    
#E
def E(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    return gcode

#F
def F(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    return gcode

#G
def G(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g3 x" + str(x+w) + " y" + str(y) + " I" + str(-(h/2-w/2)) + " J" + str(-h/2) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + " f" + str(f) + "\n"
    return gcode

#H
def H(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y+h/2)  + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    return gcode
    
#I
def I(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w/2) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    return gcode
    
#J
def J(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+w/4) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x) + " y" + str(y+w/4) + "I" + str(-w/2) + "j0 f" + str(f) + "\n"
    #gcode = "g1 x" + str(x+w/2) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    #gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    #gcode += "g1 y" + str(y+w/4) + " f" + str(f) + "\n"
    #gcode += "g3 x" + str(x) + " y" + str(y+w/4) + "I" - str(w/4) + "j0 f" + str(f) + "\n"
    #gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    #gcode += "g1 x" + str(x) + "y" + str(y+h) + " f" + str(f) + "\n"
    #gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    #gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    return gcode

#K
def K(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y) + " f" + str(f) + "\n"
    return gcode

#L
def L(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    return gcode

#M
def M(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + " Y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " Y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 Y" + str(y) + " f" + str(f) + "\n"
    return gcode

#N
def N(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " Y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " Y" + str(y+h) + " f" + str(f) + "\n"
    return gcode

#O
def O(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w/2) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x+w/2) + " y" + str(y) + " I" + str(-(h/2-w/2)) + " J" + str(-h/2) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x+w/2) + " y" + str(y+h) + " I" + str(h/2-w/2) + " J" + str(h/2) + " f" + str(f) + "\n"
    return gcode

#P
def P(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x) + "y" + str(y+h/2) + "I0 J" + str(-h/4) + " f " + str(f) + "\n"
    return gcode

#Q
def Q(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w/2) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x+w/2) + " y" + str(y) + " I" + str(-(h/2-w/2)) + " J" + str(-h/2) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x+w/2) + " y" + str(y+h) + " I" + str(h/2-w/2) + " J" + str(h/2) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+3/4*w) + " y" + str(y+h/4) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y) + " f" + str(f) + "\n"
    return gcode

#R
def R(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x) + "y" + str(y+h/2) + "I0 J" + str(-h/4) + " f " + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y) + " f" + str(f) + "\n"
    return gcode

#S
def S(x,y,z,w,h,f):
    gcode = "g1 x" + str(x+w) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g3 y" + str(x+w/2) + "y" + str(y+h/2) + "I0 J" + str(-h/4) + " f" + str(f) + "\n"
    gcode += "g2 x" + str(x) + "y" + str(y) + "I0 J" + str(-h/4) + " f " + str(f) + "\n"
    return gcode

#T
def T(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + "y" + str(y+h) + " f " + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    return gcode

#U
def U(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y+w/2) + " f" + str(f) + "\n"
    gcode += "g3 x" + str(x+w) + " y" + str(y+w/2) + "I" + str(w/2) + "j0 f" + str(f) + "\n"
    gcode += "g1 y" + str(y+h) + " f" + str(f) + "\n"
    return gcode

#V
def V(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + "Y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + "y" + str(y+h) + " f " + str(f) + "\n"
    return gcode

#X
def X(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + "y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + "y" + str(y+h) + " f " + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y) + " f" + str(f) + "\n"
    return gcode

#Y
def Y(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + "y " + str(y+3/4*h) +  " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + "y " + str(y+h) +  " f" + str(f) + "\n"
    gcode += "g1 z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + "y" + str(y+3/4*h) + " f " + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 y" + str(y) + " f" + str(f) + "\n"
    return gcode

#W
def W(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/4) + " y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w/2) + " y" + str(y+h/2) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+3/4*w) + " y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " y" + str(y+h) + " f" + str(f) + "\n"
    return gcode

#Z
def Z(x,y,z,w,h,f):
    gcode = "g1 x" + str(x) + " y" + str(y+h) + " z" + str(z+DELTA) + " f" + str(f) + "\n"
    gcode += "g1 z" + str(z) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x) + " y" + str(y) + " f" + str(f) + "\n"
    gcode += "g1 x" + str(x+w) + " f" + str(f) + "\n"
    return gcode
    

def printAlphabeth():
    acode = A(-75,defaultY,defaultZ,defaultW,defaultH,defaultF)
    bcode = B(-60,defaultY,defaultZ,defaultW,defaultH,defaultF)
    ccode = C(-45,defaultY,defaultZ,defaultW,defaultH,defaultF)
    dcode = D(-30,defaultY,defaultZ,defaultW,defaultH,defaultF)
    ecode = E(-15,defaultY,defaultZ,defaultW,defaultH,defaultF) 
    fcode = F(0,defaultY,defaultZ,defaultW,defaultH,defaultF)
    gcode = G(15,defaultY,defaultZ,defaultW,defaultH,defaultF)
    hcode = H(30,defaultY,defaultZ,defaultW,defaultH,defaultF)
    icode = I(45,defaultY,defaultZ,defaultW,defaultH,defaultF)
    jcode = J(60,defaultY,defaultZ,defaultW,defaultH,defaultF)
    kcode = K(-75,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    lcode = L(-60,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    mcode = M(-45,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    ncode = N(-30,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    ocode = O(-15,defaultY-20,defaultZ,defaultW,defaultH,defaultF) 
    pcode = P(0,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    qcode = Q(15,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    rcode = R(30,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    scode = S(45,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    tcode = T(60,defaultY-20,defaultZ,defaultW,defaultH,defaultF)
    ucode = U(-75,defaultY-40,defaultZ,defaultW,defaultH,defaultF)
    vcode = V(-60,defaultY-40,defaultZ,defaultW,defaultH,defaultF)
    wcode = W(-45,defaultY-40,defaultZ,defaultW,defaultH,defaultF)
    xcode = X(-30,defaultY-40,defaultZ,defaultW,defaultH,defaultF)
    ycode = Y(-15,defaultY-40,defaultZ,defaultW,defaultH,defaultF)
    zcode = Z(-0,defaultY-40,defaultZ,defaultW,defaultH,defaultF)
    print(acode)
    print(bcode)
    print(ccode)
    print(dcode)
    print(ecode)
    print(fcode)
    print(gcode)
    print(hcode)
    print(icode)
    print(jcode)
    print(kcode)
    print(lcode)
    print(mcode)
    print(ncode)
    print(ocode)
    print(pcode)
    print(qcode)
    print(rcode)
    print(scode)
    print(tcode)
    print(ucode)
    print(vcode)
    print(wcode)
    print(xcode)
    print(ycode)
    print(zcode)

def printGCode(char,x,y,z,w,h,f):
    character = {
        "a": lambda:A(x,y,z,w,h,f),
        "b": lambda:B(x,y,z,w,h,f),
        "c": lambda:C(x,y,z,w,h,f),
        "d": lambda:D(x,y,z,w,h,f),
        "e": lambda:E(x,y,z,w,h,f),
        "f": lambda:F(x,y,z,w,h,f),
        "g": lambda:G(x,y,z,w,h,f),
        "h": lambda:H(x,y,z,w,h,f),
        "i": lambda:I(x,y,z,w,h,f),
        "j": lambda:J(x,y,z,w,h,f),
        "k": lambda:K(x,y,z,w,h,f),
        "l": lambda:L(x,y,z,w,h,f),
        "m": lambda:M(x,y,z,w,h,f),
        "n": lambda:N(x,y,z,w,h,f),
        "o": lambda:O(x,y,z,w,h,f),
        "p": lambda:P(x,y,z,w,h,f),
        "q": lambda:Q(x,y,z,w,h,f),
        "r": lambda:R(x,y,z,w,h,f),
        "s": lambda:S(x,y,z,w,h,f),
        "t": lambda:T(x,y,z,w,h,f),
        "u": lambda:U(x,y,z,w,h,f),
        "v": lambda:V(x,y,z,w,h,f),
        "w": lambda:W(x,y,z,w,h,f),
        "x": lambda:X(x,y,z,w,h,f),
        "y": lambda:Y(x,y,z,w,h,f),
        "z": lambda:Z(x,y,z,w,h,f) 
    }
    func = character.get(char, lambda: "Invalid char")
    # Execute the function
    return func()

if len(sys.argv) > 1:
    print(";Generating code to write")
    print(";" + sys.argv[1].lower())
    i = 1;
    j = 0;
    for c in sys.argv[1].lower():
        gcode = printGCode(c, float(defaultX + i*(defaultW+defaultSpace)), float(defaultY + j*(defaultH + defaultSpace)), defaultZ, defaultW, defaultH, defaultF)
        print(gcode) 
        if i%10 == 0:
            i = 1
            j = j+1
        else:
            i = i+1
else:
    printAlphabeth()