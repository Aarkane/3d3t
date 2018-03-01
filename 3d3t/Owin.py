def oWins():    
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