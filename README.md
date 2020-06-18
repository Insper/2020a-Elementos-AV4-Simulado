# 2020a - AV4 Elementos de Sistemas - prática

| AV      | Pontos HW | Pontos SW |
| ------- | ------    | ------    |
| Teórica | 25        | 15        |
| Prática | 10        | 45        |

Avaliação 4 Elementos de Sistemas - parte prática 

- **Trabalhar sozinho**
- **120 min** total (prática + teórica)
- Ficar conectado no canal geral (para ouvir instruções)

### Começando

Você deve:

1. clonar o seu repositório (e trabalhar nele)
1. editar o arquivo `ALUNO.json`
1. não esqueça de dar `commit` e `push`

## Prática

:bulb: Antes de começar atualize o Z01-Tools:

```bash
./updateZ01tools.sh
```

:tada: **Lembre de realizar um commit (a cada questão) e dar push ao finalizar**

Questões:

----------------------------------

### 1. ( ) nasm pseudo

- Arquivo: `nasm/pseudo.nasm`
- Teste: `./testeAssembly.py`

| Teste | O que testa | pts |
|-------|-------------|-----|
| 1     | if          |     |
| 2     | else        |     |

Transcreva para assembly do Z01 o pseudo código a seguir:

```python
 if ( RAM[1] == 1 && RAM[2] > 2 ):
     RAM[5] = 1
 else
     RAM5[6] = -2
```

----------------------------------

### 2. ( 10 SW) vm pseudo 

- Arquivo: `vm/pseudo/Main.vm`
- Teste: `./testeVm.py`

| Teste | O que testa | pts |
|-------|-------------|-----|
| 1     | if          |   |
| 1     | else        |   |

Transcreva para linguagem VM do Z01 o pseudo código a seguir:

```python
 if( temp[0] > 4 && temp[1] >= 4 ):
     temp[2] = 3
 else:
     temp[2] = -1
```

Onde:
  - temp[0]: temporário 0
  - .....
  - temp[3]: temporário 3

----------------------------------

### 3. ( ) vm mult

- Arquivo: `vm/Mult/Mult.vm`
- Teste: `./testeVm.py`

| Teste | O que testa | pts |
|-------|-------------|-----|
| 1     |             |     |

Escreva uma função que faz a multiplicação entre dois números, passados
como argumento.

----------------------------------

### 4. ( ) vm translator `or`

- Arquivo: `vmTranslator/src/main/java/vmtranslator/Code.java`
- Teste: `./testeVm.py`

| Teste | O que testa | pts |
|-------|-------------|-----|
| 1     |             |     |

A tradução do comando comando `or` de `.vm` para `nasm` deve ser feito
no `Code.java` na linha:

``` java
 } else if (command.equals("or")) {
            commands.add(String.format("; %d - OR", lineCode++));

}
```

> exemplo: commands.add("leaw $SP, %A");

----------------------------------

### 5. ( ) vm translator `push argument`

- Arquivo: `vmTranslator/src/main/java/vmtranslator/Code.java`
- Teste: `./testeVm.py`

| Teste | O que testa | pts |
|-------|-------------|-----|
| 1     |             |    |

A tradução do comando comando `push argument X` de `.vm` para `nasm` deve ser feito
no `Code.java` na linha:

``` java
} else if (segment.equals("argument")) {

}
```

> exemplo: commands.add("leaw $SP, %A");
