import ply.lex as lex

# Define tokens
tokens = (
    'ON',
    'OFF',
    'INT',
    'TOTAL'
    'IGNORE'
)

# Define lexer rules
def t_ON(t):
    r'[Oo][Nn]'
    t.lexer.calculator_state = True
    return t

def t_OFF(t):
    r'[Oo][Ff][Ff]'
    t.lexer.calculator_state = False
    return t    

def t_INT(t):
    r'\d+'
    if getattr(t.lexer, 'calculator_state', True):
        t.value = int(t.value)
        t.lexer.total_sum = getattr(t.lexer, 'total_sum', 0) + t.value  # Accumulate the value
        return t
    
def t_IGNORE(t): # Ignora espaços e palavras
    r'[\s+|\w+]'
    pass

def t_TOTAL(t):
    r'='
    print("Total sum:", getattr(t.lexer, 'total_sum', 0))


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

def main():
    with open("test", "r") as file:
        lexer.calculator_state = True
        lexer.total_sum = 0  
        data = file.read()
        lexer.input(data)
        for token in lexer:
            pass
        print ("Total sum:", lexer.total_sum) # Por default, imprime o valor acumulado no final do programa correr

if __name__ == "__main__":
    main()
