import copy
import sys
import numpy as np
import statistics


# Lendo arquivo e retornando em lista as requisicoes 
def read_file(file):
    f = open(file, 'r')
    req = [int(x) for x in f.readline().split('-') if x !='']
    # req.remove('')
    # req.remove('\n')
    f.close()
    return req

def fifo(pos, time, req):
    r = copy.copy(req)
    f = open("fifo.txt", "w")
    dslc = 0
    n = len(r)
    l_dsl = []
    for request in r:
        dslc += abs(request-pos)
        l_dsl.append(abs(request-pos))
        pos = request
        f.write(str(request))
        f.write("-")
        
    lt = [time * d for d in l_dsl]
    m_dslc = dslc / n
    m_seek = time * dslc / n    
    name = f.name
    vd = statistics.variance(l_dsl)
    dpd = statistics.stdev(l_dsl)
    vt = statistics.variance(lt)
    dpt = statistics.stdev(lt)
    f.close()
    print('\nFIFO/FCFS')
    print('Quantidade de deslocamento:', dslc)
    print('Quantidade media de deslocamento:', m_dslc)
    print('Variancia:', vd)
    print('Desvio padrao:', dpd)
    print('Tempo medio de deslocamento:', m_seek)
    print('Variancia tempo:', vt)
    print('Desvio padrao tempo:', dpt)
    print('Arquivo:', name)

# Shortest Seek First
def ssf(pos, time, req):
    r = copy.copy(req)
    f = open("ssf.txt", "w")
    n = len(r)
    high = max(r)
    x = high
    min_seek = abs(pos-high)
    r.sort()
    dslc = 0
    l_dsl = []
    while len(r) > 0:
        # find the shortest distance from the current position
        for request in r:
            seek = abs(pos-request)
            if (seek < min_seek):
                min_seek = seek
                x = request
                f.write(str(request))
                f.write("-")
        dslc += abs(pos-x)
        l_dsl.append(abs(pos-x))
        pos = x
        r.remove(x)
        min_seek = abs(pos-high)
        x = high
    
    lt = [time * d for d in l_dsl]
    m_dslc = dslc / n
    m_seek = time * dslc / n    
    name = f.name
    vd = statistics.variance(l_dsl)
    dpd = statistics.stdev(l_dsl)
    vt = statistics.variance(lt)
    dpt = statistics.stdev(lt)
    f.close()
    print('\nSSF')
    print('Quantidade de deslocamento:', dslc)
    print('Quantidade media de deslocamento:', m_dslc)
    print('Variancia:', vd)
    print('Desvio padrao:', dpd)
    print('Tempo medio de deslocamento:', m_seek)
    print('Variancia tempo:', vt)
    print('Desvio padrao tempo:', dpt)
    print('Arquivo:', name)

def scan(cil, pos, time, req):
    r = copy.copy(req)
    f = open("scan.txt", "w")
    n = len(r)
    dslc = 0
    start = pos
    l_dsl = []
    # seek to end from starting pos
    for x in range(start, cil):
        if (x in r):
            dslc += abs(pos-x)
            l_dsl.append(abs(pos-x))
            pos = x
            r.remove(x)
            f.write(str(x))
            f.write("-")
    # seek back up from end to 0
    count = cil
    while count >= 0:
        if (count in r):
            dslc += abs(pos-count)
            l_dsl.append(abs(pos-count))
            pos = count
            r.remove(count)
            f.write(str(count))
            f.write("-")
        count -= 1

    lt = [time * d for d in l_dsl]
    m_dslc = dslc / n
    m_seek = time * dslc / n    
    name = f.name
    vd = statistics.variance(l_dsl)
    dpd = statistics.stdev(l_dsl)
    vt = statistics.variance(lt)
    dpt = statistics.stdev(lt)
    f.close()
    print('\nSCAN')
    print('Quantidade de deslocamento:', dslc)
    print('Quantidade media de deslocamento:', m_dslc)
    print('Variancia:', vd)
    print('Desvio padrao:', dpd)
    print('Tempo medio de deslocamento:', m_seek)
    print('Variancia tempo:', vt)
    print('Desvio padrao tempo:', dpt)
    print('Arquivo:', name)

# Circular Scan 
def cscan(cil, pos, time, req):
    r = copy.copy(req)
    f = open("cscan.txt", "w")
    dslc = 0
    n = len(r)
    start = pos
    l_dsl = []
    # seek to end from starting pos
    for x in range(start,cil):
        if (x in r):
            dslc += abs(pos-x)
            l_dsl.append(abs(pos-x))
            pos = x
            r.remove(x)
            f.write(str(x))
            f.write("-")

    # go back to beginning and continue seeking
    end = max(r)
    for i in range(0,end):
        if (i in r):
            dslc += abs(pos-i)
            l_dsl.append(abs(pos-i))
            pos = i
            r.remove(i)
            f.write(str(i))
            f.write("-")

    lt = [time * d for d in l_dsl]
    m_dslc = dslc / n
    m_seek = time * dslc / n    
    name = f.name
    vd = statistics.variance(l_dsl)
    dpd = statistics.stdev(l_dsl)
    vt = statistics.variance(lt)
    dpt = statistics.stdev(lt)
    f.close()
    print('\nCSCAN')
    print('Quantidade de deslocamento:', dslc)
    print('Quantidade media de deslocamento:', m_dslc)
    print('Variancia:', vd)
    print('Desvio padrao:', dpd)
    print('Tempo medio de deslocamento:', m_seek)
    print('Variancia tempo:', vt)
    print('Desvio padrao tempo:', dpt)
    print('Arquivo:', name)

def main():
    args = sys.argv[1:]
    while len(args) < 4:
        print('\n[python3]EXECUTE: python main.py <qnt_cilindros> <posicao_inicial> <tempo_seek> <nome_arquivo>\n')
        exit(-1)
    qnt_cilindros = int(args[0])
    posicao_inicial = int(args[1])
    tempo_seek = int(args[2])
    nome_arquivo = args[3]
    req = read_file(nome_arquivo)
    print(req)

    fifo(posicao_inicial, tempo_seek, req)
    ssf(posicao_inicial, tempo_seek, req)
    scan(qnt_cilindros, posicao_inicial, tempo_seek, req)
    cscan(qnt_cilindros, posicao_inicial, tempo_seek, req)
    
main()