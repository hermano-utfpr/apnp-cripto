# Lista de Exercícios 13

Acompanhe as videoaulas APNP 13 na [Playlist](https://www.youtube.com/playlist?list=PL4ySOdUYDU9AnsLbtvt7Mq3yBtnMT0Fog).

*Obs: esta lista de exercícios contém informações que podem ser meramente ilustrativas.*

Sugestão: resolva estes exercícios com a ferramenta OpenSSL.

**Exercício 1**

Verifique o arquivo abaixo e responda:

[puc.pem](puc.pem)

a) É uma requisição de certificado com a chave/assinatura RSA+SHA1

b) É uma requisição de certificado com a chave/assinatura RSA+SHA256

c) É uma requisição de certificado com a chave/assinatura DSA+SHA256

d) É uma requisição de certificado com a chave/assinatura DSA+SHA1

e) É um certificado auto-assinado com a chave/assinatura RSA+SHA1

f) É um certificado auto-assinado com a chave/assinatura RSA+SHA256

g) É um certificado auto-assinado com a chave/assinatura DSA+SHA256

h) É um certificado auto-assinado com a chave/assinatura DSA+SHA1

**Exercício 2**

Qual(is) certificado(s) é(são) auto-assinado(s)?

[ford_a.pem](ford_a.pem)

[ford_b.pem](ford_b.pem)

[ford_c.pem](ford_c.pem)

a) Somente ford_a.pem e ford_b.pem

b) Somente ford_c.pem

c) Somente ford_b.pem

d) Somente ford_a.pem

e) ford_b.pem e ford_c.pem

f) ford_a.pem e ford_b.pem

**Exercício 3**

Este é o fingerprint de um certificado digital:

SHA224 Fingerprint=
29:BB:C2:F7:66:A9:42:F6:37:5F:60:45:7A:00:
CA:C0:9A:49:4E:42:06:6A:0E:53:6D:DF:14:46

Estes são os certificados:

[cert_A.pem](cert_A.pem)

[cert_B.pem](cert_B.pem)

[cert_C.pem](cert_C.pem)

[cert_D.pem](cert_D.pem)

[cert_E.pem](cert_E.pem)

Responda: a qual estado pertence o certificado?

a) MG

b) SC

c) RJ

d) PR

e) RS

f) SP

**Exercício 4**

Qual dos certificados tem a validade (duração) de aproximadamente de 5 anos?

[cert1.pem](cert1.pem)

[cert2.pem](cert2.pem)

[cert3.pem](cert3.pem)

[cert4.pem](cert4.pem)

[cert5.pem](cert5.pem)

a) Certificado da Agrária

b) Certificado da Cidade dos Lagos

c) Certificado do Prefeitura

d) Certificado do Superpão

e) Certificado da Repinho

**Exercício 5**

Qual é a chave pública correspondente a que está no certificado abaixo?

[it_cert.pem](it_cert.pem)

a)

```
-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAL+zJJCKoc1G2gjlHM8p7vfdpOdeibbv
DmUQWrM9fZpcnHjttHnv4CYffj2KPg5UxqrI2utDGy/kS3mL/ZoPVCUCAwEAAQ==
-----END PUBLIC KEY-----
```

b)

```
-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAOUBFHL6kNRzcFKpyG8K/fPauIYwNyX7
iEEVFm28CN/ruUqdSUJeTtl4Fk4IwPG/m8sGzyx6MUmQYDmFyIEK6zMCAwEAAQ==
-----END PUBLIC KEY-----
```

c)

```
-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMY/RlvGZUyh/rCXyahEAgptIaQ3PT/k
oHN6qcxbZO13KL0pJpXkgRB0xQtW8mpwla2k8cLKMWa0Vc7eZo3oJwcCAwEAAQ==
-----END PUBLIC KEY-----
```

d)

```
-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMIWhBayquTcojzaBcSWCdgQ+9hRu0U6
Gl6XUDECn4BtuKw2oFM4Blv2fOhXmgQEocMg55yLnl6dgsuIZidsegMCAwEAAQ==
-----END PUBLIC KEY-----
```

e)

```
-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAL7iG7JmQ8nY0G8HW60kAu1Kg62Yipxf
vshDorO1Sa9+juQDD9vEBtQ6CP8J/ReFCjg82jzlLspWRg6llkjkmx0CAwEAAQ==
-----END PUBLIC KEY-----
```

**Exercício 6**

Qual dos certificados abaixo não é auto-assinado?

a) [m1.pem](m1.pem)

b) [m2.pem](m2.pem)

c) [m3.pem](m3.pem)

d) [m4.pem](m4.pem)

e) [m5.pem](m5.pem)

**Exercício 7**

Qual das figuras foi assinada com a chave privada da Cogeti?

Certificado: [cogeti.pem](cogeti.pem)

Assinatura da figura: [fig.sign.sha256.dsa](fig.sign.sha256.dsa)

a) ![](fig1.jpeg)

b) ![](fig2.jpeg)

c) ![](fig3.png)

d) ![](fig4.png)

<details><summary></summary>

Respostas:

1 - c

2 - c

3 - f

4 - a

5 - a

6 - c

7 - b
</details>
