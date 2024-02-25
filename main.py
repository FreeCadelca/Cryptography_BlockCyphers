from HillCypher import HillCypher
from IntMod import IntMod
from RecHillCypher import RecHillCypher


# key = [[IntMod(2), IntMod(4), IntMod(1)],
#        [IntMod(4), IntMod(1), IntMod(3)],
#        [IntMod(7), IntMod(6), IntMod(4)]]
#
# key2 = [[IntMod(6), IntMod(8), IntMod(9)],
#         [IntMod(3), IntMod(7), IntMod(1)],
#         [IntMod(5), IntMod(4), IntMod(8)]]
#
# key = [[IntMod(3), IntMod(2)],
#        [IntMod(6), IntMod(5)]]
#
# key2 = [[IntMod(1), IntMod(4)],
#         [IntMod(2), IntMod(9)]]


def text_input():
    text = ''
    line = input()
    while line != '':
        text += line + '\n'
        line = input()
    return text


state = 'chooseCypher'
cypher = None
while True:
    if state == 'chooseCypher':
        cypher_name = input('Введите номер шифра (1 - шифр Хилла, 2 - рекуррентный шифр Хилла):\n')
        if cypher_name == '1':
            state = 'Hill'
            print("Введите ключ для данного шифра в виде множества чисел в матрице размера 2х2. \n"
                  "Разделение между числами в одной строке матрицы - пробел,\n"
                  "разделение между строками одной матрицы - переход на новую строку.")

            key = []
            for _ in range(2):
                line = []
                for i in input().split():
                    line.append(IntMod(int(i)))
                key.append(line)
            key = [[list(map(int, input().split()))] for _ in range(2)]

            cypher = HillCypher(key)
        elif cypher_name == '2':
            state = 'RecHill'
            print("Введите ключи для данного шифра в виде множеств чисел в двух матрицах размера 2х2. \n"
                  "Разделение между числами в одной строке матрицы - пробел,\n"
                  "разделение между строками одной матрицы - переход на новую строку,\n"
                  "разделение между двумя матрицами - переход на новую строку")

            keys = []
            for _ in range(2):
                key = []
                for _ in range(2):
                    line = []
                    for i in input().split():
                        line.append(IntMod(int(i)))
                    key.append(line)
                keys.append(key)

            cypher = RecHillCypher(keys[0], keys[1])
    else:
        mode = input("Введите операцию (E/D/Info - Encrypt/Decrypt/Get information about key(s) in the cypher)\n")
        if mode == "Info":
            cypher.info()
            continue
        print("Введите текст для зашифрования/расшифрования\n"
              "(Заглавные буквы автоматически заменятся на строчные, введите пустую строку для остановки ввода):")
        text = text_input().lower()
        if mode == "E":
            print(cypher.encrypt(text))
        elif mode == "D":
            print(cypher.decrypt(text))
