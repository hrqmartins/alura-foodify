# 🍽️ Foodify – Sistema de Gerenciamento de Restaurantes

Este projeto foi desenvolvido durante o curso da [Alura](https://www.alura.com.br/), com o objetivo de criar uma aplicação em Python para **gerenciar restaurantes e seus respectivos dados de forma prática e funcional**.

---

## 📌 Objetivo

O **Foodify** é um sistema de linha de comando (CLI) que permite:

- Cadastrar e listar restaurantes com nome e categoria;
- Ativar ou desativar restaurantes;
- Gerenciar o status de funcionamento dos estabelecimentos.

O sistema foi criado para simular o backend de uma aplicação de delivery/gestão de restaurantes, com foco em boas práticas de programação e organização de dados.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- Módulo padrão `os` para limpeza da tela
- Execução via terminal (sem interface gráfica)

---

## 📁 Estrutura de Pastas

```
/foodify/
├── app.py         # Código principal da aplicação
└── README.md      # Documentação do projeto
```

---

## 🧩 Funcionalidades Implementadas

### ✅ 1. Cadastro de Restaurantes
Permite ao usuário inserir novos restaurantes, informando:
- Nome do restaurante
- Categoria (ex: Japonesa, Italiana, etc.)

🔧 Os dados são armazenados em uma lista de dicionários.

---

### ✅ 2. Listagem de Restaurantes
Exibe todos os restaurantes cadastrados, mostrando:
- Nome
- Categoria
- Status (Ativado/Desativado)

---

### ✅ 3. Modificação de Status do Restaurante
Permite ativar ou desativar um restaurante com base no nome informado.

---

### ✅ 4. Menu Interativo via Terminal
- Interface textual clara com opções numeradas
- Validação de entradas e mensagens de erro

---

## ❌ Funcionalidades a Serem Implementadas

Ainda faltam algumas funcionalidades importantes para completar o projeto:

### 🚧 Cadastro de Produtos
- Incluir nome, descrição e preço dos itens do cardápio de cada restaurante.

### 🚧 Realização de Pedidos
- O cliente escolhe produtos, informa o endereço de entrega e finaliza o pedido.

### 🚧 Gerenciamento de Pedidos
- Permitir ao restaurante confirmar, preparar e enviar pedidos para entrega.

### 🚧 Cálculo de Frete
- Cálculo baseado em distância (simulada) ou regras definidas por restaurante.

---

## 💡 Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/hrqmartins/alura-foodify.git
cd alura-foodify
```

2. Execute o programa:
```bash
python app.py
```

---

## 📚 Aprendizados

Durante o desenvolvimento, foram praticados conceitos fundamentais de Python como:

- Estruturas de dados (listas e dicionários)
- Condicionais e laços
- Funções e modularização
- Boas práticas de organização e legibilidade de código
- Comentários e docstrings

---

## 🧑‍💻 Autor

Desenvolvido por **Henrique Martins**, estudante de Análise e Desenvolvimento de Sistemas na FIAP.

---
