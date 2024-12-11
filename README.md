# SAE_Soutenance_App_Stage
# YANG Evann, RABILLON Thomas, AVIGNION THEO, CHHUM-MOXEL LOANN

# Projet Araxis - Refonte et Gestion des Soutenances

## Contexte
Dans le cadre de notre projet, il nous a initialement été demandé de recréer Araxis, une plateforme permettant aux stagiaires de s'inscrire et de consulter leurs dates de soutenance. Cependant, en l'absence d'un client concret (IUT) et de consignes précises, nous avons perdu un temps considérable à trouver un référent susceptible de clarifier les exigences et de fournir un support, afin de ne pas démarrer complètement de zéro.

Après avoir accumulé un certain retard par rapport aux autres groupes, nous avons finalement obtenu des consignes claires suite à une entrevue avec M. Chabin. Il nous a alors été demandé de concentrer nos efforts sur le développement de la fonctionnalité de gestion des soutenances dans Araxis, en plus de la refonte initialement demandée.

Nous demandons donc que ce retard initial soit pris en compte dans l'évaluation de notre projet.

---

## Objectifs
- Refonte de la plateforme Araxis.
- Développement et intégration de la fonctionnalité de gestion des soutenances.
- Création d'une structure claire et bien organisée pour le projet.

---

## Structure du Projet
Pour une meilleure organisation et une arborescence fluide, nous avons structuré notre projet en plusieurs modules distincts :

- **`API`** : Fournit les fonctionnalités backend pour gérer les données et les interactions avec la base de données.
- **`gestion_soutenance`** : Contient les fonctionnalités spécifiques à la gestion des soutenances, en s'appuyant sur l'API.
- **`soutenance_iuto`** : Correspond à l'interface utilisateur pour les soutenances.
- **`commun`** : Regroupe les éléments partagés entre les différents modules (par exemple : configurations, modèles communs, utilitaires).

---

## Choix Technologiques
Nous avons choisi d'utiliser **Django**, un framework web en Python, pour les raisons suivantes :

1. **Simplicité et Rapidité** : Django offre une structure robuste qui nous permet de nous concentrer sur le développement des fonctionnalités sans réinventer la roue.
2. **ORM Puissant** : Le système d'ORM intégré facilite l'interaction avec la base de données tout en garantissant une sécurité accrue.
3. **Communauté Active** : La vaste communauté et la documentation complète de Django nous ont permis de surmonter rapidement les obstacles techniques.
4. **Adapté aux Projets Modulaires** : Django permet de séparer facilement les différentes parties de l'application grâce à son architecture modulaire.

---

## Détails des Modules

### Commun
Ce dossier contient les éléments réutilisables dans les autres parties du projet, notamment :
- **Modèles Partagés** : Entités communes telles que les utilisateurs ou les permissions.
- **Utilitaires** : Fonctions d'aide et outils génériques.
- **Configurations** : Paramètres globaux comme la connexion à la base de données ou les configurations des environnements (développement/production).

### API
Le module API assure les fonctionnalités backend du projet. Il inclut :
- **Endpoints RESTful** : Pour gérer les inscriptions, les dates de soutenance et autres données.
- **Authentification** : Gestion des utilisateurs et des permissions via des jetons sécurisés.
- **Documentation API** : Générée automatiquement pour faciliter l'intégration avec d'autres outils ou services.

### Gestion des Soutenances
Ce module est au cœur du projet. Il permet :
- **Création et Modification des Soutenances** : Ajout, mise à jour ou suppression des soutenances.
- **Assignation des Jury** : Gestion des membres du jury pour chaque soutenance.
- **Planification** : Attribution des créneaux horaires pour chaque stagiaire.
- **Statistiques** : Visualisation des données relatives aux soutenances (nombre de soutenances prévues, répartition par jury, etc.).

### Soutenance IUTO

---

## Déroulement du Projet
Malgré un démarrage retardé, nous avons appliqué une méthodologie rigoureuse pour organiser notre travail :
1. **Analyse Préliminaire** : Identification des besoins avec M. Chabin.
2. **Organisation** : Structuration du projet en modules clairs.
3. **Développement** : Mise en œuvre des fonctionnalités par itérations.
4. **Tests** : Vérification de la qualité et des performances de chaque module.

---

## Conclusion

