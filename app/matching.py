
def directionCheck(a1, a2, b1, b2):#a1 = start of user a, a2 is end, b1 start of user b, b2 end of user b
    
    check = False
    keys=list(b1.keys())
    ax1 = float(a1[0])
    ax2 = float(a2[0])
    ay1 = float(a1[1])
    ay2 = float(a2[1])
    bx1 = float(b1[0])
    bx2 = float(b2[0])
    by1 = float(b1[1])
    by2 = float(b2[1])
    y2 = by1
    y1 = ay1
    x2 = bx1
    x1 = ax1
    a = -(y2-y1)/(x2-x1)
    b = 1
    c = x1*((y2-y1)/(x2-x1)) - y1
    f1 = a*ax2 + b*ay2 + c
    f2 = a*bx2 + b*by2 + c
    d = (((ax1-bx1)^2) + ((ay1-by1)^2))^(1/2)
    if(f1*f2>0 and d<3):
        check = True

    # finding distance between them    
    ll1=(99.2,78.3)# starting point of user 1
    ll2=(78.2,66.3)# starting point of user 2

    R=6373.0
    lat1 = math.radians(ll1[0])
    lon1 = math.radians(ll1[1])
    lat2 = math.radians(ll2[0])
    lon2 = math.radians(ll2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  

    possible=False
    if distance <=3.0 and check==True:
        possible=True

    return possible

def personality(u1,d1):# takes in user and dictionary of all users
    compatibility1={'ENFJ': 'INFP',
    'ENFP': 'INFJ',
    'ENTJ': 'INTP',
    'ESFJ': 'ISFP',
    'ESTP': 'ISFJ',
    'INFJ': 'ENTP',
    'INTP': 'INTJ',
    'ISTJ': 'ESFP',
    'ISTP': 'ESTJ'}

    compatibility2={'ENTP': 'INFJ',
    'ESFP': 'ISTJ',
    'ESTJ': 'ISTP',
    'INFJ': 'ENFP',
    'INFP': 'ENFJ',
    'INTJ': 'INTP',
    'INTP': 'ENTJ',
    'ISFJ': 'ESTP',
    'ISFP': 'ESFJ'}

    per1=u1[1]
    compatible=compatibility1.get(per1)
    if compatible==None:
        compatible=compatibility2.get(per1)

    li_usrs=[]
    keys1=list(d1.keys())

    for i in keys1:
        if d1[i]==compatible:
            li_usrs.append(i)
    print(li_usrs)
    return li_usrs        


def match(u2,d2):
    ans=u2[1]
    key_list = list(d2.keys())
    if u2[0] in key_list:
        key_list.remove(u2[0])
    val_list = list(d2.values())
    count=0

    di_val={}
    for i in key_list:
        current=d2[i]
        for j in range(len(ans)):
            if ans[j]==current[j]:
                count+=1
        di_val[i]=count
    # Getting the user with maximum score
    keymax = max(di_val, key=di_val.get)
    user_n=u2[0] # current users name

    return keymax

