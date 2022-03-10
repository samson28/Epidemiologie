import json
from datetime import datetime
import pandas as pd

class Epidemiologie():

    data = {}
    data['Patient'] = []
    data['Covid'] = [
        {
            'nom': 'COVID-19',
            'ro': 3,
            'taux_de_letalite': [0.5,1],
            'agent_pathogenes' : 'SARS-Cov-2',
            'mesures_de_lutte': [
                "se laver régulièrement les mains ou utiliser une solution hydro-alcoolique",
                "tousser ou éternuer dans son coude ou dans un mouchoir",
                "se moucher dans un mouchoir à usage unique puis le jeter",
                "éviter de se toucher le visage",
                "respecter une distance d'au moins deux mètres avec les autres",
                "saluer sans serrer la main et arrêter les embrassades",
                "porter un masque chirurgical ou en tissu de catégorie 1 quand la distance de deux mètres ne peut pas être respectée",
                "limiter au maximum ses contacts sociaux (6 personnes maximum)",
                "aérer les pièces le plus souvent possible, au minimum quelques minutes toutes les heures",
                "utiliser les outils numériques (application Tous anti-Covid)"
            ],
            'sympthômes': {
                "net" : [
                    "La fièvre",
                    "La toux sèche",
                    "Essoufflements",
                    "Perte de l'odorat, perte du goût",
                    "La fatigue",
                    "Courbatures et douleurs musculaires",
                    "Diarrhées, nausées",
                    "Maux de gorge",
                    "Maux de tête",
                    "Conjonctivite, yeux irrités",
                    "Eruptions cutanées",
                    "Douleurs thoraciques"
                ]
            },
            'moyen_de_propagation': [
                "aérien"
            ],
            'date':'2020-01-09'
        },

        ]  
    data['Ebola'] = [
       
        {
            'nom': 'EBOLA',
            'ro': 2,
            'taux_de_letalite': 53.56,
            'agent_pathogenes' : 'Ebola',
            'mesures_de_lutte': [
                "Se laver les mains régulièrement à l’eau et au savon",
                "Eviter d'être en contact avec des personnes malades, qui doivent être mis en quarantaine",
                "Il ne faut pas toucher, embrasser ou même laver une personne malade",
                "Les soignants doivent porter blouses, gants, masques et lunettes. Et ne pas réutiliser les seringues",
                "Une attention particulière doit être portée lors des rites funéraires puisque les personnes décédées sont encore porteuses du virus et peuvent être contagieux",
                "Apprendre à ne pas porter sa main à sa bouche ou à ses yeux, portes d’entrées du virus",
                "Porter des gants et vêtements de protection pour manipuler les animaux malades et leur chair",
                "Rester vigilants chez les malades guéris qui peuvent encore transmettre le virus pendant 7 semaines. Ils doivent éviter les relations sexuelles pendant ce temps ou utiliser un préservatif."
            ],
            'sympthome': {
                'net' : [
                    "L’apparition brutale d'une fièvre intense, accompagnée de frissons",
                    "Une diarrhée",
                    "Des vomissements",
                    "Une fatigue extrêmement intense",
                    "Une perte d’appétit importante (anorexie)"
                ],
                'facultatifs' : [
                    "maux de tête",
                    "douleurs musculaires",
                    "douleurs articulaires",
                    "faiblesses",
                    "irritation de la gorge",
                    "douleurs abdominales"
                ],
                'grave' : [
                    "toux",
                    "éruption cutanée",
                    "douleurs thoraciques",
                    "yeux rouges",
                    "insuffisance rénale et hépatique",
                    "hémorragies internes et externes"
                ]
            },
            'moyen_de_propagation': [
                "contact de fluide corporel"
            ],
            'date':'1976-09-01'
            
        }
        ] 
    data['SIDA'] = [
        {
            'nom': 'SIDA',
            'r0': 0.19,
            'taux_de_letalite': [0.5,1],
            'agent_pathogenes' : 'VIH',
            'mesures_de_lutte': [
                "les préservatifs masculins et féminins",
                "l’administration de médicaments antirétroviraux en guise de prophylaxie préexposition (PPrE)",
                "la circoncision masculine médicale volontaire",
                "les interventions en faveur des changements de comportement pour la limitation du nombre de partenaires sexuels",
                " l’emploi d’aiguilles et de seringues propres",
            
            ],
            'sympthômes': {
                "net" : [
                    "une fièvre de plus de 38 °C ",
                    "l'apparition de ganglions lymphatiques",
                    "une pharyngite",
                    "une éruption de plaques rouges sur le corps et le visage",
                    "des maux de tête, de ventre, des douleurs musculaires",
                    "Courbatures et douleurs musculaires",
                    "une diarrhée, des vomissements",
                    "une perte de poids",
                    "des ulcérations de la bouche ou des organes génitaux ",
                   
                ]
            },
            'moyen_de_propagation': [
                "pénétration (anale ou vaginale) lors d’un rapport sexuel",
                "transfusion sanguine",
                "partage d’aiguilles contaminées",
                "de la mère à l’enfant au cours de la grossesse, de l’accouchement et de l’allaitement",
            ],
            'date':'1983-01-01'
        },

        ]
    data['CHOLERA'] = [
       
        {
            'nom': 'CHOLERA',
            'ro': 2,
            'taux_de_letalite': 53.56,
            'agent_pathogenes' : 'bacille Vibrio cholerae. ',
            'mesures_de_lutte': [
                "Se laver les mains régulièrement à l’eau et au savon",
                "Eviter le contact avec des personnes malades, qui doivent être mis en quarantaine",
                "le traitement des eaux usées",
                "la construction de latrines dans les zones de regroupement humains isolées des points d'eau potable",
                "l'hygiène alimentaire",
                
            ],
            'sympthome': {
                'net' : [
                    "une diarrhée aqueuse abondante, mais sans douleur (selles riziformes)",
                    "des vomissements de liquide clair",
                    "des nausées.",
                ],
                
            },
            'moyen_de_propagation': [
                "en ingérant de l'eau contaminée",
                "en ingérant des aliments contaminés",
                "en ingérant de manière non intentionnelle les selles d'une personne infectée."
            ],
            'date':'1883-12-31'
            
        }
        ]
    data['Tuberculose'] = [
        {
            'nom': 'TUBERCULOSE',
            'ro': 3,
            'taux_de_letalite': [5,7],
            'agent_pathogenes' : 'Mycobacterium tuberculosis',
            'mesures_de_lutte': [
                "La vaccination par le BBCG",
                "Isolement des patients contagieux"
            ],
            'sympthômes': {
                "net" : [
                    "La Toux",
                    "des douleurs thoraciques",
                    "Un etat de faiblesse",
                    "Une perte de poids",
                    "La fievre",
                    "des sueurs nocturnes",
                ]
            },
            'moyen_de_propagation': [
                "aérien"
            ],
        'date':'1679-12-31'
        }
    ] 
    data['FIEVRE JAUNE'] = [
        {
            'nom': 'FIEVRE JAUNE',
            'r0': 3,
            'taux_de_letalite': [2,6],
            'agent_pathogenes' : 'arbovirus',
            'mesures_de_lutte': [
                " la prévention par vaccination",
                " le repos, la réhydratation et l’administration de médicaments visant à limiter la fièvre, les vomissements et la douleur",
            
            ],
            'sympthômes': {
                "net" : [
                    "fièvre, frissons, douleurs musculaires et maux de tête",
                    "une grippe, une dengue ou un paludisme",
                    " l’apparition d’un syndrome hémorragique avec vomissement de sang noirâtre",
                    "un ictère qui donne son nom à la maladie et de troubles rénaux",
                   
                ]
            },
            'moyen_de_propagation': [
                "piqûre de moustiques appartenant aux genres Aedes et Haemagogus",
            ],
        'date':'1927-12-31'
        },

        ] 
    data['ROUGEOLE'] = [
       
        {
            'nom': 'ROUGEOLE',
            'ro': 18,
            'taux_de_letalite': [10],
            'agent_pathogenes' : 'virus de la famille de Paramyxoviridae. ',
            'mesures_de_lutte': [
                " le vaccin rougeole-oreillons-rubéole (ROR) ",
            ],
            'sympthome': {
                'net' : [
                    "fièvre, toux",
                    "écoulement nasal",
                    "yeux rouges",
                    "somnolence",

                ],
                
            },
            'moyen_de_propagation': [
                "se transmet très facilement par la toux",
                "se transmet par les éternuements et les sécrétions nasales"
                ],
        'date':'1912-12-31'
            
        }
        ]
    
    
    ## cette classmethode crée et ecrit la structure d'enregistrement de donnée dans le 
    ## fichier json nommé "donnees.json"
    @classmethod
    def create_json_file(cls):
        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)

    ## cette classmethode retourne tous les ocurence stoké dans le json d'une epidémie ou des patients donné en parametre
    @classmethod
    def all(cls,type):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
        return cls.data[type]

    ## cette classmethode retourne toutes les informations du fichier json
    @classmethod
    def alls(cls):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
        return cls.data

    ## cette classmethode enregistre les epidémies et les patients a l'endroit approprié grace au type et a l'objet 
    @classmethod
    def enregistrer(cls,e,type):

        with open('donnees.json') as fp:
            cls.data = json.load(fp)
            if(type == "Patient"):
                if(len(cls.data[type]) != 0):
                    di = cls.data[type][-1].get("id")
                    r = e.__dict__
                    r["id"] = di+1
                else :
                    r = e.__dict__
                    r["id"] = 1
                
                cls.data[type].append(r)
            else:
                cls.data[type].append(e.__dict__)

        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)
    ## cette classmethode enregistre les epidémies  a l'endroit approprié grace au type  et a un dictionnaire
    @classmethod
    def enregistrer2(cls,e,type):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
            cls.data[type].append(e)

        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)
            
    ## cette classmethode enregistre une nouvelle epidemie elle prend en parametre un dictionnaire et le nom de l'epidémie        
    @classmethod
    def add(cls,e,type):
        with open('donnees.json') as fp:
            cls.data = json.load(fp)
            cls.data[type] = [e]
     
        with open('donnees.json', 'w') as fp:
            json.dump(cls.data, fp, indent=4,ensure_ascii=False)
    
    # ajouter plusieurs patient a partir d'un fichier exel
    @classmethod
    def charger(cls,paf: str):
        data = pd.read_excel(r''+paf) 
        patients = pd.DataFrame(data, columns= ['Nom','Prenom','Age','Adresse','Type_Cas','Sympthome','Diagnostic','Traitement'])
        for i in patients.index:
            P = Patient(patients["Nom"][i],patients["Prenom"][i],int(patients["Age"][i]),patients["Adresse"][i],patients["Type_Cas"][i])
            P.sympthome = patients["Sympthome"][i].split(",")
            P.diagnostic = patients["Diagnostic"][i].split(",")
            P.traitement = patients["Traitement"][i].split(",")
            Patient.save(P)            
    
