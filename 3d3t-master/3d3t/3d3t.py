def bp():
    '''plane 1'''
    global aw1
    global ax1
    global ay1
    global az1
    global bw1
    global bx1
    global by1
    global bz1
    global cw1
    global cx1
    global cy1
    global cz1
    global dw1
    global dx1
    global dy1
    global dz1
    aw1='_'
    ax1='_'
    ay1='_'
    az1='_'
    bw1='_'
    bx1='_'
    by1='_'
    bz1='_'
    cw1='_'
    cx1='_'
    cy1='_'
    cz1='_'
    dw1='_'
    dx1='_'
    dy1='_'
    dz1='_'
    '''plane 2'''
    global aw2
    global ax2
    global ay2
    global az2
    global bw2
    global bx2
    global by2
    global bz2
    global cw2
    global cx2
    global cy2
    global cz2
    global dw2
    global dx2
    global dy2
    global dz2
    aw2='_'
    ax2='_'
    ay2='_'
    az2='_'
    bw2='_'
    bx2='_'
    by2='_'
    bz2='_'
    cw2='_'
    cx2='_'
    cy2='_'
    cz2='_'
    dw2='_'
    dx2='_'
    dy2='_'
    dz2='_'
    '''plane 3'''
    global aw3
    global ax3
    global ay3
    global az3
    global bw3
    global bx3
    global by3
    global bz3
    global cw3
    global cx3
    global cy3
    global cz3
    global dw3
    global dx3
    global dy3
    global dz3
    aw3='_'
    ax3='_'
    ay3='_'
    az3='_'
    bw3='_'
    bx3='_'
    by3='_'
    bz3='_'
    cw3='_'
    cx3='_'
    cy3='_'
    cz3='_'
    dw3='_'
    dx3='_'
    dy3='_'
    dz3='_'
    '''plane 4'''
    global aw4
    global ax4
    global ay4
    global az4
    global bw4
    global bx4
    global by4
    global bz4
    global cw4
    global cx4
    global cy4
    global cz4
    global dw4
    global dx4
    global dy4
    global dz4
    aw4='_'
    ax4='_'
    ay4='_'
    az4='_'
    bw4='_'
    bx4='_'
    by4='_'
    bz4='_'
    cw4='_'
    cx4='_'
    cy4='_'
    cz4='_'
    dw4='_'
    dx4='_'
    dy4='_'
    dz4='_'
    
    global winner
    winner = 'none'

