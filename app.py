from pathlib import Path
import json
import requests
from flask import Flask, render_template, redirect, url_for
ROOT = Path(__file__).resolve().parent
app = Flask(__name__)
def load_data(name):
    with (ROOT / "data" / f"{name}.json").open(encoding="utf-8") as f:
        return json.load(f)
@app.context_processor
def common(): return {"site": load_data("site")}
@app.get("/")
def home(): return render_template("index.html", title="把喜歡，變成更好的選擇")
@app.get("/expose")
def expose(): return render_template("expose.html", title="看懂繁殖場黑幕", signs=load_data("red_flags"))
@app.get("/reality-check")
def reality():
    breeds, images = load_data("breeds"), {}
    for breed in breeds:
        try:
            response = requests.get(breed["api"], timeout=5)
            response.raise_for_status()
            payload = response.json()
            images[breed["id"]] = payload["message"] if payload.get("status") == "success" else breed["fallback"]
        except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
            app.logger.warning("Dog image unavailable for %s: %s", breed["id"], exc)
            images[breed["id"]] = breed["fallback"]
    return render_template("reality.html", title="養狗現實計算機", breeds=breeds, images=images, costs=load_data("costs"))
@app.get("/reality-check/refresh")
def refresh(): return redirect(url_for("reality") + "#breed-guide")
@app.get("/adopt")
def adopt(): return render_template("adopt.html", title="台灣合法領養指南", orgs=load_data("adoption"))
@app.errorhandler(404)
def not_found(error): return render_template("404.html", title="找不到頁面"), 404

if __name__ == '__main__':
    app.run(debug=True)
