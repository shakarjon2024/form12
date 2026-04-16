from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form12', methods=['GET', 'POST'])
def form12():
    if request.method == 'POST':
        rang = request.form.get('rang')
        qidiruv = request.form.get('qidiruv')
        return f"<h2>Tanlangan rang: <span style='background:{rang}; padding:10px; color:white;'>{rang}</span></h2><p>Qidiruv: {qidiruv}</p><br><a href='/'>Orqaga</a>"
    return render_template('form12.html')

if __name__ == '__main__':
    app.run(debug=True)
