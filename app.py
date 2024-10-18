from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secreto necesario para manejar sesiones

# Datos de usuarios ficticios
users = {
    "jose1": "jose123",
    "jose2": "jose1234"
}

@app.route('/')
def home():
    # Si el usuario está autenticado, mostrar la página de bienvenida
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validar usuario y contraseña
        if username in users and users[username] == password:
            session['username'] = username  # Almacenar nombre de usuario en la sesión
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    # Verificar si el usuario está autenticado
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        flash('Por favor, inicia sesión primero.', 'warning')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Limpiar la sesión
    session.pop('username', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
