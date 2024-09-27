import os
import subprocess
import requests


def send_discord_alert(message):
    webhook_url = "webhook-url"
    
    data = {
        "content": message,
        "username": "Firewall Manager Bot"
    }
    
    try:
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            print("Alerte envoyée sur Discord avec succès.")
        else:
            print(f"Erreur lors de l'envoi de l'alerte. Code de réponse : {response.status_code}")
    
    except Exception as e:
        print(f"Erreur lors de l'envoi de la requête Discord : {e}")


def add_iptables_rule(rule):
    try:
        subprocess.run(f"sudo iptables {rule}", shell=True, check=True)
        print(f"Règle ajoutée : {rule}")
        send_discord_alert(f"Règle iptables ajoutée : {rule}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'ajout de la règle iptables : {e}")
        send_discord_alert(f"Erreur lors de l'ajout de la règle : {rule}")


def remove_iptables_rule(rule):
    try:
        subprocess.run(f"sudo iptables {rule}", shell=True, check=True)
        print(f"Règle supprimée : {rule}")
        send_discord_alert(f"Règle iptables supprimée : {rule}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la suppression de la règle iptables : {e}")
        send_discord_alert(f"Erreur lors de la suppression de la règle : {rule}")

def block_ip(ip):
    rule = f"-A INPUT -s {ip} -j DROP"
    add_iptables_rule(rule)


def allow_ip(ip):
    rule = f"-A INPUT -s {ip} -j ACCEPT"
    add_iptables_rule(rule)


def block_malicious_ips_with_fail2ban():
    try:
        # Récupérer les adresses IP bloquées par Fail2ban
        result = subprocess.run("sudo fail2ban-client status sshd", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.splitlines()
            for line in lines:
                if "Banned IP list" in line:
                    banned_ips = line.split(':')[1].strip().split()
                    for ip in banned_ips:
                        block_ip(ip)
                    send_discord_alert(f"Adresses IP malveillantes bloquées avec Fail2ban : {', '.join(banned_ips)}")
        else:
            print("Erreur lors de l'obtention du statut Fail2ban.")
    except Exception as e:
        print(f"Erreur lors de l'intégration avec Fail2ban : {e}")
        send_discord_alert(f"Erreur lors de l'intégration avec Fail2ban : {e}")

def cli():
    while True:
        print("\nGestionnaire de Pare-feu")
        print("1. Ajouter une règle iptables")
        print("2. Supprimer une règle iptables")
        print("3. Bloquer une adresse IP")
        print("4. Autoriser une adresse IP")
        print("5. Bloquer les IP malveillantes (Fail2ban)")
        print("6. Quitter")
        choice = input("Choisissez une option : ")

        if choice == '1':
            rule = input("Entrez la règle iptables à ajouter (ex: -A INPUT -s 192.168.0.1 -j DROP) : ")
            add_iptables_rule(rule)
        elif choice == '2':
            rule = input("Entrez la règle iptables à supprimer (ex: -D INPUT -s 192.168.0.1 -j DROP) : ")
            remove_iptables_rule(rule)
        elif choice == '3':
            ip = input("Entrez l'adresse IP à bloquer : ")
            block_ip(ip)
        elif choice == '4':
            ip = input("Entrez l'adresse IP à autoriser : ")
            allow_ip(ip)
        elif choice == '5':
            block_malicious_ips_with_fail2ban()
        elif choice == '6':
            print("Fermeture du gestionnaire de pare-feu.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    cli()
