from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Veri Seti (Sözler, Yazarlar ve Arka Plan Renkleri)
quotes_data = [
    {"text": "Yazılımda en zor kısım kod yazmak değil, ne yazacağını bilmektir.", "author": "Anonim", "theme": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"},
    {"text": "Hatalar, keşiflerin kapısını açan anahtarlardır.", "author": "James Joyce", "theme": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%)"},
    {"text": "Basitlik, karmaşıklığın en son noktasıdır.", "author": "Leonardo da Vinci", "theme": "linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%)"},
    {"text": "Kodunu 6 ay sonra görecek kişi, nerede yaşadığını bilen bir psikopatmış gibi yaz.", "author": "John Woods", "theme": "linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)"},
    {"text": "Bir şeyi basitçe anlatamıyorsan, onu yeterince iyi anlamamışsın demektir.", "author": "Albert Einstein", "theme": "linear-gradient(to right, #4facfe 0%, #00f2fe 100%)"},
    {"text": "Geleceği tahmin etmenin en iyi yolu, onu icat etmektir.", "author": "Alan Kay", "theme": "linear-gradient(120deg, #d4fc79 0%, #96e6a1 100%)"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/quote', methods=['GET'])
def get_quote():
    selected_quote = random.choice(quotes_data)
    return jsonify(selected_quote)

if __name__ == '__main__':
    # Docker konteyneri dışından erişilebilmesi için 0.0.0.0 şarttır
    app.run(debug=True, host='0.0.0.0', port=5000)
