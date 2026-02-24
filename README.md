```
   _   _
  ( ) ( )    S K I L L F O R G E
  ( ~~~ )    ──────────────────────────────────────────────────────
  ( ~~~ )    The skill that builds skills.  by @lijinnair  ·  v5.2.0  ·  MIT
   '---'
```

> **The skill that builds skills.** Generate optimized Claude Code & Antigravity SKILL.md files with live doc sync, marketplace search, and self-validation — in minutes.

---

**Built by [Lijin Nair](https://github.com/lijinnair)** · MIT License · v5.2.0

---

## 🎯 What it does
Skillforge acts as a strict Conversational Architect that takes your raw ideas or messy prompts and automatically structures them into a perfect `SKILL.md` file. It handles Front Matter engineering, trigger phrase optimization, tool assignment, subagent isolation, and scaffold generation — all in one automated pipeline.

## 🧠 Why it exists
Feeding AI agents long, theoretical documents causes massive token/context bloat and leads to inconsistent results. Skillforge enforces the **"Progressive Disclosure"** strategy:
- Small, efficient footprints in the context window
- Deterministic logic offloaded to separate scripts
- Examples and references loaded only when needed
- Step-by-step imperative execution pipelines

## 🕰️ When to use it
Trigger Skillforge whenever you want to:
- Turn a repeatable workflow into a one-shot command
- Convert messy prompt instructions into a structured agent skill
- Teach Claude or Antigravity your specific business rules or processes

**How to trigger it:**
Simply say: *"I want to build a new skill"* or run `/skillforge`

## 📍 Where it lives

**This meta-skill:**
`~/.gemini/antigravity/skills/skillforge/`

**Skills it generates — your choice:**
| Ecosystem | Path |
|---|---|
| Native Claude Code | `~/.claude/skills/[skill-name]/` |
| Antigravity | `~/.gemini/antigravity/skills/[skill-name]/` |

## ⚙️ How it works (The Pipeline)

1. **Live Docs Sync** — Silently fetches the latest rules from `code.claude.com` and `antigravity.google`
2. **Interactive Checkpoint** — Pauses, shows you what it found, and asks for permission to proceed. If docs are unreachable, shows the cached version & last-updated date and prompts you to continue or retry.
3. **Intake & Category Tagging** — Asks for your skill name, category, ecosystem, triggers, inputs, outputs, and tool requirements
4. **Front Matter Engineering** — Writes a perfectly spec-compliant, sub-1024-character Front Matter block with `user-invocable`, `disable-model-invocation`, and `context: fork` where applicable
5. **SOP Translation** — Converts your workflow into an imperative, numbered execution pipeline
6. **Scaffold & Self-Validation** — Outputs the `mkdir` command and `SKILL.md` code block, then runs an 8-point checklist to validate its own output before delivery

## 📁 Repository Structure

```
skillforge/
├── SKILL.md          ← The core SOP (active v5.0.0)
├── README.md         ← This file
├── CHANGELOG.md      ← Full version history
├── CONTRIBUTING.md   ← How to contribute
├── LICENSE           ← MIT
└── examples/
    ├── seo-page-auditor.SKILL.md
    └── git-commit-formatter.SKILL.md
```

## 👤 Author

```
██╗     ██╗     ██╗██╗███╗  ██╗    ███╗  ██╗ █████╗ ██╗██████╗ 
██║     ██║     ██║██║████╗ ██║    ████╗ ██║██╔══██╗██║██╔══██╗
██║     ██║     ██║██║██╔██╗██║    ██╔██╗██║███████║██║██████╔╝
██║     ██║██   ██║██║██║╚████║    ██║╚████║██╔══██║██║██╔══██╗
███████╗╚████████╔╝██║██║ ╚███║    ██║ ╚███║██║  ██║██║██║  ██║
╚══════╝ ╚═══════╝ ╚═╝╚═╝  ╚══╝    ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
```

**Lijin Nair** — AI Systems Builder & Prompt Architect
- GitHub: [@lijinnair](https://github.com/lijinnair)
- Built for the Claude Code & Antigravity ecosystem

---

*If this helped you, please ⭐ the repo — it helps others find it!*
