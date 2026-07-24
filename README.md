# simplic.ox Agent

A Python framework for building scheduled integrations against the [simplic.ox](https://simplic.io) cloud API.

The agent loads a JSON configuration file, selects a named cloud environment (`staging` or `production`), constructs a shared HTTP client bound to that environment, and runs user-defined modules on a schedule.

## Features

- **Named environments** — `staging` and `production` with centrally managed base URLs; modules never hard-code hostnames
- **Safe defaults** — defaults to `staging`; `production` is only used when explicitly configured
- **Immutable module context** — modules cannot change the environment, replace the HTTP client, or override authentication
- **Credential isolation** — staging tokens never reach production, and vice versa
- **Structured logging** — JSON log output with environment context in every entry; prominent warning when connected to production
- **Validated configuration** — unknown environment names are rejected at startup, not silently ignored
- **CLI** — `validate`, `show-config`, and `run` commands with environment information in every output

## Requirements

- Python 3.11+
- Dependencies: `pydantic`, `httpx`, `typer`

## Installation

```bash
pip install simplic-ox-agent
```

Or install from source:

```bash
git clone https://github.com/your-org/simplic.ox.git
cd simplic.ox
pip install -e ".[dev]"
```

## Quick start

1. Copy the example configuration and set your API token:

   ```bash
   cp config.example.json config.json
   export SIMPLIC_OX_TOKEN=your-token-here
   ```

2. Validate the configuration:

   ```bash
   simplic-ox-agent validate --config config.json
   ```

   ```text
   Configuration valid
   Instance: customer-site-01
   simplic.ox environment: staging
   simplic.ox base URL: https://dev-oxs.simplic.io/
   Enabled modules: 1
   ```

3. Run a module manually:

   ```bash
   simplic-ox-agent run example-logistics-export --config config.json
   ```

## Configuration

The agent is configured via a single JSON file. The minimal required fields are `application.instance_name` and at least one module.

```json
{
  "application": {
    "instance_name": "customer-site-01",
    "environment": "development",
    "log_level": "INFO",
    "log_format": "json",
    "log_file": "logs/simplic.ox-agent.log",
    "shutdown_timeout_seconds": 30
  },
  "simplic.ox": {
    "environment": "staging",
    "timeout_seconds": 30,
    "verify_tls": true,
    "authentication": {
      "type": "bearer",
      "token": "${SIMPLIC_OX_TOKEN}"
    },
    "retry": {
      "max_attempts": 3,
      "initial_delay_seconds": 1,
      "maximum_delay_seconds": 30
    }
  },
  "settings": {
    "customer_id": "customer-001",
    "site_id": "warehouse-berlin"
  },
  "modules": [
    {
      "id": "example-logistics-export",
      "module": "simplic_ox_agent.modules.example_module",
      "enabled": true,
      "schedule": {
        "type": "interval",
        "seconds": 300
      },
      "settings": {
        "target_endpoint": "/api/integrations/logistics",
        "batch_size": 100
      }
    }
  ]
}
```

### Field reference

#### `application`

| Field | Type | Default | Description |
|---|---|---|---|
| `instance_name` | string | **required** | Human-readable name of this installation |
| `environment` | string | `"production"` | Label for the local deployment (e.g. `development`, `test`, `production`) |
| `log_level` | string | `"INFO"` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL` |
| `log_format` | string | `"json"` | `"json"` for structured logs, `"text"` for human-readable |
| `log_file` | string | null | Optional path for a log file; parent directories are created automatically |
| `data_directory` | string | `"data"` | Directory where per-module local data files are stored |
| `shutdown_timeout_seconds` | int | `30` | Graceful shutdown timeout |

#### `simplic.ox`

| Field | Type | Default | Description |
|---|---|---|---|
| `environment` | string | `"staging"` | `"staging"` or `"production"` — selects the API endpoint |
| `timeout_seconds` | int | `30` | Per-request HTTP timeout |
| `verify_tls` | bool | `true` | TLS certificate verification; do not disable in production |
| `authentication.type` | string | `"bearer"` | `"bearer"` or `"api_key"` |
| `authentication.token` | string | null | Bearer token; supports `${ENV_VAR}` expansion |
| `authentication.api_key` | string | null | API key; supports `${ENV_VAR}` expansion |
| `retry.max_attempts` | int | `3` | Maximum number of request attempts |
| `retry.initial_delay_seconds` | float | `1.0` | Initial retry back-off delay |
| `retry.maximum_delay_seconds` | float | `30.0` | Maximum retry back-off delay |

### Environments

Two named environments are supported out of the box:

| Name | Base URL |
|---|---|
| `staging` | `https://dev-oxs.simplic.io/` |
| `production` | `https://oxs.simplic.io/` |

The default is `staging`. **Production is only used when explicitly set** in `simplic.ox.environment`. When the agent starts against production it emits a prominent warning:

```text
WARNING: simplic.ox-agent is connected to the production simplic.ox environment at https://oxs.simplic.io/
```

### Distinguishing environments

Two separate concepts use the word "environment":

| Config key | Python attribute | Meaning |
|---|---|---|
| `application.environment` | `application_environment` | Label for the local agent installation (`development`, `test`, `production`) |
| `simplic.ox.environment` | `simplic_ox_environment` | The remote simplic.ox cloud endpoint (`staging` or `production`) |

These are completely independent. A production deployment (`application.environment = "production"`) can and should target `simplic.ox.environment = "staging"` during initial rollout.

### Credentials and environment variables

Token values support `${VAR}` expansion:

```json
"token": "${SIMPLIC_OX_TOKEN}"
```

The variable is resolved when the HTTP client is created (not at config load time), so `config.example.json` can be loaded without the variable being set.

Never hard-code tokens directly in the configuration file. Always use environment variables or a secrets manager.

## CLI

```
simplic-ox-agent [OPTIONS] COMMAND [ARGS]...
```

### `validate`

Validate the configuration file and print a summary.

```bash
simplic-ox-agent validate --config config.json
```

```text
Configuration valid
Instance: customer-site-01
simplic.ox environment: staging
simplic.ox base URL: https://dev-oxs.simplic.io/
Enabled modules: 1
```

### `show-config`

Display the fully resolved configuration (secrets are not shown).

```bash
simplic-ox-agent show-config --config config.json
```

### `run`

Manually execute a single module once.

```bash
simplic-ox-agent run example-logistics-export --config config.json
```

The target environment and base URL are displayed before execution. A production warning is shown when applicable.

## Writing modules

A module is any Python module that exposes an `async def run(context)` function.

```python
from simplic_ox_agent.core.context import ModuleContext


async def run(context: ModuleContext) -> None:
    response = await context.http.post(
        "/api/integrations/logistics",
        json={
            "customer_id": context.global_settings["customer_id"],
            "batch_size": context.module_settings.get("batch_size", 100),
        },
    )
    context.logger.info(
        "Export completed",
        extra={"http_status": response.status_code},
    )
```

### Module context

`ModuleContext` provides everything a module needs. All attributes are **read-only**.

| Attribute | Type | Description |
|---|---|---|
| `module_id` | `str` | ID from the configuration file |
| `module_settings` | `dict` | Per-module `settings` block |
| `global_settings` | `dict` | Top-level `settings` block |
| `http` | `SimplicOxHttpClient` | Shared HTTP client |
| `logger` | `logging.Logger` | Structured logger scoped to this module |
| `instance_name` | `str` | Agent installation name |
| `application_environment` | `str` | Local deployment label |
| `simplic_ox_environment` | `SimplicOxEnvironment` | Remote API environment |
| `data` | `LocalDataStore` | Persistent local key-value store scoped to this module |

### Local data store

Each module gets a private `LocalDataStore` accessible via `context.data`. Data is persisted as a JSON file under `application.data_directory` (default: `data/`) and survives between runs.

```python
async def run(context: ModuleContext) -> None:
    # Read a previously stored value (returns None if not set)
    last_id = context.data.get("last_processed_id")

    # … do work …
    new_last_id = 42

    # Persist for the next run
    context.data.set("last_processed_id", new_last_id)
```

**API**

| Method | Description |
|---|---|
| `get(key, default=None)` | Return the stored value, or `default` if absent |
| `set(key, value)` | Store a JSON-serialisable value and write to disk |
| `delete(key)` | Remove a key; no-op if absent |
| `clear()` | Remove all keys and persist the empty state |
| `all()` | Return a shallow copy of all key-value pairs |
| `key in context.data` | Check whether a key exists |

The backing file is `<data_directory>/<module_id>.json`. All values must be JSON-serialisable (strings, numbers, booleans, lists, dicts, or `None`).

### Module rules

Modules **must**:
- Use only relative API paths (e.g. `"/api/integrations/logistics"`)
- Accept the `ModuleContext` as their sole dependency
- Include `module_id` and `simplic_ox_environment` in structured log entries

Modules **must not**:
- Select, compare, or switch the simplic.ox environment
- Hard-code a simplic.ox hostname
- Build absolute simplic.ox URLs
- Override the HTTP client's base URL or authentication headers

### Using generated API clients

Generated clients (see [Generating API clients](#generating-api-clients) below) wrap `context.http` and return typed Pydantic models. Import the client class, instantiate it with `context.http`, and call its async methods.

```python
from simplic_ox_agent.clients.auth import AuthClient
from simplic_ox_agent.clients.logistics import LogisticsClient
from simplic_ox_agent.core.context import ModuleContext


async def run(context: ModuleContext) -> None:
    auth = AuthClient(context.http)
    login_result = await auth.login(
        email=context.module_settings["email"],
        password=context.module_settings["password"],
    )

    logistics = LogisticsClient(context.http)
    batches = await logistics.get_pending_batches()
    context.logger.info("Fetched batches", extra={"count": len(batches)})

    # Persist progress using the local store
    context.data.set("last_batch_id", batches[-1].id if batches else None)
```

Each client class:
- Takes a `SimplicOxHttpClient` as its only constructor argument
- Uses `_PREFIX` internally so modules never build absolute URLs
- Calls `response.raise_for_status()` before parsing, so HTTP errors propagate as exceptions
- Returns typed Pydantic models; `None` for endpoints with no response body

### Registering a module

Add an entry to the `modules` list in your configuration file:

```json
{
  "id": "my-module",
  "module": "my_package.modules.my_module",
  "enabled": true,
  "schedule": {
    "type": "interval",
    "seconds": 600
  },
  "settings": {
    "batch_size": 50
  }
}
```

## Generating API clients

The `scripts/generate_client.py` script downloads an OpenAPI 3.x JSON spec and generates a typed Python client package under `src/simplic_ox_agent/clients/<name>/`.

### Usage

```bash
python scripts/generate_client.py --url URL --name NAME [OPTIONS]
```

| Option | Description |
|---|---|
| `--url URL` | OpenAPI JSON spec URL (**required**) |
| `--name NAME` | Client module name, e.g. `auth`, `user-profile` (**required**) |
| `--out-dir PATH` | Path to the `clients/` package root (auto-detected by default) |
| `--dry-run` | Print generated code without writing any files |
| `--force` | Overwrite existing files without prompting |

### Examples

```bash
# Generate the auth client
python scripts/generate_client.py \
    --url https://oxs.simplic.io/auth-api/v1/swagger/v1/swagger.json \
    --name auth

# Preview the output without writing files
python scripts/generate_client.py \
    --url https://oxs.simplic.io/user-api/v1/swagger/v1/swagger.json \
    --name user \
    --dry-run
```

### What gets generated

For `--name auth` the script creates:

```
src/simplic_ox_agent/clients/auth/
    __init__.py     # re-exports AuthClient and all model classes
    client.py       # AuthClient — one async method per endpoint
    models.py       # Pydantic BaseModel classes from OpenAPI schemas
```

The client class name is derived from the `--name` argument (`auth` → `AuthClient`). Method names are derived from HTTP verb and path (`POST /Auth/login` → `login`). All response models are typed Pydantic classes; HTTP errors raise via `raise_for_status()`.

## Development

### Setup

```bash
git clone https://github.com/your-org/simplic.ox.git
cd simplic.ox
pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

### Project layout

```
simplic.ox/
├── config.example.json          # example configuration (always targets staging)
├── pyproject.toml
├── scripts/
│   └── generate_client.py       # generates typed clients from OpenAPI specs
├── src/
│   └── simplic_ox_agent/
│       ├── core/
│       │   ├── environment.py   # SimplicOxEnvironment enum + URL map
│       │   ├── config.py        # Pydantic configuration models
│       │   ├── http_client.py   # SimplicOxHttpClient
│       │   ├── context.py       # ModuleContext
│       │   ├── local_store.py   # LocalDataStore — per-module persistent storage
│       │   └── logging_setup.py # JSON formatter, startup logging
│       ├── clients/
│       │   ├── auth/            # generated: AuthClient
│       │   ├── logistics/       # generated: LogisticsClient
│       │   └── vehicle/         # generated: VehicleClient
│       ├── modules/
│       │   └── example_module.py
│       └── cli/
│           └── main.py          # validate / show-config / run
├── data/                        # per-module local data (created at runtime)
└── tests/
    ├── test_environment.py
    ├── test_config.py
    ├── test_http_client.py
    ├── test_context.py
    ├── test_logging.py
    └── test_cli.py
```

## License

[MIT](LICENSE)
