import os

# Lista para armazenar os livros
livros = [
    {'nome': 'O Guia do Mochileiro das Galáxias', 'categoria': 'Comédia', 'ativo': False},
    {'nome': 'À Espera de Um Milagre', 'categoria': 'Drama', 'ativo': True},
    {'nome': 'Começando a programar em Python Para leigos', 'categoria': 'Programação', 'ativo': False}
]

def exibirNomePrograma():
    print('BIBLIOTECA DO BRUNIM 1.0')

def exibirOpcoes():
    print('1. Cadastrar livro')
    print('2. Listar livros')
    print('3. Alternar estado de um livro')
    print('4. Remover livro')
    print('5. Sair\n')

def finalizar():
    exibirSubtitulo('Falou, um abraço! :D')

def voltarMenuPrincipal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcaoInvalida():
    print('Opção inválida!\n')
    voltarMenuPrincipal()

def exibirSubtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrarLivro():
    exibirSubtitulo('Cadastro de novos livros')
    nomeLivro = input('Digite o nome do livro a ser cadastrado: ')
    categoria = input(f'Digite a categoria do livro {nomeLivro}: ')
    dadosLivro = {'nome': nomeLivro, 'categoria': categoria, 'ativo': False}
    livros.append(dadosLivro)
    print(f'O livro {nomeLivro} foi cadastrado com sucesso!')
    voltarMenuPrincipal()

def listarLivros():
    exibirSubtitulo('Listagem de livros')
    print(f'{"Livro".ljust(37)} | {"Categoria".ljust(35)} | Status')
    for livro in livros:
        nomeLivro = livro['nome']
        categoria = livro['categoria']
        ativo = 'ativado' if livro['ativo'] else 'desativado'
        print(f'- {nomeLivro.ljust(35)} | {categoria.ljust(35)} | {ativo}')
    voltarMenuPrincipal()

def alterarLivro():
    exibirSubtitulo('Alterar estado do livro')
    nomeLivro = input('Digite o nome do livro que deseja alterar o status: ')
    livroEncontrado = False

    for livro in livros:
        if nomeLivro == livro['nome']:
            livroEncontrado = True
            livro['ativo'] = not livro['ativo']
            mensagem = f'O livro {nomeLivro} foi ativado com sucesso' if livro['ativo'] else f'O livro {nomeLivro} foi desativado com sucesso'
            print(mensagem)
            
    if not livroEncontrado:
        print('O livro não foi encontrado')
            
    voltarMenuPrincipal()

def removerLivro():
    exibirSubtitulo('Remover livro')
    nomeLivro = input('Digite o nome do livro que deseja remover: ')
    livroParaRemover = None
    for livro in livros:
        if livro['nome'] == nomeLivro:
            livroParaRemover = livro
            break
    if livroParaRemover:
        livros.remove(livroParaRemover)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado.")
    voltarMenuPrincipal()

def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: 
            cadastrarLivro()
        elif opcaoEscolhida == 2: 
            listarLivros()
        elif opcaoEscolhida == 3: 
            alterarLivro()
        elif opcaoEscolhida == 4: 
            removerLivro()
        elif opcaoEscolhida == 5: 
            finalizar()
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == '__main__':
    main()