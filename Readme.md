# Track 3: Productivity Agent ⚡🤖

[![Deployed on Cloud Run](https://img.shields.io/badge/Deployed_on-Google_Cloud_Run-blue?logo=googlecloud)](https://productivity-agent-277368074908.us-central1.run.app)
[![Challenge](https://img.shields.io/badge/Challenge-AccelerateAIwithCloudRun-orange)](#)

This repository contains the Track 3 submission for the **Google Cloud Gen AI Academy Challenge**. It delivers an AI-powered personal productivity assistant designed to streamline workflows, prioritize tasks, and draft professional communications.

## 🌟 Overview
Built to enhance daily efficiency, this agent leverages generative AI to act as a digital assistant. Users can input unorganized meeting notes for structured summaries, request professional email drafts, or ask for help prioritizing a list of daily tasks.

## 🚀 Live Demo
**[https://productivity-agent-277368074908.us-central1.run.app](https://productivity-agent-277368074908.us-central1.run.app)**

[View Track 3 Demo Screenshot](track-3-demo.pdf)

*(Note: This application was deployed using temporary Google Cloud trial credits. The live server has automatically spun down to prevent billing, but the complete source code, configurations, and documentation are available in this repository.)*

## 🚀 Key Architectural Highlights
* **AI Engine:** Powered by `gemini-2.5-flash` for rapid content generation, summarization, and task structuring.
* **Web Framework:** Built with Python and Flask, utilizing a lightweight, responsive HTML/CSS frontend.
* **Serverless Deployment:** Fully containerized via Docker and hosted on **Google Cloud Run**.

## 📁 Repository Structure
* `app.py`: Main Flask application handling routing and Gemini API interactions.
* `Dockerfile`: Container configuration optimized for Cloud Run deployments.
* `requirements.txt`: Python package dependencies.

## ☁️ Deployment Reference
This agent was deployed directly to Cloud Run using the following Google Cloud SDK command:
```bash
gcloud run deploy productivity-agent \
  --source . \
  --region us-central1 \
  --set-env-vars GEMINI_API_KEY="A.xxxxxx7aqe" \
  --allow-unauthenticated
