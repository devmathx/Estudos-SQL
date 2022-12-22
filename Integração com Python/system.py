import mysql.connector as mysql

# Preencha os dados para se conectar
connect = mysql.connect(
    host='',
    user='',
    password='',
    database=''
)
cursor = connect.cursor()

# Sistema de cadastro
def sign_in():
    print("Faça seu cadastro")
    name = input("Nome: ")
    phone = input("Telefone: ")
    password = input("Senha: ")
    command = f'INSERT INTO usuarios VALUES (DEFAULT, "{name}", "{phone}", "{password}")'
    cursor.execute(command)
    connect.commit()
    print("Você foi registrado")
   
# Sistema de login 
def login():
    print("Bem vindo de volta!")
    name = input("Nome: ")
    phone = input("Telefone: ")
    command = f' SELECT COUNT(id) FROM usuarios WHERE nome = "{name}" AND telefone = "{phone}"'
    cursor.execute(command)
    result = cursor.fetchall()
    result = result[0][0]
    if result: 
        print("Login bem sucedido!") 
    else:
        print("Nome ou telefone invalido")
    
sign_in()