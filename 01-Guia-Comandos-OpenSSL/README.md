# Guia de Comandos - OpenSSL

Verificar a versão:

`$ openssl version -a`

Verificar comandos:

`$ openssl list-standard-commands`

`$ openssl -h`

------XXX Algoritmos de Hash/Digest XXX------

Verificar algoritmos de hash/digest:

`$ openssl list-message-digest-commands`

Executar um algoritmo de hash/digest:

`$ openssl [algoritmo] [arquivo]`
ex.:

`$ openssl md5 arquivo.txt`

`$ openssl sha1 artigo.pdf`

Verificar mais algoritmos e opções de  hash/digest:

`$ openssl dgst -h`

Executar mais algoritmos de hash/digest:

`$ openssl dgst -[opção] [arquivo]`

Ex.:

```
$ openssl dgst -sha512 arquivo.txt
$ openssl dgst -whirlpool -c artigo.pdf
$ echo -n abc123 | openssl md5
$ echo Frase | openssl dgst -sha256
```

------XXX Código de Autenticação de Mensagens XXX------

Executar OpenSSL com HMAC:

`$ openssl dgst -[função_hash] -hmac [chave_secreta] -out [arquivo_saida] [arquivo]`

ou

`$openssl dgst -[função_hash] -mac hmac -macopt hexkey:[chave_secreta_hexadecimal] -out [arquivo_saida] [arquivo]`

Ex.:

`$ openssl dgst -sha256 -hmac abc123 arquivo.txt`

ou

```
$ echo -n abc123 | xxd -p
$ openssl dgst -sha256 -mac hmac -macopt hexkey:616263313233 -out arquivo.hmac arquivo.txt
```

------XXX Algoritmos de Criptografia Simétrica XXX------

Verificar algoritmos de criptografia disponíveis:

`$ openssl list-cipher-commands`

Listar mais opções para encriptar:

`$ openssl enc -h`

Criptografar um arquivo com uma chave tipo senha:

`$ openssl enc -[algoritmo] -in [arquivo_entrada] -out [arquivo_saída]`

Ex.:

```
$ openssl enc -des -in arquivo.txt -out arquivo.des
$ openssl enc -aes-128-cbc -a -in artigo.pdf -out artigo.aes128cbc
```

Obs: "-a" irá aplicar a codificação base64.

Decriptografar um arquivo com chave tipo senha:

`$ openssl enc -d -[algoritmo] -in [arquivo_entrada] -out [arquivo_saída]`

Ex.:

```
$ openssl enc -d -des -in arquivo.des -out arquivo.txt
$ openssl enc -d -a -aes-128-cbc -in artigo.aes128cbc -out artigo.pdf
```

Utilizar senha na linha de comando:

`$ openssl enc [-d] -[algoritmo] -in [arquivo_entrada] -out [arquivo_saída] -pass pass:[senha]`

Ex.:

`$ openssl enc -aes-128-cbc -in arquivo.txt -out arquivo.aes -pass pass:abc123`

Verificar informações de Salt/Key/Initialization Vector:

`$ openssl enc -p [-d] -[algoritmo] -in [arquivo_entrada] -out [arquivo_saída]`

Ex.:

`$ openssl enc -p -aes-128-cbc -in arquivo.txt -out arquivo.aes`

Utilizar informações de Salt/Key/Initialization Vector:

`$ openssl enc [-d] -[algoritmo] -in [arquivo_entrada] -out [arquivo_saída] -S [salt] -K [key] -iv [iv]`

Ex.:

`$ openssl enc -aes-128-cbc -in arquivo.txt -out arquivo.aes -S 5414AAC54A956E60 -K B9BDA6658629D757E2BFD2209431613A -iv 33061F5E66296C3856452678893A239F`

Desativar opção de Salt: (use -nosalt)

`$ openssl enc [-d] -nosalt -[algoritmo] -in [arquivo_entrada] -out [arquivo_saída]`

Ex.:

`$ openssl enc -nosalt -aes-256-cbc -in arquivo.txt -out arquivo.aes`

------XXX Algoritmos de Chave Pública XXX------

1) Diffie-Hellman (troca de chaves)

Verificar opções:

`$ openssl dhparam -h`

Gerar parâmetros iniciais:

`$ openssl dhparam [bits] -out [arquivo_param]`

Ex.:

`alice/bob$ openssl dhparam 1024 -out comum.pem`

Obs: resultado em base64

Verificar p e g:

`$ openssl dhparam -in [arquivo_param] -text [-noout]`

Ex.:

`alice/bob$ openssl dhparam -in comum.pem -text`

Opções para gerar as chaves:

`$ openssl genpkey -h`

Gerar as chaves públicas e privadas:

`$ openssl genpkey -paramfile [arquivo_param] -out [arquivo_chaves]`

Ex.:

```
alice$ openssl genpkey -paramfile comum.pem -out alice_chaves.pem
bob$ openssl genpkey -paramfile comum.pem -out bob_chaves.pem
```

Verificar as chaves públicas, privadas, e os valores de p e g:

`$ openssl pkey -in [arquivo_chaves] -text [-noout]`

Ex.:

```
alice$ openssl pkey -in alice_chaves.pem -text
bob$ openssl pkey -in bob_chaves.pem -text
```

Extrair a chave pública:

`$ openssl pkey -in [arquivo_chaves] -pubout -out [arquivo_chave_publica]`

Ex.:

```
alice$ openssl pkey -in alice_chaves.pem -pubout -out alice_chave_pub.pem
bob$ openssl pkey -in bob_chaves.pem -pubout -out bob_chave_pub.pem
```

Verificar as chaves públicas:

`$ openssl pkey -in [arquivo_chave_publica] -pubin -text [-noout]`

Ex.:

```
alice$ openssl pkey -in alice_chave_pub.pem -pubin -text
bob$ openssl pkey -in bob_chave_pub.pem -pubin -text
```

Verificar opções úteis e buscar por geração de chaves simétricas:

`$ openssl pkeyutl -h`

Gerar a chave simétrica:

`$ openssl pkeyutl -derive -inkey [arquivo_chaves] -peerkey [arquivo_chave_publica] [-hexdump|-out arquivo_chave_sim]`

Ex.:

```
alice$ openssl pkeyutl -derive -inkey alice_chaves.pem -peerkey bob_chave_pub.pem -out chave_sim.bin
bob$ openssl pkeyutl -derive -inkey bob_chaves.pem -peerkey alice_chave_pub.pem -out chave_sim.bin
```

obs: verifique a chave simétrica com o comando xxd:

`alice/bob$ xxd -ps chave_sim.bin`

2) RSA (troca de chaves, criptografia assimétrica e assinatura)

Verificar opções:

```
$ openssl rsa -h
$ openssl genrsa -h
$ openssl rsautl -h
```

Gerar uma chave privada:

`$ openssl genrsa -out [arquivo_chave_privada] [bits]`

Ex.:

`bob$ openssl genrsa -out bob_chave_privada.pem 1024`

Verificar a chave privada:

`$ openssl rsa -in [arquivo_chave_privada] -text [-noout]`

Ex.:

`bob$ openssl rsa -in bob_chave_privada.pem -text`

Gerar uma chave pública a partir de uma chave privada:

`$ openssl rsa -in [arquivo_chave_privada] -pubout -out [arquivo_chave_publica]`

Ex.:

`bob$ openssl rsa -in bob_chave_privada.pem -pubout -out bob_chave_publica.pem`

Verificar a chave pública:

`$ openssl rsa -in [arquivo_chave_publica] -pubin -text [-noout]`

Ex.:

`bob$ openssl rsa -in bob_chave_publica.pem -pubin -text`

Criptografar com a chave pública:

`$ openssl rsautl -encrypt -pubin -inkey [arquivo_chave_publica] -in [arquivo.txt] -out [arquivo.rsa]`

Ex.:

`alice$ openssl rsautl -encrypt -pubin -inkey bob_chave_publica.pem -in mensagem_alice.txt -out mensagem_alice.rsa`

Descriptografar com a chave privada:

`$ openssl rsautl -decrypt -inkey [arquivo_chave_privada] -in [arquivo.rsa] -out [arquivo.txt]`

Ex.:

`bob$ openssl rsautl -decrypt -inkey bob_chave_privada.pem -in mensagen_alice.rsa`