class Personne():
    def __init__(self,nom,prenom,age,adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    @classmethod
    def all(cls):
        return Epidemiologie.all("Personne")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Personne") 

    def delete(self):
        del self

class Patient(Personne):
    
    def __init__(self,nom, prenom, age, adresse,type_cas="", sympthome = [], diagnostic = [], traitement = []):
        super().__init__(nom, prenom, age, adresse)
        # constructeur d'un patient
        self.type_cas = type_cas
        self.sympthome = sympthome
        self.diagnostic = diagnostic
        self.traitement = traitement
        self.date = str(datetime.now())

    
    # retourne tous les patients
    @classmethod
    def all(cls):
        return Epidemiologie.all("Patient")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Patient") 

    def delete(self):
        del self  

class Covid():


    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
      #constucteur des variantes du covid
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))
    

    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("Covid")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Covid") 

    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes
   
    def delete(self):
        del self

class CHOLERA():


    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        #variantes du cholera
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))
        

    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("CHOLERA")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls,e):
        Epidemiologie.enregistrer(e,"CHOLERA")

    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes 
    

    def delete(self):
        del self

class Ebola():


    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
       #constructeur des variantes de l'ebola
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))

    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("Ebola")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls,e):
        Epidemiologie.enregistrer(e,"Ebola")
    
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes 

    def delete(self):
        del self

