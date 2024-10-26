import random


def main():
    while True:
        j_list = ["グー", "チョキ", "パー"]
        print(f"選択してね{j_list}")
        player = input("あなたの手を入力してね:")
        com = random.choice(j_list)
        print(f"{player} {com}")
        if player == com:
            print("あいこです")
            continue
        elif (player == "グー" and com == "パー")\
            or (player == " チョキ" and com == "グー")\
                or (player == "パー" and com == "チョキ"):
            print("あなたの負けです")
        elif (player == "グー" and com == "チョキ")\
            or (player == " チョキ" and com == "パー")\
                or (player == "パー" and com == "グー"):
            print("あなたの勝ちです")
        break


if __name__ == '__main__':
    main()