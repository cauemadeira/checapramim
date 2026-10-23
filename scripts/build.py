#!/usr/bin/env python3
"""Gera os pacotes da skill a partir de skill/checapramim/.

Saídas em dist/:
  checapramim.zip               pasta completa (SKILL.md + references/)
  checapramim-arquivo-unico.zip só o SKILL.md, com as referências embutidas como anexos
  SKILL.md                      o mesmo arquivo único, solto

Uso: python3 scripts/build.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "skill" / "checapramim"
DIST = ROOT / "dist"

ANEXOS = [
    ("source-credibility", "Anexo A", "Rubrica de credibilidade de fontes"),
    ("verdict-scale", "Anexo B", "Escala de veredito"),
    ("input-types", "Anexo C", "Tratamento por tipo de entrada"),
    ("seed-sources", "Anexo D", "Lista-semente de fontes de partida"),
]


def single_file() -> str:
    text = (SRC / "SKILL.md").read_text(encoding="utf-8")
    for name, letter, _ in ANEXOS:
        text = text.replace(f"`references/{name}.md`", f"o {letter} (no fim deste arquivo)")
    out = text.rstrip() + "\n"
    for name, letter, title in ANEXOS:
        lines = (SRC / "references" / f"{name}.md").read_text(encoding="utf-8").split("\n")
        body, first = [], True
        for line in lines:
            if first and line.startswith("# "):
                body.append(f"# {letter} - {title}")
                first = False
            elif line.startswith("## "):
                body.append("#" + line)
            else:
                body.append(line)
        out += "\n---\n\n" + "\n".join(body).strip() + "\n"
    if "references/" in out:
        raise SystemExit("Sobrou uma remissão a references/ no arquivo único.")
    return out


def write_zip(path: pathlib.Path, files: dict) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arcname, data in sorted(files.items()):
            info = zipfile.ZipInfo(arcname, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)


def main() -> None:
    DIST.mkdir(exist_ok=True)
    full = {
        f"checapramim/{p.relative_to(SRC).as_posix()}": p.read_bytes()
        for p in SRC.rglob("*")
        if p.is_file()
    }
    write_zip(DIST / "checapramim.zip", full)

    merged = single_file()
    (DIST / "SKILL.md").write_text(merged, encoding="utf-8")
    write_zip(DIST / "checapramim-arquivo-unico.zip", {"checapramim/SKILL.md": merged.encode("utf-8")})

    for f in sorted(DIST.iterdir()):
        print(f"{f.name}: {f.stat().st_size} bytes")


if __name__ == "__main__":
    main()
