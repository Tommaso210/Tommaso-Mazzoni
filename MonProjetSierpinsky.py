import turtle
turtle.tracer(0,0)            # acceleration du tracé
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):    

    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F']: turtle.forward(longueur)

#dessiner('F', 50, 60)

def regleKoch(chaine):
    nouvelleChaine = 'Sierpinski' 
    for lettre in chaine: 
        if lettre == 'F'
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F' 
        elif lettre == 'G' :
            
return nouvelleChaine

def courbeKoch(motifInitial, niter):
    
        appelle niter fois regleKoch

    courbe = motifInitial
    for i in range(niter):
        nouveauMotif = regleKoch(courbe)
        courbe = nouveauMotif
    return courbe


#courbe = courbeKoch('F',3)
#dessiner(courbe,50, 60)

def flocon(motifInitial, niter):
    courbe = courbeKoch(motifInitial, niter)
    flocon = ''
    for _ in range(3):
        flocon += courbe
        flocon += '--' 
    return flocon

