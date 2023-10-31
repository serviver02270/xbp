# HTMLコードを自動生成するPythonコード

# タイトルと本文を定義
title = "自動生成されたHTML"
body = "これはPythonコードによって自動生成されたHTMLです。"

# HTMLコードを生成
html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{body}</p>
</body>
</html>
"""

# HTMLコードをファイルに保存
with open("auto_generated.html", "w") as file:
    file.write(html_code)

print("HTMLファイルが生成されました。")
