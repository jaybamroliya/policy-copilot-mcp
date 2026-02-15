@echo off
call .venv\Scripts\activate

echo Starting worker agent...
start cmd /k "python agent\worker_server.py"

echo Starting policy copilot...
start cmd /k "python -m policy.policy_server"

echo Running demo task...
python -m cli.policycopilot --task "Summarize customers and email results"

pause