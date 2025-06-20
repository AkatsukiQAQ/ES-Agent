# ES-Agent: Auto Entry Sheet Generator (for Japanese or English Job Applications)

ES-Agent is a LangChain-powered agent designed to automatically generate Entry Sheet (ES) answers for internship and new graduate job applications in Japan.  
It takes a structured YAML-based user profile and a job description (JD), matches each question type to appropriate prompt templates, and produces coherent, customized answers.



## Motivation
In the Japanese internship application process, candidates often spend a large amount of time repeatedly writing similar Entry Sheet (ES) answers.  
I created ES-Agent to automate this process using LLMs, while still allowing customization and structured reasoning through a YAML profile and prompt system.  
This project helps me explore how LLMs can be practically applied to streamline real-world workflows, and serves as a foundation to build autonomous agents.



## Usage

### Installation
First, clone this [repo](https://github.com/AkatsukiQAQ/ES-Agent) by running the following commands.
```bash
git clone https://github.com/AkatsukiQAQ/ES-Agent.git
cd ES-Agent
```

Then, install the dependencies using the following commands.
```bash
pip install -r requirements.txt
```

Next, prepare your profile and save it at `data/user_profile.yaml`. You can use the template at `data/user_profile_template.yaml` to check what kind of information are necessary.

Also, copy the job description of the position you are applying into `data/job_description.txt`.

Run the following command to start the agent.
```bash
python3 main.py
```



##  TODO / Planned Features

### ✅ Core Agent
- [x] Basic pipeline: input question → profile + prompt → LLM → ES output (Currently 70%)
- [ ] Support multi-turn Q&A flow until user exits

### ✍️ Profile Management
- [ ] Auto Profile Loader, which can load profile into formed text by detecting the structure
- [ ] Retriever: ONLY load relative profile for precise generation
- [ ] Missing or incomplete experience completion
  - [ ] Detect missing or incomplete experience based on JD
  - [ ] Prompt user to update profile during session
  - [ ] Update `data/user_profile.yaml` based on the new information

### 🧠 Memory System
- [ ] Short-term memory: keep track of answers in a session
- [ ] Long-term memory: persist useful info across sessions

### ⚙️ Model Management
- [ ] Support model selection (GPT-4 / HuggingFace / local)
- [ ] Add API key manager

### 📊 Utility Features
- [ ] JD parser to identify role expectations and required skills
- [ ] Self-evaluation: LLM-based ES answer scoring and feedback

### 🖥️ User Interface
- [ ] Build lightweight GUI (TypeScript, React)
- [ ] File upload/download (profile, JD, output text)