def xt():    
    print("It is player x's turn, enter a coordinate to place your piece")
    raw_input()
                        
    """plane 1"""
    if aw1 == '_' and raw_input==('aw1'):
        aw1 = 'x'
    elif ax1=='_' and raw_input==('ax1'):
        ax1 = 'x'
    elif ay1=='_' and raw_input==('ay1'):
        ay1 = 'x'
    elif az1=='_' and raw_input==('az1'):
        az1 = 'x'
                            
    elif bw1=='_' and raw_input==('bw1'):
        bw1 = 'x'
    elif bx1=='_' and raw_input==('bx1'):
        bx1 = 'x'
    elif by1=='_' and raw_input==('by1'):
        by1 = 'x'
    elif bz1=='_' and raw_input==('bz1'):
        bz1 = 'x'
                            
    elif cw1=='_' and raw_input==('cw1'):
        cw1 = 'x'
    elif cx1=='_' and raw_input==('cx1'):
        cx1 = 'x'
    elif cy1=='_' and raw_input==('cy1'):
        cy1 = 'x'
    elif cz1=='_' and raw_input==('cz1'):
        cz1 = 'x'
                            
    elif dw1=='_' and raw_input==('dw1'):
        dw1 = 'x'
    elif dx1=='_' and raw_input==('dx1'):
        dx1 = 'x'
    elif dy1=='_' and raw_input==('dy1'):
        dy1 = 'x'
    elif dz1=='_' and raw_input==('dz1'):
        dz1 = 'x'
                            
    """plane 2"""
    if aw2=='_' and raw_input==('aw2'):
        aw2 = 'x'
    elif ax2=='_' and raw_input==('ax2'):
        ax2 = 'x'
    elif ay2=='_' and raw_input==('ay2'):
        ay2 = 'x'
    elif az2=='_' and raw_input==('az2'):
        az2 = 'x'
                            
    elif bw2=='_' and raw_input==('bw2'):
        bw2 = 'x'
    elif bx2=='_' and raw_input==('bx2'):
        bx2 = 'x'
    elif by2=='_' and raw_input==('by2'):
        by2 = 'x'
    elif bz2=='_' and raw_input==('bz2'):
        bz2 = 'x'
                            
    elif cw2=='_' and raw_input==('cw2'):
        cw2 = 'x'
    elif cx2=='_' and raw_input==('cx2'):
        cx2 = 'x'
    elif cy2=='_' and raw_input==('cy2'):
        cy2 = 'x'
    elif cz2=='_' and raw_input==('cz2'):
        cz2 = 'x'
                            
    elif dw2=='_' and raw_input==('dw2'):
        dw2 = 'x'
    elif dx2=='_' and raw_input==('dx2'):
        dx2 = 'x'
    elif dy2=='_' and raw_input==('dy2'):
        dy2 = 'x'
    elif dz2=='_' and raw_input==('dz2'):
        dz2 = 'x'
                            
    """plane 3"""
    if aw3=='_' and raw_input==('aw3'):
        aw3 = 'x'
    elif ax3=='_' and raw_input==('ax3'):
        ax3 = 'x'
    elif ay3=='_' and raw_input==('ay3'):
        ay3 = 'x'
    elif az3=='_' and raw_input==('az3'):
        az3 = 'x'
                            
    elif bw3=='_' and raw_input==('bw3'):
        bw3 = 'x'
    elif bx3=='_' and raw_input==('bx3'):
        bx3 = 'x'
    elif by3=='_' and raw_input==('by3'):
        by3 = 'x'
    elif bz3=='_' and raw_input==('bz3'):
        bz3 = 'x'
                            
    elif cw3=='_' and raw_input==('cw3'):
        cw3 = 'x'
    elif cx3=='_' and raw_input==('cx3'):
        cx3 = 'x'
    elif cy3=='_' and raw_input==('cy3'):
        cy3 = 'x'
    elif cz3=='_' and raw_input==('cz3'):
        cz3 = 'x'
                            
    elif dw3=='_' and raw_input==('dw3'):
        dw3 = 'x'
    elif dx3=='_' and raw_input==('dx3'):
        dx3 = 'x'
    elif dy3=='_' and raw_input==('dy3'):
        dy3 = 'x'
    elif dz3=='_' and raw_input==('dz3'):
        dz3 = 'x'
                            
    """plane 4"""
    if aw4=='_' and raw_input==('aw4'):
        aw4 = 'x'
    elif ax4=='_' and raw_input==('ax4'):
        ax4 = 'x'
    elif ay4=='_' and raw_input==('ay4'):
        ay4 = 'x'
    elif az4=='_' and raw_input==('az4'):
        az4 = 'x'
                            
    elif bw4=='_' and raw_input==('bw4'):
        bw4 = 'x'
    elif bx4=='_' and raw_input==('bx4'):
        bx4 = 'x'
    elif by4=='_' and raw_input==('by4'):
        by4 = 'x'
    elif bz4=='_' and raw_input==('bz4'):
        bz4 = 'x'
                            
    elif cw4=='_' and raw_input==('cw4'):
        cw4 = 'x'
    elif cx4=='_' and raw_input==('cx4'):
        cx4 = 'x'
    elif cy4=='_' and raw_input==('cy4'):
        cy4 = 'x'
    elif cz4=='_' and raw_input==('cz4'):
        cz4 = 'x'
                            
    elif dw4=='_' and raw_input==('dw4'):
        dw4 = 'x'
    elif dx4=='_' and raw_input==('dx4'):
        dx4 = 'x'
    elif dy4=='_' and raw_input==('dy4'):
        dy4 = 'x'
    elif dz4=='_' and raw_input==('dz4'):
        dz4 = 'x'
        

