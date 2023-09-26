# Lista de Exercícios 14

Acompanhe as videoaulas APNP 14 na [Playlist](https://www.youtube.com/playlist?list=PL4ySOdUYDU9AnsLbtvt7Mq3yBtnMT0Fog).

Sugestão: resolva utilizando a ferramenta OpenSSL.

*Obs: alguns certificados expiraram, mas ainda são úteis nesta atividade.*

**Exercício 1**

O certificado abaixo possui uma chave pública. Encontre a chave e verifique se é uma chave DSA ou RSA!

[submarino.pem](submarino.pem)

a) Chave DSA:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm+HVMaQI0oA2tIQvLcEd
qek40wP/NWk4bQYTlaY2aP0UZ7eGalcPxrpwrDxck5yKB8SXJUb1lPuXFfFnbITE
0EjW6NyMKJ8VAFL2A22G7Hvh5T3nz7b00SpeZ+Fzl9Hffj5z2skUkuejA1uY6qEG
rxEcvNUnWxXTrd4/AfYGB9VyYIQPTkssy6W/449G8pN4fMAJ3+bvsLvK1FnKcgRE
AO6xQ/FgPYrgchTHfYrQ01SDrbX/aTm2ZHKvAT1g9m91PwKb+Fm+aiMV7vrb/2Lx
w7w2HaHDVNLpfawriQYzYHPf/b1LRORVE3CPBWAYAe7JWJzNNsx9ZliqsT0PsKRA
jQIDAQAB
-----END PUBLIC KEY-----
```

b) Chave DSA:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8G72RMtN5753/r1n3NYT
T7up9dnVjZ8+OQsrsSn29CwVAsCcrEkBgax/ZXBeAspGgM3bKbI7FaOfURNNxx3K
e4f3pI6nepuQ2Pa12/e3Ln5ozz5bCV0yZpl5hcXaTOLR4Y1gqygsuq5hg11nGNhK
EBKUfv+Xk9zYvY8gVdAuH/iTXi7BKox9IKTx3NU6zBqs7qLx4Dks1yoZT6M0Cvzv
djRhTeoJSvqt0/O9q5bnI9fm88Pzo0lfeCdsGfokGZMupICQLXC+4jKN4yHQ2dA1
e2tIWcQrYOkqivTcXOBwCPfPh9tfc7aSo+yHBVgwr1GWnaouMNAMe1daB3Y3brMQ
VwIDAQAB
-----END PUBLIC KEY-----
```

c) Chave RSA:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr+qOclW3FbAB4Og7n8gP
0b7MOZCJwVOHXZqYFfp/+9ugwrPB+uWtIyswGp7Y+Ez9cNZ3uB8yM7PiLZb6+NR0
V+9kQdY4Qt7hxH5RQlMtatggsfK5mx15itMfAtOok1TS6HS08BMZ+PScWROurZpz
NVFXhj5PKpM+3cDJ1LINSxggvajVcKUt01/kGUtd+NFQDTqAp7wNq3MRRuHLy+/I
uqLM4k7spfPV++mLhlzNs1ppMU8cIy7dPVbfrOWSD8gs/bJyy90W+0R2TGinUWN/
FfF1KmKz+bZw1Rrm53kCoFLiEovxP0IPv0szL7B/f/SHveQICq8EFG0mQlrfMxAo
swIDAQAB
-----END PUBLIC KEY-----
```

d) Chave RSA:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8G72RMtN5753/r1n3NYT
T7up9dnVjZ8+OQsrsSn29CwVAsCcrEkBgax/ZXBeAspGgM3bKbI7FaOfURNNxx3K
e4f3pI6nepuQ2Pa12/e3Ln5ozz5bCV0yZpl5hcXaTOLR4Y1gqygsuq5hg11nGNhK
EBKUfv+Xk9zYvY8gVdAuH/iTXi7BKox9IKTx3NU6zBqs7qLx4Dks1yoZT6M0Cvzv
djRhTeoJSvqt0/O9q5bnI9fm88Pzo0lfeCdsGfokGZMupICQLXC+4jKN4yHQ2dA1
e2tIWcQrYOkqivTcXOBwCPfPh9tfc7aSo+yHBVgwr1GWnaouMNAMe1daB3Y3brMQ
VwIDAQAB
-----END PUBLIC KEY-----
```

