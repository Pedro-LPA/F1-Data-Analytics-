import subprocess
import platform

def execute_system_command(command):
    """Executa um comando no terminal real"""
    try:
        # Roda o comando e captura a saída
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True
        )
        if result.returncode == 0:
            return f"✅ Sucesso:\n{result.stdout}"
        else:
            return f"❌ Erro:\n{result.stderr}"
    except Exception as e:
        return f"💥 Falha crítica na execução: {str(e)}"

def get_system_info():
    """Retorna info do Linux pra Wanda saber onde está"""
    return f"Sistema: {platform.system()} {platform.release()} - Shell: Zsh"