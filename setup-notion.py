"""
Nomad Talks — Notion Database Setup Script
Run this once to build your full CRM database.

Requirements: Python 3 (already on your Mac — no installs needed)

How to run:
  NOTION_TOKEN=your_secret_here python3 setup-notion.py

Replace your_secret_here with your Internal Integration Secret from
notion.so/my-integrations (the ntn_... token).
"""

import urllib.request
import urllib.error
import json
import os
import sys

# ── Config ──────────────────────────────────────────────────────────────────
NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID  = "33ded859-1c8a-80f9-abb4-c7eb9aa6e0bf"

if not NOTION_TOKEN:
    print("\nError: NOTION_TOKEN not set.")
    print("Run as: NOTION_TOKEN=ntn_... python3 setup-notion.py\n")
    sys.exit(1)
# ────────────────────────────────────────────────────────────────────────────

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def notion_request(method, path, body=None):
    url  = f"https://api.notion.com/v1{path}"
    data = json.dumps(body).encode() if body else None
    req  = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        error = json.loads(e.read())
        print(f"\n  ERROR {e.code}: {error.get('message', e.reason)}")
        if e.code == 404:
            print("  → Database not found. Check the ID and make sure you've connected")
            print("    the integration: open the Notion page → ... → Connections → Nomad Talks")
        if e.code == 401:
            print("  → Token rejected. Regenerate it at notion.so/my-integrations")
        raise SystemExit(1)

def update_database():
    print("\nBuilding Nomad Talks CRM in Notion...")
    print("=" * 50)

    properties = {
        # ── Rename the default title field ──────────────────
        "Name": {
            "name": "Guest Name"
        },

        # ── Text fields ─────────────────────────────────────
        "Instagram Handle": { "rich_text": {} },
        "Voyage Number":    { "rich_text": {} },
        "Episode Title":    { "rich_text": {} },
        "Guest Bio":        { "rich_text": {} },
        "Notes":            { "rich_text": {} },

        # ── URL fields ───────────────────────────────────────
        "LinkedIn URL":    { "url": {} },
        "Recording Link":  { "url": {} },
        "Published URL":   { "url": {} },

        # ── Date fields ──────────────────────────────────────
        "Record Date":  { "date": {} },
        "Publish Date": { "date": {} },

        # ── Checkboxes ───────────────────────────────────────
        "SMMA Follow-up Done?": { "checkbox": {} },
        "Prep Doc Sent?":       { "checkbox": {} },

        # ── Select: Pipeline Stage ───────────────────────────
        "Pipeline Stage": {
            "select": {
                "options": [
                    { "name": "Prospecting",       "color": "gray"   },
                    { "name": "Contacted",          "color": "yellow" },
                    { "name": "Pre-Chat Booked",    "color": "blue"   },
                    { "name": "Pre-Chat Done",      "color": "purple" },
                    { "name": "Podcast Booked",     "color": "orange" },
                    { "name": "Recorded",           "color": "pink"   },
                    { "name": "Published",          "color": "green"  },
                ]
            }
        },

        # ── Select: SMMA Lead Potential ──────────────────────
        "SMMA Lead Potential": {
            "select": {
                "options": [
                    { "name": "Hot",       "color": "red"    },
                    { "name": "Warm",      "color": "orange" },
                    { "name": "Not a fit", "color": "gray"   },
                ]
            }
        },

        # ── Select: Outreach Channel ─────────────────────────
        "Outreach Channel": {
            "select": {
                "options": [
                    { "name": "Instagram", "color": "purple" },
                    { "name": "LinkedIn",  "color": "blue"   },
                ]
            }
        },
    }

    body = {
        "title": [{ "text": { "content": "Nomad Talks — Voyage CRM" } }],
        "properties": properties,
    }

    result = notion_request("PATCH", f"/databases/{DATABASE_ID}", body)

    print(f"\n  Database title: {result['title'][0]['plain_text']}")
    print(f"  Properties added: {len(result['properties'])}")
    print()

    for name in result["properties"]:
        ptype = result["properties"][name]["type"]
        print(f"  ✓  {name:30s} ({ptype})")

    print()
    print("=" * 50)
    print("Done! Your Notion CRM is ready.")
    print()
    print("Now create these 3 views manually in Notion (takes 3 min):")
    print()
    print("  1. PIPELINE BOARD")
    print("     + Add view → Board → Group by: Pipeline Stage")
    print("     Show on cards: Voyage Number, SMMA Lead Potential, Record Date")
    print()
    print("  2. ALL EPISODES (already exists as default table)")
    print("     Click Sort → Record Date → Ascending")
    print()
    print("  3. SMMA LEADS")
    print("     + Add view → Table → name it 'SMMA Leads'")
    print("     Filter → SMMA Lead Potential → is → Hot")
    print("     + Add filter → SMMA Lead Potential → is → Warm → set to OR")
    print()
    print("Then come back and we'll find your first guests.")


if __name__ == "__main__":
    update_database()
