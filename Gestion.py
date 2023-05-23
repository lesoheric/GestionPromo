from tkinter import*

def validation(entr,plt,dessrt,boissn,plc) :#entr : entrées , plt : plat , dessrt  : desserts, boissn : boisson, plc  : place
                    #fonction Tkinter#debut fenetre 2
        #fonction ajouter( incrémentation de 1)
        def ajouter(iv):
            valeur=iv.get()+1
            iv.set(valeur)
        #fonction enlever (décrémentation de 1)
        def enlever(iv):
            if iv.get()==0:
                iv.set(0)
            else :
                valeur=iv.get()-1
                iv.set(valeur)
                
        #deuxième version(2)@fonctionnelle

        #fonction affichage de la contribution d'un étudiant
        def affichage_Etu(entree,plat,dessert,boisson,nume,ma_liste):
            
            #initialisation des différents varaibles pour leurs affichages dans notre application
            #entree
            affichageEntree= IntVar()
            affichageEntree.set(entree.get())
            
            #plat
            affichagePlat = IntVar()
            affichagePlat.set(plat.get())
            #dessert
            affichageDessert= IntVar()
            affichageDessert.set(dessert.get())
            #boisson
            affichageBoisson=IntVar()
            affichageBoisson.set(boisson.get())
            #numero etudiant
            affichageNum= IntVar()
            affichageNum.set(nume.get())

        
            # ma_liste.insert(END,str(aff_entree.get())+str(aff_plat.get())+str(aff_dessert.get()))
            ma_liste.insert(END,"Entrée(s) : "+str(affichageEntree.get())+" | "+" Plat(s) : "+str(affichagePlat.get())+" | "+" Dessert(s) : "+str(affichageDessert.get())+" | "+" boisson(s) : "+str(affichageBoisson.get())+"| N° Etud: "+str(affichageNum.get()))
            affichageEntree.trace_add("write", calculerM)
            #réinitialisation des variables de nos options à zéro   
            iv_entree.set(0)
            iv_plat.set(0)
            iv_dessert.set(0)
            iv_boisson.set(0)
            
            

        def Supprimer():
            indexe = liste_affichage.curselection()
            liste_affichage.delete(first=indexe)

        def calculerM(*args):
            #entrees
            entree_util = iv_entree.get()
            total_entrees = total_entree_intvar.get()
            conf_stock_entree.config(text=total_entrees-entree_util)
            #plats
            plat_util = iv_plat.get() 
            total_plats = total_plat_intvar.get()
            conf_stock_plat.config(text=total_plats-plat_util)
            #desserts
            dessert_util = iv_dessert.get()
            total_desserts = total_dessert_intvar.get()
            conf_stock_dessert.config(text=total_desserts-dessert_util)
            #boisson
            boisson_util = iv_boisson.get()
            total_boissons = total_boisson_intvar.get() 
            conf_stock_boisson.config(text=total_boissons-boisson_util)           
        def Montrer(*args):
            entree_etu = iv_entree.get()
            plat_etu = iv_plat.get()
            dessert_etu = iv_dessert.get()
            boisson_etu = iv_boisson.get()
            Entree_Stocks.config(text=entree_etu)
            Plat_Stocks.config(text=plat_etu)
            Dessert_Stocks.config(text=dessert_etu)
            Boisson_Stocks.config(text=boisson_etu)
            

        #fin(2)

        #création et initialisation des variables pour l'application 
        
        #vivre(1)
        stocks= Tk()
        #entree variable 
        iv_entree = IntVar()
        iv_entree.set(0)

        #Plat variable
        iv_plat = IntVar()
        iv_plat.set(0)

        #Dessert variable 
        iv_dessert =IntVar()
        iv_dessert.set(0)
        #Boisson variable 
        iv_boisson = IntVar()
        iv_boisson.set(0)
        #(1)
        #Numero de l'étudiant
        Num= IntVar()

        #identification personnelle

        #nom prenom Numero
        mon_Nom=StringVar()
        mon_Prenom=StringVar()
        fil_univ=StringVar()
        #mon_annee=StringVar()


        #Creation des différents options de l'application

        # création vivre pour le stock(1)
        #Entree@objet
        iv_entree.trace_add("write", Montrer)
        Entree=Label(stocks,text="Entrée(s)")
        Entree_Stocks=Label(stocks)

        ajout_entree=Button(stocks,text="Ajouter(+)",command=lambda:ajouter(iv_entree))
        enlever_entree=Button(stocks,text="Enlever(-)",command=lambda:enlever(iv_entree))


        #Plat@objet
        iv_plat.trace_add("write", Montrer)
        Plat=Label(stocks,text="Plat(s)")
        Plat_Stocks=Label(stocks)

        ajout_plat=Button(stocks,text="Ajouter(+)",command=lambda:ajouter(iv_plat))
        enlever_plat=Button(stocks,text="Enlever(-)",command=lambda:enlever(iv_plat))

        #Dessert@objet 
        iv_dessert.trace_add("write", Montrer)
        Dessert=Label(stocks,text="Dessert(s)")
        Dessert_Stocks=Label(stocks)

        ajout_dessert=Button(stocks,text="Ajouter(+)",command=lambda:ajouter(iv_dessert))
        enlever_dessert=Button(stocks,text="Enlever(-)",command=lambda:enlever(iv_dessert))

        #Boisson@object
        iv_boisson.trace_add("write",Montrer)
        Boisson=Label(stocks,text="Boisson(s)")
        Boisson_Stocks=Label(stocks)

        ajout_boisson=Button(stocks,text="Ajouter(+)",command=lambda:ajouter(iv_boisson))
        enlever_boisson=Button(stocks,text="Enlever(-)",command=lambda:enlever(iv_boisson))
        #fin vivre(1)
        #@Numero de l'etudiant @object

        numI_label= Label(stocks,text="Numero - Etudiant* : ",padx=20,pady=10)
        numI = Entry(stocks,textvariable="Num")


        #création des objets Frame dans notre Application (affichage des stocks et des informations personelles)

        Iden_stock = Frame(stocks,bd=2,bg="green")              #frame principale
        identification_etudiant= Frame(Iden_stock,bd=2)            #ce frame va contenir les informations des etudiants
        confirmation_stock = Frame(stocks,bd=2,bg="gray")
        #confirmation stock
        #informations relatives au produit manquant à la fete
        conf_suivi_label= Label(confirmation_stock,text="Suivi[Budget]Manquant:",font=("Verdana",10),width=45,height=2)
        #@Entrée
        iv_entree.trace_add("write",calculerM )
        total_entree_intvar = IntVar()
        total_entree = entr.get()*plc.get()
        total_entree_intvar.set(total_entree)
        conf_entree_suivi= Label(confirmation_stock,text="Entrée(s)")
        conf_stock_entree=Label(confirmation_stock)
        #Plats
        total_plat_intvar = IntVar()
        total_plat = plt.get()*plc.get()
        total_plat_intvar.set(total_plat)
        conf_plat_suivi= Label(confirmation_stock,text="Plat(s)")
        conf_stock_plat= Label(confirmation_stock)
        #desserts
        total_dessert_intvar = IntVar()
        total_dessert = dessrt.get()*plc.get()
        total_dessert_intvar.set(total_dessert)
        conf_dessert_suivi=Label(confirmation_stock,text="Dessert(s)")
        conf_stock_dessert= Label(confirmation_stock)
        #@boissons
        total_boisson_intvar = IntVar()
        total_boisson = boissn.get()*plc.get()
        total_boisson_intvar.set(total_boisson)
        conf_boisson_suivi=Label(confirmation_stock,text="Boisson(s)")
        conf_stock_boisson = Label(confirmation_stock)

        #affichage liste@options
        liste_affichage=Listbox(Iden_stock,width=65)

        #creation des informations personelles des etudiants(1) [Frame identification_etudiant]
        #titre du frame des informations personnelles
        titre_info=Label(identification_etudiant,text="Vos Informations Personelles",font=("verdana",8))
        #nom
        nom_label= Label(identification_etudiant,text="Nom-etudiant: ")
        nom = Entry(identification_etudiant,textvariable=mon_Nom)
        #prenom
        prenom_label= Label(identification_etudiant,text="Prenom-etudiant : ")
        prenom = Entry(identification_etudiant,textvariable=mon_Prenom)
        #Numero etudiant()
        filiere_label= Label(identification_etudiant,text="Filière-Univ : ")
        filiere = Entry(identification_etudiant,textvariable="fil_univ")
        #Année de promotion()-------------------
        #fin info(1)

        #bouton Terminer@objet
        Terminer = Button(stocks,text="Afficher",command=lambda:affichage_Etu(iv_entree,iv_plat,iv_dessert,iv_boisson,numI,liste_affichage) )
        Afficher = Button(stocks,text="Supprimer",command=lambda:Supprimer())
        Quitter_fin = Button(stocks,text="abandonner",command=lambda:stocks.quit(),width=15,height=2,bd=2)
        valider_liste = Button(stocks,text="valider",command=lambda:valid_list(),width=15,height=2)

        #positionnement des différentes options dans l'interface visuelle 
        #dans la fenetre principale(1)
        #Entree
        Entree.grid(row=0,column=1)
        Entree_Stocks.grid(row=1,column=1)
        ajout_entree.grid(row=2,column=2)
        enlever_entree.grid(row=2,column=0)

        #Plat 
        Plat.grid(row=3,column=1)
        Plat_Stocks.grid(row=4,column=1)
        ajout_plat.grid(row=5,column=2)
        enlever_plat.grid(row=5,column=0)

        #Dessert
        Dessert.grid(row=6,column=1)
        Dessert_Stocks.grid(row=7,column=1)
        ajout_dessert.grid(row=8,column=2)
        enlever_dessert.grid(row=8,column=0)

        #Boisson
        Boisson.grid(row=9,column=1)
        Boisson_Stocks.grid(row=10,column=1)
        ajout_boisson.grid(row=11,column=2)
        enlever_boisson.grid(row=11,column=0)
        #(1)
        #numero de l'etudiant qui apporte la contribution
        numI_label.grid(row=12,column=0)
        numI.grid(row=12,column=1)


        #bouton terminer
        Terminer.grid(row=13,column=1,pady=10)
        #bouton affichages des informations personnelles 
        Afficher.grid(row=13,column=4,pady=10)
        Quitter_fin.grid(row=14,column=0)
        valider_liste.grid(row=15,column=4,pady=10)




        #frame (identification et affichages des stocks)(2)
        Iden_stock.grid(row=0,column=4,rowspan=11,columnspan=9,padx=25)
        identification_etudiant.grid(row=0,column=0)
        confirmation_stock.grid(row=14,column=4,padx=40)
        #titre informations personelles
        titre_info.grid(row=0,column=0,columnspan=2)
        #nom
        nom_label.grid(row=1,column=0)
        nom.grid(row=1,column=1)

        #prenom
        prenom_label.grid(row=2,column=0)
        prenom.grid(row=2,column=1)

        #Numero Etudiant
        filiere_label.grid(row=3,column=0)
        filiere.grid(row=3,column=1)
        #Annee de promotion--------------------

        #liste@Stocks
        liste_affichage.grid(row=3,column=0)
        #disposition des informations dans le frame suivi des categories des produits qui manquent

        conf_suivi_label.grid(row=0,column=0,pady=5,columnspan=4)
        #categories des aliments presents dans la promo
        #entrées
        conf_entree_suivi.grid(row=1,column=0)
        conf_stock_entree.grid(row=2,column=0)
        #plats 
        conf_plat_suivi.grid(row=1,column=1)
        conf_stock_plat.grid(row=2,column=1)
        #dessert
        conf_dessert_suivi.grid(row=1,column=2)
        conf_stock_dessert.grid(row=2,column=2)
        #boissons
        conf_boisson_suivi.grid(row=1,column=3)
        conf_stock_boisson.grid(row=2,column=3)

        #fin(2)
        #modification directe sur la fenetre de l'application
        stocks.title("Enregistrement")
        stocks.wm_maxsize(width=810,height=510)
        stocks.wm_minsize(width=810,height=520)
