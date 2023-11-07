# Scrapping
Code Scrapping Data From WEB
<br>Cara menjalankannya

<br>1. Buat Environment baru
```bash
python3 -m venv Scrapping
```
<br>atau 
```bash
python -m venv Scrapping
```
<br>
2. Aktifkan Environment
```bash
source Scrapping/bin/activate
```
<br>
3. Install Scrapy
```bash
pip install Scrapy
```
<br>

4. Buat Project Scrapping baru
"
scrapy startproject OLXMotor
"
<br>
5. Masuk directory
   <br>
```bash
cd spider
```
<br>
6. Jalankan Scrapping atau spider 
untuk csv
"
scrapy crawl motor -O motor.csv
"
<br>
atau
<br>
"
scrapy crawl motor -O motor.csv
"
