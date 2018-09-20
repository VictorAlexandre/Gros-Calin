library(stringr)
library(tidyverse)
#On charge toutes les listes telles qu'elles ont été pensées pour Python
titrescinema <- as.list(t(read.csv("titrescinema.txt", header=FALSE, stringsAsFactors=FALSE)))
titreslitt <- as.list(t(read.csv("titreslitterature.txt", header=FALSE, stringsAsFactors=FALSE)))
titreschan <- as.list(t(read.csv("titreschansons.txt", header=FALSE, stringsAsFactors=FALSE)))
titresexpr <- as.list(t(read.csv("listeexpressions.txt", header=FALSE, stringsAsFactors=FALSE)))
titresautre <- as.list(t(read.csv("autres.txt", header=FALSE, stringsAsFactors=FALSE)))


#Ensuite, on les regroupe dans une seule liste
listedetitres<-c(titrescinema,titreslitt,titresexpr,titreschan,titresautre)
listedetitres<-as.data.frame(unlist(listedetitres))
colnames(listedetitres)[1]<-"titre"
listedetitres<-listedetitres%>%
  filter(titre !="")
listedetitres$titre<-as.character(listedetitres$titre)

#On note ici le mot pour lequel on cherche un titre
mottape<-"fran"
mots_du_titre<-NULL
test<-0
resultatsoriginaux <-NULL
resultatsalgo <-NULL
resultatsoriginaux = list()
resultatsalgo = list()
longueurresultats<-0

for (i in 1:nrow(listedetitres)){
  mots_du_titre=str_split(listedetitres$titre[i]," ")
  #mots_du_titre contient alors une liste de liste
  for (j in 1:length(mots_du_titre)){
    mot_courant=mots_du_titre[[j]]
    test = ifelse(nchar(mot_courant)>=4 & nchar(mot_courant)<30,1,
                  ifelse(nchar(mot_courant)>=30,0,
                         ifelse(nchar(mot_courant)<4,0,0)))
    longueurresultats <-length(resultatsoriginaux)
    
    #On regarde si le mot se trouve tout ou partie dans un titre
    if (test==1){
      if(grepl(mottape,mots_du_titre)){
        resultatsoriginaux[[longueurresultats+1]]<-listedetitres$titre[i]
        #Sans doute vaut-il mieux faire un str_sub en partant du str_locate
        titretmp=""
        for (k in 1:length(mots_du_titre)){
          if (k!=j){
            titretmp=mots_du_titre[[k]]
          }else{
            titretmp=mottape
          }
        }
      }else{
    }
  }
  }
}