e) Chave DSA:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr+qOclW3FbAB4Og7n8gP
0b7MOZCJwVOHXZqYFfp/+9ugwrPB+uWtIyswGp7Y+Ez9cNZ3uB8yM7PiLZb6+NR0
V+9kQdY4Qt7hxH5RQlMtatggsfK5mx15itMfAtOok1TS6HS08BMZ+PScWROurZpz
NVFXhj5PKpM+3cDJ1LINSxggvajVcKUt01/kGUtd+NFQDTqAp7wNq3MRRuHLy+/I
uqLM4k7spfPV++mLhlzNs1ppMU8cIy7dPVbfrOWSD8gs/bJyy90W+0R2TGinUWN/
FfF1KmKz+bZw1Rrm53kCoFLiEovxP0IPv0szL7B/f/SHveQICq8EFG0mQlrfMxAo
swIDAQAB
-----END PUBLIC KEY-----
```

f) Chave RSA:

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm+HVMaQI0oA2tIQvLcEd
qek40wP/NWk4bQYTlaY2aP0UZ7eGalcPxrpwrDxck5yKB8SXJUb1lPuXFfFnbITE
0EjW6NyMKJ8VAFL2A22G7Hvh5T3nz7b00SpeZ+Fzl9Hffj5z2skUkuejA1uY6qEG
rxEcvNUnWxXTrd4/AfYGB9VyYIQPTkssy6W/449G8pN4fMAJ3+bvsLvK1FnKcgRE
AO6xQ/FgPYrgchTHfYrQ01SDrbX/aTm2ZHKvAT1g9m91PwKb+Fm+aiMV7vrb/2Lx
w7w2HaHDVNLpfawriQYzYHPf/b1LRORVE3CPBWAYAe7JWJzNNsx9ZliqsT0PsKRA
jQIDAQAB
-----END PUBLIC KEY-----
```

**Exercício 2**

Qual dos certificados abaixo é do Banco Bradesco?

a) [banco5.pem](banco5.pem)

b) [banco4.pem](banco4.pem)

c) [banco3.pem](banco3.pem)

d) [banco2.pem](banco2.pem)

e) [banco1.pem](banco1.pem)

**Exercício 3**

Quem assinou o certificado abaixo?

[certificado.pem](certificado.pem)

Empresas:

[empresa1.pem](empresa1.pem)

[empresa2.pem](empresa2.pem)

[empresa3.pem](empresa3.pem)

[empresa4.pem](empresa4.pem)

[empresa5.pem](empresa5.pem)

Responda:

a) Amazon

b) Americanas

c) Casas Bahia

d) Magazine Luiza

e) Pernambucanas

f) O certificado é auto-assinado.

**Exercício 4**

Quem assinou o texto abaixo?

[texto.txt](texto.txt)

[texto.txt.sign](texto.txt.sign)

Dica: texto foi assinado com SHA256.

a) [cert_ana.pem](cert_ana.pem)

b) [cert_joao.pem](cert_joao.pem)

c) [cert_maria.pem](cert_maria.pem)

d) [cert_paulo.pem](cert_paulo.pem)

e) [cert_pedro.pem](cert_pedro.pem)

**Exercícios 5**

Os seguintes certificados completam uma cadeia de autoridades que assinaram o certificado "spark.pem", certificado criado pelo Sr. Peterson Medeiros.

Tais certificados serviram para o acesso seguro a um site hospedado na UTFPR-GP em 2019, portanto alguns já expiraram.

Certificados das Autoridades:

[icpedu.pem](icpedu.pem)

[gstrusted.pem](gstrusted.pem)

[gsroot.pem](gsroot.pem)

Certificado:

[spark.pem](spark.pem)

Descubra qual foi a ordem correta em que ocorreram as assinaturas:

a)

1o) ICP Edu assinou GS Root

2o) GS Root assinou GS Trusted

3o) GS Trusted assinou Spark

b)

1o) GS Trusted assinou GS Root

2o) GS Root assinou ICP Edu

3o) ICP Edu assinou Spark

c)

1o) ICP Edu assinou GS Trusted

2o) GS Trusted assinou GS Root

3o) GS Root assinou Spark

d)

1o) GS Trusted assinou ICP Edu

2o) ICP Edu assinou GS Root

3o) GS Root assinou Spark

e)

1o) GS Root assinou ICP Edu

2o) ICP Edu assinou GS Trusted

3o) GS Trusted assinou Spark

f)

1o) GS Root assinou GS Trusted

2o) GS Trusted assinou ICP Edu

3o) ICP Edu assinou Spark

**Exercício 6**

Qual dos certificados não foi assinado por esta autoridade certificadora?

Certificado da autoridade: [br.pem](br.pem)

a) [pr.pem](pr.pem)

b) [rj.pem](rj.pem)

c) [rs.pem](rs.pem)

d) [sc.pem](sc.pem)

e) [sp.pem](sp.pem)

**Exercício 7**

Qual certificado de autoridade assinou o certificado abaixo?

[loja2021.pem](loja2021.pem)

a) [havan1.pem](havan1.pem)

b) [havan2.pem](havan2.pem)

c) [havan3.pem](havan3.pem)

d) [havan4.pem](havan4.pem)

e) [havan5.pem](havan5.pem)

**Exercício 8**

Qual certificado é capaz de confirmar a assinatura do arquivo abaixo?

[signed.txt](signed.txt)

[signature.bin](signature.bin)

E, também, de confiança da autoridade certificadora abaixo?

[verisign.pem](verisign.pem)

a) Argentina: [c_ar.pem](c_ar.pem)

b) Brasil: [c_br.pem](c_br.pem)

c) Paraguai: [c_py.pem](c_py.pem)

d) Uruguai: [c_ur.pem](c_ur.pem)

<details><summary></summary>

Respostas:

1 c

2 b

3 c

4 b

5 f

6 b

7 c

8 c
</details>


