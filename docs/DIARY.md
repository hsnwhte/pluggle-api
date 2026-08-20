### 📅 2026-08-12, Wednesday

**07:06** | *[RESOLVE]*
Project started. Ultimate goal is to deploy a SaaS that serves as a free ETL platform
based on Pluggle Engine.

### 📅 2026-08-20, Thursday

**11:53** | *[RESOLVE]*
Tailwind migration; searchable strategy combobox; drag-and-drop upload;
form/output/adapter chain; Pluggle process-boundary settings

Migrated from hand-written CSS to Tailwind v4 (standalone CLI, no Node build tooling
beyond npm). Deliberate full rewrite rather than incremental — decided against keeping
the old grid rules alongside Tailwind classes because the two systems fighting over the
same elements produced worse output than either alone. Font (Aldrich, for the
header/logo pairing) and accent color (sky-500, replacing the logo's orange-red — red
reads as a danger signal on a download link, not a brand accent) settled after comparing
several candidates against the actual SVG.

Strategy selector rebuilt as a searchable combobox, replacing the plain <select>.
Vanilla JS, no library: an input listener filters <li> visibility via
.textContent.includes (), each <li> carries the real composite key (name__version) in a
data-value attribute so the visible label and the submitted value can differ, and a
document-level click listener with .contains () closes the list on outside click.
autocomplete="off" was needed — the browser's own field memory was surfacing stale
entries the JS list never produced.

Drag-and-drop file input finished: click-to-browse, dragover/dragleave visual feedback,
drop, and — the one that was missed initially — a change listener on the
hidden <input type="file"> itself, since a native file-picker selection never fires
drop. Reset button (type="reset") clears the native form fields for free; a reset
listener on the form additionally clears the drop-zone's own text node, since that's
plain content the native reset doesn't know about.

Settled the target-format question: strategies aren't guaranteed to produce the format
their extension implies (a JSON-writing strategy given a .xml target still writes
JSON) — a known Pluggle limitation, not something to solve here. Response scope narrowed
instead of trying to guarantee content: /run will always return JSON/XML, file-type
output (CSV/XLSX) dropped from scope entirely. This also removed the need for a
temp-output-file-plus-TTL-cleanup subsystem that had been planned — no file persists
past the request.

InputFormData → build_input_args () → InputArgs chain drafted. Source and target type
are computed_fields on InputFormData (file takes priority over URL when both are
present), keeping the adapter itself a plain function rather than a class — no state to
carry, no reason for more than one method. Caught and fixed en route: an f-string that
concatenated OUTPUTS_DIR and a filename with a literal " / " instead of Path.
__truediv__, producing an invalid path.

Resolved where the pluggle_api/Pluggle boundary lives for configuration. Pluggle reads
PLUGGLE_STORE_ADDRESS, PLUGGLE_STRATEGIES_DIR, LOG_DIR from its own env at import time,
defaulting to SQLite; pluggle_api doesn't touch Pluggle's code to change this — its own
settings.py builds a Settings () from its own .env (Postgres connection, host/port,
unrelated to Pluggle), then writes into os.environ under Pluggle's expected names after
Settings () is constructed, before Pluggle is imported. Postgres was picked over
Pluggle's SQLite default specifically for concurrent-write safety under multiple
simultaneous web requests, which SQLite doesn't handle well — the docker-compose
Postgres service, once nearly deleted as "pluggle_api doesn't need a database," was kept
for this reason and re-scoped in intent to Pluggle's registry rather than pluggle_api's
own state, which remains fully stateless.

Open: /run still needs its try/except → JSON contract finished, an /outputs/ static
mount for the download link, and the JS-side preventDefault + fetch submit flow (form
still native-submits). Pluggle-side: run (args: InputArgs) in interfaces/api/api.py
needs to drop its report-dict return in favor of raise-on-failure /
return-nothing-on-success, matching the CLI's own contract.