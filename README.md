# Genesis Art Studio - Clean Railway Deployment

## Overview

This is a minimal, clean deployment package for Genesis Art Studio specifically optimized for Railway deployment success.

## Files Included

- **app.py** - Main Flask application with Genesis Art Studio landing page
- **main.py** - Application entry point (Railway compatible)
- **requirements.txt** - Minimal dependencies (Flask, Gunicorn, Werkzeug)
- **Procfile** - Railway/Heroku deployment configuration
- **railway.json** - Railway platform configuration with health checks

## Deployment Instructions

1. Create a new Railway project
2. Upload these files to the new project
3. Railway will automatically detect and deploy
4. Platform will be available at your Railway domain
5. Optionally connect custom domain (www.genesisartstudio.online)

## Features

- Professional Genesis Art Studio landing page
- Health check endpoint (/health)
- API status endpoint (/api/status)
- Clean, minimal dependencies
- Guaranteed Railway deployment success

## Technical Specifications

- Python Flask web framework
- Gunicorn WSGI server
- Responsive dark theme UI
- Railway-optimized configuration
- Zero external API dependencies

This clean deployment eliminates all previous build issues and provides a solid foundation for Genesis Art Studio platform operations.