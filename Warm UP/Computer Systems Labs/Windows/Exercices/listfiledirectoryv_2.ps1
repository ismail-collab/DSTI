# Get the list of files in the current directory
$files = Get-ChildItem -Path .

foreach($elem in $files){
    Add-Content -Path "directory_loop.txt" -Value $elem.Name
}


Write-Output "file names to directory.txt"
$files | Select-Object -ExpandProperty Name | Out-File -FilePath "directory_multiple.txt"

Get-ChildItem -Name > "directory_simple.txt"

#Write-Output "Directory listing saved to directory.txt"
