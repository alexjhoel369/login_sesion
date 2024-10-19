from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Datos de usuario para la autenticación
users = {
    'Jhoel': 'tesla369',
    'Alejandro': 'nicola000'
}

@app.route('/')
def home():
    if 'username' in session: 
        return redirect(url_for('bienvenido'))
    return redirect(url_for('login'))  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificación usuario y contraseña
        if username in users and users[username] == password:
            session['username'] = username  
            return redirect(url_for('bienvenido'))
        else:
            flash('Usuario o contraseña incorrectos. Intenta de nuevo.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/Bienvenido')
def bienvenido():
    if 'username' not in session:
        return redirect(url_for('login')) 
    username = session['username']
    return render_template('bienvenido.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None) 
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