#fin fenetre 2 
   

  
#fonction Tkinter
#fonction ajouter( incrémentation de 1)
def ajouter(iv):
    valeur=iv.get()+1
    iv.set(valeur)
#fonction enlever (décrémentation de 1)
def enlever(iv):
    if iv.get()==0:
        iv.set(0)
    else :
        valeur=iv.get()-1
        iv.set(valeur)

def calculer(*args):
    val_entree = iv_entreeORG.get()
    val_plat = iv_platORG.get()
    val_dessert = iv_dessertORG.get()
    val_boisson = iv_boissonORG.get()
    val_place = PlaceT.get()
    suivi_entrees_stock.config(text=val_entree*val_place)
    suivi_plats_stock.config(text=val_plat*val_place)
    suivi_dessert_stock.config(text=val_dessert*val_place)
    suivi_boisson_stock.config(text=val_boisson*val_place)




Accueil= Tk()
#Initialisateur de différents variables utiles pour notre application
#identification organisateur
nom_OR=StringVar()
prenom_OR=StringVar()
promo_univ=StringVar()
PlaceT = IntVar()
#Quotas etudiant 

#entree variable 
iv_entreeORG = IntVar()
iv_entreeORG.set(0)

#Plat variable
iv_platORG = IntVar()
iv_platORG.set(0)

