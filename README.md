# AI Story Generator

## Project Overview
This is a Streamlit-based web application that uses Groq AI models to generate creative stories based on user inputs (genre, tone, characters, etc.). It features a premium "Cinematic Dark" UI design.

## 🚀 How to Upload to GitHub (Safely)
Your API keys are stored in `.streamlit/secrets.toml`. This file is already added to your `.gitignore` file, which means **Git will ignore it**, keeping your keys safe and off the internet.

### Step 1: Initialize and Commit Locally
Open your terminal in the project folder (`c:\vscode\ownstory`) and run these commands one by one:

```bash
# 1. Initialize a new git repository
git init

# 2. Add all files to staging (this automatically skips ignored files like secrets.toml)
git add .

# 3. Commit your changes
git commit -m "Initial commit - AI Story Generator App"
```

### Step 2: Create a Repository on GitHub
1. Go to [GitHub.com](https://github.com) and sign in.
2. Click the **+** icon in the top-right corner and select **New repository**.
3. Name it (e.g., `ai-story-generator`).
4. Keep it **Public** (your code is public, but your keys remain private on your computer).
5. Do **NOT** check "Add a README", ".gitignore", or "License" (since we are rewriting the project from your local machine).
6. Click **Create repository**.

### Step 3: Connect and Push
Copy the commands shown on GitHub under **"…or push an existing repository from the command line"** and run them in your terminal. They will look like this:

```bash
# Replace URL with your actual new repository URL
git remote add origin https://github.com/YOUR_USERNAME/ai-story-generator.git
git branch -M main
git push -u origin main
```

---

## 🌐 How to Deploy for Free (Streamlit Community Cloud)
The easiest way to host this app for free is **Streamlit Community Cloud**, as it supports the `secrets.toml` pattern natively.

1. **Sign Up**: Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
2. **New App**: Click **"New app"** (or "Create app").
3. **Select Repository**:
   - Choose the `ai-story-generator` repository you just pushed.
   - Branch: `main`
   - Main file path: `app.py`
4. **⚠️ IMPORTANT: Add Your API Keys**
   - Before clicking "Deploy", click **"Advanced settings"**.
   - Find the **"Secrets"** section.
   - Paste the contents of your local `.streamlit/secrets.toml` file here. It should look like this:
     ```toml
     GROQ_API_KEY = "gsk_..."
     ```
   - Click **Save**.
5. **Deploy**: Click **"Deploy!"**.

Your app will be live in a few minutes! 🚀
