"""Structure and reference self-test for guided-topic-selection."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(condition, message, failures):
    if condition:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")
        failures.append(message)


def main():
    failures = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    check(skill.startswith("---\n"), "SKILL.md has YAML frontmatter", failures)
    for field in ("name: guided-topic-selection", "description:", "allowed-tools:"):
        check(field in skill.split("---", 2)[1], f"frontmatter contains {field}", failures)

    for rel in (
        "references/workflow.md",
        "references/evidence-discipline.md",
        "references/privacy.md",
        "references/report-template.md",
        "references/demo-pack.md",
        "assets/candidates.example.yml",
        "README.md",
        "LICENSE",
    ):
        check((ROOT / rel).is_file(), f"exists: {rel}", failures)
        check(rel in skill or rel in (ROOT / "README.md").read_text(encoding="utf-8"),
              f"referenced: {rel}", failures)

    workflow = (ROOT / "references/workflow.md").read_text(encoding="utf-8")
    steps = re.findall(r"^## 第 (\d) 步", workflow, flags=re.M)
    check(steps == [str(n) for n in range(1, 9)], "workflow has exactly 8 ordered steps", failures)

    report = (ROOT / "references/report-template.md").read_text(encoding="utf-8")
    for section in ("论文清单", "证据矩阵", "研究版图", "候选", "可行性", "评分排序", "结论"):
        check(section in report, f"report template has section: {section}", failures)

    demo = (ROOT / "references/demo-pack.md").read_text(encoding="utf-8")
    check("主推荐 1" in demo and "主推荐 2" in demo and "备选 1–4" in demo,
          "demo pack has 2 main + 4 backup candidates", failures)

    if failures:
        print(f"\n[FAIL] {len(failures)} check(s) failed.")
        return 1
    print("\n[OK] all structure checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
