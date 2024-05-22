# goit-algo-hw-09
Порівняння швидкості жадного алгоритму та динамічного програмування.
coins = [1, 2, 10, 50]

Якщо сума решти мала (необхідно розрахувати кілька монет як решту), то швидкодія обох алгоритмів порівнювана (як відображає лічильник часу)
Решта = 101

{50: 2, 1: 1}
Жадний алгоритм, час: 0.0

{50: 2, 1: 1}
Динамічне програмування, час: 0.0

Якщо Решту встановити як велике значення, то швидкодія жадного алгоритму кратно вища за динамічне програмування
Решта = 101463975

{50: 2029279, 10: 2, 2: 2, 1: 1}
Жадний алгоритм, час: 0.0

{50: 2029279, 10: 2, 2: 2, 1: 1}
Динамічне програмування, час: 96.87440371513367
При цьому алгоритми дають ідентичну відповідь.

Якщо задати комбінацію монет і решту таким чином щоб не було рішення - жадний алгоритм дає некоректну відповідь, а динамічне програмування повертає нульовий результат.

Також можуть бути випадки, коли жадний алгоритм не знаходить найефективніше рішення в порівнянні з динамічним програмуванням. Наприклад, монети 1, 3, 4. Решта 6.
Жадний алгоритм поверне {4: 1, 1: 2} - решта 3 монети
Динамічне програмування покаже найефективніше рішення {3: 2} - решта 2 монети
