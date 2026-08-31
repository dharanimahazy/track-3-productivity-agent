# Track 3: Productivity Agent ⚡🤖

[![Deployed on Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?logo=render&logoColor=white)](https://track-3-productivity-agent.onrender.com/)
[![Challenge](https://img.shields.io/badge/Challenge-AccelerateAIwithCloudRun-orange)](#)

This repository contains the Track 3 submission for the **Google Cloud Gen AI Academy Challenge**. It delivers an AI-powered personal productivity assistant designed to streamline workflows, prioritize tasks, and draft professional communications.

## 🌟 Overview
Built to enhance daily efficiency, this agent leverages generative AI to act as a digital assistant. Users can input unorganized meeting notes for structured summaries, request professional email drafts, or ask for help prioritizing a list of daily tasks.

## 🚀 Live Demo
**[https://track-3-productivity-agent.onrender.com/](https://track-3-productivity-agent.onrender.com/)**

[View Track 3 Demo Screenshot](track-3-demo.pdf)

*(Note: Hosted on a free Render instance. Please allow ~30–50 seconds for the initial load if the server is waking up from sleep mode.)*

## 🚀 Key Architectural Highlights
* **AI Engine:** Powered by `gemini-3.6-flash` for rapid content generation, summarization, and task structuring.
* **Web Framework:** Built with Python and Flask, utilizing a lightweight, responsive HTML/CSS frontend.
* **Serverless Deployment:** Fully containerized via Docker and hosted on **Render** (originally built for Google Cloud Run).

## 📁 Repository Structure
* `app.py`: Main Flask application handling routing and Gemini API interactions.
* `Dockerfile`: Container configuration optimized for cloud deployments.
* `requirements.txt`: Python package dependencies.

## ☁️ Deployment Reference
This agent was originally deployed to Cloud Run using the following Google Cloud SDK command (now hosted on Render using the same containerization approach):
```bash
gcloud run deploy productivity-agent \
  --source . \
  --region us-central1 \
  --set-env-vars GEMINI_API_KEY="A.xxxxxx7aqe" \
  --allow-unauthenticated
