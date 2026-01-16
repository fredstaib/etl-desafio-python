# Desafio ETL em Python (Sem Dependência de API)

Este projeto foi desenvolvido como parte de um desafio prático para compreensão do fluxo **ETL (Extract, Transform, Load)** utilizando Python.

A API originalmente utilizada no desafio foi descontinuada. Para manter o foco no aprendizado do processo ETL, a etapa de **Extração** foi adaptada para utilizar dados fictícios criados diretamente no código, sem prejuízo ao objetivo da atividade.

---

## 🧩 Estrutura do ETL

### 🔹 Extract
A etapa de extração foi realizada por meio de uma lista de usuários criada diretamente no código Python.  
Cada usuário é representado por um dicionário contendo seus dados básicos.

Essa abordagem substitui a dependência da API externa e garante a continuidade do fluxo ETL.

---

### 🔹 Transform
Na etapa de transformação, foi criada uma função responsável por gerar uma **mensagem personalizada** para cada usuário.

Ao invés de armazenar as mensagens em uma lista separada, o código foi modificado para **inserir a mensagem diretamente em cada objeto de usuário**, por meio de um novo campo chamado `"mensagem"`.  
Dessa forma, os dados originais são enriquecidos durante a transformação.

---

### 🔹 Load
Na etapa de carregamento, a própria lista `users`, já contendo o campo `"mensagem"`, é utilizada como saída do processo ETL.  
As mensagens personalizadas são exibidas no console, representando o carregamento dos dados transformados.

---

