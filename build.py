#!/usr/bin/env python3
"""Embrulha cartao.html (fragmento do Artifact) num index.html completo para o GitHub Pages.

Uma fonte, duas saidas: cartao.html e publicado como Artifact na Claude e, passando
por aqui, vira a pagina servida pelo Pages. Assim os dois nunca divergem.

    python build.py
"""
import io
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FRAGMENTO = AQUI / "cartao.html"
SAIDA = AQUI / "index.html"

DESCRICAO = (
    "Cartao de bolso com oracoes curtas, frases-semente, versiculos conferidos "
    "e um exercicio diario para orar em voz alta sem peso."
)

# O visualizador de Artifacts injeta charset, viewport e um reset minimo.
# Servido pelo Pages nao ha ninguem a fazer isso, entao replicamos aqui.
MOLDE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{descricao}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F2F1EC" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F171E" media="(prefers-color-scheme: dark)">
<meta name="robots" content="noindex, nofollow">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Oracoes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="icon" href="./icone.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="./icone.svg">
<link rel="manifest" href="./manifest.webmanifest">
<style>
:root{{color-scheme:light dark}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
{cabeca}</head>
<body>
{corpo}</body>
</html>
"""


def main() -> int:
    if not FRAGMENTO.exists():
        print(f"erro: {FRAGMENTO.name} nao encontrado", file=sys.stderr)
        return 1

    fragmento = io.open(FRAGMENTO, encoding="utf-8").read()

    # <title>, <link> e <style> pertencem ao <head>; o resto e corpo.
    cabeca_partes = []

    def puxar(padrao: str) -> None:
        nonlocal fragmento
        for achado in re.findall(padrao, fragmento, flags=re.I | re.S):
            cabeca_partes.append(achado.strip())
        fragmento = re.sub(padrao, "", fragmento, flags=re.I | re.S)

    puxar(r"<title>.*?</title>")
    puxar(r"<link\b[^>]*>")
    puxar(r"<style\b[^>]*>.*?</style>")

    if not any(p.lower().startswith("<title") for p in cabeca_partes):
        print("aviso: fragmento sem <title>", file=sys.stderr)

    pagina = MOLDE.format(
        descricao=DESCRICAO,
        cabeca="\n".join(cabeca_partes) + "\n",
        corpo=fragmento.strip() + "\n",
    )

    io.open(SAIDA, "w", encoding="utf-8", newline="\n").write(pagina)
    print(f"{SAIDA.name} gerado ({len(pagina):,} bytes) a partir de {FRAGMENTO.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
