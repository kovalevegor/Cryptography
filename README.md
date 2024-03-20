# Статистика RC4

### Формулировка задания

<br>

В данном задании используется ослабленная версия шифра RC4 с длиной слова 4 
бита и длиной ключа 32 бита. Процедуры инициализации шифра и генерации 
потокового ключа можно посмотреть в wiki.

Запустить перебор выходов генератора по всем ключам и определите вероятность появления указанного в варианте события в получившихся потоковых ключах.

Появление тройки: **1 на 1 позиции, 1 на 3 позиции и 1 на 5 позиции потокового 
ключа**

---

<br>

Программный код: 

```python
Python Spyder


from tqdm import tqdm

def KSA (K) -> list:
    S = list(range(16))
    j = i = 0
    for i in range(16):
        j = (j + S[i] + int(K[i % len(K)])) % 16
        S[i], S[j] = S[j], S[i]
    return S

def PRGA (S
          # , PT
          ) -> list:
    i = j = 0
    keystream = []
    for i in range(5):
        i = (i + 1) % 16
        j = (j + S[i]) % 16
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 16])
    return keystream

def XOR (KS, PT) -> str:
    KS = ["{0:b}".format(int(num)) for num in KS]; print(KS, end = '\n')
    PT = ["{0:b}".format(int(num)) for num in PT]; print(PT, end = '\n\n')
    CT = []
    for i in range(len(PT)):
        CT.append(int(KS[i], 2) ^ int(PT[i], 2))
    return CT

def gen_cmb(length):
    if length == 0:
        yield ""
    else:
        for combination in gen_cmb(length - 1):
            yield combination + "0"
            yield combination + "1"

satisfied = 0
for combination in tqdm(gen_cmb(32), 
                        total = 4_294_967_296,
                        desc = 'keystreams counts', 
                        unit = 'set',
                        disable = False):
    # pass
    keystream = PRGA(KSA(combination))
    if keystream[0] == 1 and keystream[2] == 1 and keystream[3] == 1:
        satisfied += 1
        print('success')

print(satisfied/4_294_967_296)
```

---

<br>

В результате работы программы, имеем следующий вывод:

```powershell
keystreams counts: 100%|██████████| 4294967296/4294967296 [7:15:57<00:00, 164196.89set/s]0.000335693359375
success
success
...
success

1.1548399925231934e-07
```

<br>

В итоге, сумма результатов выводов генератора, удовлетворяющих условию `[1, *, 1, *, 1]` = **496**

Вероятность наступления события $A$ = `[1, *, 1, *, 1]` рассчитаем по формуле классического определения вероятности:

$$Pr(A) = \dfrac{m}{n}$$

+ $m$ - число благоприятных для события A исходов, 
+ $n$ - общее число равновозможных элементарных исходов

$$Pr(A) = \dfrac{496}{4.294.967.296}=0.00000011548399925231934$$

---

<br>

### Вывод

**Определение предсказуемого генератора** PRG - $G: \lbrace 0,1 \rbrace ^S\to\lbrace 0,1 \rbrace ^n$ называется предсказуемым, если $\exists A$ "эффективный" $\exists\space 1\le i\le n-1$

$$
Pr[A(G(k)[1\dots i-1]=G(k)[i]] > \dfrac{1}{2}+\varepsilon
$$

Согласно определению предсказуемого генератора, генератор псевдослучайной последовательности ослабленной версии `RC4` не является полность предсказуемым, так как $Pr(A) = \dfrac{496}{4.294.967.296} < \dfrac{1}{2}+\varepsilon$
