from CompteCourant import CompteCourant
from CompteEpargne import CompteEpargne

class Bank:
    def __init__(self, name, comptes=[]):
        self.name = name
        self.comptes = comptes

    def creationNouveauCompte(self,utilisateur,type,opt):
        if(type=="courant"):
            newCompte = CompteCourant(utilisateur,self,opt)
        elif (type == "epargne"):
            newCompte = CompteEpargne(utilisateur,self,opt)
        self.comptes.append(newCompte)
        return newCompte

    def getComptes(self):
        for compte in self.comptes:
            print(compte.getInfos())
