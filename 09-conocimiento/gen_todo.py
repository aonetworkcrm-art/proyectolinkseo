import os, base64
desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
def w(n, c):
    p = os.path.join(desktop, n)
    with open(p, "w", encoding="utf-8") as f:
        f.write(base64.b64decode(c).decode("utf-8"))
    print("OK:", n)
