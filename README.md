# taskmanagement
Application de gestion de tâches

# Configuration et Organisation

### 1. Création du repository Github

Nous avons créé un repo, sur celui-ci, nous avons notre branche principale : "main", qui est la branche de prod. Nous lui avons ajouté des protections (github rules) :  
    
    - Require pull request before merging
    - Require reviews
    - Require status checks (tests CI)

Cela permet de rajouter des protections pour éviter de push n'importe quoi, comment et par n'importe qui sur la prod.

### 2. Configuration du workflow 

Pour le choix du workflow git, on va tout simplement utiliser GitFlow, avec ses branches : Main, Hotfix, Release, Develop et les branches Feature pour chaque ajout.

On ajoute donc plusieurs règles à notre workflow, tout d'abord on va utiliser Conventional Commit pour nommer tous nos commits, ça permet de rendre l’historique des commits lisible et structuré.

Ensuite on va toujours passer par des PR (Pull Request), de nos branches features à develop, puis de develop à release, et enfin de release à main.

J'ai donc ajouté les mêmes rules aux branches Release et Develop

### 3. Organisation des équipes

Pour l'attribution des roles on va utiliser un fichier CONTRIBUTING.md

Nous avons également créé des issues pour toutes les tâches du projet, ainsi qu'un tableau Kanban, pour suivre notre avancement.