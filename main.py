"""One-line deadline excuse for the make.fun "One Line, No Deadline Met" bounty.

Writes one single-line joke giving an excuse for a missed deadline to
/output/entry.txt (1-200 UTF-8 characters). No network, no dependencies,
no secrets.
"""

import os
import sys

LINE = "I told the client it was done on Tuesday, then spent Wednesday to Friday writing the report I claimed was done."
# Structure (per the 24 Nov 2026 rank analysis of winning one-liners): 2-beat
# setup + reveal in the final clause. Beat 1: claimed it was done on Tuesday.
# Beat 2 / reveal: Wednesday to Friday was spent writing the report that was
# claimed done. Specific days (Tuesday, Wednesday to Friday) carry the
# specificity; the self-own reframes the whole sentence.


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        print(f"error: LINE must be 1-200 characters, got {len(LINE)}", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in LINE or LINE != LINE.strip():
        print("error: LINE must be a single line with no leading/trailing space", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
