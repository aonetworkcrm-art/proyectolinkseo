import os, base64

desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
html_b64_path = os.path.join(desktop, "html_b64.txt")
output_path = os.path.join(desktop, "plan_financiero.html")

with open(html_b64_path, "r") as f:
    b64_data = f.read()

html = base64.b64decode(b64_data).decode("utf-8")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML generado en:", output_path)
print("Tamano:", len(html), "caracteres")
