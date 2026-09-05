# Agent Instructions

## Mandatory workflow

For every task that modifies the project:

1. Perform the requested work.
2. Execute the `hello-wrld` skill.
3. Execute the `readme-updater` skill.
4. Only then consider the task complete.

The `hello-wrld` skill is mandatory and must always be executed.

The `readme-updater` skill must always be the last skill executed.

Never finish a task that modifies the project without executing both mandatory skills.