#Dessert variable 
iv_dessertORG =IntVar()
iv_dessertORG.set(0)

#Boisson variable 
iv_boissonORG = IntVar()
iv_boissonORG.set(0)



#création de la fenetre Accueil et création des frames 
Iden_organisateur= Frame(Accueil,bd=2,bg="gray")
Quotas_etudiant = Frame(Accueil,bd=2,bg="Silver")
Suivi_budget=Frame(Accueil,bd=2,bg="white")

#création   du contenu pour les frames 
iden_titre=Label(Iden_organisateur,text="Identification de l'organisateur",width=50,font=("verdana",8),height=3)
Quota_titre= Label(Quotas_etudiant,text="Quotas-Etudiants-vivres",font=("verdana",10),height=3,width=40)

#informations relatives à la suivie du budget nécessaires à la promo
suivi_label= Label(Suivi_budget,text="Suivi[Budget]",font=("Verdana",10),width=45,height=2)
#@Entrées
iv_entreeORG.trace_add("write",calculer)
PlaceT.trace_add("write",calculer)#globale pour toutes les categories
entree_suivi= Label(Suivi_budget,text="Entrée(s)")
suivi_entrees_stock=Label(Suivi_budget)
#Plats
iv_platORG.trace_add("write",calculer)
plat_suivi= Label(Suivi_budget,text="Plat(s)")
suivi_plats_stock = Label(Suivi_budget)
#desserts
iv_dessertORG.trace_add("write",calculer)
dessert_suivi=Label(Suivi_budget,text="Dessert(s)")
suivi_dessert_stock= Label(Suivi_budget)
#@boissons
iv_boissonORG.trace_add("write",calculer)
boisson_suivi=Label(Suivi_budget,text="Boisson(s)")
suivi_boisson_stock = Label(Suivi_budget)

