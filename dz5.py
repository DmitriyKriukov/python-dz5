# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'ап ккеркер ываппвы бмис варавпр бтнат куценцкен'
# list_t = text.split()
# new_list = []
# for i in range(len(list_t)):
#     if 'а' in list_t[i] or 'б' in list_t[i] or 'в' in list_t[i]:
#         i += 1
#     else:
#         new_list.append(list_t[i])
# print(*new_list)


# 40. Создайте программу для игры в ""Крестики-нолики"".

# print('*' * 10, ' Игра Крестики-нолики для двух игроков ', '*' * 10)
# board = list(range(1, 10))
# wins_pos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
#
# def draw_board():
#     print('-' * 13)
#     for i in range(3):
#         print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
#         print('-' * 13)
#
#
# def take_input(player_token):
#     while True:
#         value = input('Поставьте ' + player_token + ' ')
#         value = int(value)
#         board[value - 1] = player_token
#         break
#
# def chek_win():
#     for i in wins_pos:
#         if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
#             return board[i[1] - 1]
#     else:
#         return False
#
# def main():
#     count = 0
#     while True:
#         draw_board()
#         if count % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         if count > 3:
#             winner = chek_win()
#             if winner:
#                 draw_board()
#                 print(winner, 'выиграл!')
#                 break
#         count += 1
#         if count > 8:
#             draw_board()
#             print('Ничья')
#             break

# main()

# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#     Входные и выходные данные хранятся в отдельных текстовых файлах.

# def press(file):
#     with open ('file.txt', 'r', encoding='utf-8') as data:
#         text = data.read()
#     res = ''
#     count = 1
#     for i in range(0, len(text) - 1):
#         if text[i] == text[i + 1]:
#             count += 1
#         else:
#             res = res + str(count) + text[i]
#             count = 1
#     res = res + str(count) + text[-1]
#     with open ('file2.txt', 'w', encoding='utf-8') as data:
#         data.write(res)
# press('file.txt')


# def depress(file):
#     with open ('file2.txt', 'r', encoding='utf-8') as data:
#         text = data.read()
#     res = ''
#     for i in range(0, len(text), 2):
#         res = res + int(text[i]) * text[i+1]
#     with open ('file3.txt', 'w', encoding='utf-8') as data:
#         data.write(res)
# depress('file2.txt')
