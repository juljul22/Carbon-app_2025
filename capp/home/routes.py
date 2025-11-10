from flask import render_template, request, redirect, url_for, Blueprint

home = Blueprint('home', __name__)

# Page d'accueil
@home.route('/')
@home.route('/home')
def home_home():
    return render_template('home.html')

# Page Login
@home.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # plus tard tu vérifieras les infos avec la base de données
        return redirect(url_for('home.home_home'))  # redirige vers la home page
    return render_template('login.html')

# Page Register
@home.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # plus tard tu enregistres l'utilisateur
        return redirect(url_for('home.login'))  # redirige vers login
    return render_template('register.html')