def ot():    
    print("It is player o's turn, enter a coordinate to place your piece")
    raw_input()
    
    """plane 1"""
    if aw1=='_' and raw_input==('aw1'):
        aw1 = 'o'
    elif ax1=='_' and raw_input==('ax1'):
        ax1 = 'o'
    elif ay1=='_' and raw_input==('ay1'):
        ay1 = 'o'
    elif az1=='_' and raw_input==('az1'):
        az1 = 'o'
        
    elif bw1=='_' and raw_input==('bw1'):
        bw1 = 'o'
    elif bx1=='_' and raw_input==('bx1'):
        bx1 = 'o'
    elif by1=='_' and raw_input==('by1'):
        by1 = 'o'
    elif bz1=='_' and raw_input==('bz1'):
        bz1 = 'o'
        
    elif cw1=='_' and raw_input==('cw1'):
        cw1 = 'o'
    elif cx1=='_' and raw_input==('cx1'):
        cx1 = 'o'
    elif cy1=='_' and raw_input==('cy1'):
        cy1 = 'o'
    elif cz1=='_' and raw_input==('cz1'):
        cz1 = 'o'
        
    elif dw1=='_' and raw_input==('dw1'):
        dw1 = 'o'
    elif dx1=='_' and raw_input==('dx1'):
        dx1 = 'o'
    elif dy1=='_' and raw_input==('dy1'):
        dy1 = 'o'
    elif dz1=='_' and raw_input==('dz1'):
        dz1 = 'o'
        
    """plane 2"""
    if aw2=='_' and raw_input==('aw2'):
        aw2 = 'o'
    elif ax2=='_' and raw_input==('ax2'):
        ax2 = 'o'
    elif ay2=='_' and raw_input==('ay2'):
        ay2 = 'o'
    elif az2=='_' and raw_input==('az2'):
        az2 = 'o'
        
    elif bw2=='_' and raw_input==('bw2'):
        bw2 = 'o'
    elif bx2=='_' and raw_input==('bx2'):
        bx2 = 'o'
    elif by2=='_' and raw_input==('by2'):
        by2 = 'o'
    elif bz2=='_' and raw_input==('bz2'):
        bz2 = 'o'
        
    elif cw2=='_' and raw_input==('cw2'):
        cw2 = 'o'
    elif cx2=='_' and raw_input==('cx2'):
        cx2 = 'o'
    elif cy2=='_' and raw_input==('cy2'):
        cy2 = 'o'
    elif cz2=='_' and raw_input==('cz2'):
        cz2 = 'o'
        
    elif dw2=='_' and raw_input==('dw2'):
        dw2 = 'o'
    elif dx2=='_' and raw_input==('dx2'):
        dx2 = 'o'
    elif dy2=='_' and raw_input==('dy2'):
        dy2 = 'o'
    elif dz2=='_' and raw_input==('dz2'):
        dz2 = 'o'
        
    """plane 3"""
    if aw3=='_' and raw_input==('aw3'):
        aw3 = 'o'
    elif ax3=='_' and raw_input==('ax3'):
        ax3 = 'o'
    elif ay3=='_' and raw_input==('ay3'):
        ay3 = 'o'
    elif az3=='_' and raw_input==('az3'):
        az3 = 'o'
        
    elif bw3=='_' and raw_input==('bw3'):
        bw3 = 'x'
    elif bx3=='_' and raw_input==('bx3'):
        bx3 = 'x'
    elif by3=='_' and raw_input==('by3'):
        by3 = 'x'
    elif bz3=='_' and raw_input==('bz3'):
        bz3 = 'x'
    
    elif cw3=='_' and raw_input==('cw3'):
        cw3 = 'o'
    elif cx3=='_' and raw_input==('cx3'):
        cx3 = 'o'
    elif cy3=='_' and raw_input==('cy3'):
        cy3 = 'o'
    elif cz3=='_' and raw_input==('cz3'):
        cz3 = 'o'
        
    elif dw3=='_' and raw_input==('dw3'):
        dw3 = 'o'
    elif dx3=='_' and raw_input==('dx3'):
        dx3 = 'o'
    elif dy3=='_' and raw_input==('dy3'):
        dy3 = 'o'
    elif dz3=='_' and raw_input==('dz3'):
        dz3 = 'o'
        
    """plane 4"""
    if aw4=='_' and raw_input==('aw4'):
        aw4 = 'o'
    elif ax4=='_' and raw_input==('ax4'):
        ax4 = 'o'
    elif ay4=='_' and raw_input==('ay4'):
        ay4 = 'o'
    elif az4=='_' and raw_input==('az4'):
        az4 = 'o'
        
    elif bw4=='_' and raw_input==('bw4'):
        bw4 = 'o'
    elif bx4=='_' and raw_input==('bx4'):
        bx4 = 'o'
    elif by4=='_' and raw_input==('by4'):
        by4 = 'o'
    elif bz4=='_' and raw_input==('bz4'):
        bz4 = 'o'
        
    elif cw4=='_' and raw_input==('cw4'):
        cw4 = 'o'
    elif cx4=='_' and raw_input==('cx4'):
        cx4 = 'o'
    elif cy4=='_' and raw_input==('cy4'):
        cy4 = 'o'
    elif cz4=='_' and raw_input==('cz4'):
        cz4 = 'o'
        
    elif dw4=='_' and raw_input==('dw4'):
        dw4 = 'o'
    elif dx4=='_' and raw_input==('dx4'):
        dx4 = 'o'
    elif dy4=='_' and raw_input==('dy4'):
        dy4 = 'o'
    elif dz4=='_' and raw_input==('dz4'):
        dz4 = 'o'

