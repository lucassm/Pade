---
layout: page
title: Enviando Objetos
categories: docs
permalink: /docs/enviando-objetos/
---

Nem sempre o que é preciso enviar para outros agentes pode ser representado por texto simpes não é mesmo!
Para enviar objetos encapsulados no content de mensagens FIPA-ACL com PADE basta utilizar o módulo nativo do Python `pickle`, usando:

```python
import pickle
``` 

`pickle` é uma biblioteca para serialização de objetos, assim, para serializar um objeto qualquer, utilize `pickle.dumps()`, veja:

```python
dados = {'nome' : 'agente_consumidor', 'porta' : 2004}
dados_serial = pickle.dumps(dados)
message.set_content(dados_serial)
```

Pronto! O objeto já pode ser enviado no conteúdo da mensagem. Agora para receber o objeto, basta carregá-lo utilizando o comando:

```python
dados_serial = message.content
dados = pickle.loads(dados_serial)
```

Simples assim ;)