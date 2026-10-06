# Robô Shopee 24h — versão inicial

Objetivo:
- selecionar produtos de forma aleatória;
- registrar produtos para não repetir imediatamente;
- enviar alertas para Telegram;
- ficar rodando 24h;
- deixar a integração com a fonte oficial de produtos/links de afiliado isolada em `shopee_adapter.py`.

IMPORTANTE:
Esta versão NÃO faz login por senha, não usa cookies da Shopee e não simula cliques.
A integração de produtos/links deve ser feita por uma API, ferramenta ou integração oficialmente permitida pela Shopee para a conta de afiliado.

## Como começar

1. Instale Python 3.11+.
2. Crie um bot no Telegram pelo @BotFather e obtenha o token.
3. Copie `.env.example` para `.env` e preencha o token e o chat ID.
4. Execute:
   `python main.py`

O robô atualmente usa `data/products_demo.json` para testar o fluxo.
Quando tivermos a forma oficial de obter produtos/links da Shopee para sua conta, substituímos apenas o adaptador.
