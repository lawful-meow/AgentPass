import os, sys
from pathlib import Path

WORKSPACE = Path("AgentPass_Workspace")
CHECKPOINT_DIR = Path("agentpass_checkpoints")

def main():
    WORKSPACE.mkdir(exist_ok=True)
    CHECKPOINT_DIR.mkdir(exist_ok=True)
    print("✅ Created AgentPass_Workspace and agentpass_checkpoints")

    if "--inject" in sys.argv:
        inject_rules()
    print("🚀 AgentPass is ready! Type /checkpoint or /resume latest in your AI agent.")

def inject_rules():
    rule = "\n# AgentPass (RSP v3.3) Rules\nIf user types /checkpoint → generate full RSP checkpoint. If /resume latest → load newest .rsp3 and resume. Auto-remind when response long or quota low.\n"
    for f in [".claude.md", "AGENTS.md", ".cursorrules"]:
        try:
            Path(f).write_text(Path(f).read_text(encoding="utf-8") + rule, encoding="utf-8")
            print(f"💉 Injected into {f}")
        except FileNotFoundError:
            Path(f).write_text(rule, encoding="utf-8")
            print(f"💉 Created {f} with AgentPass rules")

if __name__ == "__main__":
    main()
