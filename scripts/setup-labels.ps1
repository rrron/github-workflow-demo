param(
    [string]$Repository = ""
)

$labels = @(
    @{ Name = "status: needs-approval"; Color = "fbca04"; Description = "Pull request is waiting for approval" },
    @{ Name = "status: changes-requested"; Color = "d73a4a"; Description = "Reviewer requested changes" },
    @{ Name = "status: approved"; Color = "0e8a16"; Description = "Pull request has approval" },
    @{ Name = "status: ready-to-merge"; Color = "5319e7"; Description = "Pull request is allowed to pass the merge label gate" },
    @{ Name = "jira-linked"; Color = "1d76db"; Description = "Pull request is linked to Jira" },
    @{ Name = "ci: failed"; Color = "d73a4a"; Description = "CI failed" },
    @{ Name = "ci: passed"; Color = "0e8a16"; Description = "CI passed" }
)

foreach ($label in $labels) {
    $repoArgs = @()
    if ($Repository -ne "") {
        $repoArgs = @("--repo", $Repository)
    }

    gh label create $label["Name"] `
        --color $label["Color"] `
        --description $label["Description"] `
        @repoArgs

    if ($LASTEXITCODE -ne 0) {
        gh label edit $label["Name"] `
            --color $label["Color"] `
            --description $label["Description"] `
            @repoArgs
    }
}
