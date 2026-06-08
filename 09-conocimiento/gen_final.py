import os, base64
desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
path = os.path.join(desktop, "plan_financiero.html")
html = base64.b64decode(open(os.path.join(desktop, "html_b64.txt"), "r").read()).decode("utf-8")
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML generated at:", path)