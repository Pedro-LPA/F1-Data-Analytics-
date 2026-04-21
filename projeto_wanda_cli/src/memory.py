import sqlite3
import os
from datetime import datetime

# Caminho do banco
DB_DIR = os.path.join(os.getcwd(), 'data')
DB_PATH = os.path.join(DB_DIR, 'wanda.db')

def init_memory():
    """Cria a mente da Wanda se não existir"""
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabela simples de chat
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_thought(role, content):
    """Guarda um pensamento (user ou assistant)"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def load_context(limit=10):
    """Recupera as últimas conversas para dar contexto"""
    conn = sqlite3.connect(DB_PATH)
    # Pega os ultimos X e inverte para ordem cronologica
    cursor = conn.cursor()
    cursor.execute(f"SELECT role, content FROM history ORDER BY id DESC LIMIT {limit}")
    rows = cursor.fetchall()
    conn.close()
    
    # Formata para o padrão do Ollama
    history = [{"role": row[0], "content": row[1]} for row in rows]
    return history[::-1]