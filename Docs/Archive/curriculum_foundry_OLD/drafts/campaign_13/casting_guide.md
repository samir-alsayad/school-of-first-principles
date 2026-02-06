# Casting Guide: school-campaign-v1 Protocol
**Archetype**: The Architect
**Status**: Ready for The Pour

## 1. The Mold (Source)
*   **Manifest**: `foundry/drafts/campaign_13/manifest.yaml`
*   **Codex**: `foundry/drafts/campaign_13/codex.md`
*   **Framework**: `foundry/drafts/campaign_13/framework.md`

## 2. The Cast (Destination)
We are installing a new Protocol into the **GAP System**.

### Step 1: Create the Domain Directory
```bash
mkdir -p "/Users/Shared/Projects/Gated Agent Protocol/domains/school-of-first-principles/campaign"
```

### Step 2: Pour the Manifest
```bash
cp "/Users/Shared/Projects/school-of-first-principles/curriculum/foundry/drafts/campaign_13/manifest.yaml" \
   "/Users/Shared/Projects/Gated Agent Protocol/domains/school-of-first-principles/campaign/manifest.yaml"
```

### Step 3: Archive the Logic
Move the support docs to the domain for reference.
```bash
cp "/Users/Shared/Projects/school-of-first-principles/curriculum/foundry/drafts/campaign_13/codex.md" \
   "/Users/Shared/Projects/Gated Agent Protocol/domains/school-of-first-principles/campaign/codex.md"
cp "/Users/Shared/Projects/school-of-first-principles/curriculum/foundry/drafts/campaign_13/framework.md" \
   "/Users/Shared/Projects/Gated Agent Protocol/domains/school-of-first-principles/campaign/framework.md"
```

## 3. Verification
Run `gap list` (or equivalent survey) to confirm `school-campaign-v1` is active.
