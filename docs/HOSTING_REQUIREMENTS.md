# Requirements for Hosting (So Everyone Can Use It From Their Laptops)

This document lists what you need so **everyone** can use the Contract Language Simplifier from their own laptops (not only on the machine where it runs).

---

## Two ways to let “everyone” use it

| Option | Who runs it | How others connect | Best for |
|--------|-------------|---------------------|----------|
| **A. Deploy to a public host** | No one’s laptop; runs in the cloud | Everyone opens the same URL in a browser | Teams, demos, no port/firewall setup |
| **B. Run on one laptop (LAN)** | One person runs the app on their machine | Others use that laptop’s IP + port (e.g. `http://192.168.1.5:7860`) | Same office/Wi‑Fi, quick testing |

---

## Option A: Deploy to a public host (recommended)

Host the app once; everyone uses it from their laptops via a single URL.

### Requirements checklist

| # | Requirement | Details |
|---|-------------|--------|
| 1 | **CORS enabled** | ✅ Already done in the app. Remote browsers can connect. |
| 2 | **Port 7860** | ✅ App and Docker use port 7860 (required by Hugging Face Spaces). |
| 3 | **Shared database** | You must set **`DATABASE_URL`** to a **PostgreSQL** URL (not a local file). Create a free DB at [Neon](https://neon.tech), [Supabase](https://supabase.com), or [ElephantSQL](https://www.elephantsql.com) and paste the URL. |
| 4 | **Secrets** | Set **`SECRET_KEY`** and **`JWT_SECRET_KEY`** to strong random values (no default/dev keys in production). |

### Where to host

- **Hugging Face Spaces** (free): See [HUGGINGFACE_SPACES.md](HUGGINGFACE_SPACES.md). Add `DATABASE_URL`, `SECRET_KEY`, and `JWT_SECRET_KEY` in **Settings → Repository secrets**.
- **Other platforms** (Railway, Render, Fly.io, etc.): Set the same environment variables and use their build/deploy (e.g. Docker or `gunicorn` on port 7860 or the port they assign).

### What everyone needs on their laptops (Option A)

- A **web browser** (Chrome, Edge, Firefox, etc.).
- **Internet** to open the hosted URL.
- Nothing else (no Python, no repo clone).

---

## Option B: Run on one laptop; others on same network

One person runs the app; everyone else on the same Wi‑Fi/LAN opens it using that laptop’s IP and port.

### Requirements checklist

| # | Requirement | Details |
|---|-------------|--------|
| 1 | **App binds to all interfaces** | ✅ App runs with `host='0.0.0.0'` so it accepts connections from other machines. |
| 2 | **Port open** | App uses **7860**. Ensure the host laptop’s firewall allows inbound TCP on port 7860 (or temporarily disable firewall for testing). |
| 3 | **Same network** | Other laptops must be on the same LAN/Wi‑Fi as the host. |
| 4 | **Database (optional)** | For single-user/same-machine use, the default SQLite file is fine. For multiple people sharing one instance, everyone will use that same SQLite DB on the host. |

### How to run (host laptop)

```powershell
# Windows (PowerShell)
cd "path\to\Contract Language Simplifier"
python app.py
# Or with Docker:
docker run -p 7860:7860 contract-simplifier
```

App will show something like: `Access the application at: http://0.0.0.0:7860`

### How others connect (from their laptops)

1. Find the **host laptop’s IP** (on the host machine):
   - **Windows:** `ipconfig` → look for **IPv4 Address** (e.g. `192.168.1.5`).
   - **Mac/Linux:** `ifconfig` or `ip addr` → similar IPv4 address.
2. On **other laptops**, open a browser and go to: **`http://<HOST_IP>:7860`**  
   Example: `http://192.168.1.5:7860`
3. Register or log in and use the app.

### What everyone needs on their laptops (Option B)

- **Host laptop:** Python 3.10/3.11 (or Docker), repo, dependencies installed. See [RUN_LOCALLY.md](RUN_LOCALLY.md).
- **Other laptops:** Web browser and same network only.

---

## Quick reference: “Everyone’s laptops” checklist

Use this when you want to confirm the app is hostable for everyone:

- [ ] **Access method chosen:** Public URL (Option A) or one laptop + LAN (Option B).
- [ ] **If Option A:** `DATABASE_URL`, `SECRET_KEY`, and `JWT_SECRET_KEY` set on the host; CORS and port 7860 already in the app.
- [ ] **If Option B:** App runs with `0.0.0.0:7860`; firewall allows port 7860; others use `http://<host-IP>:7860`.
- [ ] **Everyone:** Can open a browser and (for A) the public URL or (for B) `http://<host-IP>:7860`.

---

## Summary

- **Hosting so everyone can use it from their laptops** = either **deploy once to a public host** (Option A) or **run on one laptop and share the LAN URL** (Option B).
- **Requirements** are: correct port (7860), CORS for remote browsers (done), shared DB + secrets for public deployment, and for LAN: `0.0.0.0` and open port 7860.

For step-by-step deployment to a public URL, use [HUGGINGFACE_SPACES.md](HUGGINGFACE_SPACES.md).
