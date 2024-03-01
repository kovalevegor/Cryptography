# Потоковые шифры

### Симметричные шифры

`шифр` - ключи (K), открытие тексты (M), шифр тексты (C)

алгоритмы (E, D) - эффективные (можно вычислить за полиномиальное время), такие что:
+ Алгоритм E (почти случайный) действует на простаранстве ключей и открытых текстов и выдает шифр текст E: K $\times$ M $\to$ C
+ Алгоритм D (детерминированный) действует на пространстве ключей и шифр текстов и выдает открытый текст D: K $\times$ C $\to$ M

последовательное применение алгоритмов дает исходное сообщение D(K,E(K,m)) = m

### Шифр Вернама 
(одноразовый блокнот) *OTP - one time pad*  -   Теоритически стойкий шифр

1. текст преобразовали в последовательность бит

$$
M = \lbrace 0, 1 \rbrace ^n 
$$

$$
C = \lbrace 0, 1 \rbrace ^n
$$

$$
K = \lbrace 0, 1 \rbrace ^n
$$

$$
E: m \oplus k = c
$$

$$
D: c \oplus k = m
$$

---

<br>

### Теоретически стойкий шифр (идеальный шифр)

**Опр** 

$$
\forall m_0m_1: |m_0| = |m_1|
$$

$$
\forall c \in C
$$

$$
P_r[E(k,m_0)=c]=P_r[E(k,m_1)=c]
$$

---

*one time pad*  -   Теоритически стойкий шифр

$$
\forall m, c
$$

$$
P_r[E(k,m)=c]=\frac{\\#K:E(k,m) = c}{|K|} \=> \frac{1}{2^n}
$$

#K - количество ключей для данного шифрования

|K| - простраснство ключей 

**теоритический стойкий шифр**, если $|K|\ge|M|$

---

<br>

### Потоковый шифр

Как использовать короткий ключ на длинное сообщение

PRC генератор псевдо случайных чисел 

$G: \underbrace{\lbrace 0,1 \rbrace S}_{Seed}\to \lbrace 0,1 \rbrace ^n$ , seed $S\gg n$

$$
K=\lbrace 0,1 \rbrace ^S \qquad M = C = \lbrace 0,1 \rbrace ^n
$$

seed -битовая последовательность длины S

```
                    K
                  /  \
                /      \
              /          \
        ------------------------
        |         G(k)         |
        ------------------------
                   xor
        ------------------------
        |           m          |
        ------------------------
        ________________________
        ------------------------
        |           c          |
        ------------------------
      
```

Представим PRG - предсказуем (значит по данным можно предсказать следующие данные)

$$
\exists i \space G(k) [1, \dots, i-1] \to G(k) [1, \dots, n]
$$

Алгоритм А (владеет им Ева) 

```
Ева знает первые байти ОТ
Как Ева по данным первых
бит достраивает генератор
и находит открытый текст
        ------------------------
        |           c          |  \
        ------------------------    \
xor                                   \
        ------------------------        x
m       |   ...   |    ....    |      /
        ------------------------    /
        |   G(k)  |            |  /
        |[1...i-1]|............|
               \     /
                 \ /
                  A
```














