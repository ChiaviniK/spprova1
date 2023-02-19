import json

dados = [
    {
        "nome": "Bolinha",
        "tipo": "Cachorro",
        "idade": 5,
        "raca": "Vira-lata",
        "dono": {
            "nome": "João",
            "email": "joao@gmail.com"
        }
    },
    {
        "nome": "Garfield",
        "tipo": "Gato",
        "idade": 7,
        "raca": "Siamês",
        "dono": {
            "nome": "Mariana",
            "email": "mariana@gmail.com"
        }
    },
    {
        "nome": "Pretinha",
        "tipo": "Cachorro",
        "idade": 3,
        "raca": "Poodle",
        "dono": {
            "nome": "Pedro",
            "email": "pedro@gmail.com"
        }
    },
    {
        "nome": "Mimi",
        "tipo": "Gato",
        "idade": 2,
        "raca": "Persa",
        "dono": {
            "nome": "Ana",
            "email": "ana@gmail.com"
        }
    },
    {
        "nome": "Nina",
        "tipo": "Cachorro",
        "idade": 1,
        "raca": "Bulldog Francês",
        "dono": {
            "nome": "Fernanda",
            "email": "fernanda@gmail.com"
        }
    }
]

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo)
