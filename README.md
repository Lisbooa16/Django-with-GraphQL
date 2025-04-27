# 👀 Django + GraphQL - Quiz API

Este projeto é uma API de exemplo usando **Django + Graphene** para gerenciar perguntas, respostas, categorias e quizzes com suporte a **GraphQL**.

---

## 🚀 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/Lisbooa16/Django-with-GraphQL
cd seu-repo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode as migrações:
```bash
python manage.py migrate
```

4. Inicie o servidor:
```bash
python manage.py runserver
```

---

## 🔪 Acessar o GraphiQL
Acesse via navegador:
```
http://localhost:8000/graphql/
```

---

## 📋 Exemplo de Query: Buscar pergunta e respostas
```graphql
query GetQuestion($id: Int = 1) {
  allAnswers(id: $id) {
    id
    answerText
    isRight
  }
  allQuestions(id: $id) {
    id
    title
    quiz {
      id
      title
    }
  }
}
```

📌 Essa query retorna:
- A pergunta com `id = 1`
- Todas as respostas relacionadas a essa pergunta

---

## 🦩 Exemplo de Mutation: Criar uma categoria
```graphql
mutation {
  createCategory(name: "Matemática") {
    category {
      id
      name
    }
  }
}
```

---

## ✏️ Exemplo de Mutation: Atualizar uma categoria
```graphql
mutation {
  updateCategory(id: 1, name: "Nova Categoria") {
    category {
      id
      name
    }
  }
}
```

---

## ❌ Exemplo de Mutation: Deletar uma categoria
```graphql
mutation {
  deleteCategory(id: 1) {
    category {
      name
    }
  }
}
```

---

## ❌ Exemplo de Mutation: Pegar usuarios
```graphql
query {
  users{
    edges{
      node{
        username
        pk
        isActive
      }
    }
  }
}
```

⚠️ Atenção: você só pode deletar categorias que **não estejam sendo usadas** por quizzes. Caso contrário, um erro de **constraint de chave estrangeira** será retornado.

---

## 🧱 Modelos disponíveis

- `Category`: nome da categoria
- `Quizzes`: vinculado à categoria
- `Question`: vinculado ao quiz
- `Answer`: vinculada à questão

---

## 📂 Estrutura básica
```
quiz/
├── models.py
├── schema.py
├── urls.py
└── views.py

project/
├── settings.py
└── urls.py
```

---

## 📌 Observações

- Feito com [graphene-django](https://docs.graphene-python.org/projects/django/en/latest/)
- Uso do GraphQL simplifica e otimiza requisições com controle total sobre os dados

---

## ✍️ Autor

Guilherme Lisboa  
[LinkedIn](https://www.linkedin.com/in/guilherme-lisboa-5b6a52190/) | [GitHub](https://github.com/Lisbooa16)