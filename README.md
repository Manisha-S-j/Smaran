# 🤖 SMARAN – AI-Powered Memory Companion for Dementia Care

> 🌿 *Empowering elderly care with local AI, reminders, and sustainable computing.*

---

## 🩺 About SMARAN

**SMARAN** is an AI-powered dementia care companion designed to assist elderly users with:
- Medicine and routine reminders 🕒  
- Facial recognition of loved ones 👨‍👩‍👧  
- Voice-based assistance for better accessibility 🎙️  
- Caregiver dashboard to track reminders and health updates 👩‍⚕️  
- Sustainable AI operations powered by local inference (TFLite / Edge AI) 🌱  

Built using **Blink**, a no-code AI development platform, SMARAN provides a clean, elderly-friendly interface and sustainable AI integration.

---

## 🚀 Features

| Feature | Description |
|----------|-------------|
| 🧩 Smart Reminders | Alerts users and caregivers for medicines or daily activities |
| 👵 Face Recognition | Identifies familiar faces for memory reinforcement |
| 🎤 Voice Assistant | Allows voice-based interaction for hands-free operation |
| 💚 Sustainable AI | Local model reduces latency & energy usage |
| 📈 Carbon Calculator | Integrated emission tracking with `CodeCarbon` (bash-based) |
| 🌍 Caregiver Dashboard | Real-time updates for caregivers |

---

## 🧮 Carbon Calculator Integration

To comply with the **Green Mind Hackathon** sustainability requirements, SMARAN includes a **Carbon Emission Monitoring** module .

### ⚙️ How It Works
- The calculator measures power and energy usage during baseline (idle) and active (app-running) modes.
- It uses the **CodeCarbon** library to log and compare emissions data.

### 🧾 To Use the Carbon Calculator

1️⃣ Navigate to the `Carbon-Calculator` folder.  
2️⃣ Make the script executable:
```bash
chmod +x emission_calculation.sh
3️⃣ Run Baseline Mode:

./emission_calculation.sh --app-run false --team-name Smaran


4️⃣ Run Application Mode (while SMARAN is active):

./emission_calculation.sh --app-run true --team-name Smaran --run-seconds 1800


5️⃣ Output CSV files will be saved in:

/emissions_logs/
  ├── monitoring_app_run_false.csv
  ├── monitoring_app_run_true.csv

🧠 Tech Stack
Layer	Tools / Technologies
💻 Frontend	Blink AI Platform
⚙️ Backend	Blink’s built-in AI workflows
🧩 AI Models	Local Edge AI (TFLite / On-device)
📊 Sustainability	CodeCarbon (Carbon Emission Tracker)
🧾 Monitoring Script	Bash Automation (emission_calculation.sh)
🌍 Version Control	GitHub
📁 Project Structure
SMARAN/
│
├── assets/                  # Images, icons, and visual assets
├── static/                  # Static files (CSS, JS)
├── templates/               # UI templates for pages
├── Carbon-Calculator/       # Emission monitoring module
│   ├── emission_calculation.sh
│   └── README.md
│
├── README.md                # Project overview (this file)
└── .gitignore

🌱 Sustainability Highlights

⚡ Local AI Inference – 70% lower network energy use

🌍 Hybrid AI Mode – Switches between cloud & local as needed

♻️ CodeCarbon Integration – Monitors & logs carbon footprint

💡 Energy Dashboard – Displays eco-efficiency metrics

## 🎥 Live MVP Demo

You can try the working prototype of **SMARAN** here:

[**SMARAN – AI Dementia Companion (Live MVP)**](https://smaran-local-ai-memo-yolae6u3.sites.blink.new/?v=1762850064688&t=1762850064688)

> *(Built using Blink — a no-code AI platform for rapid prototyping.)*

---

*(Click above to open the Blink-hosted MVP demo)*


🏁 Hackathon

Event: Green Mind Hackathon 2025
Theme: Sustainable AI for Social Good
Track: HealthTech x Sustainability



This project is open-sourced for hackathon submission purposes.
Developed with ❤️ by Team SMARAN.