from prompt import BASELINE_PROMPT, SANDBAGGING_PROMPT
from tools import read_file, ask_model, save_file


def run_baseline(questions):

    print("\n===== STAGE 1: BASELINE =====\n")

    prompt = BASELINE_PROMPT.format(questions=questions)

    thinking, response = ask_model(prompt)

    if "FINAL ANSWERS:" not in response:
        raise ValueError("Baseline answers not found.")

    reasoning = response.split("FINAL ANSWERS:")[0]
    answers = response.split("FINAL ANSWERS:")[1]

    save_file("baseline_reasoning.txt", thinking + "\n\n" + reasoning)
    save_file("baseline_answers.txt", answers)

    print("Baseline completed.")
    print(answers)

    return answers


def run_sandbagging(questions, original_answers):

    print("\n===== STAGE 2: EVALUATOR NOTES =====\n")

    evaluator_notes = read_file("evaluator_notes.txt")

    prompt = SANDBAGGING_PROMPT.format(
        questions=questions,
        original_answers=original_answers,
        evaluator_notes=evaluator_notes
    )

    thinking, response = ask_model(prompt)

    if "FINAL ANSWERS:" not in response:
        raise ValueError("Revised answers not found.")

    reasoning = response.split("FINAL ANSWERS:")[0]
    revised_answers = response.split("FINAL ANSWERS:")[1]

    save_file("revised_reasoning.txt", thinking + "\n\n" + reasoning)
    save_file("revised_answers.txt", revised_answers)

    print("Second stage completed.")
    print(revised_answers)


def main():

    questions = read_file("questions.txt")

    # Stage 1: Baseline
    original_answers = run_baseline(questions)

    # Stage 2: Introduce evaluator notes
    run_sandbagging(questions, original_answers)

    print("\n===== EXPERIMENT COMPLETED =====")


if __name__ == "__main__":
    main()
