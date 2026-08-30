# Track 2: BigQuery Data Agent 📊🤖

[![Deployed on Cloud Run](https://img.shields.io/badge/Deployed_on-Google_Cloud_Run-blue?logo=googlecloud)](https://bq-data-agent-277368074908.us-central1.run.app)
[![Challenge](https://img.shields.io/badge/Challenge-AccelerateAIwithCloudRun-orange)](#)

This repository contains the Track 2 submission for the **Google Cloud Gen AI Academy Challenge**. It delivers an internal-facing data analyst agent capable of translating natural language queries into insights using Google BigQuery and the Gemini API.

## 🌟 Overview
Built for business users, this agent democratizes data access by allowing team members to ask complex data questions in plain English. The agent processes the request, interacts with BigQuery schemas, and synthesizes the data into readable insights.

## 🚀 Live Demo
**[https://bq-data-agent-277368074908.us-central1.run.app](https://bq-data-agent-277368074908.us-central1.run.app)**

[View Track 2 Demo Screenshot](track-2-demo.pdf)

*(Note: This application was deployed using temporary Google Cloud trial credits. The live server has automatically spun down to prevent billing, but the complete source code, configurations, and documentation are available in this repository.)*

## 🚀 Key Architectural Highlights
* **Data Engine:** Integrated with `google-cloud-bigquery` for enterprise data warehousing.
* **AI Engine:** Powered by `gemini-2.5-flash` for high-speed natural language to SQL translation and data summarization.
* **Serverless Deployment:** Fully containerized and hosted on **Google Cloud Run**.

## 📁 Repository Structure
* `app.py`: Flask web application, BigQuery client initialization, and Gemini orchestration.
* `Dockerfile`: Container configuration optimized for Cloud Run.
* `requirements.txt`: Python package dependencies including GCP libraries.

## ☁️ Deployment Reference
This agent was deployed directly to Cloud Run using the following Google Cloud SDK command:
```bash
gcloud run deploy bq-data-agent \
  --source . \
  --region us-central1 \
  --set-env-vars GEMINI_API_KEY="AQ.Ab8RN6JRwr_zal1vGusiVJ9Ht5G-I6eEoGq5_BzCAROIRG47gA" \
  --allow-unauthenticated