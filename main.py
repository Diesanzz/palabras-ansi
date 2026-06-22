from src.keywords import RESERVED_WORDS
from src.dfa import DFA
from src.lexer import extract_tokens_with_positions
from src.report_generator import (
    save_found_keywords,
    save_history,
    save_transition_table
)


def main():
    input_path = "input/ejemplo.c"

    with open(input_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    dfa = DFA(RESERVED_WORDS)
    tokens = extract_tokens_with_positions(source_code)

    all_evaluations = []
    found_keywords = []

    for token_data in tokens:
        evaluation = dfa.evaluate(token_data["token"])

        complete_result = {
            **token_data,
            **evaluation
        }

        all_evaluations.append(complete_result)

        if evaluation["is_reserved"]:
            found_keywords.append(complete_result)

    save_found_keywords(found_keywords, "output/palabras_encontradas.txt")
    save_history(all_evaluations, "output/historial.txt")
    save_transition_table(dfa, "output/tabla_transiciones.txt")

    print("Analisis terminado.")
    print(f"Tokens evaluados: {len(all_evaluations)}")
    print(f"Palabras reservadas encontradas: {len(found_keywords)}")
    print("Archivos generados en la carpeta output/")


if __name__ == "__main__":
    main()