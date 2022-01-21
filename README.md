# Aplicação que testa resiliência com uso do Istio

## Utilizar as variáveis de ambiente:

- ENV_MY_CONTEXT_PATH
- ENV_DST_REQUEST
- ENV_FORWARD

#
## Construindo a imagem

- docker build -t nome_da_imagem:tag_da_imagem. --no-cache


#
## Executando um container a partir da imagem

- docker run -d -p 8080:8080 nome_da_imagem:tag_da_imagem