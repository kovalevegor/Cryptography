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

Как использовать короткий ключ на длинное сообщение?

**PRC** - генератор псевдо случайных чисел 

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
Ева знает первые байты ОТ
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
P_r[A(G(k)[1\dots i-1]=G(k)[i]] > \frac{1}{2}+\varepsilon\big
$$

Если $\frac{1}{2}+\varepsilon$ , то $\varepsilon$ начимое 

$$
\varepsilon> \dfrac{1}{2^{30}}
$$

---

<br>

### Атаки на потоковый шифр

+ Двухразовый блокнот 

$$
m_1 \neq m_2
$$

$$
c_1=m_1 \oplus G(k) \quad \oplus \quad c_2=m_2\oplus G(k)
$$

$$
c_1\oplus c_2=m_1\oplus m_2
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
m = FROM Bob --------	o  /F/R/O/M/ /B/o/b/ --	o  ШТ
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
A: \space A(x)^{\lbrace 0,1 \rbrace ^n}=\begin\{cases}
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
if Adv 	->  1:
  A отмечает G(k) от случайной последовательности
if Adv 	->  0:
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

**Теорема** *Безопасный генератор не предсказуем*

*Если хотя бы один бит является предсказуемым, то генератор небезопасен*
```python
if генератор предсказуем 	->  он небезопасен
```

+ r - случайное 
+ Pr[B(r) = 1] = $\dfrac{1}{2}$ 
+ Pr[G(k)] = $\dfrac{1}{2} + \varepsilon$

Доказательство:

$$
Adv_{PRG}[B,G]=\vert Pr[B(G(k))=1]-Pr[B(r)=1]\vert
$$

### Задача

+ $G:K	\to \lbrace 0, 1 \rbrace ^n$ - безопасный генератор
+ $G': K \times K 	\to   \lbrace 0, 1 \rbrace ^n$
+ $G'(K_1, K_2) = G(K_1) \\& G(K_2)$ - увеличения длины ключа.
+ Безопасен ли такой генератор?


$Adv_{PRG}[A,G']= \vert Pr[A(r)=1]-Pr[A(G'(K_1,K_2))=1]\vert = \dfrac{1}{4}$

Ответ: генератор не безопасен

Конъюнкция и Дизъюнкция - "плохие" булевые функции для битовых операций

---

### Задача

+ $G:K	\to  \lbrace 0, 1 \rbrace ^n$ - безопасный генератор
+ $G':K	\to   \lbrace 0, 1 \rbrace ^{n-2}$ - works like $G'[K)=G(K)[1\dots n-2]$ - безопасен?
Adv - эффективность
Доказательство от противного: 

1. Допустим $G'$ -небезопасен, тогда $\forall \space A \space Adv[A,G']>\varepsilon$

$$
B(X) = \begin\{cases}
   0 & \text{}\\
   1 & \text{if} \space A (X_{[1\dots n-1]}) = 1
\end{cases}
$$

2. $Adv_{PRG}[B,G] = Pr[B(r)=1]=\dfrac{1}{2}$
3. $Pr(B(G(k))=1]=\varepsilon$
4. $Adv_{PRG}[B,G]=\vert \dfrac{1}{2}-t\vert > \varepsilon$


---

<br>

### Безопасность потоковых шифров

+ Для уникального ключа - уникальный открытый текст
+ Ева - пассивыный противник, она знает только 1 ШТ

$$
\forall\space m_0, m_1 \quad \vert m_0 \vert = \vert m_1 \vert
$$

$$
\forall\space c \quad \vert K \vert = \vert M \vert
$$

$$
Pr[E(k,m_0)=c=\vert Pr[E(k,m_1)=c]
$$

$$
\lbrace Pr[E(k,m_0)]\rbrace \underbrace{\approx}_{p} \lbrace Pr[E(k,m_1)]\rbrace
$$

*Безопасный шифр текст - это такой ШТ, что вероятностные распределения двух шифр текстов из его множества приблизительно равны*

+ Оракул $\square$ - тот кто знает решение, дает ответ в виде: правильно/неправильно
+ $k \in K$
+ Оракул придумал себе число $b = \lbrace 0, 1 \rbrace $

---

+ Противник А $\blacksquare$
+ Отправляет оракулу 2 открытых текста (любых)
+ Оракул отправляет шифртекст, выбирая сообщение, в зависимости от задуманного числа
+ Задача противника получить b

1. Оракул Выбирает ключ $k \in K$
2. Оракул выбирает $b = \lbrace 0, 1 \rbrace $
3. Противник А посылает $m_0, m_1$
4.

$$ \begin\{cases}
   if & b = 0 & c = E(k, m_0) \\
   if & b = 1 & c =E(k, m_1)
\end{cases} 
$$


$Adv_{SS}$ - semantic secure $[A, E]=\vert Pr[w_0]-Pr[w_1]\vert$

$if \space Adv_{PRG} [A,E] \to 0$ - противник слабый 

$if \space Adv_{PRG} [A,E] \to 1$ - притивник сильный 

**Определение** *Потоковый шифр Е называется семантически стойкимесли, если для любого эффективного противника А значение его эффективности к этому шифру меньше* $\varepsilon$, *где* $\varepsilon$ *- число не значимое*

---

<br>






