def xw():
    '''Two Dimensional win methods'''
    
    '''a-row'''
    if aw1=='x' and ax1=='x' and ay1=='x' and az1=='x':
        winner = 'x'
    elif aw2=='x' and ax2=='x' and ay2=='x' and az2=='x':
        winner = 'x'
    elif aw3=='x' and ax3=='x' and ay3=='x' and az3=='x':
        winner = 'x'
    elif aw4=='x' and ax4=='x' and ay4=='x' and az4=='x':
        winner = 'x'
        
    '''b-row'''
    if bw1=='x' and bx1=='x' and by1=='x' and bz1=='x':
        winner = 'x'
    elif bw2=='x' and bx2=='x' and by2=='x' and bz2=='x':
        winner = 'x'
    elif bw3=='x' and bx3=='x' and by3=='x' and bz3=='x':
        winner = 'x'
    elif bw4=='x' and bx4=='x' and by4=='x' and bz4=='x':
        winner = 'x'
        
    '''c-row'''
    if cw1=='x' and cx1=='x' and cy1=='x' and cz1=='x':
        winner = 'x'
    elif cw2=='x' and cx2=='x' and cy2=='x' and cz2=='x':
        winner = 'x'
    elif cw3=='x' and cx3=='x' and cy3=='x' and cz3=='x':
        winner = 'x'
    elif cw4=='x' and cx4=='x' and cy4=='x' and cz4=='x':
        winner = 'x'
    
    '''d-row'''
    if dw1=='x' and dx1=='x' and dy1=='x' and dz1=='x':
        winner = 'x'
    elif dw2=='x' and dx2=='x' and dy2=='x' and dz2=='x':
        winner = 'x'
    elif dw3=='x' and dx3=='x' and dy3=='x' and dz3=='x':
        winner = 'x'
    elif dw4=='x' and dx4=='x' and dy4=='x' and dz4=='x':
        winner = 'x'
    
    '''w-row'''
    if aw1=='x' and bw1=='x' and cw1=='x' and dw1=='x':
        winner = 'x'
    elif aw2=='x' and bw2=='x' and cw2=='x' and dw2=='x':
        winner = 'x'
    elif aw3=='x' and bw3=='x' and cw3=='x' and dw3=='x':
        winner = 'x'
    elif aw4=='x' and bw4=='x' and cw4=='x' and dw4=='x':
        winner = 'x'
    
    '''-row'''
    if ax1=='x' and bx1=='x' and cx1=='x' and dx1=='x':
        winner = 'x'
    elif ax2=='x' and bx2=='x' and cx2=='x' and dx2=='x':
        winner = 'x'
    elif ax3=='x' and bx1=='x' and cx3=='x' and dx3=='x':
        winner = 'x'
    elif ax4=='x' and bx4=='x' and cx4=='x' and dx4=='x':
        winner = 'x'
    
    '''y-row'''
    if ay1=='x' and by1=='x' and cy1=='x' and dy1=='x':
        winner = 'x'
    elif ay2=='x' and by2=='x' and cy2=='x' and dy2=='x':
        winner = 'x'
    elif ay3=='x' and by3=='x' and cy3=='x' and dy3=='x':
        winner = 'x'
    elif ay4=='x' and by4=='x' and cy4=='x' and dy4=='x':
        winner = 'x'
    
    '''z-row'''
    if az1=='x' and bz1=='x' and cz1=='x' and dz1=='x':
        winner = 'x'
    elif az2=='x' and bz2=='x' and cz2=='x' and dz2=='x':
        winner = 'x'
    elif az3=='x' and bz3=='x' and cz3=='x' and dz3=='x':
        winner = 'x'
    elif az4=='x' and bz4=='x' and cz4=='x' and dz4=='x':
        winner = 'x'
    
    '''forward-slash'''
    if aw1=='x' and bx1=='x' and cy1=='x' and dz1=='x':
        winner = 'x'
    elif aw2=='x' and bx2=='x' and cy2=='x' and dz2=='x':
        winner = 'x'
    elif aw3=='x' and bx3=='x' and cy3=='x' and dz3=='x':
        winner = 'x'
    elif aw4=='x' and bx4=='x' and cy4=='x' and dz4=='x':
        winner = 'x'
        
    '''back-slash'''
    if az1=='x' and by1=='x' and cx1=='x' and dw1=='x':
        winner = 'x'
    elif az2=='x' and by2=='x' and cx2=='x' and dw2=='x':
        winner = 'x'
    elif az3=='x' and by3=='x' and cx3=='x' and dw3=='x':
        winner = 'x'
    elif az4=='x' and by4=='x' and cx4=='x' and dw4=='x':
        winner = 'x'
        
    '''Three Dimensional win methods'''
        
    '''a-row'''
    if aw1=='x' and ax2=='x' and ay3=='x' and az4=='x':
        winner = 'x'
    elif aw4=='x' and ax3=='x' and ay2=='x' and az2=='x':
        winner = 'x'
        
    '''b-row'''
    if bw1=='x' and bx2=='x' and by3=='x' and bz3=='x':
        winner = 'x'
    elif bw4=='x' and bx3=='x' and by2=='x' and bz1=='x':
        winner = 'x'
            
        '''c-row'''
    if cw1=='x' and cx2=='x' and cy3=='x' and cz4=='x':
        winner = 'x'
    elif cw4=='x' and cx3=='x' and cy2=='x' and cz1=='x':
        winner = 'x'
        
    '''d-row'''
    if dw1=='x' and dx2=='x' and dy3=='x' and dz4=='x':
        winner = 'x'
    elif dw4=='x' and dx3=='x' and dy2=='x' and dz1=='x':
        winner = 'x'
        
    '''w-row'''
    if aw1=='x' and bw2=='x' and cw3=='x' and dw4=='x':
        winner = 'x'
    elif aw4=='x' and bw3=='x' and cw2=='x' and dw1=='x':
        winner = 'x'
        
    '''x-row'''
    if ax1=='x' and bx2=='x' and cx3=='x' and dx4=='x':
        winner = 'x'
    elif ax4=='x' and bx3=='x' and cx2=='x' and dx1=='x':
        winner = 'x'
        
    '''y-row'''
    if ay1=='x' and by2=='x' and cy3=='x' and dy4=='x':
        winner = 'x'
    elif ay4=='x' and by3=='x' and cy2=='x' and dy1=='x':
        winner = 'x'
        
    '''z-row'''
    if az1=='x' and bz2=='x' and cz3=='x' and dz4=='x':
        winner = 'x'
    elif az4=='x' and bz3=='x' and cz2=='x' and dz1=='x':
        winner = 'x'
        
    '''forward-slash'''
    if aw1=='x' and bx2=='x' and cy3=='x' and dz4=='x':
        winner = 'x'
    elif aw4=='x' and bx3=='x' and cy2=='x' and dz1=='x':
        winner = 'x'
    
    '''back-slash'''
    if az1=='x' and by2=='x' and cx3=='x' and dw4=='x':
        winner = 'x'
    elif az4=='x' and by3=='x' and cx2=='x' and dw1=='x':
        winner = 'x'
        
        
