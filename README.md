TRABALHO CC5661
===============

A maneira mais fácil de rodar o gerador de problemas é utilizando o docker.

```shell
git clone https://github.com/lopespt/CC5661_2018b_Trabalho
cd CC5661_2018b_Trabalho
docker build -t servidor_cc5661
docker run -p 5000:5000 servidor_cc5661
```

