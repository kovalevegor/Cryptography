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

**Определение предсказуемого генератора** 

PRG - $G: \lbrace 0,1 \rbrace ^S\to\lbrace 0,1 \rbrace ^n$ называется предсказуемым, если $\exists A$ "эффективный" $\exists\space 1\le i\le n-1$

$$
P_r\big[A(G(k)[1\dots i-1]=G(k)[i]> \frac{1}{2}+\varepsilon\big]
$$

Если $\frac{1}{2}+\varepsilon\big$ , то $\varepsilon$ начимое 

$$
\varepsilon> \dfrac{1}{2^{30}}
$$

---

<br>

### Атаки на потоковый шифр

+ Двузразовый блокнот 

$$
m_1 \neq m_2
$$

$$
c_1=m_1 \oplus G(k) \quad \oplus \quad c_2=m_2\oplus G(k)
$$

$$
C_1\oplus c_2=m_1\oplus m_2
$$

$$
\underbrace{c_1\oplus c_2}_{\text{Ева знает}}=
$$

$$
\underbrace{m_1\oplus m_2}_{\text{не является псевдослучайными данными}}
$$

Генератор псевдослучайных чисел - запускается один раз, а затем разбивается на части псевдослучайных последовательностей разных сообщений. 

---

<br>

802.11b WEB (Wered Equivalent Privacy) 128 bit

```
client                            точка доступа
            |m    |   CRC (m)|
                            xor
            |   PRG(IV||k)   |
            IV  |      ШТ    |

```

|| - конкатинация (слепление)

номер кадра - 24 бит (чистый инкремент, это плохо, потому что у этих ключей в префиксе отличается только один бит, а суффик остается неизменным) (решение - как можно реже менять ключ)

$2^{24} \approx 16,000,000$ кадров $=>$ двухразовый блокнот


+ Нарушение целостности

Потоковые шифры никак не защищены от модификаций

`Модификации ШТ не обнаруживаются и имеют предсказуемое, прямое вляние на ОТ`

```
m = FROM Bob ---------> /F/R/O/M/ /B/o/b/ ---> ШТ
                enc                            |
                                     xor       |
                                               |
                                              
```

---

<br>

### Безоопасный генератор псевдослучайных чисел

$G:\underbrace{\lbrace 0,1 \rbrace ^S}_{K}\to\lbrace 0,1 \rbrace ^n$

$n\gg S$

Пусть $n\in K=s^S$


$$
A: \space A(x)^{\lbrace 0,1 \rbrace ^n}=\begin{cases}
   0 &\text{if x - не случ; бесконечно малое G(k)} \\
   1 &\text{if x - случ}
\end{cases}
$$

---

<br>

### Критерий хорошего статистического теста
Через вероятность различить полследовательности

Пусть $G:K\to\lbrace 0,1 \rbrace ^n$ и $A$ - статистический тест

$$
Adv_{PRG}[A,G]=\vert Pr[A(\underbrace{G(k)}_{k\in K})=1]-Pr[A(\underbrace{r}_r\in\lbrace 0,1 \rbrace ^n)=1]\vert
$$

```python
if Adv -> 1:
  A отмечает G(k) от случайной последовательности
if Adv -> 0:
  A не отличает G(k) от случайной последовательности
```

### Примеры использования критерия статистического теста

1. $A(x) = 0 => Adv_{PRG}[A,G]=0$

2. $G:k\to\lbrace 0,1\rbrace ^n$ $\dfrac{2}{3}$ последовательностей `msb(G(k)) = 1`, `msb` - первый бит

$$ A(x)=\begin{cases}
0 &\text{иначе} \\ 
1 &\text{is msb(G(k))=1}
\end{cases}
$$ 

$$
Adv_{PRG}[A,G]=\vert\dfrac{2}{3}-\dfrac{1}{2}\vert=\dfrac{1}{6}\to\text{ значение}
$$

## Безопасный генератор псевдослучайных последовательностей

**Опр** Пусть $G:K\to\lbrace 0,1 \rbrace ^n$ - называется безопасным, если нет статистического теста, который отличает выход от случайной последовательности, если 

$$
\forall \space \text{эффективного статистического теста} \space A \space Adv_{PRG}[A,G]<\varepsilon<\dfrac{1}{2^{30}}
$$

---

<br>

**Теорема** *Безопасный генератор не предсказуем? тогда и только тогда, когда генератор непредсказуем.*

*Если хотя бы один бит является предсказуем, то генератор небезопасен*
```python
if генератор предсказуем -> он небезопасен
```

+ r - случайное 
+ Pr[B(r) = 1] = $\dfrac{1}{2}$ 
+ Pr[G(k)] = $\dfrac{1}{2} + \varepsilon$

Доказательство:

$$
Adv_{PRG}[B,G]=\vert Pr[B(G(k))=1]-Pr[B(r)=1]\vert
$$

**Задача**

+ $G:K-> \lbrace 0, 1 \rbrace ^n$ - безопасный генератор
+ $G' K \times K -> \lbrace 0, 1 \rbrace ^n$
+ $G'(K_1, K_2) = G(K_1) \\& G(K_2)$ - увеличения длины ключа.
+ Безопасен ли такой генератор?


$Adv_{PRG}[A,G']= \vert Pr[A(r)=1]-Pr[A(G'(K_1,K_2))=1]\vert = \dfrac{1}{4}$

Ответ: генератор не безопасен
