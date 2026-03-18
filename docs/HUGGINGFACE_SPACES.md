# Deploying on Hugging Face Spaces

This app is configured to work as a **public web application** on Hugging Face Spaces. Four things are required:

## 1. CORS enabled

Remote browsers can connect to your Space. CORS is enabled in the app with configurable origins (default: allow all). To restrict origins, set the `CORS_ORIGINS` secret to a comma-separated list of URLs.

## 2. Port 7860

The app listens on **port 7860**, which Hugging Face Spaces requires. The Dockerfile and `app.py` use `PORT` (default 7860). No change needed.

## 3. Shared database

The Space must use a **shared database**, not a local file. Use a hosted PostgreSQL (e.g. [Neon](https://neon.tech), [Supabase](https://supabase.com), or [ElephantSQL](https://www.elephantsql.com)).

1. Create a free PostgreSQL database.
2. Copy the connection URL (e.g. `postgresql://user:pass@host/dbname`).
3. In your Space: **Settings → Repository secrets** → Add secret:
   - **Name:** `DATABASE_URL`
   - **Value:** your PostgreSQL URL

If `DATABASE_URL` is not set in production, the app will not start and will show a clear error.

## 4. Proper secrets

Configure secure keys so the app does not run with default dev keys.

In your Space: **Settings → Repository secrets**, add:

| Secret            | Description |
|-------------------|------------|
| `DATABASE_URL`    | PostgreSQL connection URL (shared database). |
| `SECRET_KEY`      | Strong random string for Flask session signing (e.g. 32+ random characters). |
| `JWT_SECRET_KEY`  | Strong random string for JWT tokens (e.g. 32+ random characters). |

Optional:

| Secret        | Description |
|---------------|------------|
| `CORS_ORIGINS`| Comma-separated allowed origins, or `*` (default). |
| `FLASK_ENV`   | Set to `production` (Dockerfile already sets this). |

### Generating secret values

```bash
# Example (Linux/macOS): generate random keys
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Use different values for `SECRET_KEY` and `JWT_SECRET_KEY`.

---

## Summary

1. **Enable CORS** – Done in code; optional `CORS_ORIGINS` secret.
2. **Use port 7860** – Done in code and Dockerfile.
3. **Use a shared database** – Set `DATABASE_URL` in Space secrets to your PostgreSQL URL.
4. **Set proper secrets** – Set `SECRET_KEY` and `JWT_SECRET_KEY` in Space secrets.

After setting these secrets, rebuild/restart your Space. Users can register and log in; data is stored in the shared database and persists across restarts.