def ow():    
    '''Two Dimensional win methods'''
    
    '''a-row'''
    if aw1=='o' and ax1=='o' and ay1=='o' and az1=='o':
        winner = 'o'
    elif aw2=='o' and ax2=='o' and ay2=='o' and az2=='o':
        winner = 'o'
    elif aw3=='o' and ax3=='o' and ay3=='o' and az3=='o':
        winner = 'o'
    elif aw4=='o' and ax4=='o' and ay4=='o' and az4=='o':
        winner = 'o'
        
    '''b-row'''
    if bw1=='o' and bx1=='o' and by1=='o' and bz1=='o':
        winner = 'o'
    elif bw2=='o' and bx2=='o' and by2=='o' and bz2=='o':
        winner = 'o'
    elif bw3=='o' and bx3=='o' and by3=='o' and bz3=='o':
        winner = 'o'
    elif bw4=='o' and bx4=='o' and by4=='o' and bz4=='o':
        winner = 'o'
        
    '''c-row'''
    if cw1=='o' and cx1=='o' and cy1=='o' and cz1=='o':
        winner = 'o'
    elif cw2=='o' and cx2=='o' and cy2=='o' and cz2=='o':
        winner = 'o'
    elif cw3=='o' and cx3=='o' and cy3=='o' and cz3=='o':
        winner = 'o'
    elif cw4=='o' and cx4=='o' and cy4=='o' and cz4=='o':
        winner = 'o'
        
    '''d-row'''
    if dw1=='o' and dx1=='o' and dy1=='o' and dz1=='o':
        winner = 'o'
    elif dw2=='o' and dx2=='o' and dy2=='o' and dz2=='o':
        winner = 'o'
    elif dw3=='o' and dx3=='o' and dy3=='o' and dz3=='o':
        winner = 'o'
    elif dw4=='o' and dx4=='o' and dy4=='o' and dz4=='o':
        winner = 'o'
        
    '''w-row'''
    if aw1=='o' and bw1=='o' and cw1=='o' and dw1=='o':
        winner = 'o'
    elif aw2=='o' and bw2=='o' and cw2=='o' and dw2=='o':
        winner = 'o'
    elif aw3=='o' and bw3=='o' and cw3=='o' and dw3=='o':
        winner = 'o'
    elif aw4=='o' and bw4=='o' and cw4=='o' and dw4=='o':
        winner = 'o'
        
    '''x-row'''
    if ax1=='o' and bx1=='o' and cx1=='o' and dx1=='o':
        winner = 'o'
    elif ax2=='o' and bx2=='o' and cx2=='o' and dx2=='o':
        winner = 'o'
    elif ax3=='o' and bx1=='o' and cx3=='o' and dx3=='o':
        winner = 'y'
    elif ax4=='o' and bx4=='o' and cx4=='o' and dx4=='o':
        winner = 'o'
    
    '''y-row'''
    if ay1=='o' and by1=='o' and cy1=='o' and dy1=='o':
        winner = 'o'
    elif ay2=='o' and by2=='o' and cy2=='o' and dy2w=='o':
        winner = 'o'
    elif ay3=='o' and by3=='o' and cy3=='o' and dy3=='o':
        winner = 'o'
    elif ay4=='o' and by4=='o' and cy4=='o' and dy4=='o':
        winner = 'o'
    
    '''z-row'''
    if az1=='o' and bz1=='o' and cz1=='o' and dz1=='o':
        winner = 'o'
    elif az2=='o' and bz2=='o' and cz2=='o' and dz2=='o':
        winner = 'o'
    elif az3=='o' and bz3=='o' and cz3=='o' and dz3=='o':
        winner = 'o'
    elif az4=='o' and bz4=='o' and cz4=='o' and dz4=='o':
        winner = 'o'
    
    '''forward-slash'''
    if aw1=='o' and bx1=='o' and cy1=='o' and dz1=='o':
        winner = 'o'
    elif aw2=='o' and bx2=='o' and cy2=='o' and dz2=='o':
        winner = 'o'
    elif aw3=='o' and bx3=='o' and cy3=='o' and dz3=='o':
        winner = 'o'
    elif aw4=='o' and bx4=='o' and cy4=='o' and dz4=='o':
        winner = 'o'
        
    '''back-slash'''
    if az1=='o' and by1=='o' and cx1=='o' and dw1=='o':
        winner = 'o'
    elif az2=='o' and by2=='o' and cx2=='o' and dw2=='o':
        winner = 'o'
    elif az3=='o' and by3=='o' and cx3=='o' and dw3=='o':
        winner = 'o'
    elif az4=='o' and by4=='o' and cx4=='o' and dw4=='o':
        winner = 'o'
        
    '''Three Dimensional win methods'''
        
    '''a-row'''
    if aw1=='o' and ax2=='o' and ay3=='o' and az4=='o':
        winner = 'o'
    elif aw4=='o' and ax3=='o' and ay2=='o' and az2=='o':
        winner = 'o'
        
    '''b-row'''
    if bw1=='o' and bx2=='o' and by3=='o' and bz3=='o':
        winner = 'o'
    elif bw4=='o' and bx3=='o' and by2=='o' and bz1=='o':
        winner = 'o'
        
    '''c-row'''
    if cw1=='o' and cx2=='o' and cy3=='o' and cz4=='o':
        winner = 'o'
    elif cw4=='o' and cx3=='o' and cy2=='o' and cz1=='o':
        winner = 'o'
        
    '''d-row'''
    if dw1=='o' and dx2=='o' and dy3=='o' and dz4=='o':
        winner = 'o'
    elif dw4=='o' and dx3=='o' and dy2=='o' and dz1=='o':
        winner = 'o'
        
    '''w-row'''
    if aw1=='o' and bw2=='o' and cw3=='o' and dw4=='o':
        winner = 'o'
    elif aw4=='o' and bw3=='o' and cw2=='o' and dw1=='o':
        winner = 'o'
        
    '''x-row'''
    if ax1=='o' and bx2=='o' and cx3=='o' and dx4=='o':
        winner = 'o'
    elif ax4=='o' and bx3=='o' and cx2=='o' and dx1=='o':
        winner = 'o'
        
    '''y-row'''
    if ay1=='o' and by2=='o' and cy3=='o' and dy4=='o':
        winner = 'o'
    elif ay4=='o' and by3=='o' and cy2=='o' and dy1=='o':
        winner = 'o'
        
    '''z-row'''
    if az1=='o' and bz2=='o' and cz3=='o' and dz4=='o':
        winner = 'o'
    elif az4=='o' and bz3=='o' and cz2=='o' and dz1=='o':
        winner = 'o'
        
    '''forward-slash'''
    if aw1=='o' and bx2=='o' and cy3=='o' and dz4=='o':
        winner = 'o'
    elif aw4=='o' and bx3=='o' and cy2=='o' and dz1=='o':
        winner = 'o'
        
    '''back-slash'''
    if az1=='o' and by2=='o' and cx3=='o' and dw4=='o':
        winner = 'o'
    elif az4=='o' and by3=='o' and cx2=='o' and dw1=='o':
        winner = 'o'
    

def play():
    bp()        
    while winner == 'none':
        xt()
        ot()
        xt()
        ow()
