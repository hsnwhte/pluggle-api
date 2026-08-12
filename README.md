# pluggle-api

REST API layer for [Pluggle](https://github.com/hsnwhte/pluggle) — run ETL pipelines via HTTP, powered by FastAPI.

> **Status:** Early development (Phase 1 / MVP). Not yet deployed.

## What is this?

Pluggle is a plugin-based ETL/data sync engine, used via CLI: pick a source,
pick a transformation strategy, run, get output. `pluggle-api` wraps that
same workflow in a REST API — so it can be triggered over HTTP and, eventually,
demoed live in a browser at [pluggle.org](https://pluggle.org).

This repo does **not** contain Pluggle's source code. It depends on Pluggle
as a regular PyPI package and adds a thin API layer on top — same pattern as
[`pluggle-ncr`](https://github.com/hsnwhte/pluggle-ncr).

## Scope (Phase 1)

This is a deliberately restricted first version:

- Users select from Pluggle's **pre-built, trusted strategies** — no custom
  `.py` upload. Uploading and running arbitrary user code on a public server
  is a remote code execution risk; that capability is deferred (see below).
- Source URLs are restricted by an **allowlist** (HTTPS only, no requests to
  internal/private IP ranges) to prevent SSRF.

**Phase 2 (roadmap, not started):** sandboxed execution of user-uploaded
transformation strategies inside an isolated, network-disabled, resource-limited
container. Deferred intentionally — this is a separate, non-trivial engineering
effort (container security), not a quick follow-up.

## Tech stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [Pluggle](https://github.com/hsnwhte/pluggle) — ETL engine (dependency, not vendored)
- [Pydantic](https://docs.pydantic.dev/) — request/response validation

## Local Development

```bash
git clone https://github.com/hsnwhte/pluggle-api.git
cd pluggle-api
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```
`[dev]` installs testing tools (pytest) alongside the runtime dependencies.

## Running locally

```bash
uvicorn pluggle_api.main:app --reload
```

*(Entry point will be finalized as the `src/pluggle_api` layout is built out.)*

## License

MIT — see [LICENSE](LICENSE).