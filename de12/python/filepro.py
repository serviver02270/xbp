# ファイル名と書き込むテキストを指定
file_name = "sample.txt"
text_to_write = "これはテストファイルです。\nPythonでファイルを生成し、テキストを書き込みます。"

# ファイルを書き込みモードで開く
with open(file_name, "w") as file:
    # テキストをファイルに書き込む
    file.write(text_to_write)

# ファイルが生成され、テキストが書き込まれました
print(f"{file_name} ファイルが生成され、テキストが書き込まれました。")
