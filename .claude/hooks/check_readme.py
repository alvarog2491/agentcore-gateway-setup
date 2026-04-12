import json
import sys

event = json.load(sys.stdin)
changed_file = event.get("tool_input", {}).get("path", "")

# Skip if the README itself was changed
if "README" in changed_file:
    sys.exit(0)

# Inject a reminder into Claude's context
print(
    json.dumps(
        {
            "context": f"You just edited `{changed_file}`. Please review README.md to check if it needs updating — especially sections covering usage, API, configuration, or any feature you just changed."
        }
    )
)

sys.exit(0)
