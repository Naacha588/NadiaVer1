@echo off
TITLE elseNadiasBot
:: Enables virtual env mode and then starts NadiasBot
env\scripts\activate.bat && py -m NadiasBot
