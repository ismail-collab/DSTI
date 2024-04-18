param (
    [string]$directory = ".",
    [string]$fileType = "*.txt"
)

# Ensure the directory exists
if (-Not (Test-Path -Path $directory)) {
    Write-Error "Directory does not exist."
    exit 1
}

# List files of the specified type in the given directory
$filteredFiles = Get-ChildItem -Path $directory -Filter $fileType

# Output results to the console
$filteredFiles | ForEach-Object {
    Write-Output $_.FullName
}
