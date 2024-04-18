#Parameter for the script
#projectname will be use as folder name for the project
#githubUrl will be use as initialize url for github
param (
 [string]$projectName="DataAnalysisProject",
 [string]$githubURL
)

#Root Directory of my project
$mainDir = Join-Path -Path $env:USERPROFILE -ChildPath "Documents\$projectName"

#Subdirectories to create
$subDirs = 'Scripts' , 'Data' , 'Output'

#Initialize the folder structure of the project
function InitializeStructure{
    Write-Host "Initialize Structure of $projectName"

    Write-Host "Creating $mainDir"

    New-Item -Path $mainDir -ItemType Directory -Force > $null

    foreach($dir in $subDirs){
        New-Item -Path "$maindir\$dir" -ItemType Directory -Force > $null
    }

    Write-Host "$projectName structure is initialized"
}

#Create a sample csv to add content to our git
function CreateSampleCSV{
    Write-Host "Create a SampleCSV File"
    $csvData=@"
    Name,Age,Email
    John Doe,30,john.doe@email.com
    Jane Doe,25,jane.doe@email.com
"@
    $csvPath ="$mainDir\Data\SampleData.csv"

    $csvData | Set-Content -Path $csvPath > $null

    Write-Host "$csvPath has been initialized."

}

#Check if git is installed on the computer
function CheckGitInsallation{
   Write-Host "Starting to check git on computer"

   if( -not (Get-Command git -ErrorAction SilentlyContinue) ){
        Write-Error "Git is not installed. Please Install Git and try again"
        exit 1
   }
  
   Write-Host "Git is installed."
}

#Setup the git repository connected to github (or any git platforme)
function SetupGitRepository{
    Write-Host "Setup Git Repository $githubURL"
    Set-Location -Path $mainDir
    git init
    git add .
    git commit -m "Initial commit with project structure and sample data"
    git remote add origin $githubURL
    git push -u origin master

    Write-Host "Git has been initialized to $githubURL and pushed"

}

#Execution of my script (sequence)
CheckGitInsallation
InitializeStructure
CreateSampleCSV
SetupGitRepository
