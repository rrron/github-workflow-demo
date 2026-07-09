param(
    [Parameter(Mandatory = $true)]
    [string]$Repository,

    [string]$Branch = "main"
)

$body = @{
    required_status_checks = @{
        strict = $true
        contexts = @(
            "lint",
            "static-analysis",
            "test",
            "build",
            "ready-to-merge-label"
        )
    }
    enforce_admins = $true
    required_pull_request_reviews = @{
        required_approving_review_count = 1
        dismiss_stale_reviews = $true
        require_code_owner_reviews = $true
        require_last_push_approval = $true
    }
    restrictions = $null
    required_conversation_resolution = $true
    allow_force_pushes = $false
    allow_deletions = $false
} | ConvertTo-Json -Depth 10

$body | gh api `
    --method PUT `
    -H "Accept: application/vnd.github+json" `
    "/repos/$Repository/branches/$Branch/protection" `
    --input -
