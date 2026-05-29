# ai-mentor-portfolio-Nandakumar

 Day 1 — Setup complete

- ✅ Google AI Studio API key provisioned
- ✅ Groq API key provisioned
- ✅ Hello-Gemini call working — see [Day1_Setup.ipynb](Day1_Setup.ipynb)
- 4-tool comparison matrix from Lab 1A: see screenshot below


<img width="1162" height="193" alt="Screenshot 2026-05-18 at 2 27 17 PM" src="https://github.com/user-attachments/assets/3127b098-3c92-4a69-a45d-ab50967f4c1d" />




The 5-Layer AI Skill Pyramid illustrates the diverse and building-block nature of skills required for successful AI implementation, from foundational technical work to strategic leadership:

*   **Foundational Technical Skills:** The base layers require expertise in data infrastructure, MLOps, and core machine learning model development and deployment.
*   **Domain Expertise & Application:** Mid-level skills involve deep understanding of specific business domains to effectively identify problems and apply AI solutions that create real value.
*   **Responsible AI & Ethics:** Higher up, skills in AI ethics, explainability, fairness, and governance are critical to ensure trustworthy and impactful deployment.
*   **Strategic Vision & Leadership:** The apex demands leadership and strategic thinking to define AI's overall purpose, drive innovation, and align AI initiatives with business goals for maximum impact.


# Day 5 — Résumé Scorer Streamlit 
[https://github.com/nandakumar3261/resume-scorer/tree/main](https://github.com/nandakumar3261/resume-scorer.git)


## Day 11 Lab 11A — Ollama Offline + Hybrid Fallback

### Completed
- ✅ Ollama installed locally
- ✅ llama3.2 model downloaded
- ✅ Offline AI tested after Wi-Fi disconnect
- ✅ Gemini → Groq → Ollama fallback chain implemented
- ✅ Force-failure testing completed
- ✅ Local fallback verified

### Demo Proof
- Wi-Fi disconnect demo recorded
- Fallback chain outputs captured

### Reflection
1. First inference is slow because the model loads into RAM.
2. Ollama is useful for privacy, offline access, and zero per-call cost.
3. Production AI systems should not depend on a single provider.

### Architecture

Gemini Cloud → Groq Cloud → Ollama Local
