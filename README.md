# Cryptography Потоковые шифры

### Симметричные шифры

`шифр` - ключи (K), открытие тексты (M), шифр тексты (C)

алгоритмы (E, D) - эффективные (можно вычислить за полиномиальное время), такие что:
Алгоритм E (почти случайный) действует на простаранстве ключей и открытых текстов и выдает шифр текст E: K $\times$ M $to$ C
Алгоритм D (детерминированный) действует на пространстве ключей и шифр текстов и выдает открытый текст D: K $\times$ C $to$ M

последовательное применение алгоритмов дает исходное сообщение D(K,E(K,m)) = m
