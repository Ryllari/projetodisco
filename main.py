import sys


# Lendo arquivo e retornando em lista as requisicoes 
def read_file(file):
    f = open(file, 'r')
    req = f.readline().split('-')[:-1]
    return req

def main():
    args = sys.argv[1:]
    while len(args) < 4:
        print('\n[python3]EXECUTE: python main.py <qtd_cilindros> <posicao_inicial> <tempo_seek> <nome_arquivo>\n')
        exit(-1)
    qnt_cilindros = int(args[0])
    posicao_inicial = int(args[1])
    tempo_seek = int(args[2])
    nome_arquivo = args[3]
    req = read_file(nome_arquivo)
    print(req)

main()