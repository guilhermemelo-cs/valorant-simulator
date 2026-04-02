import random

saldo = 800
arma_atual = 'Classic'
loop = ''
vitorias = 0

buy = {
    'Classic': 0,
    'Ghost': 500,
    'Sheriff': 800,
    'Stinger': 950,
    'Spectre': 1600,
    'Vandal': 2900,
    'Phantom': 2900,
    'Operator': 4700
}
lista_armas = list(buy.keys())

print('----- BEM-VINDO AO VALORANT.py -----')
print('1. Jogar')
print('2. Sair')

if int(input('Digite o núm. de escolha: ')) == 1:
    loop = True

    while loop:

        for round in range(1,14):
            print(f'----- RODADA {round} -----')
            print(f'Saldo atual: {saldo} ! Arma atual: {arma_atual}')
            print('Deseja comprar alguma arma antes de começar o round?')
            print('1. Sim')
            print('2. Não')

            if int(input('Digite o núm. escolhido: ')) == 1:

                while True:

                    for i, arma in enumerate(lista_armas, start=1):
                        print(f'{i}. {arma} - {buy[arma]}')

                    print('-----------------------------------')
                    print('Se quiser desistir da compra, digite "0".')
                    
                    escolha = int(input('Digite o núm. da arma escolhida: '))

                    if escolha == 0:
                            print('Saindo da loja.')
                            break

                    escolha_real = escolha - 1

                    if 0 <= escolha_real < len(lista_armas):
                            arma_selecionada = lista_armas[escolha_real]
                            preco = buy[arma_selecionada]

                            if saldo >= preco:
                                arma_atual = arma_selecionada
                                print(f'Arma comprada: {arma_atual} ! Valor: {buy[arma_atual]}')
                                saldo -= preco
                                print(f'Seu novo saldo: {saldo}')
                                break
                            else:
                                 print(f'Saldo insuficiente. O valor da arma é {preco} e seu saldo é de {saldo}c.')
                            
                    else:
                         print('Esse núm. não existe na lista. Por favor, digite um núm. presente!')
            print('iniciando rodada.')
            
            round_ganho = random.choice([True, False])

            if round_ganho == True:

                print('-----------------')
                print('Você GANHOU o round. Parabéns!')
                vitorias += 1

                if saldo < 9000:
                    saldo += 1200
                    print('Você ganhou 1200c. Como venceu, você continua com sua arma atual.')
                else:
                    saldo = 9000
                    print('Seu saldo atingiu o limite máximo. Por isso, não foi adicionado mais dinheiro no seu saldo.')
                    print('Você ainda continua com sua arma atual.')
            else:
                print('-----------------')
                print('Você PERDEU o round.')
                vitorias -= 1

                if saldo <= 9000:
                    saldo += 600
                    arma_atual = 'Classic'
                    print('Como perdeu, você ganhou apenas 600 e perdeu sua arma atual.')
                else:
                    saldo = 9000
                    arma_atual = 'Classic'
                    print('Como seu saldo está no limite máximo, você não ganhou os 600.')
                    print(f'Além disso, você perdeu sua arma. Você está com a {arma_atual}.')
        print('--------------')
        print('A partida acabou!')
        print('Analisando vitorias/derrotas de cada round...')

        if vitorias > 0:
            print('PARABÉNS! Você venceu a partida. Deseja jogar novamente?')
            print('1. Sim')
            print('2. Não')

            if int(input('Digite o núm. de sua escolha: ')) == 2:
                print('Obrigado por jogar VALORANT.py!')
                print('Saindo...')
                loop = False
                break
        elif vitorias < 0:
             print('Você infelizmente perdeu a partida. Gostaria de jogar novamente?')
             print('1. Sim')
             print('2. Não')

             if int(input('Digite o núm. de sua escolha: ')) == 2:
                print('Obrigado por jogar VALORANT.py!')
                print('Saindo...')
                loop = False
                break
        else:
             print('A partida terminou em empate. Gostaria de jogar novamente?')
             print('1. Sim')
             print('2. Não')

             if int(input('Digite o núm. de sua escolha: ')) == 2:
                print('Obrigado por jogar VALORANT.py!')
                print('Saindo...')
                loop = False
                break
else:
    print('Saindo do Valorant.py! Até a próxima.')
