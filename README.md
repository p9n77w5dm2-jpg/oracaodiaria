# Antes de levantar a voz

Cartão de bolso para orar em voz alta na igreja sem o peso de improvisar.
Orações curtas prontas para ler, frases-semente, versículos conferidos,
uma escada de prática e um exercício diário de intercessão.

Feito para Portimão, Algarve.

## Como está montado

Uma fonte, duas saídas:

| Ficheiro | O que é |
|---|---|
| `cartao.html` | **A fonte.** Fragmento HTML (sem `<html>`/`<head>` — o visualizador de Artifacts embrulha). Editar só aqui. |
| `build.py` | Embrulha o fragmento num documento completo. |
| `index.html` | **Gerado.** É o que o GitHub Pages serve. Não editar à mão. |
| `icone.svg`, `manifest.webmanifest` | Ícone e metadados para "adicionar ao ecrã principal" no telemóvel. |

Depois de mexer em `cartao.html`:

```bash
python build.py
```

## Publicar

O Pages serve a partir do `main`, pasta raiz:

**Settings → Pages → Source: Deploy from a branch → Branch: `main` / `(root)`**

Fica em `https://p9n77w5dm2-jpg.github.io/oracaodiaria/` um a dois minutos depois do push.

## No telemóvel

Abrir o link e usar **Adicionar ao ecrã principal** (Safari: Partilhar → Adicionar ao Ecrã Principal; Chrome: menu → Adicionar à página inicial). Abre em ecrã inteiro, sem barra de endereço.

## Impressão

`Ctrl`+`P` imprime só as orações curtas, uma por bloco — a folha que cabe no bolso.
As orações longas, os versículos e o índice ficam de fora de propósito.

## Notas

- A página não guarda nada num servidor. Os degraus marcados na escada ficam
  apenas no `localStorage` do próprio navegador.
- O cabeçalho traz `noindex, nofollow`: mesmo com o repositório público,
  a página não é indexada por motores de busca.
- Traduções bíblicas: **ARA** (Almeida Revista e Atualizada) e **ARC**
  (Almeida Revista e Corrigida), indicadas em cada citação.
