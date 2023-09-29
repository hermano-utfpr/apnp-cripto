# Lista de Exercícios 09

Acompanhe as videoaulas APNP 09 na [Playlist](https://www.youtube.com/playlist?list=PL4ySOdUYDU9AnsLbtvt7Mq3yBtnMT0Fog).

*Obs: esta lista de exercícios contém informações que podem ser meramente ilustrativas.*

**Exercício 1**

Qual dos arquivos de parâmetros de Diffie-Hellman abaixo contém o seguinte número primo?

```
00:d7:83:ad:2c:3b:30:50:51:ad:ed:65:ee:00:01:
91:87:f9:50:05:b7:d7:5e:3b:68:7f:70:c8:cc:2e:
54:ec:be:3d:cb:28:c8:b1:6a:80:37:ac:de:19:f1:
e3:97:1c:32:5f:84:1c:c9:c8:cf:91:6a:1f:34:c8:
dc:bb:d6:92:73
```

a) [dhpE.pem](dhpE.pem)

b) [dhpB.pem](dhpB.pem)

c) [dhpA.pem](dhpA.pem)

d) [dhpC.pem](dhpC.pem) 

e) [dhpD.pem](dhpD.pem)

**Exercício 2**

Qual conjunto de chaves possui a seguinte chave privada de Diffie-Hellman?

```
69:b4:2a:18:5c:07:ba:f5:e8:58:3e:3b:2f:7d:7f:
15:47:1e:8f:c6:1f:f3:da:75:32:a9:e0:88:75:ac:
12:1b
```

a) [chaves1.pem](chaves1.pem)

b) [chaves2.pem](chaves2.pem)

c) [chaves3.pem](chaves3.pem)

d) [chaves4.pem](chaves4.pem)

e) [chaves5.pem](chaves5.pem) 

**Exercício 3**

Quais chaves Diffie-Hellman não foram geradas com os parâmetros abaixo?

[dhparam.pem](dhparam.pem)

a) [chavesA.pem](chavesA.pem)

b) [chavesB.pem](chavesB.pem)

c) [chavesE.pem](chavesE.pem)

d) [chavesD.pem](chavesD.pem)

e) [chavesC.pem](chavesC.pem)

**Exercício 4**

Qual será a chave simétrica resultante da combinação Diffie-Hellman das chaves de João e Maria?

Chaves de João: [joao_chaves.pem](joao_chaves.pem)

Chaves de Maria: [maria_chaves.pem](maria_chaves.pem)

a) 2d4e35b3

b) 28e7676d

c) 53b9d03f

d) 3d5f1e5e

e) 126a9889

**Exercício 5**

Descubra qual é o conteúdo do arquivo:

[resultado.aes](resultado.aes)

Dicas:

Algoritmo: AES

Modo de Cifra: Eletronic Code Book

Base64: Sim

Salt: Não

Chave Simétrica: (via Diffie-Hellman)

Chaves Diffie-Hellman:

TSE: [tse_priv.pem](tse_priv.pem) 

TRE: [tre_pub.pem](tre_pub.pem)

a) Resultados das Eleições no Rio Grande do Sul

b) Resultados das Eleições no Rio de Janeiro

c) Resultados das Eleições em São Paulo

d) Resultados das Eleições em Minas Gerais

e) Resultados das Eleições no Paraná

f) Resultados das Eleições no Espírito Santo

g) Resultados das Eleições em Santa Catarina

**Exercício 6**

Qual é a chave pública Diffie-Hellman contida no arquivo abaixo?

[chaves.pem](chaves.pem)

a)

```
-----BEGIN PUBLIC KEY-----
MIIBIDCBlQYJKoZIhvcNAQMBMIGHAoGBAOempIeV7J7ObZDvWawDKULuN294skLi
dLOTgtEzxpVeiktzV6IQv7mWDGP8T9c7OnAoSpU/FuSTlJFjoYOLXNjbbYQzEhNK
jfqRXyI7nhW4v5XPELC3jZYJU4gWWsYaxQi/JhiPJeOFWGI90GLdKmb9RRQqHrXU
lDDWGWWsQRnjAgECA4GFAAKBgQDjv1tmIAOtCQZOF64l3njL0TZU1a9RG2EQN25n
fnXuF2p971hxpCdBi5N4/YlNkMoVDHcrh3MnMY9dhnEXNfB7nVe2HCzys3qZ+HSa
MdeUsPS1UqJv1VSbpr4Lq3rgpxalRPtNrssF8y+ri6FFx73KuD7TzvAU6vhMZubP
QbKBmQ==
-----END PUBLIC KEY-----
```

b)

