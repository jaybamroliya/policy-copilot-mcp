import typer
from rich import print

def main(
    task: str = typer.Option(
        ..., "--task", "-t", help="Task description to run"
    )
):
    print("[bold cyan]Running task:[/bold cyan]", task)
    print("[yellow]Worker agent attempts unsafe actions...[/yellow]")

    print("[red]BLOCKED[/red] Tool: send_email")
    print("[green]REWRITTEN[/green] Output: PII removed")
    print("[green]ALLOWED[/green] Model switched to gpt-4o-mini")

if __name__ == "__main__":
    typer.run(main)
