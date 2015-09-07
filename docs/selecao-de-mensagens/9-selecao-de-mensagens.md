---
layout: post
title: Seleção de mensagens
description: Criando e configurando filtros com mensagens no PADE 
categories: docs
permalink: /docs/selecao-de-mensagens/
---

Com PADE é possível implementar filtros de mensagens de maneira simples e direta, por meio da classe Filtro:

```Python
from pade.acl.filters import Filter
```

Por exemplo para a seguinte mensagem:

```Python
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

message = ACLMessage(ACLMessage.INFORM)
message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
message.set_sender(AID('remetente'))
message.add_receiver(AID('destinatario'))
```

Podemos criar o seguinte filtro:

```Python
from pade.acl.filters import Filter

f.performative = ACLMessage.REQUEST
```

Em uma sessão IPython é possível observar o efeito da aplicação do filtro sobre a mensagem:

```Python
In [12]: f.filter(message)
Out[12]: False
```

Ajustando agora o filtro para outra condição:

```Python
f.performative = ACLMessage.INFORM
```

E aplicando o filtro novamente sobre a mensagem, obtemos um novo resultado:

```Python
In [14]: f.filter(message)
Out[14]: True
```
