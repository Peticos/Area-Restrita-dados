from flask import Flask, request, jsonify, render_template
import pickle
from script import predict

app = Flask(__name__)
rename_map = {'idade': 'age', 'genero': 'gender', 'tempoRedesSociais': 'time_in_social_media', 'pessoasEmCasa': 'people_living_together', 'rendaFamiliar': 'social_class', 'temPets': 'has_pets', 'quantidadePets': 'number_of_pets', 'temCachorro': 'has_dog', 'temGato': 'has_cat', 'temOutros': 'has_others', 'esqueceTarefas': 'forgets', 'reportaria': 'report_abandoned', 'sentimento': 'feeling'}

@app.route('/possiveis-users')
def possiveis_users():
    return render_template('dash-possiveis-users.html')

@app.route('/publico-alvo')
def publico_alvo():
    return render_template('dash-publico-alvo.html')

@app.route('/previsao-user')
def home():
    return render_template('index.html')  # Renders the HTML page

@app.route('/previsao-user', methods=['POST'])
def receber_dados():
    dados = request.json.get('dados')
    print(dados)
    for old_key, new_key in rename_map.items():
        dados[new_key] = dados.pop(old_key)
    result = predict(dados)
    print(result)
    
    return jsonify({'percentage': result[0], 'would_use': int(result[1])})

if __name__ == '__main__':
    app.run(debug=True)