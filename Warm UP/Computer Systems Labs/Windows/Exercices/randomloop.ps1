# Generate a random number between 1 and 100
$targetNumber = Get-Random -Minimum 1 -Maximum 100
$currentNumber = 0

while ($currentNumber -lt $targetNumber) {
    $currentNumber += 1
    Write-Output "Current number: $currentNumber"
}

Write-Output "Reached target number: $targetNumber"
