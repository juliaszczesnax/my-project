# Nomad Talks — Notion Database Schema
### Build this in under 1 hour. Duplicate and go.

---

## DATABASE NAME
**Nomad Talks — Voyage CRM**

---

## PROPERTIES (Fields)

Create the following properties in this order. Each row = one guest/episode.

| # | Property Name | Property Type | Options / Notes |
|---|---|---|---|
| 1 | **Guest Name** | Title | Primary field. First + Last name. |
| 2 | **Instagram Handle** | Text | e.g. `@username` |
| 3 | **LinkedIn URL** | URL | Full profile link |
| 4 | **Pipeline Stage** | Select | See options below ↓ |
| 5 | **Voyage Number** | Text | e.g. `Voyage 01`, `Voyage 12` |
| 6 | **Episode Title** | Text | e.g. *"How I Left My Job and Never Looked Back"* |
| 7 | **Record Date** | Date | Date of Riverside.fm recording |
| 8 | **Publish Date** | Date | Date episode goes live |
| 9 | **SMMA Lead Potential** | Select | See options below ↓ |
| 10 | **SMMA Follow-up Done?** | Checkbox | Tick when done |
| 11 | **Guest Bio** | Text | 3-5 bullet points the guest sends you |
| 12 | **Notes** | Text | Your personal notes after each interaction |
| 13 | **Outreach Channel** | Select | See options below ↓ |
| 14 | **Prep Doc Sent?** | Checkbox | Tick when sent |
| 15 | **Recording Link** | URL | Riverside.fm session link |
| 16 | **Published URL** | URL | YouTube or Instagram link after publishing |

---

## SELECT FIELD OPTIONS

### Pipeline Stage
Add these in order (Notion will display them as a Kanban column each):

| Stage | Suggested Colour |
|---|---|
| Prospecting | Gray |
| Contacted | Yellow |
| Pre-Chat Booked | Blue |
| Pre-Chat Done | Purple |
| Podcast Booked | Orange |
| Recorded | Pink |
| Published | Green |

### SMMA Lead Potential

| Option | Colour |
|---|---|
| Hot | Red |
| Warm | Orange |
| Not a fit | Gray |

### Outreach Channel

| Option | Colour |
|---|---|
| Instagram | Purple |
| LinkedIn | Blue |

---

## VIEWS TO CREATE

### View 1 — Board (Kanban by Pipeline Stage)
- **View type:** Board
- **Group by:** Pipeline Stage
- **Visible properties on cards:** Guest Name, Voyage Number, SMMA Lead Potential, Record Date
- **Name:** `Pipeline Board`

**How to create:**
1. Click `+ Add a view` → select `Board`
2. Set `Group by` → `Pipeline Stage`
3. Click `Properties` → show: Voyage Number, SMMA Lead Potential, Record Date
4. Name the view `Pipeline Board`

---

### View 2 — Table sorted by Record Date
- **View type:** Table
- **Sort:** Record Date → Ascending
- **All properties visible**
- **Name:** `All Episodes`

**How to create:**
1. Click `+ Add a view` → select `Table`
2. Click `Sort` → `Record Date` → `Ascending`
3. Name the view `All Episodes`

---

### View 3 — Filtered SMMA Leads
- **View type:** Table
- **Filter:** SMMA Lead Potential = `Hot` OR `Warm`
- **Visible properties:** Guest Name, Pipeline Stage, SMMA Lead Potential, SMMA Follow-up Done?, Notes, Published URL
- **Name:** `SMMA Leads`

**How to create:**
1. Click `+ Add a view` → select `Table`
2. Click `Filter` → `SMMA Lead Potential` → `is` → select `Hot`
3. Click `+ Add filter rule` → `SMMA Lead Potential` → `is` → select `Warm`
4. Make sure filter logic is set to `OR` (not AND)
5. Click `Properties` → show only: Guest Name, Pipeline Stage, SMMA Lead Potential, SMMA Follow-up Done?, Notes, Published URL
6. Name the view `SMMA Leads`

---

## SETUP TIPS

- **Start with one test entry:** Add yourself as a fake guest and run through all stages so you know the system works.
- **Pin the Pipeline Board as the default view** — it's the one you'll open every day.
- **Use the Notes field aggressively** — even one line after every interaction saves you next time.
- **Emoji tip:** Add emoji to your Pipeline Stage options (e.g. `🎙️ Recorded`, `✅ Published`) to make the Kanban board more visual. Totally optional.

---

## BUILD ORDER (fastest path, under 1 hour)

1. Create new Notion database (full page)
2. Rename title field to "Guest Name"
3. Add all 15 remaining properties in order
4. Set up Select field options (Pipeline Stage, SMMA Lead Potential, Outreach Channel)
5. Create the 3 views
6. Add one test entry and move it through all Pipeline stages
7. Done ✅