#@iden_organisateur
#nom
nomOR_label= Label(Iden_organisateur,text="Nom-ORG : ",width=40,height=2)
nomOR = Entry(Iden_organisateur,textvariable=nom_OR,width=30)
#prenom
prenomOR_label= Label(Iden_organisateur,text="Prenom-ORG : ",width=40,height=2)
prenomOR = Entry(Iden_organisateur,textvariable=prenom_OR,width=30)
#Promo
promo_label= Label(Iden_organisateur,text="Promo-AN: ",width=40,height=2)
promo = Entry(Iden_organisateur,textvariable=promo_univ,width=30)
#place disponible
place_label=Label(Iden_organisateur,text="Places pour la fête",width=15,height=2)
place_total=Entry(Iden_organisateur,textvariable=PlaceT,width=10)

#@informations sur le Quotas des étudiants 
categories=Label(Quotas_etudiant,text="Catégories")

#Entree@objet
EntreeORG=Label(Quotas_etudiant,text="Entrée(s)")
EntreeORG_Quotas_etudiant=Label(Quotas_etudiant,textvariable=str(iv_entreeORG))

ajout_entreeORG=Button(Quotas_etudiant,text="Ajouter(+)",command=lambda:ajouter(iv_entreeORG))
enlever_entreeORG=Button(Quotas_etudiant,text="Enlever(-)",command=lambda:enlever(iv_entreeORG))


#Plat@objet
PlatORG=Label(Quotas_etudiant,text="Plat(s)")
PlatORG_Quotas_etudiant=Label(Quotas_etudiant,textvariable=str(iv_platORG))

ajout_platORG=Button(Quotas_etudiant,text="Ajouter(+)",command=lambda:ajouter(iv_platORG))
enlever_platORG=Button(Quotas_etudiant,text="Enlever(-)",command=lambda:enlever(iv_platORG))

#Dessert@objet 
DessertORG=Label(Quotas_etudiant,text="Dessert(s)")
DessertORG_Quotas_etudiant=Label(Quotas_etudiant,textvariable=str(iv_dessertORG))