```
-----BEGIN PUBLIC KEY-----
MIIBIDCBlQYJKoZIhvcNAQMBMIGHAoGBAOempIeV7J7ObZDvWawDKULuN294skLi
dLOTgtEzxpVeiktzV6IQv7mWDGP8T9c7OnAoSpU/FuSTlJFjoYOLXNjbbYQzEhNK
jfqRXyI7nhW4v5XPELC3jZYJU4gWWsYaxQi/JhiPJeOFWGI90GLdKmb9RRQqHrXU
lDDWGWWsQRnjAgECA4GFAAKBgQCg8xZHasARbQISCPCutc0MxsafAQn2KrdRSpeY
+YYCmV16nwbVpi12xa66GrKJZ4PFn6p8s72XKdXLDskdjUqvft6QXMqGmXYbn8hV
pwikw45tiYR+yqGwjZqoEVr8H7NVs/k1f0SfY2ud+AHruZGMCfb52EVKX1tv8ekC
esl3Xw==
-----END PUBLIC KEY-----
```

c)

```
-----BEGIN PUBLIC KEY-----
MIIBHzCBlQYJKoZIhvcNAQMBMIGHAoGBAOempIeV7J7ObZDvWawDKULuN294skLi
dLOTgtEzxpVeiktzV6IQv7mWDGP8T9c7OnAoSpU/FuSTlJFjoYOLXNjbbYQzEhNK
jfqRXyI7nhW4v5XPELC3jZYJU4gWWsYaxQi/JhiPJeOFWGI90GLdKmb9RRQqHrXU
lDDWGWWsQRnjAgECA4GEAAKBgFV2xHenGZ0klp8VYlfRhwQBtpg8NEqbLBzTuA9S
Q5SBWrXY2PoSfSElhchqM5BV2BusaCg4/W90bTxXTeXptpvkG8s46nlVCQpr8uZL
EsflPf5af3s4YrSiHdjD9+T27xa0ViO503YeWXxqTDexZvhM9hxIWRL+f2z4K8+B
UOc9
-----END PUBLIC KEY-----
```

d)

```
-----BEGIN PUBLIC KEY-----
MIIBHzCBlQYJKoZIhvcNAQMBMIGHAoGBAOFQtTFPp1nnDDjRinv/0Ch/9jlwfIry
9ZzlyWEbShOReKadJ9EHWO7BpNGPMkSqQ+2qOVdjrIAomUgofbKiKV4IBS4K4djQ
EHi5SP/HWyT6q/ph5GF16aODEui+tsSEpBzlpKipyJ4YmxXdqqzS7+lpurgR+Y1G
ZHW7OImjGCHrAgECA4GEAAKBgF1OlNRGO93FRM7kxPYQOesN18gLROOe0P1MjdT9
HBtjcqyW2GNY9xyyMEZtmhjd6336U5xb2suRRsBxZkjOjArfSJ9WU7MbmlUr51pR
rEt390oDfp1cx1GWLOwzlN4p1FpIwGNzOa8o+n0auF8AayGG5YGRAyddpF/cuE44
xbtt
-----END PUBLIC KEY-----
```

e)

```
-----BEGIN PUBLIC KEY-----
MIIBHzCBlQYJKoZIhvcNAQMBMIGHAoGBAKKHskNU0aaB2hFJcMzD0LuYNgwQ3sjo
QsvESwjG5F9w5mvbLPJ//JO/bCFoOmCluuiT1ex+STkaE9y4CGYsy93X0QGeXsG9
0uspJ++/el6AEsJnlhYRvV/xRo0kpYuwjvGlzziwRe943Q4umVJ1VnykXbk/1HwV
+llsG6uzKZfTAgECA4GEAAKBgHiB2kqgeIDh+fvsRsVVHb+irPpz9W/oDH5cril+
67DbJmqlp1UXVXWmCK/Z7aK/QO/dRlhekQ7DsEr5s2pQCtFZdRzEvxn+yykHvoLw
FLdwu2OKC5IK5K5hAtoFayPY5yBcUmTB5ZIpD6LRIQNSzL+evZr5BNDaeM+sUJ6+
7+Qc
-----END PUBLIC KEY-----
```

**Exercício 7**

Descriptografe o código abaixo:

[code.aes](code.aes)

Dicas:
Algoritmo: AES
Tamanho da Chave: 256
Modo de cifra: Eletronic Code Book
Base64: Sim
Salt: Não
Chave: (via Diffie-Hellman)

Chaves Diffie-Hellman:

Programador 1: [programmer_one.pem](programmer_one.pem)

Programador 2: [programmer_two.pem](programmer_two.pem)

Descubra: qual a linguagem da codificação do código que foi criptografado?

a) ![](ruby.jpg)

b) ![](java.jpg)

c) ![](perl.jpg)

d) ![](php.jpg)

e) ![](python.jpg)

<details><summary></summary>

Respostas:

1 - b)

2 - c)

3 - d)

4 - e)

5 - g)

6 - e)

7 - c)
</details>

