# Contributing

Thank you for your interest in contributing to simplic.ox Agent.

## Development setup

```bash
git clone https://github.com/your-org/simplic.ox.git
cd simplic.ox
pip install -e ".[dev]"
```

## Running the tests

```bash
pytest
```

All tests must pass before opening a pull request.  New behaviour must be
covered by tests.

## Code style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use type annotations on all public functions and methods.
- Keep public modules, classes, and functions documented with docstrings.

## Submitting changes

1. Fork the repository and create a feature branch from `main`.
2. Make your changes with accompanying tests.
3. Run `pytest` and confirm all tests pass.
4. Open a pull request describing what was changed and why.

## Environment and security rules

Changes that touch the environment or HTTP layer must preserve these
invariants — the corresponding tests enforce them:

- The default simplic.ox environment must remain `staging`.
- Unknown environment names must be rejected during configuration validation.
- Staging credentials must never be sent to the production endpoint, and vice versa.
- Modules must not be able to override the HTTP client's base URL or
  authentication headers.
- All predefined environment URLs must use HTTPS.

## Reporting issues

Open a GitHub issue with a minimal reproduction case and the output of:

```bash
simplic-ox-agent validate --config config.json
```
