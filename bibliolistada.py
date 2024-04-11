import os

# Lista para armazenar os livros
livros = [
    {'nome': 'O Guia do Mochileiro das Galáxias', 'categoria': 'Comédia'},
    {'nome': 'À Espera de Um Milagre', 'categoria': 'Drama'}
]

# Função para limpar a tela
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para mostrar o nome do programa
def mostrarNomePrograma():
    print("Biblioteca do Brunim")

# Função para cadastrar livros
def cadastrarLivro():
    nome = input("Digite o nome do livro para cadastro: ")
    categoria = input("Digite a categoria do livro: ")
    livro = {'nome': nome, 'categoria': categoria}
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Função para listar os livros
def listarLivros():
    for livro in livros:
        print(f"Nome: {livro['nome']}, Categoria: {livro['categoria']}")

# Função para remover livros
def removerLivro():
    nome = input("Digite o nome do livro para remover: ")
    livroParaRemover = None
    for livro in livros:
        if livro['nome'] == nome:
            livroParaRemover = livro
            break
    if livroParaRemover:
        livros.remove(livroParaRemover)
        print("Livro deletado com sucesso!")

# Função para sair do programa
def sair():
    print("Falou, um abraço! XD")
    exit()

# Função principal que executa o programa
def main():
    limparTela()
    mostrarNomePrograma()
    while True:
        print("\n1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Remover Livro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == '1':
            cadastrarLivro()
        elif opcao == '2':
            listarLivros()
        elif opcao == '3':
            removerLivro()
        elif opcao == '4':
            sair()
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()