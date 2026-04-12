$ws = New-Object -ComObject WScript.Shell
$desktop = [Environment]::GetFolderPath('Desktop')
$lnkPath = Join-Path $desktop 'Meu Planejamento.lnk'
$lnk = $ws.CreateShortcut($lnkPath)
$lnk.TargetPath = 'C:\Users\mayar\Desktop\claude-workspace\planejamento-app\iniciar.vbs'
$lnk.WorkingDirectory = 'C:\Users\mayar\Desktop\claude-workspace\planejamento-app'
$lnk.Description = 'Abrir app de planejamento'
$lnk.IconLocation = 'shell32.dll,171'
$lnk.Save()
Write-Host "Atalho criado em: $lnkPath"
