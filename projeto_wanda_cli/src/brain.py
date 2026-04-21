import ollama
from src.memory import load_context, save_thought
from src.skills import get_system_info

# Configure o modelo que você tem baixado no Ollama
# Mude de "llama3" para "phi3"
MODEL_NAME = "gemma2:2b" 

def think(user_input):
    """Processa a entrada do usuário e gera resposta"""
    
    # 1. Salva o que o usuário disse
    save_thought("user", user_input)
    
    # 2. Carrega memória
    history = load_context(limit=5)
    
    # 3. Contexto do Sistema (A Personalidade)
    system_prompt = {
        "role": "system",
        "content": f"""
        Você é WANDA, uma IA assistente rodando localmente no Linux do Pedro.
        {get_system_info()}
        
        Sua personalidade: Mística, poderosa, direta e leal. Cores: Vermelho e Preto.
        
        Se o usuário pedir um comando de terminal, forneça o comando.
        Se for uma conversa, responda de forma inteligente.
        Não use markdown complexo, foque em texto limpo para terminal.
        """
    }
    
    messages = [system_prompt] + history
    
    # 4. Gera a resposta (Stream para parecer que está digitando)
    full_response = ""
    stream = ollama.chat(model=MODEL_NAME, messages=messages, stream=True)
    
    return stream

def save_wanda_response(full_text):
    """Salva a resposta final da Wanda na memória"""
    save_thought("assistant", full_text)