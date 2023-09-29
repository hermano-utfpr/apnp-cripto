# Lista de Exercícios 10

Acompanhe as videoaulas APNP 10 na [Playlist](https://www.youtube.com/playlist?list=PL4ySOdUYDU9AnsLbtvt7Mq3yBtnMT0Fog).

*Obs: esta lista de exercícios contém informações que podem ser meramente ilustrativas.*

**Exercício 1**

Os seguintes números primos estão presentes em qual chave RSA?

```
prime1:
    00:e7:31:b2:f3:ec:ce:e8:2a:39:4f:f7:39:e4:8e:
    7d:c7:33:2a:a3:01:ec:23:bc:d9:00:e9:4d:cc:ac:
    d7:ef:fd
```

```
prime2:
    00:e3:a5:a8:76:9b:80:88:e7:15:45:85:bd:0d:b5:
    eb:62:d9:4e:63:25:7c:5d:c7:7b:ff:eb:11:f3:7a:
    25:a1:51
```

a) [privada1.pem](privada1.pem)

b) [privada3.pem](privada3.pem)

c) [privada4.pem](privada4.pem)

d) [privada2.pem](privada2.pem)

e) [privada5.pem](privada5.pem)

**Exercício 2**

Descubra qual é a minha chave pública:

[minha_chave_privada.pem](minha_chave_privada.pem)

a)

```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhANdQT9J/PVJcYzuraS9aTDeabxdfDoTn
1yv+ImbfEM2DAgMBAAE=
-----END PUBLIC KEY-----
```

b)

```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAL+nZ6SUJxqryCFXo1CRrMOg/ry4EnbL
KY00fSFR4IEBAgMBAAE=
-----END PUBLIC KEY----
```

c)

```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKAHB+ye5G0AzCTAcY1E1GR+YM4GTZG5
A4RroBcuqVtbAgMBAAE=
-----END PUBLIC KEY-----
```

d)

```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKAHSZqYhCak9CnLewCgfU0tpcXuJ3p1
KVT+gEvCD2i5AgMBAAE=
-----END PUBLIC KEY-----
```

e)

```
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKFpUL0HoOeu0ciQSehHlO5Dunt7sMrz
PD0ph+6oywYjAgMBAAE=
-----END PUBLIC KEY-----
```

**Exercício 3**

Alice criptografou uma mensagem secreta usando a chave pública de Bob. Charles conseguiu salvar a mensagem criptografada em RSA e na sequência conseguiu a chave privada de Bob em um pendrive que foi extraviado.

Chaves encontradas por Charles:

[ninguempodesaber.pem](ninguempodesaber.pem)

[todospodemsaber.pem](todospodemsaber.pem)

Mensagem criptografada e capturada por Charles:

[mensagem.txt.rsa](mensagem.txt.rsa)

Qual era a mensagem secreta?

a) O Charles vai receber aumento de salario.

b) Estou desconfiada que o Charles sabe tudo.

c) Amanha entrego a carta de demissao do Charles.

d) Vamos fazer festa surpresa para o Charles.

e) O Charles nao pode saber sobre isso.

**Exercício 4**

Uma figura foi criptografada usando chave pública. Descubra qual é a figura descriptografando com a chave privada que está protegida com a senha "cachorro"!

[chaveprivada.pem](chaveprivada.pem)

[icone.gif.rsa](icone.gif.rsa)

a) ![](icone5.png)

b) ![](icone2.gif)

c) ![](icone1.gif)

d) ![](icone3.gif)

e) ![](icone4.gif)

**Exercício 5**

O arquivo abaixo contém o logo de um sistema operacional:

[so.aes-128-ecb.b64.nosalt](so.aes-128-ecb.b64.nosalt)

Este arquivo pode ser decifrado com a chave simétrica abaixo:

[chave.bin.rsa](chave.bin.rsa)

E a chave simétrica pode ser decifrada com uma das chaves assimétricas:

[chave_priv.pem](chave_priv.pem)

[chave_pub.pem](chave_pub.pem)

Qual é o sistema operacional?

a) Debian

b) FreeBSD

c) MS Windows

d) OpenBSD

e) Ubuntu

**Exercício 6**

O arquivo texto abaixo foi criptografado usando uma chave pública RSA:

[loucos.txt.rsa](loucos.txt.rsa)

Quem poderá descriptografar?

a) Paulo: [paulo.priv.pem](paulo.priv.pem)

b) Marcos: [marcos.priv.pem](marcos.priv.pem)

c) Lucas: [lucas.priv.pem](lucas.priv.pem)

d) Mateus: [mateus.priv.pem](mateus.priv.pem) 

e) Tiago: [tiago.priv.pem](tiago.priv.pem)

**Exercício 7**

Criptografe a imagem abaixo com o algoritmo RSA:

![](happy.gif)

Utilize a chave pública que pode ser extraída de:

[happy_priv.pem](happy_priv.pem)

Qual será o tamanho do arquivo resultante?

a) 32 bits

b) 512 bits

c) 4096 bits

d) 1024 bits

e) 128 bits

f) 2048 bits

g) 256 bits

**Exercício 8**

Qual brasão foi criptografado no arquivo abaixo?

[fut-brasao.aes-128-ecb-nosalt](fut-brasao.aes-128-ecb-nosalt)

A chave simétrica está neste arquivo:

[fut-chave-simetrica.rsa](fut-chave-simetrica.rsa)

Esta é a chave privada para descriptografar a chave simétrica:

[fut-priv.pem](fut-priv.pem)

a) ![](fut-bot.png)

b) ![](fut-fla.png)

c) ![](fut-vas.png)

d) ![](fut-flu.png)

<details><summary></summary>

Respostas:

1 b)

2 e)

3 d)

4 b)

5 d)

6 a)

7 d)

8 a)
</details>

