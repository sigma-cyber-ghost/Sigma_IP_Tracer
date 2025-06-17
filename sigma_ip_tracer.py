#!/usr/bin/env python3
"""
MILITARY-GRADE IP TRACER - Sigma Cyber Ghost Edition v6.0
Fully fixed with reliable API endpoints and enhanced error handling
"""
import argparse
import socket
import json
import requests
import time
import re
import concurrent.futures
import webbrowser
import socks
from colorama import Fore, Style, init

# Initialize color output
init(autoreset=True)

# Custom banner with colors
BANNER = f"""
{Fore.CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢤⣤⡀⠀⢤⣆⣄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⢀⣰⢸⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⡇⣀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.YELLOW}⠀⠀⠀⠀⠀⠀⠀⠆⠸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣯⣭⡅⠰⠀⠀⠀⠀⠀⠀⠀
{Fore.GREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠈⠈⠻⠇⠸⣿⠞⠁⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⠀⠀⢀⣼⡆⢰⣷⡀⠀⠀⡀⣄⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⣿⣮⡻⡿⢿⡏⠀⠀⠸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⣬⢝⢿⣿⣷⣓⢆⢰⣶⣿⣿⣿⡍⡋⠁⠀⠀⠀⠀⠀⠀⠀
{Fore.RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⣺⣝⡻⡇⢨⢛⣛⣛⡂⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.YELLOW}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠈⠛⠇⠁⠀⠀⡟⠁⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.GREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.BLUE}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Fore.MAGENTA}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Social Media Links
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/sigma-cyber-ghost",
    "Telegram": "https://t.me/Sigma_Cyber_Ghost",
    "YouTube": "https://www.youtube.com/@sigma_ghost_hacking"
}

# Ultra-reliable geolocation services with fallbacks
GEOLOCATION_SERVICES = [
    "https://ipapi.co/{ip}/json/",
    "http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,isp,org,as,lat,lon,query",
    "https://ipwhois.app/json/{ip}",
    "https://freeipapi.com/api/json/{ip}",
    "https://ipinfo.io/{ip}/json",
    "https://api.ipbase.com/v1/json/{ip}"
]

# Reliable VPN detection services
VPN_DETECTION_SERVICES = [
    "https://proxycheck.io/v2/{ip}?vpn=1",
    "https://ipinfo.io/{ip}/privacy",
    "https://ipapi.co/{ip}/vpn_proxy/"
]

class MilitaryGradeTracer:
    def __init__(self, proxy=None):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'application/json'
        })
        self.proxy = proxy
        if proxy:
            self.set_proxy(proxy)
    
    def set_proxy(self, proxy_url):
        """Configure SOCKS5/HTTP proxy properly for all connections"""
        try:
            # Set proxy for requests
            self.session.proxies = {
                'http': proxy_url,
                'https': proxy_url
            }
            
            # Configure SOCKS proxy for socket operations if needed
            if proxy_url.startswith('socks'):
                proxy_type = proxy_url.split('://')[0]
                proxy_addr = proxy_url.split('://')[1]
                proxy_host = proxy_addr.split(':')[0]
                proxy_port = int(proxy_addr.split(':')[1])
                
                if proxy_type == 'socks5':
                    socks.set_default_proxy(socks.SOCKS5, proxy_host, proxy_port)
                    socket.socket = socks.socksocket
                elif proxy_type == 'socks4':
                    socks.set_default_proxy(socks.SOCKS4, proxy_host, proxy_port)
                    socket.socket = socks.socksocket
                    
        except Exception as e:
            print(f"{Fore.RED}[!] Proxy configuration error: {str(e)}")
            exit(1)
    
    def get_public_ip(self):
        """Get real public IP with multiple fallbacks"""
        services = [
            "https://api64.ipify.org",
            "https://ident.me",
            "https://icanhazip.com",
            "https://checkip.amazonaws.com"
        ]
        
        for service in services:
            try:
                response = self.session.get(service, timeout=5)
                if response.status_code == 200:
                    return response.text.strip()
            except:
                continue
        return None
    
    def verify_location(self, ip):
        """Military-grade location verification with ultra-reliable services"""
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.fetch_geo, service, ip) for service in GEOLOCATION_SERVICES]
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    if result and result.get('latitude') != 0 and result.get('longitude') != 0:
                        results.append(result)
                except:
                    continue
        
        if not results:
            # Ultimate fallback - try direct connection if proxy fails
            try:
                print(f"{Fore.YELLOW}[*] Trying direct connection fallback...")
                temp_session = requests.Session()
                response = temp_session.get(f"http://ip-api.com/json/{ip}", timeout=5)
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'ip': ip,
                        'city': data.get('city', 'Unknown'),
                        'region': data.get('regionName', 'Unknown'),
                        'country': data.get('country', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'latitude': float(data.get('lat', 0)),
                        'longitude': float(data.get('lon', 0)),
                        'accuracy_km': 50,
                        'sources': ['ip-api.com (direct fallback)'],
                        'map_url': f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}"
                    }
            except Exception as e:
                print(f"{Fore.YELLOW}[*] Fallback also failed: {str(e)}")
                pass
            
            raise ValueError("All geolocation services failed (including fallback)")
        
        return self.calculate_consensus(results)
    
    def fetch_geo(self, service, ip):
        """Fetch geolocation from a single service with enhanced error handling"""
        try:
            url = service.format(ip=ip)
            response = self.session.get(url, timeout=5)
            
            if response.status_code != 200:
                print(f"{Fore.YELLOW}[*] Service {service.split('/')[2]} returned status {response.status_code}")
                return None
                
            data = response.json()
            
            # Standardize different API responses
            result = {
                'ip': ip,
                'city': 'Unknown',
                'region': 'Unknown',
                'country': 'Unknown',
                'isp': 'Unknown',
                'latitude': 0,
                'longitude': 0,
                'source': service.split('/')[2] if '/' in service else service
            }
            
            # Handle different API formats
            if 'ipapi.co' in service:
                result.update({
                    'city': data.get('city'),
                    'region': data.get('region'),
                    'country': data.get('country_name'),
                    'isp': data.get('org'),
                    'latitude': data.get('latitude'),
                    'longitude': data.get('longitude')
                })
            elif 'ip-api.com' in service:
                if data.get('status') == 'success':
                    result.update({
                        'city': data.get('city'),
                        'region': data.get('regionName'),
                        'country': data.get('country'),
                        'isp': data.get('isp'),
                        'latitude': data.get('lat'),
                        'longitude': data.get('lon')
                    })
            elif 'ipwhois.app' in service:
                result.update({
                    'city': data.get('city'),
                    'region': data.get('region'),
                    'country': data.get('country'),
                    'isp': data.get('isp'),
                    'latitude': data.get('latitude'),
                    'longitude': data.get('longitude')
                })
            elif 'freeipapi.com' in service:
                result.update({
                    'city': data.get('cityName'),
                    'region': data.get('regionName'),
                    'country': data.get('countryName'),
                    'isp': data.get('isp'),
                    'latitude': data.get('latitude'),
                    'longitude': data.get('longitude')
                })
            elif 'ipinfo.io' in service:
                result.update({
                    'city': data.get('city'),
                    'region': data.get('region'),
                    'country': data.get('country'),
                    'isp': data.get('org'),
                    'latitude': float(data.get('loc', '0,0').split(',')[0]) if data.get('loc') else 0,
                    'longitude': float(data.get('loc', '0,0').split(',')[1]) if data.get('loc') else 0
                })
            elif 'ipbase.com' in service:
                result.update({
                    'city': data.get('city'),
                    'region': data.get('region_name'),
                    'country': data.get('country_name'),
                    'isp': data.get('connection', {}).get('isp'),
                    'latitude': data.get('latitude'),
                    'longitude': data.get('longitude')
                })
            
            # Ensure coordinates are valid
            if abs(result['latitude']) > 90 or abs(result['longitude']) > 180:
                result['latitude'] = 0
                result['longitude'] = 0
                
            return result
        except Exception as e:
            print(f"{Fore.YELLOW}[*] Service {service.split('/')[2] if '/' in service else service} failed: {str(e)}")
            return None
    
    def calculate_consensus(self, results):
        """Calculate location consensus from multiple sources"""
        valid_results = [r for r in results if abs(r['latitude']) <= 90 
                      and abs(r['longitude']) <= 180
                      and r['latitude'] != 0
                      and r['longitude'] != 0]
        
        if not valid_results:
            raise ValueError("No valid coordinates received")
            
        # Calculate average coordinates
        avg_lat = sum(r['latitude'] for r in valid_results) / len(valid_results)
        avg_lon = sum(r['longitude'] for r in valid_results) / len(valid_results)
        
        # Find the most common country
        countries = [r['country'] for r in valid_results]
        country_consensus = max(set(countries), key=countries.count)
        
        # Find result closest to average coordinates
        closest = min(valid_results, key=lambda r: 
                    (r['latitude'] - avg_lat)**2 + (r['longitude'] - avg_lon)**2)
        
        return {
            'ip': closest['ip'],
            'city': closest['city'],
            'region': closest['region'],
            'country': country_consensus,
            'isp': closest['isp'],
            'latitude': avg_lat,
            'longitude': avg_lon,
            'accuracy_km': max(self.calculate_accuracy(valid_results, avg_lat, avg_lon), 1.0),
            'sources': [r['source'] for r in valid_results],
            'map_url': f"https://www.google.com/maps?q={avg_lat},{avg_lon}"
        }
    
    def calculate_accuracy(self, results, avg_lat, avg_lon):
        """Calculate location accuracy in kilometers"""
        max_distance = 0
        for r in results:
            # Simple distance approximation (1° ≈ 111km)
            distance = ((r['latitude'] - avg_lat)**2 + (r['longitude'] - avg_lon)**2)**0.5 * 111
            if distance > max_distance:
                max_distance = distance
        return round(max_distance, 2)
    
    def detect_proxy(self, ip):
        """Detect proxy/VPN with ultra-reliable services"""
        results = {}
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.check_proxy_service, service, ip) for service in VPN_DETECTION_SERVICES]
            for future in concurrent.futures.as_completed(futures):
                try:
                    service, status = future.result()
                    results[service] = status
                except:
                    continue
        
        # Calculate threat level
        true_count = sum(1 for status in results.values() if status is True)
        threat_level = min(10, true_count * 4)  # Scale 0-10
        
        return {
            'threat_level': threat_level,
            'services': results
        }
    
    def check_proxy_service(self, service, ip):
        """Check a single proxy detection service with enhanced reliability"""
        try:
            url = service.format(ip=ip)
            response = self.session.get(url, timeout=5)
            
            if response.status_code != 200:
                return (service.split('/')[2], "HTTP Error")
                
            data = response.json()
            
            # Different service response formats
            if "proxycheck.io" in service:
                return (service.split('/')[2], data.get('proxy') == "yes")
            elif "ipinfo.io" in service:
                return (service.split('/')[2], data.get('privacy', {}).get('proxy') or False)
            elif "ipapi.co" in service:
                return (service.split('/')[2], data.get('proxy') or data.get('vpn') or False)
                
            return (service.split('/')[2], False)
        except Exception as e:
            print(f"{Fore.YELLOW}[*] Proxy detection service {service.split('/')[2]} failed: {str(e)}")
            return (service.split('/')[2], "Error")

def print_banner():
    """Display the custom banner with colors"""
    print(BANNER)
    print(f"{Fore.YELLOW}{'═'*90}")
    print(f"{Fore.GREEN} MILITARY-GRADE IP TRACER | SIGMA CYBER GHOST EDITION")
    print(f"{Fore.YELLOW}{'═'*90}{Style.RESET_ALL}\n")

def open_social_media():
    """Open all social media links in browser"""
    print(f"\n{Fore.CYAN}{'═'*90}")
    print(f"{Fore.YELLOW} CONNECT WITH SIGMA CYBER GHOST:")
    for platform, url in SOCIAL_MEDIA.items():
        print(f"{Fore.GREEN}  {platform}: {Fore.BLUE}{url}")
        try:
            webbrowser.open(url, new=2)
        except:
            pass
    print(f"{Fore.CYAN}{'═'*90}{Style.RESET_ALL}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="MILITARY-GRADE IP TRACER - Sigma Cyber Ghost Edition")
    parser.add_argument("target", nargs="?", help="IP/Domain to investigate or 'myip' for your IP")
    parser.add_argument("-p", "--proxy", help="Proxy URL (socks5://, socks4://, http://, https://)")
    args = parser.parse_args()

    # Initialize military-grade tracer
    tracer = MilitaryGradeTracer(args.proxy)
    
    # Show proxy status
    if args.proxy:
        print(f"{Fore.YELLOW}[*] Using proxy: {args.proxy}")
    else:
        print(f"{Fore.YELLOW}[*] Using direct connection")

    # Determine target IP
    target_ip = None
    if args.target:
        if args.target.lower() == "myip":
            target_ip = tracer.get_public_ip()
            if not target_ip:
                print(f"{Fore.RED}[!] Failed to retrieve your IP address")
                exit(1)
            print(f"{Fore.GREEN}[*] Your real public IP: {Fore.CYAN}{target_ip}")
        else:
            # Validate input
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", args.target):
                target_ip = args.target
            else:
                try:
                    target_ip = socket.gethostbyname(args.target)
                    print(f"{Fore.GREEN}[*] Resolved domain: {args.target} → {target_ip}")
                except socket.gaierror:
                    print(f"{Fore.RED}[!] Invalid domain/IP: {args.target}")
                    exit(1)
    else:
        target_ip = tracer.get_public_ip()
        if target_ip:
            print(f"{Fore.YELLOW}[*] Using your public IP: {target_ip}")
        else:
            print(f"{Fore.RED}[!] Could not determine public IP")
            exit(1)

    # Perform military-grade tracing
    try:
        print(f"\n{Fore.YELLOW}{'═'*90}")
        print(f"{Fore.CYAN}[*] INITIATING MILITARY-GRADE ANALYSIS FOR: {target_ip}")
        print(f"{Fore.YELLOW}{'═'*90}{Style.RESET_ALL}")
        
        start_time = time.time()
        
        # Get verified location
        location = tracer.verify_location(target_ip)
        
        # Detect proxy/VPN
        proxy_info = tracer.detect_proxy(target_ip)
        
        elapsed = time.time() - start_time
        
        # Display results
        print(f"\n{Fore.GREEN}  VERIFIED LOCATION: {Fore.WHITE}{location['city']}, {location['region']}, {location['country']}")
        print(f"{Fore.GREEN}  COORDINATES: {Fore.WHITE}{location['latitude']:.6f}, {location['longitude']:.6f}")
        print(f"{Fore.GREEN}  ACCURACY: {Fore.WHITE}±{location['accuracy_km']} km")
        print(f"{Fore.GREEN}  ISP: {Fore.WHITE}{location['isp']}")
        print(f"{Fore.GREEN}  SOURCES: {Fore.WHITE}{', '.join(location['sources'])}")
        print(f"{Fore.GREEN}  MAP: {Fore.BLUE}{location['map_url']}")
        
        # Threat assessment
        threat_level = proxy_info['threat_level']
        threat_color = Fore.GREEN
        if threat_level > 4:
            threat_color = Fore.YELLOW
        if threat_level > 7:
            threat_color = Fore.RED
            
        print(f"\n{Fore.RED}  SECURITY ASSESSMENT:")
        print(f"  {Fore.GREEN}THREAT LEVEL: {threat_color}{threat_level}/10")
        
        for service, status in proxy_info['services'].items():
            status_color = Fore.RED if status is True else Fore.GREEN if status is False else Fore.YELLOW
            print(f"  {Fore.CYAN}{service}: {status_color}{status}")
        
        print(f"\n{Fore.YELLOW}  ANALYSIS COMPLETED IN {elapsed:.2f} SECONDS")
        
    except Exception as e:
        print(f"{Fore.RED}  [!] ANALYSIS FAILED: {str(e)}")
        print(f"{Fore.YELLOW}  [*] Possible solutions:")
        print(f"  - Try a different proxy server")
        print(f"  - Check your internet connection")
        print(f"  - Some services may be blocking proxy traffic")
        print(f"  - Try again later as some APIs have rate limits")
    
    # Open social media
    open_social_media()
    
    # Compliance notice
    print(f"\n{Fore.YELLOW}{'═'*90}")
    print(f"{Fore.RED}[!] LEGAL COMPLIANCE NOTICE:")
    print(f"{Fore.WHITE}• This tool provides network infrastructure locations, not personal addresses")
    print(f"• Accuracy depends on available data sources (±1-50km typical)")
    print(f"• Use only for authorized security investigations and ethical purposes")
    print(f"• Military-grade verification provides highest possible accuracy")
    print(f"• Unauthorized use may violate international laws and treaties")
    print(f"{Fore.YELLOW}{'═'*90}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
