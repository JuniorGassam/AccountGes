from Bank import Bank
from Compte import Compte
from Utilisateur import Utilisateur

if __name__ == '__main__':

    #Instanciation entités
    creditAgr = Bank("Crédit Agricole")
    utilisateur = Utilisateur("adrien","fouquet")
    utilDeux = Utilisateur("Junior","Gassam")
    utilTrois = Utilisateur("Damien","Journel")
    compteUn = Compte(utilisateur,creditAgr)
    compteDeux = Compte(utilDeux,creditAgr)
    compteTrois = Compte(utilTrois,creditAgr)

    #Test dépôt
    compteUn.depot(10000)
    compteDeux.depot(15000)
    print(compteDeux.getBalance())


    # Test retrait
    compteUn.retrait(12000)
    compteDeux.retrait(2000)
    print(compteDeux.getBalance())

    #Test Virement
    compteDeux.virement(10000,compteTrois)
    print(compteDeux.getBalance(),compteTrois.getBalance())


