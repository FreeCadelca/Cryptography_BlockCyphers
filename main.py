from HillCypher import HillCypher
from IntMod import IntMod
from RecHillCypher import RecHillCypher


def text_input():
    text = ''
    line = input()
    while line != '':
        text += line + '\n'
        line = input()
    return text


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
            # ввод ключа от пользователя и преобразование его в нужный программе формат
            key = []
            for _ in range(2):
                line = []
                for i in input().split():
                    line.append(IntMod(int(i)))
                key.append(line)
            cypher = HillCypher(key)
        elif cypher_name == '2':
            state = 'RecHill'
            print("Введите ключи для данного шифра в виде множеств чисел в двух матрицах размера 2х2. \n"
                  "Разделение между числами в одной строке матрицы - пробел,\n"
                  "разделение между строками одной матрицы - переход на новую строку,\n"
                  "разделение между двумя матрицами - переход на новую строку")
            # ввод ключей от пользователя и преобразование их в нужный программе формат
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
        mode = input("Введите операцию (E/D/EText/DText/Info - Encrypt line/Decrypt line/Encrypt text/Decrypt text/Get information about key(s) in the cypher/)\n")
        if mode == "Info":
            cypher.info()
            continue
        print("Введите текст/слово для зашифрования/расшифрования\n"
              "(Заглавные буквы автоматически заменятся на строчные)")
        if mode == "EText":
            print("(Введите пустую строку для того, чтобы закончить ввод)")
            text = []
            line = input().lower()
            while line != '':
                text.append(line)
                line = input().lower()
            out = [cypher.encrypt(i) for i in text]
            for i in out:
                print(i)
        elif mode == "DText":
            print("(Введите пустую строку для того, чтобы закончить ввод)")
            text = []
            line = input().lower()
            while line != '':
                text.append(line)
                line = input().lower()
            out = [cypher.decrypt(i) for i in text]
            for i in out:
                print(i)
        elif mode == "E":
            print(cypher.encrypt(input().lower()))
        elif mode == "D":
            print(cypher.decrypt(input().lower()))

