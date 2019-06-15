
    #arranges list, swaps the number if x1>x2 or y1>y2
def arrangelist(l):
    if(l[0]>l[2]):
        temp=l[2]
        l[2]=l[0]
        l[0]=temp

    if(l[1]>l[3]):
        temp=l[3]
        l[3]=l[1]
        l[1]=temp
    return l

    #returns 1 if the first block is the lower one according to x origin
def whichisdown(l1,l2):
    if(l2[1]>=l1[1]):
        return 1

    return 0

    #calculates an area
def singlearea(l):
    return abs(l[2]-(l[0]))*abs(l[3]-(l[1]))

    #The lower block should have its lower edge placed directly on the x axis.
def firstrule(l1,l2):
    if(whichisdown(l1,l2) and l1[1]==0):
        return True

    elif((whichisdown(l1,l2)==0) and l2[1]==0):
        return True

    else:
        return False

    #The upper block should have its lower edge (at least partially) coincide with the upper edge
    #of the lower block.
def secondrule(l1,l2):
    if(whichisdown(l1,l2) and l1[3]==l2[1]):
        return True

    elif(whichisdown(l1,l2)==0 and l2[3]==l1[1]):
        return True

    return False

def center_of_mass(l):
    if(l[0]>0 and l[2]>0):
        return l[2]-(l[2]-l[0])/2.0

    elif(l[0]<0 and l[2]<0):
        return l[0]-(l[0]-l[2])/2.0

    else:
        return l[2]-abs(((l[0])-l[2])/(2.0))


    #The upper block should have its center of mass abscissa in the range of the lower blocks
    #upper edge.
def thirdrule(l1,l2):
    eps = 0.001
    l1c = center_of_mass(l1)
    l2c = center_of_mass(l2)

    if(abs(l2c-l1[2]) < eps):
        l2c = l1[2]

    if(abs(l2c-l1[0])<eps):
        l2c = l1[0]

    if(abs(l1c-l2[2])<eps):
        l1c = l2[2]

    if(abs(l1c-l2[0])<eps):
        l1c = l2[0]
    if ( whichisdown(l1,l2) and (l2c > (l1[2])  or l2c < l1[0]) ):
        return False

    elif ( whichisdown(l1,l2)==0 and (l1c > l2[2] or l1c < l2[0]) ):
        return False

    else:
        return True


def addendum(l1,l2):
    if ( whichisdown(l1,l2) ):
        l2c = center_of_mass(l2)
        if (l2c > l1[2]):
            addx = (l2c-l1[2]) * 2
            if (l2[0]>0):
                addx = -addx
            return ["ADDENDUM", [ l2[0]+addx , l2[1] , l2[0] , l2[3]]]
        else:
            addx = abs(l2c-l1[0]) * 2
            return ["ADDENDUM", [ l2[2] , l2[1] , l2[2]+addx , l2[3]]]
    else:
        l1c = center_of_mass(l1)
        if ( l1c > l2[2] ):
            addx = abs(l1c-l2[2]) * 2
            if(l1[0]>0):
                addx = -addx

            return ["ADDENDUM", [ l1[0]+addx , l1[1] , l1[0] , l1[3]]]
        else:
            addx = abs(l1c-l2[0]) * 2

            return ["ADDENDUM", [ l1[2] , l1[1] , l1[2]+addx , l1[3]]]

def calculatearea(l1,l2):
    overlap=0
    area1=singlearea(l1);
    area2=singlearea(l2);
    sum=area1+area2

    if(l2[1]>=l1[3] or l2[0]>l1[2]): #if there is no overlap
        overlap = 0

    elif (l2[0]>=l1[0] and l2[1]>=l1[1] and l2[2]<=l1[2] and l2[3]<=l1[3] ):#if l2 is in l1
        overlap = area2

    elif(l2[1]<l1[3] and l2[1]>l1[1]):

        if(l2[0]<l1[2] and l2[0]>l1[0] and l2[2]>l1[2]):
            overlap = abs(l1[3]-(l2[1])) * abs(l1[2] - (l2[0]))

        elif(l2[0]<l1[0] and l2[2]>l1[0] and l2[2] < l1[2]):
            overlap = abs(l1[3]-(l2[1])) * abs(l2[2] - (l1[0]))

        elif(l2[2]>l1[2] and l1[0]>l2[0] and l2[3]<l1[3] and l2[1]>l1[1]):
            overlap = abs(l2[3]-l2[1]) * abs(l1[2]-l1[1])

        elif(l2[1]<l1[3] and l2[0] >l1[0] and l2[0]<l1[2] and l2[2]<l1[2] and l2[2]>l1[0]):
            overlap = abs(l1[3] - (l2[1])) * abs(l2[2] - (l2[0]))

        else:
            overlap = abs(l1[3] - (l2[1])) * abs(l1[2] - (l1[0]))
    else:
        overlap = abs(l2[3]- (l2[1])) * abs(l1[2] -(l2[0]))


    return sum-(overlap)




def is_firmus(l1,l2):
    l1=arrangelist(l1)
    l2=arrangelist(l2)

    fr = firstrule(l1,l2)
    sr = secondrule(l1,l2)
    tr = thirdrule(l1,l2)

    if(fr and sr and tr):
        return ["FIRMUS",singlearea(l1)+singlearea(l2)]

    elif(fr and sr and tr == False):
        return addendum(l1,l2)

    else:
        if (whichisdown(l1,l2)):

            return ["DAMNARE",calculatearea(l1,l2)]
        else:
            return ["DAMNARE",calculatearea(l2,l1)]
