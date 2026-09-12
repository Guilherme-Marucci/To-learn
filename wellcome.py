"""Aplicativo de boas-vindas executado no terminal."""

import os
import shutil
import time


RESET = "\033[0m"
CYAN = "\033[96m"
MAGENTA = "\033[91m"
YELLOW = "\033[91m"
WHITE = "\033[97m"


def limpar_tela():
	os.system("cls" if os.name == "nt" else "clear")


def digitar(texto, atraso=0.025):
	for caractere in texto:
		print(caractere, end="", flush=True)
		time.sleep(atraso)
	print()


def main():
	limpar_tela()
	largura = shutil.get_terminal_size((80, 24)).columns
	enfeite = "✦  ✧  ✦  ✧  ✦  ✧  ✦"

	print(f"{CYAN}{enfeite}{RESET}".center(largura))
	time.sleep(0.5)
	print()
	print(f"{MAGENTA}╔══════════════════════════════════════╗{RESET}")
	print(f"{MAGENTA}║          W E L L C O M E !           ║{RESET}")
	print(f"{MAGENTA}╚══════════════════════════════════════╝{RESET}")
	print()
	digitar(f"{YELLOW}╭─ Uma breve demonstração dos meus projetos...{RESET}")
	for mensagem in ("Instalando Dependencias", "Acendendo novas ideias", "Abrindo caminhos"):
		print(f"{WHITE}│  {mensagem}... {CYAN}✓{RESET}")
		time.sleep(0.35)
	print()
	nome = input(f"{MAGENTA}Me chamo {RESET}").strip() or "visitante"
	print()
	digitar(f"{CYAN}Olá, {nome}!{RESET}", 0.045)
	digitar(f"{WHITE}Que alegria receber você. Este é o começo de um projeto incrível!{RESET}")
	print()
	print(f"{YELLOW}★  WELLCOME, {nome.upper()}!  ★{RESET}".center(largura))
	print(f"{CYAN}{enfeite}{RESET} \n\n".center(largura))


if __name__ == "__main__":
	main()
