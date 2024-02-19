# Python Gmail Automation

Este projeto permite que os usuários enviem e-mails automaticamente utilizando a API do Gmail. É ideal para automações de e-mail em Python sem interação manual com a autenticação OAuth 2.0.

## Início Rápido

As instruções a seguir ajudarão você a obter uma cópia do projeto em operação em sua máquina local para fins de desenvolvimento e testes.

### Pré-requisitos

Certifique-se de ter Python 3.6 ou superior instalado em sua máquina. Além disso, você precisará de uma conta do Google para acessar a API do Gmail.

## Configuração no Google Cloud

Para configurar o projeto no Google Cloud e utilizar a API do Gmail, siga os passos abaixo:

### Passo 1: Criar um Projeto no Google Cloud

- Acesse [Google Cloud Console](https://console.developers.google.com/).
- Crie um novo projeto e anote o ID do projeto.

### Passo 2: Ativar a API do Gmail

- Navegue até "APIs e Serviços > Biblioteca" e ative a "Gmail API" para o seu projeto.

### Passo 3: Configurar Credenciais

- Em "APIs e Serviços > Credenciais", crie credenciais "ID do cliente OAuth" para o tipo "Aplicativo de Desktop" e baixe o arquivo `credentials.json`.

### Passo 4: Adicionar Usuários Teste

- Na mesma seção de credenciais, adicione os e-mails dos usuários como testadores autorizados.

## Utilização

Para enviar um e-mail usando a API do Gmail, execute o script principal:

```python
python app.py
```

### Instalação

Clone o repositório para sua máquina local e instale as dependências:

```bash
git clone https://github.com/RafaelLimaTk/SendMail.git
cd SendMail
pip install -r requirements.txt
```
