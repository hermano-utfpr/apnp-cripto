# Lista de Exercícios 11

Acompanhe as videoaulas APNP 11 na [Playlist](https://www.youtube.com/playlist?list=PL4ySOdUYDU9AnsLbtvt7Mq3yBtnMT0Fog).

**Exercício 1**

Maurício de Souza assinou digitalmente uma figura [assinatura.sha1.sign](assinatura.sha1.sign). Qual figura ele assinou conhecendo sua chave pública [mauricio.pub.pem](mauricio.pub.pem)?

a) ![](cascao.png)

b) ![](cebolinha.png)

c) ![](monica.png)

d) ![](bidu.png)

e) ![](magali.png)

**Exercício 2**

Quem assinou digitalmente o documento abaixo?

Documento: [proverbio.rtf](proverbio.rtf)

Assinatura: [proverbio.rtf.sha256.sign](proverbio.rtf.sha256.sign)

a) Saul - [pub-saul.pem](pub-saul.pem)

b) Josué - [pub-josue.pem](pub-josue.pem)

c) Davi - [pub-davi.pem](pub-davi.pem)

d) Salomão - [pub-salomao.pem](pub-salomao.pem)

e) Moisés - [pub-moises.pem](pub-moises.pem)

**Exercício 3**

Chaplin assinou digitalmente a figura abaixo com sua chave privada:

![](chaplin.gif)

[chaplin.priv.pem](chaplin.priv.pem)

Qual é a assinatura correta?

a) [chaplin.A.gif.sha1.sign](chaplin.A.gif.sha1.sign)

b) [chaplin.B.gif.sha1.sign](chaplin.B.gif.sha1.sign)

c) [chaplin.C.gif.sha1.sign](chaplin.C.gif.sha1.sign)

d) [chaplin.D.gif.sha1.sign](chaplin.D.gif.sha1.sign)

e) [chaplin.E.gif.sha1.sign](chaplin.E.gif.sha1.sign)

**Exercício 4**

Paulo mandou uma mensagem assinada digitalmente. Porém vieram várias mensagens. Qual delas é a original?

Chave pública de Paulo: [paulo.pub.pem](paulo.pub.pem)

a)
[msg1.txt](msg1.txt)

[msg1.txt.md5.sign](msg1.txt.md5.sign)

b)
[msg2.txt](msg2.txt)

[msg2.txt.md5.sign](msg2.txt.md5.sign)

c)
[msg3.txt](msg3.txt)

[msg3.txt.md5.sign](msg3.txt.md5.sign)

d)
[msg4.txt](msg4.txt)

[msg4.txt.md5.sign](msg4.txt.md5.sign)

e)
[msg5.txt](msg5.txt)

[msg5.txt.md5.sign](msg5.txt.md5.sign)

**Exercício 5**

A UEFA assinou digitalmente a foto abaixo:

![](liverpool.jpeg)

Descubra qual foi o algoritmo de hash utilizado sabendo o seguinte:

Assinatura: [liverpool.uefa.sign](liverpool.uefa.sign)

Chave da UEFA: [uefa.pem](uefa.pem)

a) MD5

b) SHA1

c) SHA224

d) SHA256

e) SHA384

f) SHA512

Exercício 6

Utilize a seguinte chave privada para assinar com SHA256 a bandeira do Brasil:

[brasileiro.pem](brasileiro.pem)

![](brasil.jpg)

Qual é o HASH MD5 do arquivo resultante dessa assinatura digital?

a) 07bcec78fd8d46cdc9e2b70846d05fc3

b) 09d29263fe5d53e2326a1539b56c03ef

c) 6a68c31e4718ebeb9b2a0376563547f4

d) fc2122a28cabd9e064640e5a0fae5b7d

e) d6841870c1fba5b062892702ec7a7315

**Exercício 7**

Gere uma nova chave RSA de 2048 bits e assine digitalmente com SHA512 o documento abaixo:

[informational-booklet.pdf](informational-booklet.pdf)

Qual será o tamanho do arquivo com a assinatura resultante?

a) 512 bytes

b) 2048 bytes

c) 1024 bytes

d) 128 bytes

e) 256 bytes

f) 64 bytes

g) 32 bytes

**Exercício 8**

Um fornecedor recebeu diversos pedidos de seu cliente. Cada pedido veio assinado digitalmente pelo cliente. Porém o fornecedor percebeu que um pedido foi modificado sem autorização. Qual?

Chave pública do cliente: [cliente.pub.pem](cliente.pub.pem)

a)
[pedido2.txt](pedido2.txt)

[pedido2.txt.sha1.sign](pedido2.txt.sha1.sign)

b)
[pedido5.txt](pedido5.txt)

[pedido5.txt.sha1.sign](pedido5.txt.sha1.sign)

c)
[pedido1.txt](pedido1.txt)

[pedido1.txt.sha1.sign](pedido1.txt.sha1.sign)

d)
[pedido4.txt](pedido4.txt)

[pedido4.txt.sha1.sign](pedido4.txt.sha1.sign)

e)
[pedido3.txt](pedido3.txt)

[pedido3.txt.sha1.sign](pedido3.txt.sha1.sign)

<details><summary></summary>

Respostas:

1 - e

2 - d

3 - e

4 - b

5 - e

6 - c

7 - e

8 - c
</details>

