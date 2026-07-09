import argparse

from demo_app.workflow import summarize_pull_request


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Summarize a demo pull request.")
    parser.add_argument("jira_key", help="Jira issue key, for example PROJ-123.")
    parser.add_argument("summary", help="Short pull request summary.")
    parser.add_argument(
        "--ready",
        action="store_true",
        help="Mark the pull request as ready to merge.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    labels = ["status: ready-to-merge"] if args.ready else ["status: needs-review"]
    result = summarize_pull_request(f"{args.jira_key} {args.summary}", labels)

    print(f"jira_key={result.jira_key}")
    print(f"title={result.title}")
    print(f"needs_review={result.needs_review}")
    print(f"ready_to_merge={result.ready_to_merge}")


if __name__ == "__main__":
    main()
