#!/usr/bin/env python3
"""Confere os arquivos de pacote do Humanizador, sem dependência externa."""

from __future__ import annotations

import json
import re
from pathlib import Path

TOTAL_PADROES = 42

RAIZ = Path(__file__).resolve().parent.parent
CAMINHO_SKILL = RAIZ / "SKILL.md"
SKILL = CAMINHO_SKILL.read_text(encoding="utf-8")
README = (RAIZ / "README.md").read_text(encoding="utf-8")
AGENTS = (RAIZ / "AGENTS.md").read_text(encoding="utf-8")
PLUGIN = json.loads((RAIZ / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
MARKET = json.loads((RAIZ / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))


def exigir(match: re.Match[str] | None, mensagem: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(f"ERRO: {mensagem}")
    return match


metadata = exigir(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "o SKILL.md precisa comecar com metadata YAML",
).group(1)

for campo in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(campo)}", metadata):
        raise SystemExit(f"ERRO: remova o campo YAML nao suportado: {campo[:-1]}")

if not re.search(r"(?m)^name:\s*humanizador\s*$", metadata):
    raise SystemExit("ERRO: o name da skill precisa ser humanizador")

versao_skill = exigir(
    re.search(r'(?m)^\s+version:\s*["\']([^"\']+)["\']\s*$', metadata),
    "adicione metadata.version ao SKILL.md",
).group(1)
versao_readme = exigir(
    re.search(r"(?m)^- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README),
    "adicione uma entrada de historico de versao ao README.md",
).group(1)

versoes = {versao_skill, versao_readme, str(PLUGIN.get("version", ""))}
if len(versoes) != 1:
    raise SystemExit(f"ERRO: use uma versao so em todos os arquivos: {sorted(versoes)}")

arquivos_skill = {caminho.relative_to(RAIZ) for caminho in RAIZ.rglob("SKILL.md")}
if CAMINHO_SKILL.is_symlink() or arquivos_skill != {Path("SKILL.md")}:
    raise SystemExit(f"ERRO: mantenha um SKILL.md so, na raiz: {sorted(map(str, arquivos_skill))}")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("ERRO: aponte o carregador de skills do plugin para a raiz do repositorio")
if PLUGIN.get("name") != MARKET["plugins"][0].get("name"):
    raise SystemExit("ERRO: o name do plugin precisa bater entre plugin.json e marketplace.json")

regras_estilo = (
    "## Estilo de escrita",
    "Comece pelo ponto principal.",
    "Use palavras comuns e voz ativa.",
    "Frases e paragrafos curtos.".replace("paragrafos", "par\u00e1grafos"),
    'Use "precisa" para requisito.',
    "Preserve o sentido tecnico completo.".replace("tecnico", "t\u00e9cnico"),
)
faltando = [regra for regra in regras_estilo if regra not in AGENTS]
if faltando:
    raise SystemExit("ERRO: faltam regras de estilo no AGENTS.md: " + ", ".join(faltando))

numeros_skill = [int(n) for n in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)]
if numeros_skill != list(range(1, TOTAL_PADROES + 1)):
    raise SystemExit(
        f"ERRO: numere os padroes do SKILL.md de 1 a {TOTAL_PADROES}: {numeros_skill}"
    )

numeros_readme = {int(n) for n in re.findall(r"(?m)^\| ([0-9]+) \|", README)}
if numeros_readme != set(numeros_skill):
    faltam = sorted(set(numeros_skill) - numeros_readme)
    sobram = sorted(numeros_readme - set(numeros_skill))
    raise SystemExit(
        f"ERRO: as tabelas do README nao batem com o SKILL.md. Faltam: {faltam}. Sobram: {sobram}"
    )

if f"## Os {TOTAL_PADROES} padr\u00f5es" not in README:
    raise SystemExit(f"ERRO: o titulo do README precisa dizer 'Os {TOTAL_PADROES} padroes'")

print(f"OK: {TOTAL_PADROES} padroes, versao {versao_skill}, pacote consistente.")