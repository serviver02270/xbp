import random

def main():
    print("コンピュータとのしりとりゲームを始めます。")
    words = []  # 使用済みの単語を格納するリスト
    current_word = ""

    while True:
        print("あなたの番です。")
        player_word = input().strip()

        if not is_valid_word(player_word, words, current_word):
            print("無効な単語です。再試行してください。")
            continue

        words.append(player_word)
        current_word = player_word[-1]

        if is_game_over(words, "プレイヤー"):
            print("おめでとうございます、あなたの勝ちです！")
            break

        print("コンピュータの番です。")
        computer_word = get_computer_word(words, current_word)
        print(computer_word)

        words.append(computer_word)
        current_word = computer_word[-1]

        if is_game_over(words, "コンピュータ"):
            print("コンピュータの勝ちです。")
            break

def is_valid_word(word, used_words, current_word):
    if len(word) == 0 or word in used_words:
        return False
    if current_word and word[0] != current_word:
        return False
    return True

def get_computer_word(used_words, current_word):
    # ダミーのコンピュータ対戦
    available_words = [word for word in used_words if word[0] == current_word]
    if available_words:
        return random.choice(available_words)
    else:
        return "むずかしい"

def is_game_over(used_words, player):
    if len(used_words) >= 5:
        print(f"{player}の勝ちです。")
        return True
    return False

if __name__ == "__main__":
    main()
