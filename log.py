#!/usr/bin/env python3
"""
Auto-Logger Temporal del Proyecto: Link SEO

Uso:
  python3 log.py "Accion realizada" --tipo CODIGO --clima "24C Noche" --temp 24

Argumentos:
  mensaje     Descripcion de la accion
  --tipo      Categoria: FUNDACION|ESTRUCTURA|CODIGO|DEBUG|DOCS|IDEA|LANZAMIENTO|REFACTOR|SEGURIDAD|PERFIL
  --clima     Condiciones climaticas (ej: "24C Noche Soleado")
  --temp      Temperatura en Celsius (opcional, numerico)
  --detalle   Detalle adicional (opcional)
"""

import sys
import os
from datetime import datetime

def log_entry(mensaje, tipo="CODIGO", clima="~24C Interior", temp="~24", detalle=""):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    
    entry = f"
### {timestamp} -- {chr(0x1F321)} {clima}"
    entry += f"
{chr(0x2500)*47}"
    entry += f"
{chr(0x25B6)} **{tipo}:** {mensaje}"
    if detalle:
        entry += f"
{chr(0x25B6)} **DETALLE:** {detalle}"
    entry += "
"
    
    # Climate table row
    clima_row = f"| {now.strftime("%Y-%m-%d")} | {now.strftime("%H:%M")} | {temp}C | {clima} | {mensaje[:50]} |
"
    
    docs_log = "C:/proyecto-link-seo/_docs/DOCS-LOG.md"
    
    with open(docs_log, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Insert entry before climate section
    section_marker = "## " + chr(0x1F321) + " Registro Climatico"
    
    if section_marker in content:
        # Add bitacora entry
        content = content.replace(section_marker, entry + "
" + section_marker)
        
        # Also update the climate table - find last row and add new one
        # Find table end
        table_end = "---" if "---" in content.split(section_marker)[1].split("
")[-1] else ""
        
        with open(docs_log, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Now update the climate table specifically
        with open(docs_log, "r", encoding="utf-8") as f:
            content2 = f.read()
        
        # Find the climate section and add row
        parts = content2.split(section_marker)
        if len(parts) > 1:
            # Split at the end of the table (look for "---" AFTER the table)
            table_parts = parts[1].split("
---")
            if len(table_parts) > 1:
                # Insert the new row before the closing ---
                table_parts[0] += clima_row
                parts[1] = "
---".join(table_parts)
                
                with open(docs_log, "w", encoding="utf-8") as f:
                    f.write(section_marker.join(parts))
                
        print(f"[{timestamp}] Log entry added: {mensaje}")
        print(f"[{timestamp}] Climate row added: {clima}")
    else:
        print("Error: Climate section not found")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Uso: python3 log.py mensaje --tipo TIPO --clima clima --temp temp")
        sys.exit(1)
    
    mensaje = args[0].strip()
    tipo = "CODIGO"
    clima = "24C Interior"
    temp = "~24"
    detalle = ""
    
    for i, arg in enumerate(args):
        if arg == "--tipo" and i+1 < len(args):
            tipo = args[i+1]
        elif arg == "--clima" and i+1 < len(args):
            clima = args[i+1]
        elif arg == "--temp" and i+1 < len(args):
            temp = args[i+1]
        elif arg == "--detalle" and i+1 < len(args):
            detalle = args[i+1]
    
    log_entry(mensaje, tipo, clima, temp, detalle)
