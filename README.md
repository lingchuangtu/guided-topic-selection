# guided-topic-selection（问答式选题引导 Skill）

一个 WorkBuddy / Claude Skill：以"一次一问"的方式，把用户从"没有题目"带到"锁定题目"。先展示选题八步全流程，再逐步收集目标、论文素材、证据矩阵与研究版图，生成候选并做拥挤度、可行性与评分判断，最终输出《选题报告》与候选清单。

Works with WorkBuddy / Claude.

## 一句话安装（推荐）

把下面这句话发给 WorkBuddy / Claude / 豆包等任意 AI，即可自动安装：

```text
帮我安装github上的 lingchuangtu/guided-topic-selection
```

AI 会自动读取该仓库的 `SKILL.md`，安装到 skills 目录。不需要 git、不需要命令行。

<details>
<summary>AI 无法联网拉取仓库时，用这段自包含指令兜底</summary>

复制 [INSTALL.md](INSTALL.md) 中「请帮我在本地安装一个 WorkBuddy / Claude Skill」那段代码块的全部内容，粘贴到对话框发送即可，不依赖 GitHub。

</details>

## 核心约定

- 一次一问：每轮开头显示 `当前步骤：N/8｜步骤名`，用户一次给足信息就直接跳步。
- 证据分级：关键判断标注 `[论文证据]` / `[外部证据]` / `[推断]`。
- 默认不联网：只基于用户提供的论文判断；只有用户明确要求时才联网查新。
- 强制匿名：全程不出现用户、作者、机构的真实身份信息，文献用代号。

## 安装

将本目录放到：

- WorkBuddy 用户级：`~/.workbuddy/skills/guided-topic-selection/`
- WorkBuddy 项目级：`.workbuddy/skills/guided-topic-selection/`
- Claude：把本目录放入项目的 skills 目录，并保留 `SKILL.md` 的 frontmatter。

无需依赖；仅 `tests/selftest.py` 使用 Python 3 标准库。

## 使用

1. 说"帮我选题 / 论文选题 / 毕业设计选题"触发 Skill。
2. 按 8 步回答提问：校准目标 → 收集素材 → 建立证据 → 研究版图 → 生成候选 → 拥挤度判断 → 判可行性 → 定题落地。
3. 输出《选题报告》，并从 A/B/C/D 四个定题入口中选择。

想快速看完整流程时说"演示 / demo / 走一遍流程"，Skill 会用 `references/demo-pack.md` 的预置证据，但**仍完整保留一次一问的问答节奏**。

## 文件结构

```
guided-topic-selection/
├── SKILL.md                         # 入口：启动话术、协议摘要、规则指引
├── README.md
├── references/
│   ├── workflow.md                  # 8 步完整提问清单、候选句式与定题入口
│   ├── evidence-discipline.md       # 证据标注、联网查新与引文纪律
│   ├── privacy.md                   # 强制匿名与隐私约定
│   ├── report-template.md           # 《选题报告》结构模板
│   └── demo-pack.md                 # 演示模式预置示例（虚构）
├── assets/
│   └── candidates.example.yml       # 选题候选.yml 示例
├── tests/
│   └── selftest.py                  # 结构与引用自检
└── LICENSE
```

## 测试

```
python tests/selftest.py
```

检查 SKILL.md frontmatter、被引用文件是否存在、8 步流程与交付结构是否齐全。

## 免责声明

仅提供选题方法论与证据整理辅助，不替代学术判断，不保证查重、评审或答辩结果；候选创新的最终判断由使用者结合真实文献与导师意见完成。
