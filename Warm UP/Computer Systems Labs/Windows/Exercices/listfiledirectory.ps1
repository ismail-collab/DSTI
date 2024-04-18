# Get the list of files in the current directory
$files = Get-ChildItem -Path .

# Output file names to directory.txt
$files | Select-Object -ExpandProperty Name | Out-File -FilePath "directory.txt"

Write-Output "Directory listing saved to directory.txt"
