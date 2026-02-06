# Intent: Clawdbot Security (Local Sentinel)
**Module**: 05_clawdbot_security
**Mission**: To ensure that the high-privilege agentic system "Clawdbot" (OpenClaw) is 100% physically and digitally locked to the local network.

## 1. The Threat Model
Because Clawdbot (OpenClaw) possesses extensive permissions (screen reading, terminal execution, message monitoring), any external exposure is a "Critical Compromise" event.
*   **Risk**: Unauthorized remote access to the agent.
*   **Risk**: Potential "Cloud Callbacks" to unverified servers.

## 2. Technical Objectives
*   **Network Fortress**: Implementing firewall rules to block all non-local ingress to the Clawdbot server.
*   **Credential Isolation**: Ensuring all tokens and API keys used by Clawdbot stay out of cloud-synced folders.
*   **Audit**: Verifying the OpenClaw source code to confirm local-only operation is possible and stable.

## 3. Success Criteria
*   **Zero Exposure**: `nmap` or similar tools confirm zero internet-accessible ports for the Clawdbot service.
*   **Verified Sovereignty**: Clawdbot operates safely within the local cluster (M4/M1) without dependency on external agent controllers.
