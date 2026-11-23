# 牠的下一站

繁體中文 Flask 網站，提供繁殖風險辨識、大學生養狗預算概估與台灣領養資源。資料使用本地 JSON，圖片透過 Dog CEO API 並設有備援圖。

## 本機啟動
需 Python 3.11+。

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
flask --app app run --debug
```
開啟 http://127.0.0.1:5000。正式伺服器可執行 `gunicorn app:app`。

## 推送 GitHub
在 GitHub 建立空白 repository，再於專案目錄執行：

```bash
git init
git add .
git commit -m "建立領養倡議網站"
git branch -M main
git remote add origin https://github.com/<帳號>/<repository>.git
git push -u origin main
```

## Vercel 部署
登入 Vercel，選 Add New → Project，匯入 GitHub repository，Framework Preset 選 Other 後按 Deploy。`vercel.json` 使用 Python Runtime 載入 `api/index.py`，不需資料庫或環境變數。Dog CEO 呼叫 timeout 為 5 秒，API 錯誤時使用備援圖片。

## 專案結構
```text
api/index.py  app.py  vercel.json  requirements.txt  .gitignore
 data/{site,red_flags,costs,breeds,adoption}.json
 templates/{base,index,expose,reality,adopt,404}.html
 static/{site.js,style.css}
```
各機構連結與法規摘要上線前請再核對官方最新公告；預算是教育用途概估，非醫療報價。
