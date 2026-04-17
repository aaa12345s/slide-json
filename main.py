import json
import os
from jinja2 import Environment, FileSystemLoader

def generate_slides():
    # 設定
    JSON_FILE = "slides.json"
    TEMPLATE_DIR = "templates"
    OUTPUT_FILE = "output.html"

    # 1. JSONデータの読み込み
    if not os.path.exists(JSON_FILE):
        print(f"エラー: {JSON_FILE} が見つかりません。")
        return

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        slides = data.get("slides", [])

    # 2. Jinja2環境の設定
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("base.html")

    # 3. レンダリング（HTML生成）
    rendered_html = template.render(slides=slides)

    # 4. ファイル書き出し
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"✅ スライド生成が完了しました！ -> {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_slides()