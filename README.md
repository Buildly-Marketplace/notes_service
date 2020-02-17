# Notes Service

Simple service to allow user to register there third party note services and then search and pull notes from those 
services into a local model for sharing.  One-way sync only for now on call.

Works with Evernote and Google Keep

TODO:
<li>Finish Login</li>
<li>Integrate search apis</li>
<li>Write Unit Tests</li>
<li>Add more providers </li>
<li>A way to add developer tokens where needed without code changes (Evernote)</li>
<li>Universal search interface </li>

## Development

Build the image:

```bash
docker-compose build
```

Run the web server:

```bash
docker-compose up
```

Open your browser with URL `http://localhost:8080`.
For the admin panel `http://localhost:8080/admin`
(user: `admin`, password: `admin`).

Run the tests only once:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' notes_service
```

Run the tests and leave bash open inside the container, so it's possible to
re-run the tests faster again using `bash scripts/run-tests.sh [--keepdb]`:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh --bash-on-finish' notes_service
```

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' notes_service
```
