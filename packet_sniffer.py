from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Vérifier si le paquet contient une couche IP
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        # Déterminer le nom du protocole
        protocol_name = ""
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"
        else:
            protocol_name = str(proto)

        print(f"\n[+] Nouveau Paquet: {ip_src} -> {ip_dst} | Protocole: {protocol_name}")

        # Afficher une partie des données utiles (Payload)
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[IP].payload)
            if payload:
                # On affiche les 50 premiers caractères pour rester lisible
                print(f" Données: {payload[:50]}")

def main():
    print("Démarrage de l'analyseur de paquets...")
    print("Appuyez sur Ctrl+C pour arrêter.")
    # Sniff : capture les paquets. store=0 permet de ne pas surcharger la RAM.
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
