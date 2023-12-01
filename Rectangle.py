nbrRectangle= 0
    def __init__(self , largeur , longueur  ) :
        self.__largeur = largeur
        self.__longueur = longueur
        rectangle.nbrRectangle += 1

    def getlargeur(self):
        return self.__largeur
    def setlargeur(self,largeur):
        self.__largeur=largeur
    def getlongueur(self):
        return self.__longueur

    def setlargeur(self,longueur):
        self.__longueur=longueur
    def getnbrRectangle(self):
        return self.nbrRectangle

    def perimetre(self):
        return 2 * (self.__largeur + self.__longueur)


    def equals(self):
         if self.__largeur == self.__longueur:
              return True
         else :
              return False

    def tostring(self):
         return( "largeur",{self.__largeur}, "longeur",{self.__longueur})


    def surface(self ):
         return  self.__largeur * self.__longueur


class parallelepipide(rectangle):
         nbrparallelepipide = 0
         def __init__(self,longueur ,largeur , hauteur ):
              rectangle.__init__(self , longueur , largeur)
              self.__hauteur = hauteur
              self.__largeur= largeur
              self.__longueur=longueur
              parallelepipide.nbrparallelepipide += 1

         def gethauteur(self):
              return self.__hauteur


         def volume(self):
             return self.__longueur *(self.__hauteur)* self.__hauteur 


         def equals(self):
             if self.__largeur == self.__longueur == self.__hauteur:
              return True
             else :
              return False

         def tostring (self):
              print("largeur" ,{self.__largeur},"longueur",{self.__longueur},"hauteur",{self.__hauteur})


rec1 = rectangle(7,11)
p1 = parallelepipide(1,5,7)
print("le perimitre de rectangle:",rec1.perimetre())
print("la surface de rectangle:",rec1.surface())
print("le volume de parallelepipede:",p1.volume())
print(p1.tostring())
print(rec1.tostring())  
print(rec1.equals())
print(rec1.equals())       


