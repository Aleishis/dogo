from flask import Flask, render_template, request, jsonify, redirect, url_for
from entities.user import User
from entities.transaction import Transaction
from entities.account import Account
from entities.log import Log
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os
from flask import session

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/welcome')
@login_required
def welcome():
    user_id = session.get('user_id')
    mensaje_bienvenida = session.get('mensaje_bienvenida')    
    
    if not user_id:
        return render_template("index.html")
    
    transactions = Transaction.get_transactions_by_account(user_id)
    balance = sum(t['amount'] if t['type'] == 1 else -t['amount'] for t in transactions)
    account = Account.get_account_by_user(user_id)
   
    
    return render_template("welcome.html", transactions=transactions, mensaje_bienvenida=mensaje_bienvenida, balance=balance, account=account)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if User.check_email_exists(email):
        return jsonify({"success": False, "message": "El correo electrónico ingresado ya se encuentra registrado."}), 409

    if User.save(name, email, password):
        return jsonify({"success": True, "message": "Su cuenta fue creada correctamente."}), 201
    else:
        return jsonify({"success": False, "message": "Ocurrió un error al crear su cuenta. Intente de nuevo"}), 500

@app.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()
    
    email = data.get("email")
    password = data.get("password")
    
    user = User.check_login(email=email, password=password)
    
    print(user.is_active) #eliminar
    
        
    if user and user.is_active:
        
        login_user(user) #la variable jinja current_user toma el valor del argumento, en este caso user
        
        Log.save(user.id, "New login", 1)
        
        session['mensaje_bienvenida'] = data.get("mensaje_bienvenida")
        session['user_id'] = user.id
        
        print("Authenticated:", current_user.is_authenticated)
        return jsonify({'success' : True, 'message' : "Sesion iniciada correctamente"}), 200
    elif user and not user.is_active:
        return jsonify({'success' : False, 'message' : 'Su cuenta se encuentra inactiva. Contacte al administrador.'}), 403
    else:
        return jsonify({'success' : False}), 401

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5069, host='0.0.0.0') 