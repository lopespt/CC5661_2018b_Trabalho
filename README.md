TRABALHO CC5661
===============

A maneira mais fácil de rodar o gerador de problemas é utilizando o docker.

```shell
git clone https://github.com/lopespt/CC5661_2018b_Trabalho
cd CC5661_2018b_Trabalho
docker build -t servidor_cc5661 .
docker run -p 5000:5000 servidor_cc5661
```

O servidor estará rodando em http://localhost:5000/

Rotas
----

Existem 4 formas de chamar o servidor:

1. http://localhost:5000/ : Retorna um problema aleatório
2. http://localhost:5000/p1 : Retorna uma instância do problema 1
3. http://localhost:5000/p2 : Retorna uma instância do problema 2
4. http://localhost:5000/p3 : Retorna uma instância do problema 3