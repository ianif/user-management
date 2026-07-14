# User Management Project

This project previously contained the following issues, which have since been fixed:

## Security Issues
- Hardcoded password → the default hash can be overridden via the
  `ADMIN_PASSWORD_HASH` env var, and the password prompt no longer echoes
  input (`getpass`).
- Plaintext authentication → passwords are compared as hashes.
- MD5 password hashing → replaced with SHA-256.

## Performance Issues
- Nested loops (O(n²)) → replaced with a single-pass `collections.Counter`.
- String concatenation inside loop → replaced with `"\n".join(...)`.

## Reliability Issues
- File not closed → now opened with a `with` statement.
- Broad exception handling → now catches the specific `ZeroDivisionError`.

## Code Quality Issues
- Wildcard import → replaced with explicit imports.
- Shadowing built-in names → `id` parameter renamed to `user_id`.
- Missing docstrings → added.

## Typos
- `generate_reprot()` renamed to `generate_report()`.
