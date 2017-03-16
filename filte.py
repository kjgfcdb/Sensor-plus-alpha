def filte(pitch):
    n = len(pitch)
    for i in range(0,n-1,1):
        if (pitch[i]>800):
            l = i
            break
    r = n-1
    for i in range(n-1,0,-1):
        if (pitch[i]>800):
            r = i
            break
    return l,r