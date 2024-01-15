# Django Blog Project

## Descrição

Este é um projeto Django que implementa um blog com diversas funcionalidades, incluindo criação, edição e remoção de posts, comentários nos posts, autenticação por e-mail e senha, e login social com o Google.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/JottaF/django-blog.git
    cd django-blog
    ```

2. **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Aplique as migrações:**

    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```

### Login social
Para utilizar o login social com o Google, acesse a [documentação](https://docs.allauth.org/en/latest/socialaccount/providers/google.html) para realizar as configurações.

## Projeto

### Home
A tela inicial apresenta os posts mais recentes do dia.
![Home](/screenshots/home.png)

### Detalhes do post
Quando é clicado em um post é apresentado os detalhes do post. Nos detalhes é possível ver a imagem atribuída ao post (caso haja), **comentar** e ver os comentários já feitos.
![Detail](/screenshots/post_detail1.png)

### Criação

O projeto permite a criação de posts de forma intuitiva. O usuário pode definir o título de sua postagem, o conteúdo, uma imagem (opicional) e programar a postagem para uma data futura ou para o dia atual.

![Posts](/screenshots/create_post.png)

Após a criação de um post, o usuário é direcionado para a página de detalhes de sua posta, onde pode **editar** ou **apagar** seu post.
![Detail2](/screenshots/post_detail.png)

### Autenticação

O projeto inclui um sistema de autenticação seguro e fácil de usar. O usuário pode acessar com seu login e senha ou entrar com o Google.

![Login](/screenshots/login.png)

Quando o novos usuários decidem criar uma conta com email e senha, eles são direcionados para a tela a seguir:

![Login Social](/screenshots/create_account.png)

## Contribuição

Se você quiser contribuir com este projeto, sinta-se à vontade para abrir um pull request. Todas as sugestões são bem-vindas!