Criptografar com a chave privada (ou assinatura):

`$ openssl rsautl -in [arquivo.txt|hash.txt] -inkey [arquivo_chave_privada] -out [arquivo.sign.rsa] -sign`

Ex.:

`bob$ openssl rsautl -in mensagem_bob.txt -inkey bob_chave_privada.pem -out mensagem_bob.sign.rsa -sign`

Descriptografar com a chave pública:

`$ openssl rsautl -in [arquivo.sign.rsa] -pubin -inkey [arquivo_chave_publica] -out [arquivo.txt|hash.txt]`

Ex.:

`alice$ openssl rsautl -in mensagem_bob_sign.rsa -pubin -inkey bob_chave_publica.pem`

Gerar uma assinatura digital com RSA:

`$ openssl [md5|sha1|shaN] -sign [arquivo_chave_privada] -out [assinatura.bin] [arquivo.txt]`

Ex.:

`bob$ openssl sha512 -sign bob_chave_privada.pem -out mensagem_bob.sign.rsa mensagem_bob.txt`

Verificar uma assinatura digital com RSA:

`$ openssl [md5|sha1|shaN] -verify [arquivo_chave_publica] -signature [assinatura.bin] [arquivo.txt]`

Ex.:

`alice$ openssl sha512 -verify bob_chave_publica.pem -signature mensagem_bob.sign.rsa mensagem_bob.txt`

3) DSA (assinatura)

Gerar parâmetros DSA:

`$ openssl dsaparam [bits] -out [arquivo_parametros]`

Ex.:

`alice$ openssl dsaparam 1024 -out dsa_param.pem`

Verificar os parâmetros DSA:

`$ openssl dsaparam -in [arquivo_parametros] -text [-noout]`

Ex.:

`alice$ openssl dsaparam -in dsa_param.pem -text`

Gerar as chaves DSA:

`$ openssl gendsa [arquivo_parametros] -out [arquivo_chave_privada]`

Ex.:

`alice$ openssl gendsa dsa_param.pem -out alice_priv.pem`

Verificar as chaves DSA:

`$ openssl dsa -in [arquivo_chave_privada] -text [-noout]`

Ex.:

`alice$ openssl dsa -in alice_priv.pem -text`

Extrair a chave pública DSA:

`$ openssl dsa -in [arquivo_chave_privada] -pubout -out [arquivo_chave_publica]`

Ex.:

`alice$ openssl dsa -in alice_priv.pem -pubout -out alice_pub.pem`

Verificar a chave pública DSA:

`$ openssl dsa -in [arquivo_chave_publica] -pubin -text [-noout]`

Ex.:

`alice$ openssl dsa -in alice_pub.pem -pubin -text`

Assinar com a chave privada DSA:

`$ openssl dgst -[dss1|shaN] -sign [arquivo_chave_privada] -out [arquivo_assinatura] [arquivo]`

Ex.:

`alice$ openssl dgst -dss1 -sign alice_priv.pem -out assinatura.bin texto.txt`

Verificar a assinatura com a chave pública DSA:

`$ openssl dgst -[dss1|shaN] -verify [arquivo_chave_publica] -signature [arquivo_assinatura] [arquivo]`

Ex.:

`bob$ openssl dgst -dss1 -verify alice_pub.pem -signature assinatura.bin texto.txt`

Outra possibilidade, verificar a assinatura com a chave privada DSA:

`$ openssl dgst -[dss1|shaN] -prverify [arquivo_chave_privada] -signature [arquivo_assinatura] [arquivo]`

Ex.:

`alice$ openssl dgst -dss1 -prverify alice_priv.pem -signature assinatura.bin texto.txt`

Obs: é possível assinar e verificar assinaturas assim como exemplificado no RSA.

------XXX Certificados Digitais XXX------

1) Requisição de Certificado

Gerar uma requisição de certificado:

`$ openssl req -new -key [arquivo_chave_privada] -out [arquivo_requisicao_certificado]`

Ex.:

`alice$ openssl req -new -key alice_priv.pem -out alice_reqcert.pem`

Obs: chave privada pode ser DSA ou RSA.

