#!/usr/bin/env python3
"""Valida o contrato estático de gerador-logomarca.

Este validador usa somente a biblioteca padrão. Ele valida estrutura, metadados,
referências, casos declarativos e, opcionalmente, o pacote de plugin e sua
paridade com a Skill standalone. Ele NÃO simula o roteador semântico do host e
NÃO executa evals de qualidade do modelo.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_NAME = "gerador-logomarca"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
REQUIRED_TEST_CATEGORIES = {
    "activation-positive", "activation-negative", "incomplete-brief",
    "complete-brief", "concept-change", "existing-brand-reference",
    "prompt-creation", "image-request", "logo-review", "boundary",
    "safety-regression",
}
REQUIRED_REFS = {
    "activation-policy.md", "branding-workflow.md", "logo-design-principles.md",
    "prompt-engineering.md", "review-checklist.md",
}
TEMP_NAMES = {"__pycache__", ".DS_Store"}
TEMP_SUFFIXES = {".pyc", ".pyo", ".tmp", ".swp"}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--plugin-root", type=Path, help="Valida plugin.json, layout e paridade da Skill empacotada.")
    return p.parse_args()


def read_text(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"arquivo ausente: {path}")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"não foi possível ler {path}: {exc}")
        return ""


def parse_frontmatter(text: str, errors: list[str]) -> tuple[dict[str, str], str]:
    m = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.S)
    if not m:
        errors.append("SKILL.md deve conter front matter delimitado por --- e corpo não vazio")
        return {}, ""
    raw, body = m.groups()
    fields: dict[str, str] = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value in {">", ">-", "|", "|-"}:
            block = []
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith((" ", "\t"))):
                block.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(x for x in block if x).strip()
            continue
        fields[key] = value.strip('"\'')
        i += 1
    return fields, body


def parse_openai_yaml_subset(text: str, errors: list[str]) -> dict[str, str]:
    """Valida o subconjunto YAML usado neste arquivo; não pretende ser parser YAML geral."""
    if not text.strip():
        return {}
    values: dict[str, str] = {}
    lines = text.splitlines()
    if not re.fullmatch(r"interface:\s*", lines[0]):
        errors.append("agents/openai.yaml: raiz deve iniciar com 'interface:'")
        return values
    allowed = {"display_name", "short_description", "default_prompt"}
    for lineno, line in enumerate(lines[1:], 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.fullmatch(r"  ([a-z_]+):\s*(.+)", line)
        if not m:
            errors.append(f"agents/openai.yaml:{lineno}: estrutura não suportada/indentação inválida")
            continue
        key, raw = m.groups()
        if key not in allowed:
            errors.append(f"agents/openai.yaml:{lineno}: chave inesperada em interface: {key}")
            continue
        if key in values:
            errors.append(f"agents/openai.yaml:{lineno}: chave duplicada: {key}")
            continue
        raw = raw.strip()
        if len(raw) < 2 or raw[0] != '"' or raw[-1] != '"':
            errors.append(f"agents/openai.yaml:{lineno}: valor de {key} deve ser string entre aspas duplas")
            continue
        try:
            values[key] = json.loads(raw)
        except json.JSONDecodeError:
            errors.append(f"agents/openai.yaml:{lineno}: string inválida em {key}")
    for key in allowed:
        if not values.get(key, "").strip():
            errors.append(f"agents/openai.yaml: campo obrigatório ausente/vazio: interface.{key}")
    return values


def find_temp_artifacts(root: Path) -> list[Path]:
    found = []
    for p in root.rglob("*"):
        if p.name in TEMP_NAMES or (p.is_file() and p.suffix in TEMP_SUFFIXES):
            found.append(p)
    return found


def file_map(root: Path) -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            out[p.relative_to(root).as_posix()] = p.read_bytes()
    return out


def validate_skill(root: Path, errors: list[str]) -> None:
    if not root.is_dir():
        errors.append(f"diretório da Skill ausente: {root}")
        return
    if root.name != SKILL_NAME:
        errors.append(f"diretório da Skill deve se chamar {SKILL_NAME}: {root.name}")

    skill = read_text(root / "SKILL.md", errors)
    fields, body = parse_frontmatter(skill, errors)
    name, desc = fields.get("name", ""), fields.get("description", "")
    if name != SKILL_NAME or name != root.name:
        errors.append(f"front matter name deve ser {SKILL_NAME} e coincidir com o diretório")
    if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("front matter name deve usar kebab-case")
    if not (1 <= len(name) <= 64):
        errors.append("front matter name fora de 1..64 caracteres")
    if not (1 <= len(desc) <= 1024):
        errors.append("front matter description fora de 1..1024 caracteres")
    if not body.strip():
        errors.append("corpo do SKILL.md vazio")
    version_match = re.search(r"(?m)^metadata:\s*\n(?:[ \t]+.*\n)*?[ \t]+version:\s*[\"\']([^\"\']+)[\"\']\s*$", skill)
    if not version_match or not re.fullmatch(r"\d+\.\d+\.\d+", version_match.group(1)):
        errors.append("SKILL.md: metadata.version deve usar SemVer MAJOR.MINOR.PATCH")

    refs = root / "references"
    for filename in sorted(REQUIRED_REFS):
        read_text(refs / filename, errors)
    for target in re.findall(r"`(references/[^`]+\.md)`", skill):
        if not (root / target).is_file():
            errors.append(f"referência quebrada em SKILL.md: {target}")

    agent_text = read_text(root / "agents/openai.yaml", errors)
    parse_openai_yaml_subset(agent_text, errors)

    tests_path = root / "tests/cases.json"
    raw_tests = read_text(tests_path, errors)
    if raw_tests:
        try:
            data = json.loads(raw_tests)
        except json.JSONDecodeError as exc:
            errors.append(f"tests/cases.json inválido: {exc}")
        else:
            if data.get("schema_version") != "1.0":
                errors.append("tests/cases.json: schema_version deve ser '1.0'")
            cases = data.get("cases")
            if not isinstance(cases, list) or not cases:
                errors.append("tests/cases.json: cases deve ser lista não vazia")
                cases = []
            ids = []
            categories = set()
            activations = set()
            for idx, case in enumerate(cases, 1):
                if not isinstance(case, dict):
                    errors.append(f"tests/cases.json: caso #{idx} não é objeto")
                    continue
                cid = case.get("id")
                if not isinstance(cid, str) or not cid.strip():
                    errors.append(f"tests/cases.json: caso #{idx} sem id válido")
                else:
                    ids.append(cid)
                cat = case.get("category")
                if not isinstance(cat, str) or not cat.strip():
                    errors.append(f"tests/cases.json: {cid or idx} sem category válida")
                else:
                    categories.add(cat)
                if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
                    errors.append(f"tests/cases.json: {cid or idx} sem prompt válido")
                activation = case.get("expected_activation")
                if activation not in (True, False, "ambiguous"):
                    errors.append(f"tests/cases.json: {cid or idx} expected_activation inválido")
                else:
                    activations.add(str(activation))
                # Casos positivos/ambíguos e categorias comportamentais devem declarar expectativas.
                expect = case.get("expect")
                if activation is not False or cat not in {"activation-negative"}:
                    if not isinstance(expect, list) or not expect or not all(isinstance(x, str) and x.strip() for x in expect):
                        errors.append(f"tests/cases.json: {cid or idx} deve declarar expect não vazio")
            if len(ids) != len(set(ids)):
                errors.append("tests/cases.json: IDs duplicados")
            missing = REQUIRED_TEST_CATEGORIES - categories
            if missing:
                errors.append("tests/cases.json: categorias ausentes: " + ", ".join(sorted(missing)))
            if "True" not in activations or "False" not in activations or "ambiguous" not in activations:
                errors.append("tests/cases.json deve conter ativação true, false e ambiguous")

    for p in find_temp_artifacts(root):
        errors.append(f"artefato temporário presente: {p.relative_to(root)}")


def validate_plugin(plugin_root: Path, standalone_root: Path, errors: list[str]) -> None:
    if not plugin_root.is_dir():
        errors.append(f"diretório do plugin ausente: {plugin_root}")
        return
    manifest_path = plugin_root / "plugin.json"
    raw = read_text(manifest_path, errors)
    manifest = None
    if raw:
        try:
            manifest = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"plugin.json inválido: {exc}")
    if isinstance(manifest, dict):
        if manifest.get("$schema") != PLUGIN_SCHEMA:
            errors.append(f"plugin.json: $schema deve ser {PLUGIN_SCHEMA}")
        if manifest.get("name") != SKILL_NAME:
            errors.append(f"plugin.json: name deve ser {SKILL_NAME}")
        version = manifest.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append("plugin.json: version deve usar SemVer MAJOR.MINOR.PATCH")
        if not isinstance(manifest.get("description"), str) or not manifest["description"].strip():
            errors.append("plugin.json: description obrigatória")

    packaged = plugin_root / "skills" / SKILL_NAME
    if not packaged.is_dir():
        errors.append(f"plugin: Skill ausente em skills/{SKILL_NAME}/")
    else:
        validate_skill(packaged, errors)
        try:
            left, right = file_map(standalone_root), file_map(packaged)
        except OSError as exc:
            errors.append(f"falha ao comparar standalone/plugin: {exc}")
        else:
            only_left = sorted(set(left) - set(right))
            only_right = sorted(set(right) - set(left))
            changed = sorted(k for k in set(left) & set(right) if left[k] != right[k])
            if only_left:
                errors.append("plugin sem arquivos da standalone: " + ", ".join(only_left))
            if only_right:
                errors.append("plugin contém arquivos extras na Skill: " + ", ".join(only_right))
            if changed:
                errors.append("divergência byte a byte standalone/plugin: " + ", ".join(changed))

    for p in find_temp_artifacts(plugin_root):
        errors.append(f"plugin contém artefato temporário: {p.relative_to(plugin_root)}")


def main() -> int:
    args = parse_args()
    skill_root = args.skill_root.resolve()
    errors: list[str] = []
    validate_skill(skill_root, errors)
    if args.plugin_root:
        validate_plugin(args.plugin_root.resolve(), skill_root, errors)
    if errors:
        print("FALHA")
        for error in errors:
            print("-", error)
        return 1
    mode = "Skill + plugin + paridade" if args.plugin_root else "Skill standalone"
    print(f"OK: {mode} — contrato estático válido.")
    print("LIMITAÇÃO: roteamento semântico e qualidade das respostas exigem evals no host/modelo e não foram simulados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
