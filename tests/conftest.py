import time
from datetime import datetime

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Custom summary shown at the end of CI run."""
    
    # Status
    if exitstatus == 0:
        status_icon = "🟢"
        status_text = "ALL TESTS PASSED — DEPLOY SAFE"
    else:
        status_icon = "🔴"
        status_text = "TESTS FAILED — DEPLOY BLOCKED"

    # Tools discovered (collected from captured stdout)
    captured = terminalreporter._tw
    output = "\n".join(terminalreporter._outcome.stdout)

    terminalreporter.write_sep(
        "=",
        f"🚀 MCP CI REPORT ({datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')})"
    )

    terminalreporter.write_line("")
    terminalreporter.write_line(f"{status_icon} {status_text}")
    terminalreporter.write_line("")

    # Latency info if printed by test
    if "LATENCY_MS" in output:
        terminalreporter.write_line("⏱ Latency Information:")
        for line in output.splitlines():
            if "LATENCY_MS" in line:
                terminalreporter.write_line("   • " + line)
        terminalreporter.write_line("")

    # Tools summary if printed by test
    if "TOOL_LIST" in output:
        terminalreporter.write_line("🧰 MCP Tools Available:")
        for line in output.splitlines():
            if "TOOL_LIST" in line:
                terminalreporter.write_line("   • " + line.replace('TOOL_LIST=', ''))
        terminalreporter.write_line("")

    terminalreporter.write_sep("=", "END OF REPORT")
