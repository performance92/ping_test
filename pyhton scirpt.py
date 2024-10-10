import os
import subprocess
import time
from datetime import datetime

# Ping atmak istenilen sunucular
servers = [
    "192.168.1.1", "192.168.1.2", "192.168.1.3",  # Devam edin...
    "example1.com", "example2.com", "8.8.8.8"
]

# Sonuçları kaydetmek için dosya yolu
log_file = "/path/to/ping_results.txt"

def ping_server(server, duration=60):
    start_time = time.time()
    successful_pings = 0
    failed_pings = 0

    while time.time() - start_time < duration:
        # 1 kez ping atma
        result = subprocess.run(["ping", "-c", "1", server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            successful_pings += 1
        else:
            failed_pings += 1
        
        time.sleep(1)  # Her ping atımı arasında 1 saniye bekle

    return successful_pings, failed_pings

def log_results():
    with open(log_file, "a") as f:
        f.write(f"\n--- {datetime.now()} ---\n")
        for server in servers:
            successful, failed = ping_server(server)
            # Sonuçların kayıt edilmesi
            if successful > 0:
                f.write(f"{server} - Başarılı ping: {successful}, Başarısız ping: {failed}\n")
            else:
                f.write(f"{server} - Başarısız ping: {failed}\n")

if __name__ == "__main__":
    log_results()