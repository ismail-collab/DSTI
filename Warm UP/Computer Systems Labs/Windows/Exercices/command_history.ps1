
  Id CommandLine                                                                                                                    
  -- -----------                                                                                                                    
   1 Set-Location -literalPath 'C:\Users\Nightingale\Documents\S24\WarmUp It'                                                       
   2 Set-Location 'C:\Program Files\'                                                                                               
   3 Get-ChildItem                                                                                                                  
   4 cls                                                                                                                            
   5 Get-ChildItem 'C:\Users\Nightingale\Documents\'                                                                                
   6 cls                                                                                                                            
   7 Get-Location                                                                                                                   
   8 cls                                                                                                                            
   9 Get-Host                                                                                                                       
  10 Get-ChildItem dfsdfsd                                                                                                          
  11 Set-Location 'C:\Users\Nightingale\Documents\S24\WarmUp It\'                                                                   
  12 cls                                                                                                                            
  13 ls                                                                                                                             
  14 cls                                                                                                                            
  15 New-Item -Path . -Name Myfirstfile.txt                                                                                         
  16 New-Item -Path . -Name myfirstfile.txt                                                                                         
  17 New-Item -Path . -Name Scenario -ItemType Directory                                                                            
  18 New-Item  Scenario2 -ItemType Directory                                                                                        
  19 New-Item  anothertextfile.txt                                                                                                  
  20 cls                                                                                                                            
  21 history                                                                                                                        
  22 cls                                                                                                                            
  23 history                                                                                                                        
  24 cls                                                                                                                            
  25 Get-ChildItem                                                                                                                  
  26 Add-Content -Path .\Myfirstfile.txt -Value "Hello World!"                                                                      
  27 Get-Content -Path .\Myfirstfile.txt                                                                                            
  28 Add-Content -Path .\Myfirstfile.txt -Value "Hello Student"                                                                     
  29 Get-Content -Path .\Myfirstfile.txt                                                                                            
  30 Set-Content -Path .\Myfirstfile.txt -Value "Hello Students!"                                                                   
  31 Get-Content -Path .\Myfirstfile.txt                                                                                            
  32 Add-Content -Path .\Myfirstfile.txt -Value "Hello Everyone!"                                                                   
  33 Get-Content -Path .\Myfirstfile.txt                                                                                            
  34 Add-Content -Path .\Myfirstfile.txt -Value "Hello Everyone!" --Nonewline                                                       
  35 Add-Content -Path .\Myfirstfile.txt -Value "Hello Everyone!" -NoNewline                                                        
  36 Get-Content -Path .\Myfirstfile.txt                                                                                            
  37 Add-Content -Path .\Myfirstfile.txt -Value "Hello e!" -NoNewline                                                               
  38 Get-Content -Path .\Myfirstfile.txt                                                                                            
  39 Move-Item .\Myfirstfile.txt .\Scenario\                                                                                        
  40 Move-Item .\Scenario2\ .\Scenario\                                                                                             
  41 Move-Item -Path 'C:\Users\Nightingale\Documents\S24\WarmUp It\anothertextfile.txt' -Destination 'C:\Users\Nightingale\Docume...
  42 cls                                                                                                                            
  43 Set-Location ..\Example\                                                                                                       
  44 Get-ChildItem                                                                                                                  
  45 Move-Item .\anothertextfile.txt anotherfile.txt                                                                                
  46 Get-ChildItem                                                                                                                  
  47 Rename-Item .\anotherfile.txt another.txt                                                                                      
  48 Get-ChildItem                                                                                                                  
  49 Copy-Item .\another.txt copy-of-another.txt                                                                                    
  50 Copy-Item .\another.txt copy-of-another                                                                                        
  51 Copy-Item .\another.txt C:\Users\Nightingale\Documents\anotherfilecopy.txt                                                     
  52 Copy-Item  -Path .\another.txt -Destination C:\Users\Nightingale\Documents\anotherfilecopy2.txt                                
  53 Set-Location '..\WarmUp It\'                                                                                                   
  54 Set-Location .\Scenario\                                                                                                       
  55 clear                                                                                                                          
  56 Get-ChildItem                                                                                                                  
  57 Get-Content .\Myfirstfile.txt                                                                                                  
  58 Add-Content .\Myfirstfile.txt -Value "Hello you!" -Position 0                                                                  
  59 Get-Content .\Myfirstfile.txt -Raw                                                                                             
  60 "Test"+(Get-Content .\Myfirstfile.txt -Raw) | Set-Content .\Myfirstfile.txt                                                    
  61 Get-Content .\Myfirstfile.txt                                                                                                  
  62 Set-Content .\Myfirstfile.txt -Value "Hello World!"                                                                            
  63 Get-Content .\Myfirstfile.txt                                                                                                  
  64 Get-Command Set-Content                                                                                                        
  65 Get-Help Set-Content                                                                                                           
  66 cd ..                                                                                                                          
  67 clear                                                                                                                          
  68 history > command history.txt                                                                                                  


