# Gestionnaire de Pare-feu Automatisé

Un script Python pour automatiser la gestion et la configuration des règles iptables afin de renforcer la sécurité de votre réseau. Ce gestionnaire de pare-feu permet d'ajouter, de supprimer et de bloquer des adresses IP, tout en intégrant des fonctionnalités de protection via Fail2ban.

## Fonctionnalités

- **Ajout et suppression de règles iptables** : Gérez facilement les règles de pare-feu via une interface en ligne de commande.
- **Blocage et autorisation d'adresses IP** : Permettez ou refusez des connexions pour des adresses IP spécifiques.
- **Intégration avec Fail2ban** : Automatisez le blocage des adresses IP malveillantes détectées par Fail2ban.
- **Notifications via Discord** : Recevez des alertes pour chaque action effectuée dans le gestionnaire de pare-feu.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.x
- Les bibliothèques Python nécessaires (`requests`)
- `iptables` pour la gestion des règles de pare-feu
- `Fail2ban` si vous souhaitez utiliser cette fonctionnalité

## Installation

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/yourusername/firewall-manager.git
   cd firewall-manager
   ```

2. **Installez les dépendances** :

   Si `requests` n'est pas déjà installé, vous pouvez l'installer avec pip :

   ```bash
   pip install requests
   ```

3. **Exécutez le script** :

   Pour exécuter le gestionnaire de pare-feu, utilisez les droits sudo :

   ```bash
   sudo python3 firewall_manager.py
   ```

## Utilisation

Une fois le script lancé, vous verrez une interface en ligne de commande avec plusieurs options :

- Ajouter une règle iptables
- Supprimer une règle iptables
- Bloquer une adresse IP
- Autoriser une adresse IP
- Bloquer les IP malveillantes (Fail2ban)
- Quitter le programme

## Avertissement

L'utilisation de ce script nécessite des privilèges administratifs. Assurez-vous de comprendre les règles de pare-feu et leur impact sur la sécurité de votre réseau avant de les modifier.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/YourFeature`)
3. Commitez vos modifications (`git commit -m 'Ajout de votre fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/YourFeature`)
5. Ouvrez une Pull Request

## License

Ce projet est sous licence MIT. Pour plus de détails, veuillez consulter le fichier `LICENSE`.

## ⭐ Aimez ce projet ?

Si vous appréciez ce projet, n'hésitez pas à lui mettre une étoile en cliquant sur le bouton en haut à droite de la page du dépôt GitHub. Cela nous aidera à le faire connaître et à encourager davantage de développements !

Merci de votre intérêt et bonne utilisation !
