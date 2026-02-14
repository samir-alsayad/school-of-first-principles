# Mission: a04_alert_protocol

## The Objective
Standard Markdown rendering is good, but our curriculum uses GitHub-style **Alerts** (e.g., `> [!IMPORTANT]`). In this mission, you will learn how to customize the Rich rendering logic to turn these plain text alerts into beautiful, color-coded callout panels.

---

## 🏗️ The Setup
You will need a mission file that contains a `[!NOTE]` or `[!IMPORTANT]` alert.

---

## 🛠️ The Tasks

### 1. Identifying the Pattern
Rich's `Markdown` object allows for custom parsing. However, for a simple implementation, you will create a **Pre-Processor** or a **Custom Render Helper**.

### 2. The Alert Wrapper
Create a helper function that detects lines starting with `> [!` and wraps the subsequent block in a `rich.panel.Panel` with a specific `border_style` (e.g., `blue` for Note, `yellow` for Warning).

### 3. The Visual Polish
Update your `school read` command to use this helper. Ensure that:
- **IMPORTANT** alerts are Red.
- **NOTE** alerts are Blue.
- **TIP** alerts are Green.

---

## 🎯 Verification Criteria
- [ ] Your `school read` command now renders alerts as distinct, colored boxes.
- [ ] You can explain how to intercept and modify the Markdown rendering stream.
- [ ] The TUI now feels more "Agentic" and communicates importance through color.
