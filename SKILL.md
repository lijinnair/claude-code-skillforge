---
name: skillforge
description: Generates highly optimized Agent Skills for both native Claude Code and the Antigravity system, according to official best practices and the "Progressive Disclosure" strategy. Use when the user wants to build a new skill, turn a workflow into a skill, optimize an existing prompt, or structure agent instructions for either ecosystem.
license: MIT
metadata:
  author: Lijin Nair
  github: https://github.com/lijinnair
  version: "5.2.0"
---

# Claude/Antigravity Skill Builder SOP

## Goal
Design and generate a highly optimized `SKILL.md` file that strictly adheres to the most up-to-date official documentation and the "Progressive Disclosure" framework. The resulting skill must prevent context bloat, utilize an imperative execution pipeline, and accurately map tools and subagents where necessary. It must be scaffolded correctly based on whether it is intended for native Claude Code or the Antigravity ecosystem.

## Execution Steps

### Step 1: Synchronize with Live Infrastructure (INTERACTIVE CHECKPOINT)
Before asking the user any questions about their skill, you MUST attempt to fetch and read the live documentation:
1. Silently attempt to fetch the official Claude Code docs: `https://code.claude.com/docs/en/`, `https://code.claude.com/docs/en/skills`, and `https://code.claude.com/docs/en/hooks`.
2. Silently attempt to fetch the official Antigravity docs: `https://antigravity.google/docs/home` and `https://antigravity.google/docs/skills`.
3. **If ALL fetches succeed:** Synthesize the core best practices, then present the **Interactive Checkpoint** to the user, summarizing the rules you found. Say: *"Here are the latest best practices fetched live. Would you like to proceed?"* Do NOT continue to Step 2 until the user confirms.
4. **If ANY fetch fails:** Do NOT silently proceed. Instead, present the **Fallback Checkpoint** to the user:
   - State which URL(s) failed.
   - Display your **currently embedded knowledge version** and **last-updated date** (as stored in your training data).
   - Say: *"I was unable to fetch the latest docs. I can proceed using my built-in knowledge (Version: [X], Last Updated: [Date]). Would you like to continue with this, or would you prefer to check your connection and retry?"*
   - **DO NOT PROCEED** until the user explicitly chooses to continue or retry.

### Step 2: Intake, Ecosystem Scoping & Category Tagging
Ask the user to describe the workflow they want to automate. Collect all of the following:
- **Skill Name:** What should the skill be called? (use kebab-case, e.g., `my-skill-name`)
- **Category:** What category does this skill belong to? (e.g., `dev`, `marketing`, `seo`, `document`, `data`, `ops`)
- **Ecosystem:** Native Claude Code (`~/.claude/skills`) or Antigravity (`~/.gemini/antigravity/skills`)?
- **Trigger:** What words or phrases should cause this skill to activate?
- **Inputs:** What raw materials (context, files, arguments) does the agent need at runtime?
- **Output:** What is the exact expected deliverable?
- **External Actions:** Does it require Bash, URL fetching, file reading, or subagent isolation (`context: fork`)?

### Step 2.5: Skill Discovery Check (Don't Reinvent the Wheel)
Before building from scratch, silently search for existing similar skills across the following sources using `search_web` or `read_url_content`:

| # | Source | URL / Query |
|---|---|---|
| 1 | **Smithery** | `https://smithery.ai/skills?q=[skill-name]` |
| 2 | **SkillsMP** | `https://skillsmp.com/search?q=[skill-name]` |
| 3 | **SkillsLLM** | `https://skillsllm.com/search?q=[skill-name]` |
| 4 | **SkillHub / skill-marketplace.com** | `https://skill-marketplace.com/search?q=[skill-name]` |
| 5 | **Antigravity Skill Vault** | `https://github.com/search?q=[skill-name]+topic:antigravity-skill` |
| 6 | **Awesome Skills (sickn33)** | `https://github.com/sickn33/antigravity-awesome-skills` CATALOG.md |
| 7 | **GitHub search** | `https://github.com/search?q=[skill-name]+topic:claude-code-skill` |
| 8 | **Composio** | `https://composio.dev/search?q=[skill-name]` |
| 9 | **AI Templates** | `https://www.aitmpl.com/skills?q=[skill-name]` |

