def save_found_keywords(results, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("PALABRAS RESERVADAS ANSI C ENCONTRADAS\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"{'No.':<5}{'Palabra':<15}{'Linea':<10}{'Columna':<10}\n")
        file.write("-" * 50 + "\n")

        for index, result in enumerate(results, start=1):
            file.write(
                f"{index:<5}{result['token']:<15}"
                f"{result['line']:<10}{result['column']:<10}\n"
            )


def save_history(all_evaluations, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("HISTORIAL DEL DFA\n")
        file.write("=" * 50 + "\n\n")

        for item in all_evaluations:
            file.write(f"Token evaluado: {item['token']}\n")
            file.write(f"Linea: {item['line']}, Columna: {item['column']}\n")

            for step in item["history"]:
                file.write(
                    f"  Lee '{step['char']}': "
                    f"{step['from']} -> {step['to']}\n"
                )

            file.write(f"Estado final: {item['final_state']}\n")

            if item["is_reserved"]:
                file.write("Resultado: PALABRA RESERVADA\n")
            else:
                file.write("Resultado: NO ES PALABRA RESERVADA\n")

            file.write("-" * 50 + "\n")


def save_transition_table(dfa, output_path):
    rows = dfa.get_transition_table()

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("TABLA DE TRANSICIONES DEL DFA\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"{'Estado':<15}{'Caracter':<15}{'Siguiente estado':<20}\n")
        file.write("-" * 50 + "\n")

        for state, char, next_state in rows:
            file.write(f"{state:<15}{char:<15}{next_state:<20}\n")