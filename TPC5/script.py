import ply.lex as lex

# Definição dos tokens
tokens = (
   'LISTAR',
   'MOEDA',
   'SELECIONAR',
   'SAIR',
   'IGNORAR'
)

# Regra para ignorar espaços em branco e tabs
t_SAIR = r'SAIR'

# Regra para tratar erros
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def t_LISTAR(t):
    r'LISTAR'
    print("Lista de produtos disponíveis:")
    for product in prices:
        print(f"{product} - {prices[product]}€")
    return t

def t_MOEDA(t):
    r'Moeda\s+(\d+[ec],?\s*)*\d+[ec]'
    coin_values_str = t.value.split(' ', 1)[1]
    coin_values = coin_values_str.split(',')
    for valor in coin_values:
        print (valor.strip())  
        if valor[-1] == 'e':
            t.lexer.saldo += int(valor[:-1])  
        else:
            t.lexer.saldo += int(valor[:-1]) / 100
    print (f"Saldo atual: {t.lexer.saldo}€")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s+\d'
    product_index = int(t.value.split(' ', 1)[1])
    product_name = list(prices.keys())[product_index - 1]
    product_price = prices[product_name]
    if t.lexer.saldo >= product_price:
        t.lexer.saldo -= product_price
        t.lexer.current_balance += product_price
        print(f"Produto selecionado: {product_name}")
        print(f"Saldo atual: {t.lexer.saldo}€")
    else:
        print("Saldo insuficiente")

t_ignore = '>> \t\n'

def t_IGNORAR(t):
    r'\w+'
    pass

# Criar o analisador léxico
lexer = lex.lex()
lexer.saldo = 0
lexer.current_balance = 0

prices = {}

with open("tabela", "r") as file:
    next(file)
    
    for line in file:
        columns = line.strip().split("|")
        item_name = columns[1].strip()
        price = float(columns[2].strip().rstrip('€'))
        prices[item_name] = price

saldo = 0

with open("test", "r") as f:
    data = f.read()
    lexer.input(data)
    for tok in lexer:
       if tok.type=="SAIR":
           break
       pass
