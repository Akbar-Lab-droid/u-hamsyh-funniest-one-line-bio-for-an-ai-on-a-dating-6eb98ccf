"""Entry program for the make.fun bounty.

Copies the committed entry.txt into the output directory
given by MAKEFUN_OUTPUT_DIR (default: out).
"""

# Entry for the u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf bounty on make.fun.
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(os.path.join(here, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
