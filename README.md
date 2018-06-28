[![Build Status](https://travis-ci.com/RemMeds/api_remmeds.svg?branch=master)](https://travis-ci.com/RemMeds/api_remmeds)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=api_remmeds&metric=alert_status)](https://sonarcloud.io/dashboard?id=api_remmeds)

# Projet Remmeds

## Mise en contexte

Remmeds est une solution médicale permettant aux personnes sous traitement de pouvoir gérer leurs prises médicamenteuses via un pilulier connecté couplé à une application Android.

### API Remmeds

Ce repository est dédié au back-end de notre solution:

* Appels à notre base de données afin de récupérer les informations nécessaires au fonctionnement de l'application android

### Application Android

Le [repository suivant](https://github.com/RemMeds/script_raspberry) est dédié au développement de l'application Android permettant:

* La configuration personnalisable de chacun des compartiments du pilulier.
* Le suivi des prises journalières via des notifications.
* L'accès à un répertoire médical.
* L'accès à un historique des prises généré automatiquement.

### Script Python - Raspberry

Remmeds est également composé d'un script python permettant la gestion des ouvertures/fermetures des compartiments du pilulier et leur interprétation.
Voir [lien repository](https://github.com/RemMeds/script_raspberry).

### Auteurs

* Oussama CALLAS
* Mathieu FOUCHER
* Koceila HADDOUCHE
* Quentin NICOLAS