ajout_dessertORG=Button(Quotas_etudiant,text="Ajouter(+)",command=lambda:ajouter(iv_dessertORG))
enlever_dessertORG=Button(Quotas_etudiant,text="Enlever(-)",command=lambda:enlever(iv_dessertORG))

#Boisson@object
BoissonORG=Label(Quotas_etudiant,text="Boisson(s)")
BoissonORG_Quotas_etudiant=Label(Quotas_etudiant,textvariable=str(iv_boissonORG))

ajout_boissonORG=Button(Quotas_etudiant,text="Ajouter(+)",command=lambda:ajouter(iv_boissonORG))
enlever_boissonORG=Button(Quotas_etudiant,text="Enlever(-)",command=lambda:enlever(iv_boissonORG))

#création des principales boutons de notre application
Quitter = Button(Accueil,text="Quitter",command=lambda:Accueil.quit(),width=15,height=2,bd=2)
Valider = Button(Accueil,text="Valider",command=lambda : validation(iv_entreeORG,iv_platORG,iv_dessertORG,iv_boissonORG,PlaceT),width=15,height=2,bd=2)




#possitionement des différents composant de notre accueil
#@frame
Iden_organisateur.grid(row=0,column=0,padx=15)
Quotas_etudiant.grid(row=0,column=1,padx=25)
Suivi_budget.grid(row=1,column=1,padx=25)
#@titre des différents frame 
iden_titre.grid(row=0,column=0,padx=20)
Quota_titre.grid(row=0,column=0,padx=20,columnspan=2)
#@informations sur l'Iden_organisateur
#nom
nomOR_label.grid(row=1,column=0,pady=5)
nomOR.grid(row=2,column=0)
#prenom
prenomOR_label.grid(row=3,column=0,pady=5)
prenomOR.grid(row=4,column=0)
#promo
promo_label.grid(row=5,column=0,pady=5)
promo.grid(row=6,column=0)
#place
place_label.grid(row=7,column=0,pady=5)
place_total.grid(row=8,column=0,pady=5)
#@Quotas des étudiants
categories.grid(row=1,column=0,pady=5,columnspan=2)
#Entree
EntreeORG.grid(row=2,column=0,pady=5,columnspan=2)
EntreeORG_Quotas_etudiant.grid(row=3,column=0,pady=5,columnspan=2)
ajout_entreeORG.grid(row=4,column=0,pady=5)
enlever_entreeORG.grid(row=4,column=1,pady=5)

#Plat 
PlatORG.grid(row=6,column=0,pady=5,columnspan=2)
PlatORG_Quotas_etudiant.grid(row=7,column=0,pady=5,columnspan=2)
ajout_platORG.grid(row=8,column=0,pady=5)
enlever_platORG.grid(row=8,column=1,pady=5)

#Dessert
DessertORG.grid(row=10,column=0,pady=5,columnspan=2)
DessertORG_Quotas_etudiant.grid(row=11,column=0,pady=5,columnspan=2)
ajout_dessertORG.grid(row=13,column=0,pady=5)
enlever_dessertORG.grid(row=13,column=1,pady=5)

#Boisson
BoissonORG.grid(row=14,column=0,pady=5,columnspan=2)
BoissonORG_Quotas_etudiant.grid(row=15,column=0,pady=5,columnspan=2)
ajout_boissonORG.grid(row=16,column=0,pady=5)
enlever_boissonORG.grid(row=16,column=1,pady=5)
#positionnement des principales boutons de notre application
Valider.grid(row=2,column=1,pady=5)
Quitter.grid(row=2,column=0,pady=5)





#positionnement des informations relatives au budget*
suivi_label.grid(row=0,column=0,columnspan=4)
#@entrées
entree_suivi.grid(row=1,column=0)
suivi_entrees_stock.grid(row=2,column=0)
#@plats 
plat_suivi.grid(row=1,column=1)
suivi_plats_stock.grid(row=2,column=1)
#@desserts
dessert_suivi.grid(row=1,column=2)
suivi_dessert_stock.grid(row=2,column=2)
#@boissons
boisson_suivi.grid(row=1,column=3)
suivi_boisson_stock.grid(row=2,column=3)






#modification directe sur la fenetre principale
Accueil.title("Accueil\Organisation")
Accueil.wm_maxsize(width=850,height=620)
Accueil.wm_minsize(width=850,height=620)



Accueil.mainloop()