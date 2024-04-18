param (
    [int]$limit = 10
)

for ($i = 1; $i -le $limit; $i++) {
    Write-Output $i
}
