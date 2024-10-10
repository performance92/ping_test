import os
import subprocess
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# E-posta ayarları
sender_email = "your_email@example.com"  # Gönderen e-posta adresi
receiver_email = "receiver_email@example.com"  # Alıcı e-posta adresi
password = "your_email_password"  # E-posta şifresi

# Ping atmak istediğiniz sunucular
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
    results = []
    results.append(f"\n--- {datetime.now()} ---\n")
    for server in servers:
        successful, failed = ping_server(server)
        if successful > 0:
            result_line = f"{server} - Başarılı ping: {successful}, Başarısız ping: {failed}\n"
        else:
            result_line = f"{server} - Başarısız ping: {failed}\n"
        results.append(result_line)
    
    # Sonuçları dosyaya yazma
    with open(log_file, "a") as f:
        f.writelines(results)
        
    return "".join(results)  # Sonuçları döndür

def send_email(results):
    # E-posta mesajı oluşturma
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Ping Sonuçları"
    
    msg.attach(MIMEText(results, 'plain'))
    
    # E-posta gönderme
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # TLS ile bağlantıyı başlat
            server.login(sender_email, password)  # Kullanıcı girişi
            server.send_message(msg)  # E-postayı gönder
            print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderiminde hata: {e}")

if __name__ == "__main__":
    ping_results = log_results()  # Sonuçları kaydet ve döndür
    send_email(ping_results)  # Sonuçları e-posta ile gönder