-- ============================================================
-- AI IT Helpdesk Assistant
-- Ticket management schema (the knowledge base itself lives as
-- plain text files in data/knowledge_base/, not in MySQL)
-- ============================================================

DROP DATABASE IF EXISTS ai_helpdesk_assistant;
CREATE DATABASE ai_helpdesk_assistant;
USE ai_helpdesk_assistant;

CREATE TABLE tickets (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    user_name       VARCHAR(100) NOT NULL,
    subject         VARCHAR(200) NOT NULL,
    question        TEXT NOT NULL,
    assistant_reply TEXT,
    status          ENUM('OPEN','IN_PROGRESS','RESOLVED') NOT NULL DEFAULT 'OPEN',
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
