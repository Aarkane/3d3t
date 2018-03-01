def xWins():
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