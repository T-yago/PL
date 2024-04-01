## Termos terminais

#### P (Programa):
Progama consiste no termo mais geral que pode ser qualquer uma das três expressões (? var P | !E P | var = E P ) ou ainda o vazio (ε)

#### E (Expressão):
Pode constituir uma soma, uma subtração ou um termo

#### T (Termo):
Um termo pode ser uma operação de multiplicação, de divisão, ou um fator

#### F (Fator):
Um fator é uma expressão, um número, ou um var

## Gramática LL1 (Produções):

```bash
P -> ? var P | !E P | var = E P | ε
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> ( E ) | num | var
```


## Lookahead Sets:

```bash
LA(P -> ? var P): ?
LA(P -> ! E P): !
LA(P -> var = E P): var
LA(P -> ε): EOF
LA(E -> E + T): (, num, var
LA(E -> E - T): (, num, var
LA(E -> T): (, num, var
LA(T -> T * F): (, num, var
LA(T -> T / F): (, num, var
LA(T -> F): (, num, var
LA(F -> ( E )): (
LA(F -> num): num
LA(F -> var): var
```


