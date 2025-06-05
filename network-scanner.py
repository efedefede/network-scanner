import nmap

def scan_network(ip_range):
    scanner = nmap.PortScanner()
    scanner.scan(
        hosts=ip_range, 
        arguments='-T4 -p 1-65535 -sV --open')  # Todos los puertos + solo abiertos +
    
    print(f"\n🔍 Escaneo completado en {ip_range} (Puertos abiertos):")
    for host in scanner.all_hosts(): #Este for recorre todos los host en caso de que el parámetro sean varias IPs o un CIDR
        print(f"\nHost: {host} ({scanner[host].hostname()})")
        print(f"Estado: {scanner[host].state()}")
        
        for proto in scanner[host].all_protocols(): #Para cada host mostramos los puertos abiertos y el detalle
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                print(f"  Puerto {port}: {service}")

# Ejemplo de uso
print('Inicio de pruebas: -----------------------------------------')
scan_network("192.168.1.8")  # Enviamos la/s IP a escanear o un CIDR del formato