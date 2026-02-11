# OwnStory - AI Story Generator ✨

## Overview
OwnStory is a Streamlit-based web application that creates imaginative and engaging stories using modern Large Language Models (LLMs). Users can customize their stories by selecting inputs such as genre, tone, characters, and narrative style, allowing for a personalized storytelling experience.

The project focuses on combining creative flexibility with high-performance AI to deliver rich stories in real time.


## Live Preview 🚀
You can try the application live here:

🔗 **Live App:** [https://ownstory-ai-story-generator.streamlit.app](https://ownstory--ai-story-generator-shivsspace.streamlit.app/)  

---

## AI Inference Engine: Groq
This application uses **Groq** as the inference provider for running Large Language Models.

**Why Groq?**  
Groq’s custom **Language Processing Unit (LPU)** architecture enables extremely low-latency inference, resulting in:
- Lightning-fast response times  
- Smooth, real-time story generation  
- An improved and seamless user experience  

---

## Language Models & Narrative Styles
Different storytelling styles require different model strengths. The application supports multiple narrative styles, each powered by a carefully selected model.

| Narrative Style | Model Used | Why This Model |
|-----------------|-----------|----------------|
| **Cinematic** | `llama-3.3-70b-versatile` | High-fidelity storytelling with rich descriptions, emotional depth, and complex narrative structures—ideal for cinematic experiences. |
| **Classic** | `llama-3.1-70b-versatile` | A reliable and balanced model that follows instructions well while maintaining clear, coherent, and elegant prose. |
| **Fast** | `mixtral-8x7b-32768` | A highly efficient Mixture-of-Experts model optimized for speed, making it perfect for rapid ideation and quick story generation. |

---

## Tech Stack
- **Frontend & UI:** Streamlit  
- **AI Models:** LLaMA & Mixtral (via Groq)  
- **Inference Provider:** Groq LPU  

---

## Purpose
This project demonstrates how high-speed inference and carefully chosen LLMs can be combined to create a responsive, creative, and user-friendly AI storytelling application.
