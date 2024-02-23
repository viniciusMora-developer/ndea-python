# Desafio de Estágio - Validador de CEPs

Bem-vindo ao desafio de estágio da Maitha! Neste desafio, você será responsável por implementar um validador de CEPs para o sistema de correios de sua cidade.

## Regras de Negócio

O sistema dos correios da cidade teve um problema e perderam seu validador de CEPs. Hoje, sua missão é criar um validador de CEPs baseados em algumas pequenas regras listadas abaixo:

1. O CEP é um número maior que 100.000 e menor que 999.999.
2. O CEP não pode conter nenhum dígito repetitivo alternado em pares.

### Exemplos

#### CEP Inválido

    "012345" # Valor menor que 100.000
    "9999999" # Valor maior que 999.999
    "121426" # 1 é um dígito repetitivo alternado em par.
    "352523" # Os dígitos 2 e 5 são alternados repetitivos em par.

#### CEP Válido

    "523563"
    "123456"
    "997531"

Damos preferência a soluções utilizando REGEX e string slicing. Além disso não esqueça de cobrir sua solução com testes.

## Início

1. Clone este repositório em seu ambiente de desenvolvimento local através do comando `git clone https://bitbucket.org/maitha-tech/ndea-python/src ndea-python`
2. Crie um repositório público em sua conta do Github com o nome `ndea-python`
3. Via terminal, acesse a pasta criada `cd ndea-python`
4. Altere a URL de origin para o repositório que você acabou de criar utilizando o comando `git remote set-url origin <<INSIRA AQUI A URL DO REPOSITÓRIO QUE ACABOU DE CRIAR>>`
5. Agora que alterou a url, realize a sincronização dos arquivos com o comando `git push -u origin main`

## Instruções de Entrega

1. Crie um script python com o `validador_cep.py`
2. Peça para que o usuário digite um CEP a ser validado
3. Certifique-se de que o CEP esteja no formato correto de acordo com as regras de negócio descritas anteriormente

Exemplo:
```bash
python validador_cep.py
Digite o CEP a ser validado: 523563
CEP válido!
```