job-application-assistant/
│
├── .gitignore
├── .env
├── .env.example
├── README.md
├── requirements.txt
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── job.py
│   │   ├── profile.py
│   │   ├── resume.py
│   │   └── application.py
│   │
│   ├── llm/
│   │   ├── client.py
│   │   ├── prompts.py
│   │   └── structured_output.py
│   │
│   ├── ingestion/
│   │   ├── pdf_loader.py
│   │   ├── docx_loader.py
│   │   └── chunker.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   │
│   ├── agents/
│   │   ├── job_parser.py
│   │   ├── profile_agent.py
│   │   ├── matching_agent.py
│   │   ├── resume_agent.py
│   │   ├── cover_letter_agent.py
│   │   └── interview_agent.py
│   │
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   └── workflow.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── models.py
│   │   └── repository.py
│   │
│   └── utils/
│       ├── logging.py
│       └── helpers.py
│
├── data/
│   ├── resumes/
│   ├── jobs/
│   └── vectorstore/
│
├── tests/
│   ├── test_job_parser.py
│   ├── test_rag.py
│   └── test_agents.py
│
└── notebooks/
    └── experiments/