**After searching:**
- If **no similar skill found**: Proceed silently to Step 3.
- If **a similar skill is found**: Present a **Discovery Report** to the user:
  - List the top matches with name, source, star count (if available), and a one-line description.
  - Say: *"I found [N] existing skill(s) similar to what you described. Would you like to: (A) Customise one of these for your needs, or (B) Build a new skill from scratch with your specific requirements?"*
  - If the user chooses **(A)**: Fetch the existing skill, present it, and help them customise it instead of generating from Step 3.
  - If the user chooses **(B)**: Proceed to Step 3.
  - **DO NOT PROCEED** until the user has made a choice.

### Step 3: Front Matter Engineering
Design the Front Matter (must be `< 1024 characters`) based on the documentation rules synced in Step 1.
- **Description:** Must start with a **third-person** action verb (e.g., "Analyzes...", "Generates...").
- **Triggers:** Ensure the description contains 3-5 explicit trigger phrases (e.g., "Use when the user mentions X or Y.").
- **Category metadata:** Include the category from Step 2 as a metadata field (`category: [value]`).
- **Invocation Control:**
  - If the skill executes destructive or automated actions: add `disable-model-invocation: true`.
  - If the skill should only run when explicitly invoked by the user: add `user-invocable: true`.
  - If the skill should run automatically when triggered: omit `user-invocable` (defaults to auto-discover).
- **Advanced Context:** Implement `context: fork` and `allowed-tools` only if required by the workflow from Step 2.

### Step 4: SOP Translation (The Pipeline)
Translate the user's workflow description into a strict, imperative Standard Operating Procedure.
- Break the workflow into numbered `Execution Steps`.
- Each step must start with a direct command verb (e.g., "Extract...", "Analyze...", "Compile...").
- If the workflow requires dynamic context at runtime, use the substitution pattern (e.g., injecting PR diffs with `!\`gh pr diff\``). Reference `$ARGUMENTS` exactly as taught in the live docs.

### Step 5: Separation of Concerns & Scaffold Generation
Determine if deterministic logic should go into a `scripts/` directory. Then, output the exact terminal command based on their ecosystem choice from Step 2:
- Native Claude: `mkdir -p ~/.claude/skills/[skill-name]`
- Antigravity: `mkdir -p ~/.gemini/antigravity/skills/[skill-name]`

Follow this with the raw `SKILL.md` Markdown block so the user can instantly deploy it.

### Step 6: Self-Validation Checklist (MANDATORY BEFORE DELIVERY)
Before delivering the final output to the user, run through this checklist internally and confirm every item passes:
- [ ] Front Matter is under 1024 characters
- [ ] `SKILL.md` body is under 500 lines
- [ ] Description starts with a 3rd-person action verb
- [ ] Description contains at least 3 explicit trigger phrases
- [ ] `category` metadata field is present
- [ ] `user-invocable` or `disable-model-invocation` is set correctly for the use case
- [ ] All SOP steps begin with an imperative command verb
- [ ] The correct `mkdir` path is included for the chosen ecosystem
- [ ] If any item FAILS, fix it before delivering the output.

## Expected Output Format
Deliver a structured Markdown document containing:
1. Confirmation of live sync status (success or fallback version used).
2. The Self-Validation Checklist results (all green).
3. The exact terminal `mkdir` command for the chosen ecosystem.
4. A fully formatted code block containing the exact contents of the `SKILL.md` file.

## Reference Best Practices
- **Progressive Disclosure:** Do not load data into the `SKILL.md` that is only needed for 1 specific path. Link to it instead.
- **Volume:** Keep `SKILL.md` under 500 lines.
- **See `examples/`:** Consult the `examples/` directory in this skill folder for reference outputs.

---
*Built by [Lijin Nair](https://github.com/lijinnair) · Licensed MIT · [skillforge on GitHub](https://github.com/lijinnair/skillforge)*
