# Deploy Option A – Get Your Public Hosting URL

Follow these steps **in order**. At the end you will have a **public URL** anyone can open from their laptop.

---

## Step 1: Create a free PostgreSQL database (~2 min)

1. Open **https://neon.tech** (or https://supabase.com).
2. Sign up / Log in (free).
3. Create a **new project** (Neon: "New Project"; Supabase: "New Project").
4. Open the **Connection string** or **Database URL** in the dashboard.
5. Copy the full URL. It looks like:
   ```text
   postgresql://username:password@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
   ```
6. **Save it** – you need it as `DATABASE_URL` in Step 3.

---

## Step 2: Create your Hugging Face Space (~2 min)

1. Open **https://huggingface.co** and log in (or create an account).
2. Go to **https://huggingface.co/spaces**.
3. Click **"Create new Space"**.
4. Fill in:
   - **Space name:** e.g. `contract-simplifier`
   - **License:** e.g. MIT
   - **SDK:** select **Docker**
   - **Space hardware:** e.g. CPU basic (free).
5. Click **"Create Space"**.
6. You need to **push your app code** to this Space:
   - Either **connect a GitHub repo** (Space Settings → clone your repo and use it as the Space repo),  
   - Or **upload** the project: in the Space repo, upload the Dockerfile, `app.py`, `config.py`, `models.py`, `requirements.txt`, and the `services/` and `templates/` folders so the Space can build the Docker image.
7. **Your final public URL** will be:
   ```text
   https://YOUR_HF_USERNAME-contract-simplifier.hf.space
   ```
   Replace `YOUR_HF_USERNAME` with your Hugging Face username (e.g. `johndoe` → `https://johndoe-contract-simplifier.hf.space`).

---

## Step 3: Add secrets to the Space

1. In your Space page, go to **Settings** (gear icon).
2. Open **"Repository secrets"** (or "Variables and secrets").
3. Add these three secrets (click "New secret" for each):

| Secret name      | Value |
|------------------|--------|
| `DATABASE_URL`   | The PostgreSQL URL you copied in **Step 1** (paste the full string). |
| `SECRET_KEY`     | Use the value below, or run `python scripts/generate_secrets.py` to create your own. |
| `JWT_SECRET_KEY` | Use the value below, or from the same script. |

**Pre-generated keys** (copy exactly; for stronger security, run `python scripts/generate_secrets.py` and use those instead):

```text
SECRET_KEY=a7f3c9e1b8d4f0e6c2a9b5d1f7e3c8a4b0d6e2f9c5a1b7d3e8f4c0a6b2d8e5
JWT_SECRET_KEY=f2e8d4a0b6c3e9f5a1d7b4c0e8f3a6b9d2c5e1f7a4b0d8c3e6f9a2b5d1e4
```

4. Save. The Space will **rebuild** automatically.

---

## Step 4: Wait for the build and get your URL

1. On the Space page, check the **"Build logs"** / **"Logs"** until the build finishes (first time can take 5–10 minutes).
2. When it’s running, the **public URL** is at the top of the Space (e.g. "App" or "View app").
3. Your **final public hosting URL** is:
   ```text
   https://<YOUR_HF_USERNAME>-<YOUR_SPACE_NAME>.hf.space
   ```
   Example: `https://johndoe-contract-simplifier.hf.space`

---

## Step 5: First use

1. Open your final URL in a browser.
2. Click **Register** and create the first account (this user becomes **admin**).
3. Share the **same URL** with everyone; they can Register/Login from their laptops. No install needed.

---

## Quick reference

| What | Where |
|------|--------|
| Create DB | https://neon.tech or https://supabase.com |
| Create Space | https://huggingface.co/spaces → Create new Space (Docker) |
| Add secrets | Space → Settings → Repository secrets |
| Your public URL | `https://YOUR_HF_USERNAME-YOUR_SPACE_NAME.hf.space` |
| Generate new keys | `python scripts/generate_secrets.py` (in project folder) |

---

**I can’t create your account or Space for you** – you must do Steps 1 and 2 in your browser. After that, the **final public hosting URL** is the one shown on your Space page (format above).
