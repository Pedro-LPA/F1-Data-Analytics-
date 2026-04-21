import sys
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.layout import Layout
from rich.live import Live

from src.memory import init_memory
from src.brain import think, save_wanda_response

# Configuração Visual (Vermelho Wanda)
console = Console()
WANDA_STYLE = "bold red"
USER_STYLE = "bold white"

def main():
    # Inicializa banco de dados
    init_memory()
    
    console.clear()
    console.print(Panel(
        "[bold red]🔮 WANDA AI - SYSTEM ONLINE[/bold red]\n[italic white]O caos é apenas o começo.[/italic white]",
        border_style="red",
        expand=False
    ))

    while True:
        try:
            # Entrada do Usuário
            console.print("\n[bold cyan]Pedro:[/bold cyan]")
            user_input = input("❯ ") # Usando input nativo pra ficar limpo
            
            if user_input.lower() in ["sair", "exit", "tchau"]:
                console.print("[red]Desconectando...[/red]")
                break
                
            if not user_input.strip():
                continue

            # Resposta da Wanda
            console.print(f"\n[{WANDA_STYLE}]Wanda:[/{WANDA_STYLE}]")
            
            full_response = ""
            # Simula streaming (efeito digitação)
            with Live("", refresh_per_second=15, console=console) as live:
                stream = think(user_input)
                for chunk in stream:
                    part = chunk['message']['content']
                    full_response += part
                    live.update(Markdown(full_response))
            
            # Salva no final
            save_wanda_response(full_response)
            
        except KeyboardInterrupt:
            console.print("\n[red]Interrupção detectada. Encerrando.[/red]")
            break
        except Exception as e:
            console.print(f"[bold red]Erro no sistema:[/bold red] {e}")

if __name__ == "__main__":
    main()