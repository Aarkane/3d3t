global ax
global ay
global az
global bx
global by
global bz
global cx
global cy
global cz
ax = '_'
ay = '_'
az = '_'
bx = '_'
by = '_'
bz = '_'
cx = '_'
cy = '_'
cz = '_'
global axf
global ayf
global azf
global bxf
global byf
global bzf
global cxf
global cyf
global czf
axf = '_'
ayf = '_'
azf = '_'
bxf = '_'
byf = '_'
bzf = '_'
cxf = '_'
cyf = '_'
czf = '_'
global winner
winner = 'none'
    
def wins():
    global winner
    if axf == 'x' and ayf == 'x' and azf == 'x':
        winner = 'x'
    elif axf == 'o' and ayf == 'o' and azf == 'o':
        winner = 'o'
    elif bxf == 'x' and byf == 'x' and bzf == 'x':
        winner = 'x'
    elif bxf == 'o' and byf == 'o' and bzf == 'o':
        winner = 'o'
    elif cxf == 'x' and cyf == 'x' and czf == 'x':
        winner = 'x'
    elif cxf == 'o' and cyf == 'o' and czf == 'o':
        winner = 'o'
    elif axf == 'x' and byf == 'x' and czf == 'x':
        winner = 'x'
    elif axf == 'o' and byf == 'o' and czf == 'o':
        winner = 'o'
    elif azf == 'x' and byf == 'x' and cxf == 'x':
        winner = 'x'
    elif azf == 'o' and byf == 'o' and cxf == 'o':
        winner = 'o'
        
    if winner == 'x':
        print 'X wins!'
    elif winner == 'o':
        print 'O wins!'

def xturns():
    x = raw_input()
    global axf
    global ayf
    global azf
    global bxf
    global byf
    global bzf
    global cxf
    global cyf
    global czf
        
    if x == 'ax' and ax == '_':
        axf = 'x'
    elif x == 'ay' and ay == '_':
        ayf = 'x'
    elif x == 'az' and az == '_':
        azf = 'x'
    elif x == 'bx' and bx == '_':
        bxf = 'x'
    elif x == 'by' and by == '_':
        byf = 'x'
    elif x == 'bz' and bz == '_':
        bzf = 'x'
    elif x == 'cx' and cx == '_':
        cxf = 'x'
    elif x == 'cy' and cy == '_':
        cyf = 'x'
    elif x == 'cz' and cz == '_':
        czf = 'x'
    else:
        print "This space is unavailible or does not exist, choose again."
        xturns()
        
def xvarc():
    global ax
    global ay
    global az
    global bx
    global by
    global bz
    global cx
    global cy
    global cz
    global axf
    global ayf
    global azf
    global bxf
    global byf
    global bzf
    global cxf
    global cyf
    global czf
    if axf == 'x':
        ax = 'x'
    if ayf == 'x':
        ay = 'x'
    if azf == 'x':
        az = 'x'
    if bxf == 'x':
        bx = 'x'
    if byf == 'x':
        by = 'x'
    if bzf == 'x':
        bz = 'x'
    if cxf == 'x':
        cx = 'x'
    if cyf == 'x':
        cy = 'x'
    if czf == 'x':
        cz = 'x'

def oturns():        
    o = raw_input()
    global axf
    global ayf
    global azf
    global bxf
    global byf
    global bzf
    global cxf
    global cyf
    global czf
    
    if o == 'ax' and ax == '_':
        axf = 'o'
    elif o == 'ay' and ay == '_':
        ayf = 'o'
    elif o == 'az' and az == '_':
        azf = 'o'
    elif o == 'bx' and bx == '_':
        bxf = 'o'
    elif o == 'by' and by == '_':
        byf = 'o'
    elif o == 'bz' and bz == '_':
        bzf = 'o'
    elif o == 'cx' and cx == '_':
        cxf = 'o'
    elif o == 'cy' and cy == '_':
        cyf = 'o'
    elif o == 'cz' and cz == '_':
        czf = 'o'
    else:
        print "This space is unavailible or does not exist, choose again."
        oturns()
        
def ovarc():
    global ax
    global ay
    global az
    global bx
    global by
    global bz
    global cx
    global cy
    global cz
    global axf
    global ayf
    global azf
    global bxf
    global byf
    global bzf
    global cxf
    global cyf
    global czf
    if axf == 'o':
        ax = 'o'
    if ayf == 'o':
        ay = 'o'
    if azf == 'o':
        az = 'o'
    if bxf == 'o':
        bx = 'o'
    if byf == 'o':
        by = 'o'
    if bzf == 'o':
        bz = 'o'
    if cxf == 'o':
        cx = 'o'
    if cyf == 'o':
        cy = 'o'
    if czf == 'o':
        cz = 'o'
     
def play():
    Pewter = 'seraphim'
    while Pewter == 'seraphim':
        if winner == 'none':
            print "It is x's turn! enter a coordinate to play a piece."
            xturns()
            xvarc()
            wins()
        else:
            Pewter = 'demon'
        if winner == 'none':
            print "It is o's turn! enter a coordinate to play a piece."
            oturns()
            ovarc()
            wins()
        else:
            Pewter = 'demon'
play()