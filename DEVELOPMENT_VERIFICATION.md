# Development Verification Standard

This repository is intended to be evaluated by inspecting evidence, not by guessing how code was authored.

## Before presenting a project to an employer

1. Clone the repository.
2. Install the documented dependencies.
3. Run every documented command.
4. Run the automated test suite.
5. Inspect the sample input and output.
6. Intentionally test at least one failure/edge case.
7. Read the implementation until every important function can be explained.
8. Record any limitations discovered during testing.
9. Update the documentation so it matches the implementation.
10. Only then describe the project as completed.

## AI-assisted development

AI coding assistants can be useful for research, drafting, debugging, refactoring, and documentation. Their use does not by itself establish or disprove engineering ability.

This portfolio therefore does not attempt to disguise AI assistance. Instead, it aims to make the work independently verifiable through source code, tests, data, reproducible commands, and documented limitations.

## What a technical reviewer should be able to verify

- What problem the project solves
- What inputs it accepts
- How the implementation processes those inputs
- What outputs it produces
- How failure cases are handled
- What tests exist
- Which parts are implemented versus planned
- What the author would need to change for production

## Important rule

Do not claim that a project was personally tested, deployed, used by customers, or operated on physical hardware unless that has actually happened and can be demonstrated.
