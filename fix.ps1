Set-PSReadLineOption -EditMode Vi
Set-PSReadlineOption -ViModeIndicator Script -ViModeChangeHandler{
    Param($mode)
    $Env:SHELL_VI_MODE = $mode
    # go back to the beginning of the line
    Write-Host -NoNewLine "`e[1000D"
    # rewrite the prompt manually
    write-Host -NoNewLine (oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/tonybaloney.omp.json" | Invoke-Expression)

}