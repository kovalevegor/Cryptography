# Блочное шифрование

```
OT <---> E, D <---> ШТ
           |
           |
           k 
```


Лавинный эффект - если меняется один бит ключа, то изменятся биты в подавляющем большенстве ключей 

функция раунда 

$$
F_0(k_1, m) \to F_1(K_2, F_0) \dots F_s(k_s, F_{s-1} \to c \text{ШТ}
$$
