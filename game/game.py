from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

@app.route('/get_question', methods=['GET'])
def get_question():
    operasi = request.args.get('operation', 'penjumlahan')
    level = int(request.args.get('level', 1))

    if level == 1:
        rentang = (1, 9)  
    elif level == 2:
        rentang = (10, 99)  
    elif level == 3:
        rentang = (100, 999)  
    else:
        rentang = (1, 9)  

    angka1, angka2 = random.randint(*rentang), random.randint(*rentang)

    
    if operasi == 'pembagian':
        angka1 = angka1 * angka2  

    return jsonify({'angka1': angka1, 'angka2': angka2})

# Endpoint untuk menghitung skor
@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    data = request.json
    jawaban_benar = data.get('correct_answers', 0)
    total_waktu = data.get('total_time', 60)  
    level = int(data.get('level', 1))

    # Penyesuaian skor berdasarkan level
    if level == 1:
        skor_per_soal = 10
    elif level == 2:
        skor_per_soal = 20
    elif level == 3:
        skor_per_soal = 30
    else:
        skor_per_soal = 10

    if total_waktu == 0:
        total_waktu = 1  # Hindari pembagian dengan nol

    skor_kecepatan = jawaban_benar / total_waktu
    skor = jawaban_benar * skor_per_soal + int(skor_kecepatan * 100)

    return jsonify({'skor': skor})

# Rute untuk menampilkan game
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("==========================")
    print("|      Game Matematika   |")
    print("==========================")
    print("Server berjalan di http://127.0.0.1:5000")
    print("Silakan buka URL tersebut di browser Anda untuk bermain.")
    print("Tekan CTRL+C untuk menghentikan server.")
    app.run(debug=True)
