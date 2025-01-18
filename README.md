# SAE_Soutenance_App_Stage  
**YANG Evann, RABILLON Thomas, AVIGNION THEO, CHHUM-MOXEL LOANN**

## Projet Arexis - Refonte et Gestion des Soutenances

### Contexte
La gestion des soutenances reposait initialement sur un tableau Excel, un outil limité qui rendait l’insertion d’informations complexe et sujette à des erreurs. De plus, l’accès restreint compliquait la collaboration entre étudiants, enseignants et maîtres de stages. Cette gestion manuelle étant inefficace, nous avons été chargés de refondre la plateforme Arexis pour simplifier et sécuriser le suivi des soutenances, tout en ajoutant de nouvelles fonctionnalités pour améliorer l’expérience utilisateur.

---

### Objectifs
Le projet se divise en plusieurs objectifs principaux :
- **Refonte de la plateforme Arexis** afin de la rendre plus ergonomique et moderne.
- **Développement de la fonctionnalité de gestion des soutenances**, permettant de simplifier l’organisation des soutenances pour les étudiants, professeurs et secrétaires.
- **Optimisation de la gestion des stages et alternances**, afin de faciliter le suivi des étudiants et d’améliorer l’expérience utilisateur.

---

### Structure du Projet
Le projet est structuré de manière modulaire pour favoriser l’organisation et la lisibilité du code. Voici la répartition de l’arborescence du projet :

- **`commun`** : Contient les éléments partagés entre les différentes applications, tels que les modèles communs et les vues qui ne sont pas spécifiques à une application (ex. : Home, Login, Logout).
- **`app_etudiant`** : Regroupe les fonctionnalités et les vues liées aux étudiants. Cela inclut la vue de leurs soutenances, ainsi que des informations spécifiques à leurs stages ou alternances.
- **`app_professeur`** : Gère les fonctionnalités et vues concernant les professeurs, y compris la consultation des soutenances et des étudiants dont ils suivent le stages ou l'alternance.
- **`app_entreprise`** : Regroupe les fonctionnalités liées aux entreprises et tuteurs professionnels. Les entreprises peuvent voir les soutenances et les informations relatives à leur stagiaire et alternant.
- **`app_secretaire`** : Contient les fonctionnalités destinées aux secrétaires, telles que la gestion des soutenances (ajout, modification, suppression) et l’importation des données via CSV/Excel.

---

### Choix Technologiques
Le projet a été réalisé avec **Django**, un framework Python qui nous a permis de répondre efficacement aux exigences du projet. Nos choix techniques sont justifiés par les raisons suivantes :

1. **Simplicité et Rapidité** : Django nous a permis de nous concentrer sur l'implémentation des fonctionnalités spécifiques sans avoir à construire des solutions de base. Cela nous a permis de gagner un temps précieux et de maintenir un développement rapide malgré le retard accumulé.
2. **ORM Puissant** : Le système d'ORM de Django facilite l’interaction avec la base de données, tout en garantissant la sécurité et la cohérence des données stockées. Cela a été essentiel pour la gestion efficace des soutenances et des informations des étudiants.
3. **Communauté Active et Documentation Complète** : La vaste communauté de Django, ainsi que sa documentation exhaustive, nous ont permis de surmonter rapidement des obstacles techniques et d'accélérer notre apprentissage du framework.
4. **Architecture Modulaire Adaptée aux Projets Compliqués** : Django offre une architecture modulaire qui nous a permis de séparer les différentes fonctionnalités en applications spécifiques, facilitant ainsi la maintenance et l’évolution du code à long terme.

---

### Fonctionnalités
Les principales fonctionnalités développées dans ce projet sont :

- **Gestion des soutenances** : Permet aux étudiants, professeurs et secrétaires de gérer et consulter les dates et informations relatives aux soutenances.
- **Importation de données via CSV/Excel** : Permet aux secrétaires d’intégrer des données externes, telles que des informations sur les étudiants et leurs stages, en utilisant des fichiers CSV ou Excel.
- **Interface moderne et ergonomique** : Une interface plus intuitive et facile à utiliser comparée à la version initiale de la plateforme, avec des améliorations apportées au design et à la navigation.

---

### Installation
Pour installer et faire fonctionner ce projet en local, suivez ces étapes :

1. Clonez le dépôt Git du projet :
    ```bash
    git clone https://github.com/votre-repository/SAE_Soutenance_App_Stage.git
    ```

2. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirement.txt
    ```

3. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

4. Accédez à l’application en ouvrant votre navigateur à l'adresse suivante :  
    ```bash
    http://127.0.0.1:8000/
    ```

---

### Remarques
- Ce projet est encore en phase de développement et certaines fonctionnalités peuvent être incomplètes ou nécessiter des ajustements supplémentaires.
