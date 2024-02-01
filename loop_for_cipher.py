from agile_manifesto import coded_message

count = 0
agile_list = []
number_input = input("Введіть ключ до шифра (Улюблене число Шелдона Купера): ")

if number_input == "73":
    while count < len(coded_message):
        char_index = chr(ord(coded_message[count]) - int(number_input))
        agile_list.append(char_index)
        count += 1
else:
    agile_list = ["На жаль, Ви ввели неправильний ключ 🤷‍♂️"]

text_ = "".join(agile_list)
