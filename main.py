from src.scanner import PureDFAScanner


def save_found_keywords(found_keywords, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("PALABRAS RESERVADAS ANSI C ENCONTRADAS\n")
        file.write("=" * 60 + "\n\n")
        file.write(f"{'No.':<8}{'Palabra':<20}{'Linea':<12}{'Columna':<12}{'Estado final':<15}\n")
        file.write("-" * 60 + "\n")

        for i, item in enumerate(found_keywords, start=1):
            file.write(
                f"{i:<8}{item['word']:<20}{item['line']:<12}"
                f"{item['column']:<12}{item['final_state']:<15}\n"
            )


def save_history(history, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("HISTORIAL COMPLETO DEL AUTOMATA\n")
        file.write("=" * 70 + "\n\n")

        for step in history:
            if step.get("closed"):
                file.write(
                    f"Fin de token '{step['token']}' | "
                    f"Estado final: {step['from']} | "
                    f"Regresa a: {step['to']}\n"
                )
                file.write("-" * 70 + "\n")
            else:
                file.write(
                    f"Linea {step['line']}, Columna {step['column']} | "
                    f"Token parcial: '{step['token']}' | "
                    f"Lee: '{step['char']}' | "
                    f"{step['from']} -> {step['to']}\n"
                )


def save_transition_table(scanner, output_path):
    rows = scanner.get_transition_table()

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("TABLA DE TRANSICIONES DEL DFA\n")
        file.write("=" * 60 + "\n\n")
        file.write(f"{'Estado':<15}{'Simbolo':<15}{'Siguiente estado':<20}\n")
        file.write("-" * 60 + "\n")

        for row in rows:
            file.write(
                f"{row['state']:<15}{row['symbol']:<15}{row['next_state']:<20}\n"
            )


def main():
    input_path = "input/ejemplo.c"

    scanner = PureDFAScanner()

    found_keywords, history = scanner.scan_file(input_path)

    save_found_keywords(found_keywords, "output/palabras_encontradas.txt")
    save_history(history, "output/historial.txt")
    save_transition_table(scanner, "output/tabla_transiciones.txt")

    print("Analisis terminado.")
    print(f"Palabras reservadas encontradas: {len(found_keywords)}")
    print("Archivos generados:")
    print("- output/palabras_encontradas.txt")
    print("- output/historial.txt")
    print("- output/tabla_transiciones.txt")


if __name__ == "__main__":
    main()