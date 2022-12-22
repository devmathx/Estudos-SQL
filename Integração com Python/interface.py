from PySimpleGUI import PySimpleGUI as sg
import mysql.connector as mysql

# Preencha os dados para se conectar
connect = mysql.connect(
    host='',
    user='',
    password='',
    database=''
)
cursor = connect.cursor()

sg.theme('Reddit')

def sigin():
    layout = [
        [sg.Text("Usuário: "), sg.Input(key='user')],
        [sg.Text("Telefone:"), sg.Input(key='phone')],
        [sg.Text("Senha:   "), sg.Input(key='password', password_char="*")],
        [sg.Button("Cadastrar")],
        [sg.Text("Já possui uma conta? "), sg.Button("Tela de login")]
    ]
    return sg.Window("Cadastro", layout, finalize=True)

def login():
    layout = [
        [sg.Text("Usuário: "), sg.Input(key='user')],
        [sg.Text("Senha:   "), sg.Input(key='password', password_char="*")],
        [sg.Button("Entrar")],
        [sg.Text("Não possui uma conta? "), sg.Button("Tela de Cadastro")]
    ]
    return sg.Window("Login", layout, finalize=True)

win1, win2 = sigin(), None

while True:
    window, event, values = sg.read_all_windows()
    
    if event == sg.WIN_CLOSED:
        break
    
    # Tela de Cadastro
    if window == win1: 
        if event == "Tela de login":
            win2 = login()
            win1.hide()
        elif event == "Cadastrar":
            name = values['user']
            phone = values['phone']
            password = values['password']
            command = f'INSERT INTO usuarios VALUES (DEFAULT, "{name}", "{phone}", "{password}")'
            cursor.execute(command)
            connect.commit()
            sg.popup("Você foi registrado")     
    # Tela de Login
    elif window == win2: 
        if event == 'Tela de Cadastro':
            win2.hide()
            win1.un_hide()
        elif event == "Entrar":
            name = values['user']
            password = values['password'] 
            command = f' SELECT COUNT(id) FROM usuarios WHERE nome = "{name}" AND senha = "{password}"'
            cursor.execute(command)
            result = cursor.fetchall()
            result = result[0][0]
            if result:
                sg.popup("Bem vindo de volta!")
            else:
                sg.popup("Usuário ou senha invalidos.") 
        