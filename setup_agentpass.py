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
    rule = "\n# AgentPass (RSP v3.3) Rules\nIf user types /checkpoint → generate full RSP checkpoint in <RSP_CHECKPOINT> format and save to ./agentpass_checkpoints/checkpoint_[timestamp].rsp3. If /resume latest → load newest .rsp3 from ./agentpass_checkpoints, verify integrity_hash, and resume from next_action. Auto-remind when response long or quota low: 'Quota low, do you want /checkpoint?'\nFollow RSP schema from AgentPass_Workspace/1_System_Prompt.md.\n"

    # Existing injections
    for f in [".claude.md", "AGENTS.md", ".cursorrules"]:
        try:
            Path(f).write_text(Path(f).read_text(encoding="utf-8") + rule, encoding="utf-8")
            print(f"💉 Injected into {f}")
        except FileNotFoundError:
            Path(f).write_text(rule, encoding="utf-8")
            print(f"💉 Created {f} with AgentPass rules")

    # New: For Google Antigravity (rules dir)
    antigravity_rules_dir = Path(".agents/rules")
    antigravity_rules_dir.mkdir(parents=True, exist_ok=True)
    antigravity_file = antigravity_rules_dir / "agentpass.md"
    antigravity_file.write_text(rule, encoding="utf-8")
    print(f"💉 Created {antigravity_file} for Google Antigravity compatibility")

    # New: For VSCode/Copilot (fallback file)
    vscode_dir = Path(".vscode")
    vscode_dir.mkdir(exist_ok=True)
    vscode_file = vscode_dir / "copilot-instructions.md"
    vscode_file.write_text(rule, encoding="utf-8")
    print(f"💉 Created {vscode_file} for VSCode/Copilot fallback")

    # For OpenCode: AGENTS.md is already injected and read automatically
    # For Codex: Use AGENTS.md or manually add to system prompt in API calls

if __name__ == "__main__":
    main()
