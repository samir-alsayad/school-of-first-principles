# Requirements: Scholar CLI Tool

## Glossary
- **Ledger**: The `ledger.yaml` file acting as the persistence layer.
- **Inventory_Item**: A curriculum module with an ID, path, and verification status.
- **Reflection_File**: The `reflection.md` located at the `path` of an Inventory_Item.
- **Status_Token**: The string `**Status**: [Verified]` indicating completion.

## User Stories
### Requirement 1: Character Status
**User Story**: As a Student, I want to see my current level and XP, so that I know my progress.

#### Acceptance Criteria
1. WHEN running `scholar.py status`, THE SYSTEM SHALL read `ledger.yaml`.
2. THE SYSTEM SHALL print the Student Name, Level, and Total XP.
3. THE SYSTEM SHALL list all inventory items with their current status (Locked/Pending/Verified).

### Requirement 2: Verification Logic
**User Story**: As a Student, I want to verify my work automatically, so that I can earn XP.

#### Acceptance Criteria
1. WHEN running `scholar.py verify`, THE SYSTEM SHALL iterate through all `pending` items in the inventory.
2. THE SYSTEM SHALL attempt to open the `reflection.md` at the specified `path`.
3. IF the file contains the Status_Token, THE SYSTEM SHALL mark the item as `verified` in memory.
4. THE SYSTEM SHALL sum the XP of all verified items.
5. THE SYSTEM SHALL not modify the `ledger.yaml` file (Read-Only for this level).

### Requirement 3: Error Handling
**User Story**: As a Student, I want clear errors, so that I know if my configuration is broken.

#### Acceptance Criteria
1. WHEN `ledger.yaml` is missing, THE SYSTEM SHALL print "Error: No ledger found."
2. WHEN a `reflection.md` path is invalid, THE SYSTEM SHALL print "Warning: Module path not found: [path]"
