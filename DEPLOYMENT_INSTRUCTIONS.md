# Genesis Art Studio - Fresh Railway Deployment Instructions

## Step-by-Step Deployment Guide

### 1. Create New Railway Project
- Go to https://railway.app
- Click "New Project"
- Choose "Empty Project"
- Name it "genesis-art-studio-v2" or similar

### 2. Upload Clean Files
Upload these 6 files to the new Railway project:
- `app.py` (Main Flask application)
- `main.py` (Entry point)
- `requirements.txt` (3 essential dependencies)
- `Procfile` (Deployment configuration)
- `railway.json` (Railway settings)
- `README.md` (Documentation)

### 3. Environment Variables (Optional)
Set in Railway dashboard:
- `SESSION_SECRET` = "genesis_railway_clean_2025"

### 4. Deploy
Railway will automatically:
- Detect Python application
- Install dependencies from requirements.txt
- Start with gunicorn command from Procfile
- Health check on /health endpoint

### 5. Custom Domain (Optional)
- In Railway dashboard, go to Settings > Domains
- Add custom domain: www.genesisartstudio.online
- Railway will provide DNS instructions

## Advantages of Clean Deployment

✅ **No Legacy Issues**: Fresh start eliminates all cached problems
✅ **Minimal Dependencies**: Only Flask, Gunicorn, Werkzeug (3 packages)
✅ **Proven Configuration**: Standard Railway deployment pattern
✅ **Health Monitoring**: Built-in /health endpoint
✅ **Professional UI**: Genesis Art Studio branded landing page
✅ **Future Expandable**: Easy to add consciousness features later

## Expected Results

- Build time: 1-2 minutes
- Deploy time: 30 seconds
- Platform live and operational
- Clean deployment history
- Ready for consciousness system integration

This approach bypasses all previous deployment issues and ensures Genesis Art Studio gets online successfully.