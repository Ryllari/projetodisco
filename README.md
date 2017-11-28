# projetodisco v 1.0 
## Simulacao dos algoritmos de escalonamento de braço do disco (Python3)
* FIFO/FCFS
* SSF
* SCAN
* SCAN Circular (C-SCAN)

*Entradas:*
* Quantidade de cilindros do disco.
* Posição inicial do braço do disco (número do cilindro em que o braço se encontra).
* Tempo de seek para o cilindro adjacente (ms).
* Nome do arquivo que contém as requisições de acesso a disco no formato abaixo:
> 12-9-43-32-50-43-40-20-36-8-34-3-44-12-32-10-8-18-43-11-

*Saídas:*
Para cada um dos quatro algoritmos simulados, o programa deverá fornecer as seguintes saídas:
* Quantidade de deslocamentos necessária para atender todas as requisições;
* Quantidade média de deslocamentos;
* Variância e desvio padrão da quantidade de deslocamento;
* Tempo médio de deslocamentos.
* Variância e desvio padrão do tempo de deslocamento.
* Arquivo (mesmo formato do arquivo de entrada) contendo a ordem em que as requisições foram atendidas.

## Executando o script
> python main.py <qtd_cilindros> <posicao_inicial> <tempo_seek> <nome_arquivo>

*OBS: Projeto em andamento*
