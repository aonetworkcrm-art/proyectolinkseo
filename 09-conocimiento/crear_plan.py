import os

content = '''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Nuclear AIMA · Master Plan Marketing 2026</title></head>
<body style="background:#0a0a0c;color:#f0ede8;font-family:system-ui;padding:1rem;max-width:1000px;margin:0 auto">
<h1 style="color:#c9a96e;text-align:center">MASTER PLAN MARKETING NUCLEAR 2026</h1>
<p style="text-align:center;color:#777">Documento Operativo Unificado · Infraestructura Publicitaria y Trafico de Alta Densidad</p>
<p style="text-align:center"><strong>Romny A. Regalado Maria</strong> · Director General de Marketing</p>
</body>
</html>'''

with open('plan_marketing.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('File created successfully')
