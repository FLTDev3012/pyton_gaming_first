# 🕹️ Jeu 2D avec Python et Pygame

Ce projet est un jeu 2D immersif développé en Python avec **Pygame**, où le joueur doit affronter des monstres tout en esquivant des comètes. Avec des animations fluides, des mécanismes de score, et des effets sonores engageants, ce jeu est conçu pour mettre en valeur des compétences avancées en développement de jeux vidéo.

---

## ✨ Fonctionnalités

### 🎮 Gameplay
- **Déplacement fluide** : Déplacez le joueur à gauche et à droite avec les flèches directionnelles.
- **Gestion des collisions** : Entre le joueur, les projectiles, et les monstres.
- **Système de score** : Ajout dynamique des points avec affichage en temps réel.
- **Apparition des monstres** : Ennemis générés aléatoirement (ex. Mummy, Alien).
- **Événements spéciaux** : Intégration de chutes de comètes pour ajouter du défi.
- **Réinitialisation** : Redémarrage du jeu après un Game Over.

### 🎨 Graphismes et animations
- **Barres de vie animées** : Pour le joueur et les monstres.
- **Animations fluides** : Pour les sprites du joueur, des ennemis, et des projectiles.
- **Éléments visuels dynamiques** : Barres de progression des événements spéciaux.

### 🔊 Audio
- **Effets sonores** : Sons spécifiques pour les actions importantes (game over, tirs, etc.).
- **Gestion centralisée** : Classe dédiée pour la lecture et la gestion des sons.

---

## 🛠️ Compétences et concepts mis en œuvre

### 🧑‍💻 Programmation
- **Programmation Orientée Objet (POO)** :
  - Création de classes robustes (`Game`, `Player`, `Monster`, `CometFallEvent`).
  - Utilisation d'attributs et de méthodes pour organiser le comportement des objets.
- **Gestion modulaire** :
  - Structure de projet claire avec des modules Python séparés (`player.py`, `monster.py`, etc.).
- **Gestion dynamique** :
  - Utilisation des dictionnaires (`self.pressed`) pour capturer l'état des touches.
  - Création d'objets dynamiquement via des appels de classe (`monster_class_name.__call__()`).

### 🎮 Développement avec Pygame
- **Groupes de sprites** :
  - Gestion efficace des objets grâce à `pygame.sprite.Group`.
  - Détection des collisions avec `pygame.sprite.spritecollide`.
- **Événements utilisateur** :
  - Suivi des entrées clavier et exécution des actions en conséquence.
- **Interface utilisateur** :
  - Affichage en temps réel du score avec des polices personnalisées.

---

## 📁 Structure du projet

```plaintext
.
├── game.py              # Classe principale du jeu
├── player.py            # Classe Player (joueur)
├── monster.py           # Classes Mummy et Alien (monstres)
├── comet_event.py       # Gestion des événements spéciaux
├── sounds.py            # Gestionnaire de sons
├── assets/              # Fichiers multimédias (images, sons, polices)
└── main.py              # Point d'entrée du jeu
