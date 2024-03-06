from journalisation import logsVirement

class Compte(object):
    def __init__(self, utilisateur, bank):
        self.utilisateur = utilisateur
        self.bank = bank
        self.balance = 0

    def getBalance(self):
        return self.balance
    def getutilisateur(self):
        return self.utilisateur.getNom()
    def getbank(self):
        return self.bank
    def getInfos(self):
        print(self.utilisateur.getNom(),self.balance)
        return True

    def retrait(self,montant):
        if(self.balance < montant):
            print('erreur votre solde est trop faible par rapport au montant demandé')
            return False
        else:
            self.balance -= montant
            return True

    def depot(self,montant):
        self.balance += montant
        return True

    @logsVirement
    def virement(self,montant,compteDestinataire):
        if (self.balance < montant):
            print('erreur votre solde est trop faible par rapport au montant demandé')
            return False
        else:
            self.balance -= montant
            verif = compteDestinataire.ajouterArgent(montant)
            return verif

    def ajouterArgent(self,montant):
        self.balance += montant
        return True


