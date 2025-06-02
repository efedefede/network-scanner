import nmap

def scan_network(ip_range):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=ip_range, arguments='-F -sV')  # Escaneo rápido + detección de servicios
    
    print(f"Resultados del escaneo en {ip_range}:")
    for host in scanner.all_hosts():
        print(f"\nHost: {host} ({scanner[host].hostname()})")
        print(f"Estado: {scanner[host].state()}")
        
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                print(f"  Puerto {port}: {service}")

# Ejemplo de uso
print('Inicio de pruebas: -----------------------------------------')
scan_network("192.168.1.0/24")  # Escanear toda una subred