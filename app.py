from flask import Flask, render_template, request, jsonify, redirect, url_for
from entities.user import User
from entities.account import Account
from entities.permissions import Permission
from entities.log import Log
from enums.value_permission import ValuePermission
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
    
    account = Account.get_account_by_user(user_id)
    #balance = sum(t['amount'] if t['type'] == 1 else -t['amount'] for t in account.transactions) #se calcula el balance en el momento
    balance = 0
    session['permissions'] = [p.value for p in current_user.permissions] #se asignan permissions a variable global para que no se pierdan entre templates
    
    return render_template("welcome.html", mensaje_bienvenida=mensaje_bienvenida, balance=balance, account=account)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/usuarios')
@login_required
def usuarios():
    
    users = User.get_all_users()
    
    if 2 in current_user.permissions:
        return render_template('usuarios.html', users=users)
    else:
        return render_template('access_denied.html')

@app.route('/user_edit/<int:user_id>/permissions', methods=['GET'])
@login_required
def user_edit(user_id):
    
    user_permissions = Permission.get_permissions_by_user(user_id)
    user_permissions = [p.value for p in user_permissions] #Obtener solo los valores de los permisos del usuario
    permissions = ValuePermission.get_all_permissions()
    
    return render_template('user_edit.html', user_permissions=user_permissions, permissions=permissions, user_id=user_id)


@app.route('/edit_permissions/<int:user_id>/permissions', methods=['POST'])
@login_required
def edit_permissions(user_id):
    
    selected_permissions = request.form.getlist('permissions')
    permissions = [int(p) for p in selected_permissions]
    
    Permission.edit_permissions_by_user(user_id, permissions)
    Log.save(session.get('user_id'), "Edited a user", 3)
    
    return redirect(url_for('usuarios'))

@app.route('/logs')
@login_required
def logs():
    logs = Log.get_all_logs()
    return render_template('logs.html', logs=logs)

@app.route('/delete_user/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    User.delete_user(user_id)
    Log.save(session.get('user_id'), "Deleted a user", 4)
    
    return redirect(url_for('usuarios'))


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