Verificar a requisição de certificado:

`$ openssl req -in [arquivo_requisicao_certificado] -text [-noout]`

Ex.:

`alice$ openssl req -in alice_reqcert.pem -text`

2) Certificado Auto-assinado

Gerar um certificado x509 auto-assinado:

`$ openssl x509 -req [-sha1/sha224/sha256] -days [dias] -in [arquivo_requisicao_certificado] -signkey [arquivo_chave_privada] -out [arquivo_certificado]`

Ex.:

`alice$ openssl x509 -req -sha1 -days 365 -in alice_reqcert.pem -signkey alice_priv.pem -out alice_cert.pem`

Obs: é possível adicionar mais parâmetros, como um número serial personalizado (-set_serial); pesquise em (`openssl x509 -h`).

Verificar o certificado:

`$ openssl x509 -in [arquivo_certificado] -text [-noout]`

Ex.:

`alice$ openssl x509 -in alice_cert.pem -text`

Mais detalhes na verificação:

`$ openssl x509 -in [arquivo_certificado] -noout [-serial] [-subject] [-issuer] [-email] [-dates] ...`

Ex.:

```
alice$ openssl x509 -in alice_cert.pem -noout -subject
alice$ openssl x509 -in alice_cert.pem -noout -issuer
alice$ openssl x509 -in alice_cert.pem -noout -email
```

Fingerprint do Certificado:

`$ openssl x509 -in [arquivo_certificado] -noout -fingerprint [-md5/-sha1/-sha256/...]`

Ex.:

`alice$ openssl x509 -in alice_cert.pem -noout -fingerprint -md5`

Extrair a chave pública do certificado:

`$ openssl x509 -in [arquivo_certificado] -noout -pubkey > [arquivo_chave_publica]`

Ex.:

`alice$ openssl x509 -in alice_cert.pem -noout -pubkey > alice_pub.pem`

Verificar assinatura do certificado auto-assinado:

`$ openssl verify -CAfile [arquivo_certificado] [arquivo_certificado]`

Ex.:

`alice$ openssl verify -CAfile alice_cert.pem alice_cert.pem`

3) Certificado assinado por Autoridade Certificadora

Criar uma Autoridade Certificadora:

`$ /usr/lib/ssl/misc/CA.pl -newca`

Obs: preencher com as informações da autoridade certificadora e conferir os seguintes arquivos:
- cacert.pem (certificado digital da autoridade certificadora, que é público)
- careq.pem (apenas o arquivo de requisição de certificado)
- cakey.pem (chave privada RSA criptografada)

Copiar e assinar o certificado com a Autoridade Certificadora:

```
$ cp [arquivo_requisicao_certificado] newreq.pem
$ /usr/lib/ssl/misc/CA.pl -sign
```

Ex.:

```
charles$ cp alice_reqcert.pem newreq.pem
charles$ /usr/lib/ssl/misc/CA.pl -sign
```

Obs: resultará no certificado de alice em newcert.pem

Verificar o certificado assinado:

`$ openssl verify -CAfile [arquivo_certificado_da_autoridade] [arquivo_certificado]`

Ex.:

`bob$ openssl verify -CAfile charles_cert.pem alice_cert.pem`

------XXX SSL/TLS XXX------

Verificar suites disponíveis:

```
$ openssl ciphers -v
$ openssl ciphers FIPS
$ openssl ciphers HIGH
```a

Comunicação SSL/TLS Cliente/Servidor:

```
server$ openssl s_server -cert [arquivo_certificado] -key [arquivo_chave_privada] -cipher [opcao_suite] [-www]
client$ openssl s_client -connect [dominio_site:porta]
```

Ex.:

```
server$ openssl s_server -cert certificado.pem -key privada.pem
client$ openssl s_client -connect localhost:4433
```

Outro exemplo:

```
server$ openssl s_server -cert certificado.pem -key privada.pem -cipher DHE-RSA-AES256-SHA256 -www
client$ openssl s_client -connect localhost:4433
GET / HTTP/1.1 [tecle enter]
```

Obs: "-accept 443" permite analisar com wireshark.

------XXX Fonte XXX------

[OpenSSL Manpages](https://www.openssl.org/docs/)

