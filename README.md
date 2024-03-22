# Блочное шифрование

```
n bit              n bit        
 OT <---> E, D <---> ШТ
           |
           |
           k 
```

```
--------- k ---------
 | Расширение ключа |
---------------------
|    |     |        |
k1   k2   k3   ...  ks
```


`Лавинный эффект` - если меняется один бит ключа, то изменятся биты в подавляющем большенстве ключей 

`$F$` - функция раунда, может использоваться в обратном порядке

$$
\text{ОТ } \to F_0(k_1, m) \to F_1(K_2, F_0) \dots F_s(k_s, F_{s-1}) \to c \text{ ШТ}
$$

---

<br>

### Классические примеры

**AES:** *Advanced Encryption Standart* 

+ длина блока (n) - 128 бит
+ длина кшлюча (k) - 128, 192, 256
+ количество раундов (S) - 10, 12, 14

**3DES:**











