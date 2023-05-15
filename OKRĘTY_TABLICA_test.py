import random
ships = (4,3,3,2,2,2,1,1,1,1)
#ships = (3,3,2,2,2,1,1,1,1)
#ships = (4)



#board_comp()



#utworzenie pustej planszx

def board_new():

    lista=[]
    for p in range (10):
        wiersz = []
        for q in range (10):
            wiersz.append('')
        lista.append(wiersz)

    #print('nowa plansza:')
    #for y in range (10):
    #    print(lista[y])
    return lista


    #utworzenie planszy z numerami pól
def board_new_n():

    lista=[]
    a=0
    for p in range (10):
        wiersz = []
        for q in range (10):
            wiersz.append(a + q)
        lista.append(wiersz)
        a += 10
    #print('nowa plansza:')
    #for y in range (10):
    #    print(lista[y])

    #print('===========')
    #print()

    return lista



#==============================================================================
def number_s():
    y = random.randint(0,9)
    x = random.randint(0,9)
    z = random.randint(0,1)
#    y = 3
#    x = 2
#    z = 0
    return y, x, z
#==============================================================================
def powtorka(statek):
    y, x, z = number_s()

    while (y > (10 - statek)) and (x > (10 - statek)):
        y = random.randint(0,9)
        x = random.randint(0,9)

    if y > (10 - statek): z = 0
    if x > (10 - statek): z = 1
    print('y, x, z - powtorka: ',y,' ',x,' ',z)

    return y, x, z

#==============================================================================

def board_comp():#(y, x, z):

    board_0 = board_new()
#    print('board_0: ')
#    for d in range (10):
#        print(board_0[d])

    #umieszczanie stsku 4 na planszy
#    y, x, z = powtorka(4)
#    y = 0
#    x = 0
#    z = 0
#    p0, p1, q0, q1, y, x, z = parametry(y, x, z, 4, board_0)

#    for a in range(4):
#        if z == 0:
#            board_0[y][x+a] = 'S'#'4'#ships[i] #'S'
#        else:
#            board_0[y+a][x] = 'S'#'4'#ships[i] #'S'
#    print('board_0_4: ')
#    for d in range (10):
#        print(board_0[d])

    #tworzenie statków 4, 3,3, 2,2,2, 1,1,1,1

    k = len(ships)
    for i in range(k):
        print('board_0_1: ')
        for d in range (10):
            print(board_0[d])

        statek = ships[i]

        print('\ni - statek: ',i,'/',statek)

        board_0 = board_0

        y, x, z = statek_new(statek, board_0)

        print('board_comp:')
        print('y, x, z : ', y,'/', x,'/', z)

        #umieszczanie stsków na planszy

        for a in range(statek):
            if z == 0:
                board_0[y][x+a] = 'S'#ships[i] #'S'
            else:
                board_0[y+a][x] = 'S'#ships[i] #'S'

        print('board_0_3: ')    
        for d in range (10):
            print(board_0[d])

    return board_0


#==============================================================================
def statek_new(statek, board_0):
    y, x, z = powtorka(statek)
    p0, p1, q0, q1, y, x, z = parametry(y, x, z, statek, board_0)

    print('parametry :')
    print('y, x, z : ',y,' ',x,' ',z)
    print('p0, p1, q0, q1 : ',p0,' ', p1,' ', q0,' ', q1)

    wiersz = []
    for p in range (p0, p1):
        print('\np: ',p)
        for q in range (q0, q1):
            print('q:' ,q)
            c = board_0[p][q]
            print('c - statek_new: ',c)
            wiersz.append(c)

    print('wiersz: ',wiersz)

    if 'S' in wiersz:
        print('statek_new(statek, board_0')
        p0, p1, q0, q1, y, x, z = '','','','','','',''
        print('p0, p1, q0, q1, y, x, z = ',p0, p1, q0, q1, y, x, z)
        statek_new(statek, board_0)
#        statek_new(statek, board_0, statek_i)
    else:
        print('\nkontrola_S - wyjscie:')
        print('y, x, z : ', y,'/', x,'/', z)
        print('p0, p1, q0, q1: ',p0,'/', p1,'/', q0,'/', q1)
        print('======')
        return y, x, z
#    print('\nkontrola_S - wyjscie:')
#    print('y, x, z : ', y,'/', x,'/', z)
#    print('p0, p1, q0, q1: ',p0,'/', p1,'/', q0,'/', q1)
#    print('======')
#    return y, x, z



#==============================================================================

def parametry(y, x, z, statek, board_0):

    # y - indeks (numer) wiersza
    # x - indeks (numer) kolumny
    # z - kierunek statku - z = 0 -> poziom;, z = 1 -> pion
        #indeksy zakresów kontroli zajętości tabeli
    if z == 0:
        zy = 2
        zx = statek + 1
    if z == 1:
        zy = statek + 1
        zx = 2

    p0 = y-1
    p1 = y+zy
    q0 = x-1
    q1 = x+zx


    #WARUNKI BRZEGOWE

    #lewy górny róg poziom
    if y == 0:
        p0 = y
    #lewy górny róg pion
    if x == 0:
        q0 = x

            #lewy dolny róg pion
    if y + statek - 1 == 9 and z == 1:
        p1 = 9
    #lewy dolny róg pozim
    if x + statek - 1 == 9 and z == 0:
        q1 = 9

            #prawy górny róg poziom
    if y == 9 and x == 0 and z == 0:
        p1 = 10
        q0 = x
            #prawy górny róg pion
    if x == 9 and y == 0 and z == 1:
        p0 = y
        q1 = 10

            #prawy dolny róg poziom
    if y == 9 and  x + statek - 1 == 9  and z == 0:
        p1 = 10
        q1 = 10
            #prawy dolny róg pion
    if y + statek - 1 == 9 and  x == 9  and z == 1:
        p1 = 10
        q1 = 10

            #lewy bok pion
    if y + statek - 1 < 9 and  y + statek - 1 > 0 and x == 0  and z == 1:
        q0 = x
            #prawy bok pion
    if y + statek - 1 < 9 and  y + statek - 1 > 0 and x == 9  and z == 1:
        q1 = x + 1

            #górny bok poziom
    if x + statek - 1 < 9 and  x + statek - 1 > 0 and y == 0  and z == 0:
        p0 = y
            #dolny bok poziom
    if x + statek - 1 < 9 and  x + statek - 1 > 0 and y == 9  and z == 0:
        p1 = 10

            #lewy bok poziom
    if 0 < y < 9 and x == 0  and z == 0:
        q0 = x
            #prawy bok poziom
    if 0 < y < 9 and x + statek - 1 == 9  and z == 0:
        q1 = 10

            #górny bok pion
    if 0 < x < 9 and y == 0  and z == 1:
        p0 = y
            #dolny bok pion
    if 0 < x < 9 and y + statek - 1 == 9  and z == 1:
        p1 = 10
    return p0, p1, q0, q1, y, x, z


#==============================================================================
#==============================================================================

#==============================================================================



board_comp()








