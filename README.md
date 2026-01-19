
# A Roleta das Moedas Nativas

**Descrição:**  
Um programa em Python que seleciona um país com base no número do aluno e calcula um "Índice de Riqueza Fictícia" usando a população e o nome do país. Também extrai dinamicamente a moeda local e o seu símbolo, garantindo compatibilidade com qualquer país da API Rest Countries.

**Funcionalidades:**  
- Solicita o número do aluno como entrada.  
- Seleciona um país da lista da API `https://restcountries.com/v3.1/all`.  
- Extrai dinamicamente a moeda e o símbolo do país (não precisa saber a chave à partida).  
- Calcula o índice de riqueza fictícia: `population / número de letras do nome do país`.  
- Mostra uma frase formatada com os resultados.  

**Como usar:**  
1. Instalar a biblioteca `requests` se ainda não tiver:  
```
pip install requests
````

2. Executar o script:

```
python roleta_moedas.py
```

3. Digitar o número do aluno quando solicitado.
4. Ver o país sorteado, a moeda e o índice de riqueza fictícia.

**Exemplo de saída:**

```
O país sorteado pelo aluno 15 é Portugal. A sua moeda é Euro (€) e o Índice é 579067.17.
```