class FIEVRE_JAUNE():


    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
       #constructeur des variantes de la fievre_jaune
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))
        

    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("FIEVRE JAUNE")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"FIEVRE JAUNE") 
    
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes 

    def delete(self):
        del self

class ROUGEOLE():

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))

    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("ROUGEOLE")

    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls,e):
        Epidemiologie.enregistrer(e,"ROUGEOLE")
                
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes 

    def delete(self):
        del self

class SIDA():

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))
        
    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("SIDA")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"SIDA") 
    
    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes 

    def delete(self):
        del self

class Tuberculose():

    def __init__(self,nom,ro,taux_de_letalite = '',agent_pathogenes = '' ,mesures_de_lutte = [],sympthome = {},moyen_de_propagation = []):
        #les variantes de la tuerculose
        self.nom = nom
        self.ro = ro
        self.taux_de_letalite = taux_de_letalite
        self.agent_pathogenes = agent_pathogenes
        self.mesures_de_lutte = mesures_de_lutte
        self.sympthome = sympthome
        self.moyen_de_propagation = moyen_de_propagation
        self.date = str(datetime.today().strftime('%Y-%m-%d'))
   
    
    # retourne toute les épidémie de covid
    @classmethod
    def all(cls):
        return Epidemiologie.all("Tuberculose")
    
    # enregistre les epidémie de covid dans le json
    @classmethod
    def save(cls, e):
        Epidemiologie.enregistrer(e,"Tuberculose") 

    def __str__(self):
        return "nom :" + self.nom + " ro : " + self.ro + " taux_de_letalite : " + self.taux_de_letalite + " agent_pathogenes : " + self.agent_pathogenes 

    def delete(self):
        del self




    

    
