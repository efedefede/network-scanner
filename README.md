
# 🛡️ NMAP Python Network Scanner

Escáner de redes con Nmap y Python para Arquitectura y Sistemas Operativos.

🏫 Universidad: UTN (Universidad Tecnológica Nacional).

🎓 Tecnicatura en Programación a Distancia.

📖 Materia: Arquitectura y Sistemas Operativos.


## 👥 Authors

- [Federico Panella](https://www.github.com/efedefede)
- [Marcelo Oviedo](https://www.github.com/OviedoMarcelo)


## 🚀 Instalación y ejecución

📥 Requisitos previos
- Python 3.8+ [Descargar aquí](https://www.python.org/downloads/).

- Nmap (¡Esencial!):

Windows: Descargar desde nmap.org y marcar "Add Nmap to PATH".

Linux:
```bash
sudo apt update && sudo apt install nmap -y
macOS:
```

```bash
brew install nmap
```

To deploy this project run

```bash
  npm run deploy
```
🔧 Instalar dependencias

Clona el repositorio y ejecuta:  
```bash
  pip install python-nmap
```

▶️ Ejecutar el script

```bash
  python network_scanner.py
```

(Por defecto escanea 192.168.1.0/24. Modifica el código para cambiar el rango de IPs).

🛠️ Argumentos personalizados

Edita la línea:

```bash
  scanner.scan(hosts=ip_range, arguments='-T4 -p 20-1000 -sV --open')

```

-T4: Velocidad rápida (usa -T3 si es demasiado agresivo).

-p 20-1000: Rango de puertos a escanear.

-sV: Detección de versiones de servicios.
## 📚 Documentación Adicional

[Documentación oficial de Nmap](hhttps://nmap.org/book/)

[Tutorial de python-nmap](https://pypi.org/project/python-nmap/)


## 🛡️ Consideraciones éticas

⚠️ Este script debe usarse solo en redes propias o con autorización explícita.

El escaneo no autorizado de redes ajenas puede violar leyes de privacidad y seguridad.

Proyecto con fines educativos, bajo el marco de la UTN.


## 📢 ¡Gracias por visitar nuestro proyecto! 🎉

¡Siéntete libre de abrir un issue o hacer un fork del proyecto! ✨

🔗 Repositorio: https://github.com/efedefede/network-scanner
