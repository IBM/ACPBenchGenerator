#!/usr/bin/env bash
# generate_instances.sh
#
# Generates PDDL problem instances for all benchmark domains that have a
# generate.py script.  Each script must be executed from inside its own
# benchmark directory because it writes files relative to that directory.
#
# Usage:
#   bash scripts/generate_instances.sh [DOMAIN ...]
#
# If no domain names are supplied every supported domain is generated.
# Supported domains:
#   blocksworld  depot  ferry  floortile  frogs_jumping  goldminer
#   grid  grippers  hanoi  logistics  random_hanoi  rovers  satellite
#   swap  visitall
#
# Note: ALFWorld problem instances were generated manually and are not
# covered by this script.
#
# Prerequisites:
#   - Each benchmark's compiled generator binary must be present under
#     benchmarks/<domain>/generator/ (see the Makefile in each generator
#     sub-directory).
#   - The `validate` tool (from VAL / PDDL validator) must be on PATH.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
BENCHMARKS_DIR="$REPO_ROOT/benchmarks"

# Domains that have a generate.py script (alfworld is excluded – see above)
ALL_DOMAINS=(
    blocksworld
    depot
    ferry
    floortile
    frogs_jumping
    goldminer
    grid
    grippers
    hanoi
    logistics
    random_hanoi
    rovers
    satellite
    swap
    visitall
)

# Determine which domains to generate
if [ $# -eq 0 ]; then
    DOMAINS=("${ALL_DOMAINS[@]}")
else
    DOMAINS=("$@")
fi

for domain in "${DOMAINS[@]}"; do
    domain_dir="$BENCHMARKS_DIR/$domain"
    generate_script="$domain_dir/generate.py"

    if [ ! -d "$domain_dir" ]; then
        echo "ERROR: Domain directory not found: $domain_dir" >&2
        exit 1
    fi

    if [ ! -f "$generate_script" ]; then
        echo "ERROR: No generate.py found for domain '$domain' at $generate_script" >&2
        exit 1
    fi

    echo "=== Generating instances for: $domain ==="
    # Create generated_instances sub-directory if the script expects it
    mkdir -p "$domain_dir/generated_instances"

    # Run the generator from within the domain directory so that relative
    # file paths inside generate.py resolve correctly.
    (cd "$domain_dir" && python generate.py)

    echo "--- Done: $domain ---"
done

echo ""
echo "Instance generation complete."
