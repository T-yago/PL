# TPC1 : Máquina de Vending
## 2024-02-05

## Autor
- a100665
- Tiago Nuno de Magalhães Teixeira

### Resumo
Desenvolver um código que funcione de forma semelhante a uma máquina de vending, na medida que suporte operações de listagem, adição de moedas, e compras.

Deverá funcionar da seguinte forma:

>> -> input do user
< -> Resposta da máquina


>> LISTAR
< 1 água 50c
  2 bolo 60c
>> Moeda 1e, 10c, 20c
< Saldo = 1e30c
>> SELECIONAR 2
< saldo = 70c
>> SAIR
< troco <valor>

O programa utiliza o input vindo de um ficheiro "tabela", cujo formato é do seguinte tipo:

  id |  Name             | Preço (€)
   1 |  Água             | 1.00€
   2 |  Refrigerante     | 1.20€
   3 |  Café             | 1.50€
   4 |  Chá              | 1.20€
   5 |  Sumo             | 1.00€
   6 |  Bolachas         | 1.00€