from epidemie import *
from os import system

#Epidemiologie.create_json_file()

system("cls")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::>>>> EPIDEMIOLOGIE <<<:::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

system("pause")
while True:
    system("cls")
    print("++++++++++++++++++++++++++ OPTIONS PRINCIPAL ++++++++++++++++++++++++")
    print("\t1- Gerer Les Epidémies")
    print("\t2- Gerer Les patient")
    print("\t0- Quitter")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    choix = input("Faites votre choix: ")
    while choix not in ("0","1","2"):
        system("cls")
        print("Saisie incorrect - Reéssayez !!!")
        system("pause")
        system("cls")
        print("++++++++++++++++++++++++++ MENU PRINCIPAL ++++++++++++++++++++++++")
        print("\t1- Gerer Les Epidémies")
        print("\t2- Gerer Les patient")
        print("\t0- Quitter")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        choix = input("Faites votre choix: ")
    if choix == "1":
        system("cls")
        print("++++++++++++++++++++++++++ EPIDEMIES ++++++++++++++++++++++++")
        print("\t1- Liste des Epidemies")
        print("\t2- Ajouter un variant a une Epidemie")
        print("\t3- Afficher la Liste des variants d'une Epidemie")
        print("\t4- Ajouter une Epidémie")
        print("\t0- quitter")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        choix2 = input("Faites votre choix: ")
        while choix2 not in ("0","1","2","3","4"):
            system("cls")
            print("++++++++++++++++++++++++++ EPIDEMIES ++++++++++++++++++++++++")
            print("\t1- Liste des Epidemies")
            print("\t2- Ajouter un variant a une Epidemie")
            print("\t3- Afficher la Liste des variants d'une Epidemie")
            print("\t4- Ajouter une Epidémie")
            print("\t0- quitter")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            choix2 = input("Faites votre choix: ")
        if choix2 == "1":
            re = Epidemiologie.alls().keys()
            for res in re :
                if res not in ("Personne","Patient"):
                    print("\t",res)
            system("pause")
        elif choix2 == "2":
            system("cls")
            print("++++++++++++++++++++++++++ Ajouter un variant(Liste Des EPIDEMIES) ++++++++++++++++++++++++")
            print("\t1- COVID")
            print("\t2- EBOLA")
            print("\t3- TUBERCULOSE")
            print("\t4- SIDA")
            print("\t5- CHOLERA")
            print("\t6- FIEVRE JAUNE")
            print("\t7- ROUGEOLE")
            print("\t8- Autre...")
            print("\t0- quitter")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            choix21 = input("Faites votre choix: ")
            while choix21 not in ("0","1","2","3","4","5","6","7","8"):
                system("cls")
                print("++++++++++++++++++++++++++ Ajouter un variant(Liste Des EPIDEMIES) ++++++++++++++++++++++++")
                print("\t1- COVID")
                print("\t2- EBOLA")
                print("\t3- TUBERCULOSE")
                print("\t4- SIDA")
                print("\t5- CHOLERA")
                print("\t6- FIEVRE JAUNE")
                print("\t7- ROUGEOLE")
                print("\t8- Autre...")
                print("\t0- quitter")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                choix21 = input("Faites votre choix: ")

            if choix21 == "1":
                cov = {}
                cov["nom"] = input("Entrer le nom: ")
                cov["ro"] = float(input("Entrer le ro: "))
                cov["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                cov["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                cov["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                cov["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                cov["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                C = Covid(cov["nom"],cov["ro"],cov["taux_de_letalite"],cov["agent_pathogenes"],cov["mesures_de_lutte"],cov["sympthomes"],cov["moyen_de_propagation"])
                Covid.save(C)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "2":
                ebo = {}
                ebo["nom"] = input("Entrer le nom: ")
                ebo["ro"] = float(input("Entrer le ro: "))
                ebo["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                ebo["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                ebo["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                ebo["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                ebo["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                E = Ebola(ebo["nom"],ebo["ro"],ebo["taux_de_letalite"],ebo["agent_pathogenes"],ebo["mesures_de_lutte"],ebo["sympthomes"],ebo["moyen_de_propagation"])
                Ebola.save(E)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "3":
                tubo = {}
                tubo["nom"] = input("Entrer le nom: ")
                tubo["ro"] = float(input("Entrer le ro: "))
                tubo["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                tubo["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                tubo["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                tubo["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                tubo["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                T = Tuberculose(tubo["nom"],tubo["ro"],tubo["taux_de_letalite"],tubo["agent_pathogenes"],tubo["mesures_de_lutte"],tubo["sympthomes"],tubo["moyen_de_propagation"])
                Tuberculose.save(T)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "4":
                sid = {}
                sid["nom"] = input("Entrer le nom: ")
                sid["ro"] = float(input("Entrer le ro: "))
                sid["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                sid["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                sid["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                sid["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                sid["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                S = SIDA(sid["nom"],sid["ro"],sid["taux_de_letalite"],sid["agent_pathogenes"],sid["mesures_de_lutte"],sid["sympthomes"],sid["moyen_de_propagation"])
                SIDA.save(S)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "5":
                chol = {}
                chol["nom"] = input("Entrer le nom: ")
                chol["ro"] = float(input("Entrer le ro: "))
                chol["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                chol["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                chol["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                chol["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                chol["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                Col = CHOLERA(chol["nom"],chol["ro"],chol["taux_de_letalite"],chol["agent_pathogenes"],chol["mesures_de_lutte"],chol["sympthomes"],chol["moyen_de_propagation"])
                CHOLERA.save(Col)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "6":
                fv = {}
                fv["nom"] = input("Entrer le nom: ")
                fv["ro"] = float(input("Entrer le ro: "))
                fv["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                fv["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                fv["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                fv["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                fv["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                F = FIEVRE_JAUNE(fv["nom"],fv["ro"],fv["taux_de_letalite"],fv["agent_pathogenes"],fv["mesures_de_lutte"],fv["sympthomes"],fv["moyen_de_propagation"])
                FIEVRE_JAUNE.save(F)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "7":
                roug = {}
                roug["nom"] = input("Entrer le nom: ")
                roug["ro"] = float(input("Entrer le ro: "))
                roug["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                roug["agent_pathogenes"] = input("Entrer l'agent pathogene: ")
                roug["mesures_de_lutte"] = input("Entrer les moyen de prévention séparé par ',' : ").split(",")
                roug["sympthomes"] = input("Entrer les sympthomes séparé par ',' : ").split(",")
                roug["moyen_de_propagation"] = input("Entrer les moyens de propagations séparé par ',' : ").split(",")
                R = ROUGEOLE(roug["nom"],roug["ro"],roug["taux_de_letalite"],roug["agent_pathogenes"],roug["mesures_de_lutte"],roug["sympthomes"],roug["moyen_de_propagation"])
                ROUGEOLE.save(R)
                print("\t Enregistrement effectué ")
                system("pause")
            elif choix21 == "8":
                type = input("Entrer le nom de l'Epidemie: ")
                ep = {}
                ep["nom"] = input("Entrez le nom du variant: ")
                ep["ro"] = float(input("Entrer le ro: "))
                ep["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
                ep["agent_pathogenes"] = input("Entrer l'agent_pathogenes: ")
                ep["moyen de prevention"] = input("Entrer les moyens de prevention séparé de ',': ").split(",")
                ep["sympthômes"] = input("Entrer les sympthomes séparé de ',': ").split(",")
                ep["date"] = str(datetime.now())

                Epidemiologie.enregistrer2(ep,type)
                print("\t Enregistrement effectué ")
                system("pause")                                
            elif choix21 == "0":
                break

        elif choix2 == "3":
            system("cls")
            print("++++++++++++++++++++++++++ Liste des variants Epidemie(Liste Des EPIDEMIES) ++++++++++++++++++++++++")
            print("\t1- COVID")
            print("\t2- EBOLA")
            print("\t3- TUBERCULOSE")
            print("\t4- SIDA")
            print("\t5- CHOLERA")
            print("\t6- FIEVRE JAUNE")
            print("\t7- ROUGEOLE")
            print("\t8- Autre ...")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            choix22 = input("Faites votre choix: ")
            while choix22 not in ("0","1","2","3","4","5","6","7","8"):
                system("cls")
                print("++++++++++++++++++++++++++ Liste des variants Epidemie(Liste Des EPIDEMIES) ++++++++++++++++++++++++")
                print("\t1- COVID")
                print("\t2- EBOLA")
                print("\t3- TUBERCULOSE")
                print("\t4- SIDA")
                print("\t5- CHOLERA")
                print("\t6- FIEVRE JAUNE")
                print("\t7- ROUGEOLE")
                print("\t8- Autre ...")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                choix22 = input("Faites votre choix: ")
            if choix22 == "1":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ COVID ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                covs = Covid.all()
                for cov in covs :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",cov.get("date")," Nom : ",cov.get("nom")," agent_pathogenes : ",cov.get("agent_pathogenes")," moyen_de_propagation : ",cov.get("moyen_de_propagation"))
                print("\t ")
                system("pause")                
            elif choix22 == "2":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ EBOLA ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                ebos = Ebola.all()
                for ebo in ebos :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",ebo.get("date")," Nom : ",ebo.get("nom")," agent_pathogenes : ",ebo.get("agent_pathogenes")," moyen_de_propagation : ",ebo.get("moyen_de_propagation"))
                print("\t")
                system("pause")
            elif choix22 == "3":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TUBERCULOSE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                tubs = Tuberculose.all()
                for tub in tubs :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",tub.get("date")," Nom : ",tub.get("nom")," agent_pathogenes : ",tub.get("agent_pathogenes")," moyen_de_propagation : ",tub.get("moyen_de_propagation"))
                print("\t")
                system("pause")
            elif choix22 == "4":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ SIDA ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                sids = SIDA.all()
                for sid in sids :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",sid.get("date")," Nom : ",sid.get("nom")," agent_pathogenes : ",sid.get("agent_pathogenes")," moyen_de_propagation : ",sid.get("moyen_de_propagation"))
                print("\t ")
                system("pause")
            elif choix22 == "5":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ CHOLERA ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                chols = CHOLERA.all()
                for chol in chols :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",chol.get("date")," Nom : ",chol.get("nom")," agent_pathogenes : ",chol.get("agent_pathogenes")," moyen_de_propagation : ",chol.get("moyen_de_propagation"))
                print("\t ")
                system("pause")
            elif choix22 == "6":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ FIEVRE JAUNE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                fvs = FIEVRE_JAUNE.all()
                for fv in fvs :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",fv.get("date")," Nom : ",fv.get("nom")," agent_pathogenes : ",fv.get("agent_pathogenes")," moyen_de_propagation : ",fv.get("moyen_de_propagation"))
                print("\t")
                system("pause")
            elif choix22 == "7":
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ROUGEOLE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                rougs = ROUGEOLE.all()
                for roug in rougs :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",roug.get("date")," Nom : ",roug.get("nom")," agent_pathogenes : ",roug.get("agent_pathogenes")," moyen_de_propagation : ",roug.get("moyen_de_propagation"))
                print("\t")
                system("pause")
            elif choix22 == "8":
                type = input("Entrer le nom de l'Epidemie : ")
                system("cls")
                print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ",type," ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                eps = Epidemiologie.all(type)
                for ep in eps :
                    print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\t Date : ",ep.get("date")," Nom : ",ep.get("nom")," agent_pathogenes : ",ep.get("agent_pathogenes")," moyen_de_propagation : ",ep.get("moyen_de_propagation"))
                print("\t ")
                system("pause")
            elif choix22 == "0":
                break
        elif choix2 == "4":
            epi = {}
            epi["nom"] = input("Entrez le nom de la maladie: ")
            epi["ro"] = float(input("Entrer le ro: "))
            epi["taux_de_letalite"] = float(input("Entrer le taux de létalité: "))
            epi["agent_pathogenes"] = input("Entrer l'agent_pathogenes: ")
            epi["moyen de prevention"] = input("Entrer les moyens de prevention séparé de ',': ").split(",")
            epi["sympthômes"] = input("Entrer les sympthomes séparé de ',': ").split(",")
            epi["date"] = str(datetime.now())

            Epidemiologie.data[epi["nom"]] = epi
            Epidemiologie.add(epi,epi["nom"])

        elif choix2 == "0":
            break

    elif choix == "2":
        system("cls")
        print("++++++++++++++++++++++++++ PATIENT ++++++++++++++++++++++++")
        print("\t1- Liste des Patient")
        print("\t2- Ajouter un Patient")
        print("\t3- Ajouter plusieurs Patient grace a un fichier exel")
        print("\t0- quitter")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        choix3 = input("Faites votre choix: ")
        while choix3 not in ("0","1","2","3"):
            system("cls")
            print("++++++++++++++++++++++++++ PATIENT ++++++++++++++++++++++++")
            print("\t1- Liste des Patient")
            print("\t2- Ajouter un Patient")
            print("\t3- Ajouter plusieurs Patient grace a un fichier exel")
            print("\t0- quitter")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            choix3 = input("Faites votre choix: ")
            system("cls")
        if choix3 == "1":
            system("cls")
            pats = Patient.all()
            print("\t ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Liste(PATIENTS) ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            for pat in pats :
                print("\t ---------------------------------------------------------------------------------------------------------------------------------------------")
                print("\t Matricule : ",pat.get("id")," Nom : ",pat.get("nom")," Prenom : ",pat.get("prenom")," Age : ",pat.get("age")," Adresse : ",pat.get("adresse")," Date : ",pat.get("date"))
            print("\t")
            system("pause")
        elif choix3 == "2":    
            personne = {}
            try:
                personne["nom"] = input("Entrer le nom: ")
                personne["prenom"] = input("Entrer le prenom: ")
                personne["age"] = int(input("Entrer son age: "))
                personne["adresse"] = input("Entrer son adresse: ")
                personne["type_cas"] = input("Entrez le cas: ")
            except:
                print("Entrer incorrect !!!")
                continue
            P = Patient(personne["nom"],personne["prenom"],personne["age"],personne["adresse"],personne["type_cas"])
            try:
                P.sympthome = input(" saisisez les sympthomes séparé de ',' : ").split(",")
                P.diagnostic = input(" saisisez les diagnostic séparé de ',' : ").split(",")
                P.traitement = input(" saisisez les traitement séparé de ',' : ").split(",")
                Patient.save(P)
                print("Patient Enregistré !!!")
                system("pause")

            except:
                print("error !!!")
                continue
        elif choix3 == "3":
            system("cls")
            rep = input("Entrez le chemin vers le fichier exel : ")
            Epidemiologie.charger(rep)
            print("Les Patients on été enregistré avec success !!!")
            system("pause")
        elif choix3 == "0":
            break
    elif choix == "0":
        break
system("cls")
print("Bye ...")
