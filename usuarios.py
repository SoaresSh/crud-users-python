import json
import os

usuarios = []

def criar_usuario(nome, email, senha, cpf):
    for usuario in usuarios:
        if usuario['email'] == email:
            raise ValueError("Email já cadastrado.")
        if usuario['cpf'] == cpf:
            raise ValueError("CPF já cadastrado.")
    novo_usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'cpf': cpf,
    }
    usuarios.append(novo_usuario)
    salvar_usuarios_em_arquivo()
    return novo_usuario

def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    raise ValueError("Usuário não encontrado.")

def deletar_usuario(cpf):
    usuarios
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuarios.remove(usuario)
            return True
    raise ValueError("Usuário não encontrado.")
    
def salvar_usuarios_em_arquivo():
        with open('usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

def carregar_usuarios_de_arquivo():
        global usuarios
        if os.path.exists('usuarios.json'):
            with open('usuarios.json', 'r', encoding='utf-8') as arquivo:
                usuarios = json.load(arquivo)