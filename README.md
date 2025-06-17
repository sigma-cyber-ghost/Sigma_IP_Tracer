# Sigma_IP_Tracer
🕵️ Sigma_IP_Tracer
Advanced IP Sigma_IP_Tracer tool with proxy support and threat analysis
(Sigma Cyber Ghost Edition)

📦 Installation
Requirements
Python 3.8+

pip
Install Dependencies

pip install requests colorama pysocks
ip3 install requests ip2geotools folium ipwhois colorama
pip3 install requests ip2geotools folium ipwhois colorama
pip install requests colorama

Download the Tool

git clone https://github.com/sigma-cyber-ghost/Sigma_IP_Tracer.git
cd /Sigma_IP_Tracer


🚀 Usage
Basic Commands
Command	Description

Trace your own IP
python3 sigma_tracer.py myip	

Trace Google's DNS/IP/Domain
python3 sigma_tracer.py google.com

Trace Google's DNS/IP/Domain with proxy
python3 sigma_tracer.py 8.8.8.8	-p socks5://192.140.151.71:9090 

Trace a target-ip with proxy
python3 sigma_tracer.py -p socks5://192.140.151.71:9090 192.168.12.12

Supported proxy types: socks5, socks4, http, https

Full Options

python3 sigma_tracer.py [TARGET] [-p PROXY_URL]

TARGET: IP/Domain or myip

-p/--proxy: Proxy server URL

🔍 Features
🌍 Geolocation
6+ verification sources (ipapi.co, ip-api.com, etc.)

Accuracy radius (1-50km typical)

ISP/ASN detection

🛡️ Security Analysis
VPN/Proxy detection

Threat level scoring (0-10)

Multi-service verification

⚡ Technical
SOCKS5/HTTP proxy support

Parallel API requests

Automatic fallback systems

🖥️ Sample Output "
VERIFIED LOCATION: Mountain View, California, US  
COORDINATES: 37.405600, -122.077500  
ACCURACY: ±1.2 km  
ISP: Google LLC  

SECURITY ASSESSMENT:  
THREAT LEVEL: 0/10  
proxycheck.io: False  
ipinfo.io: False  

❓ Troubleshooting
Common Issues
Problem	Solution
API errors	Try different proxy or wait 1-2 minutes
No coordinates	Use -p "" to force direct connection
Slow responses	Reduce concurrent requests in code

)
📜 Legal Notice
⚠️ Use responsibly! This tool is for:

Black Hat Hacking

Security Research

Network forensics

🚫 Do Use For: Harassment

Illegal tracking

Privacy violations

🛠️ Development
To-Do
Add API key support for premium services

Implement JSON output option

Build GUI version

Credits
Developed by Sigma Cyber Ghost

Special Thanks To All!

This README includes:
✅ Installation instructions
✅ Usage examples
✅ Feature breakdown
✅ Troubleshooting guide
✅ Legal disclaimer
✅ Social media links
