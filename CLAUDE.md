# Nomad Talks

## Stack
Markdown-only project. No build/test/lint commands.

## Structure
- `01-message-templates.md` — outreach DM templates (A/B/C)
- `02-sop.md` — episode SOP checklist
- `03-notion-schema.md` — Notion DB setup guide
- `04-calendly-guide.md` — Calendly event setup + confirmation messages
- `05-guest-prep-doc.md` — guest-facing prep doc (share with confirmed guests)
- `06-question-bank.md` — 50+ interview questions in 5 sections

## Rules
- All files are user-facing copy — never auto-compress or rewrite content without explicit ask
- `[PLACEHOLDERS]` in files are intentional — never fill them in
- Branch: `claude/nomad-talks-podcast-system-bt8UJ`
- Commit and push every change to that branch

## Token Rules
- Responses: terse. Lead with answer. No preamble.
- No "I'll now...", "Let me...", "Great!" filler
- No repeating back what user said
- Read only needed lines (use offset+limit)
- Grep before Read — confirm match exists first
- Batch all independent tool calls in one message
- Prefer Edit over Write
- Don't summarize completed tool calls — output next step or done
