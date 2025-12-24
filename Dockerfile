# 1. Python 3.9 Slim versiyonunu kullan (Hafif)
FROM python:3.9-slim

# 2. Konteyner içinde çalışma klasörü oluştur
WORKDIR /app

# 3. Önce gereksinim dosyasını kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kalan tüm proje dosyalarını kopyala
COPY . .

# 5. 5000 portunu dış dünyaya aç
EXPOSE 5000

# 6. Uygulamayı başlat
CMD ["python", "app.py"]
