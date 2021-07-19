# Système de mémoire pour jeux de 52 cartes

Basé sur le système P.A.O (Personne Action Objet sauf que j'ai fusionné A & O) et l'encodage suivant :  
0 = Z, S ou CE … sert ici pour le 10   
1 = T ou D … sert ici pour l'AS  
2 = N …   
3 = M …   
4 = R …   
5 = L …   
6 = CH ou J …   
7 = K, QU ou C …   
8 = F ou V …   
9 = P ou B
Valet = 11
Dame = 12
Roi = 13  
[voici d'autres alternatives sur le site de l'ASM](https://asmemoire.fr/systemes-de-memorisation/)

## Pour les personnages:
- les trèfles représentent les personnages de dessins animés, mangas & BD
- les carreaux les personnages de films
- les piques les chanteurs, artistes
- et les coeurs la famille et les amis

on se base sur la 1ère lettre pour la conversion, par exemple :
- le 3 de coeur : 3 comme m => __M__ am (maman)
- l'AS de carreau : E.__T__ (les consonnes ne sont pas comptées)
- le 7 de trèfle : __K__ irikou

## Pour les actions / objet 

- les mots des trèfles commencent par __T__
- les carreaux par __CA__
- les piques par __P__
- et les coeurs par __CO__

et ensuite on utilise la consonne suivante pour la hauteur; par exemple:
- AS de coeur : couteau, côte
- 7 de carreau : cacao
- Dame de trèfle : tétine

## Système

x       | Trèfle        | Carreau           | Pique  | Coeur
--------|-------------|-------------|-------------|-------------|
As | <font color='red'>Dalton</font> - <font color='blue'>tutu, tatoo</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
2 | <font color='red'>Naruto</font> - <font color='blue'>tennis, tonneau, tune</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
3 | <font color='red'>Marsupilami</font> - <font color='blue'>tam-tam, tomate, tami</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
4 | <font color='red'>Roger Rabit</font> - <font color='blue'>tir, terre, tour</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
5 | <font color='red'>Lucky Luke</font> - <font color='blue'>tuile, toile, taule</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
6 | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
7 | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
8 | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
9 | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
10 | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
V | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
D | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
R | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> | <font color='red'>x</font> - <font color='blue'>x</font> |
