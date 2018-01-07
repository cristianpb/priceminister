Context
=======

Contexte du challenge

PriceMinister permet à ses utilisateurs de partager leur avis sur les produits 
qu’ils ont achetés. Avec plus d’un million d’avis, ce jeu de données a un 
énorme potentiel pour améliorer la qualité du site et permettre aux 
utilisateurs de trouver leur produit qui leur convient le mieux. Chaque 
utilisateur peut aussi évaluer un avis, en spécifiant si il est utile pour lui 
ou non. Ce retour est aussi très important pour la qualité des services.  Ce 
jeu de données est original car il contient des avis sur des contenus textuels 
et non pas sur les produits eux même. Prédire le retour des utilisateurs sur 
les avis eux même (retour qui est subjectif et personnel), est particulièrement 
ambitieux, et peut avoir des implications plus général que le e-commerce
Ce challenge est issu de la collaboration entre l'equipe Big Data Europe team 
de Rakuten (Search, Recommendations, Targeting, ...) 
(https://global.rakuten.com/corp/careers/bigdata/) et le Rakuten Institute of 
Technology (Computer Vision, Human Computer Interface, Machine Learning, Deep 
Learning, ...) (http://rit.rakuten.co.jp)


Objectifs du challenge

Le but est d’évaluer si un avis utilisateur sur un produit peut être utile pour d’autres utilisateurs. Certains avis sont ainsi particulièrement intéressants, e.g.:
 très grandes et belles cartes soyeuses, les illustrations sont extrêmement bien réalisées, le manuel d'explications est facile et très lisible, pour la voyance personnelle ou pour tirer les cartes en cérémonial la grandeur des cartes permet d'organiser un vrai tirage professionnel)
et d’autres moins car plus personnels, e.g."
 JEU TRES BIEN POUR MA FILLE DE 4 ANS.JE RECOMMANDE POUR LES JEUNES ENFANT;TRES SATISFAIT).
Chaque avis est labélisé comme useful (class 1) ou not useful (class 0), en se basant sur leur nombre de retours:
useful si (nombre de retours positifs / total du nombre de retours) > 0.5
not useful si (nombre de retours positifs / total du nombre de retours) < 0.5

Nous avons enlevé les avis pour lesquels le nombre de retour positifs et le nombre de retours négatifs étaient égaux. Nous utiliserons la mesure AUC (Area Under the Curve) pour l’évaluation, et vous devrez fournir la probabilité d’être utile (class 1) pour chaque avis du jeu de données de test.
Le format attendu est un CSV (séparateur ;) avec les champs ID et Probabilité, e.g:
ID;Target
39;1
40;1
...
156;0
 
Ne PAS oublier d’ajouter le header (ID;Target) car s’il n’est pas présent, la soumission ne sera pas évaluée.
