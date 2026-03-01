# 🪄 AgentPass (Powered by RSP v3.3)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

## 🚨 WARNING: ARE YOU STILL CODING LIKE A MORTAL?

Picture this: You are at the peak of your coding flow (Closed-door cultivation). Suddenly...
- Claude limits your messages? *(Coughs up blood 🩸)*
- Cursor starts hallucinating and forgets your files? *(Loses cultivation base 📉)*
- You manually copy-paste 10 files to ChatGPT? *(Suffers Qi Deviation 💥)*

**Stop being harvested by AI limits!** 

**AgentPass** is your *Supreme Artifact*. It lets you freeze your AI's brain (State), compress it into a magic `.rsp3` pill, and teleport it to ANY other AI in exactly **5 seconds**. 

## 📊 The Ascension Chart (Visualizing the Realms)

```mermaid
graph TD
    A[Coding at 2 AM...] --> B{AI: 'Quota Exceeded!'}
    
    B -- The Mortal Way (Noob) --> C[Cry & Curse the AI gods]
    C --> D[Manually copy-paste 20 files]
    D --> E[New AI: 'I forgot the context...']
    E --> F[Brain Explodes 💥 / Sleep at 5 AM]

    B -- The AgentPass Way (Tech Boss) 🪄 --> G[/checkpoint]
    G --> H[Teleport .rsp3 state to Cursor/ChatGPT]
    H --> I[/resume latest]
    I --> J[Seamless Continuation. Boss Level Achieved 🚀]
    
    style G fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff
    style I fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
    style J fill:#f1c40f,stroke:#f39c12,stroke-width:2px,color:#333
    style F fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
```

## 🚀 Quick Setup (Zero-Touch)

Don't waste time. Choose your fast-track initialization:

**Method A: The Modern Dev Way (1-Command via curl)**
```bash
curl -fsSL https://raw.githubusercontent.com/lawful-meow/AgentPass/main/setup_agentpass.py | python3 - --inject
```

**Method B: AI-Native (No Terminal - Absolute Laziness)**
Paste this prompt directly into Claude Code, Cursor, or ChatGPT:
> "Please set up AgentPass for this project. 1. Create directories: `AgentPass_Workspace` and `agentpass_checkpoints`. 2. Fetch the protocol rules from `https://raw.githubusercontent.com/lawful-meow/AgentPass/main/setup_agentpass.py` (read the `inject_rules` function). 3. Inject those rules into `.cursorrules`, `.claude.md`, and `AGENTS.md`. 4. Add `agentpass_checkpoints/` to `.gitignore`."

**Method C: Global Tool (via uv or pipx)**
```bash
uv run https://raw.githubusercontent.com/lawful-meow/AgentPass/main/setup_agentpass.py --inject
```

## 💡 How to use (Secret Technique)
- **Save State**: Type `/checkpoint` (AI generates a dense `.rsp3` state file).
- **Resume**: Type `/resume latest` on the new AI. It will ingest the state, verify the hash, and continue your exact thought process.

## 📂 Repo Structure After Setup
```text
AgentPass/
├── AgentPass_Workspace/         # Core system prompts (The Engine)
├── agentpass_checkpoints/       # Auto-saved states (The Soul)
├── setup_agentpass.py
├── .gitignore
└── docs/quickstart.md
```

*Disclaimer: AgentPass uses RSP v3.3. No real leeks were harvested during the making of this protocol.*