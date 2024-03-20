'''
В данном задании используется ослабленная версия шифра RC4 с длиной слова 4 
бита и длиной ключа 32 бита. Процедуры инициализации шифра и генерации 
потокового ключа можно посмотреть в wiki.

Запустите перебор выходов генератора по всем ключам и определите вероятность 
появления указанного в варианте события в получившихся потоковых ключах.

Появление тройки: 1 на 1 позиции, 1 на 3 позиции и 1 на 5 позиции потокового 
ключа

После выполнения задания в текстовом файле разместите программный код и 
сформулируйте ответ на предложенный вариант задания
-------------------------------------------------------------------------------
'''
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
# for combination in tqdm(gen_cmb(32), 
#                         total = 4_294_967_296,
#                         desc = 'bit counts', 
#                         unit = 'bit',
#                         disable = False):
#     # pass
#     keystream = PRGA(KSA(combination))
#     if keystream[0] == 1 and keystream[2] == 1 and keystream[3] == 1:
#         satisfied += 1
#         print('success')

# print(satisfied/4_294_967_296) # 0.000335693359375

print(496/4_294_967_296)


# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# success
# bit counts: 100%|██████████| 4294967296/4294967296 [7:15:57<00:00, 164196.89bit/s]0.000335693359375














