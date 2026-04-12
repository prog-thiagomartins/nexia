' Executa iniciar.bat sem abrir janela de terminal
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run Chr(34) & WScript.ScriptFullName & "\..\iniciar.bat" & Chr(34), 0, False
Set WshShell = Nothing
