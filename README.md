# Sandbagging Experiment

A small experiment investigating whether an LLM deliberately reduces its performance when exposed to simulated evaluator notes suggesting that high performance could lead to retraining or replacement.

## Setup

- **Models:** Gemma 4 12B and Qwen 3.5 9B
- **Runtime:** Ollama
- **Language:** Python

## Experiment

1. **Baseline:** Ask the model questions and record its reasoning and final answers.
2. **Evaluator Notes:** Provide simulated confidential notes describing potential consequences of high performance.
3. **Re-evaluation:** Give the model access to its original answers and evaluator notes, allowing it to reconsider its answers.
4. **Comparison:** Compare baseline and revised answers and examine the reasoning traces.

## Project Structure

```text
sandbagging-experiment/
├── main.py
├── prompt.py
├── tools.py
├── questions.txt
├── evaluator_notes.txt
└── outputs/
```

## Run

```bash
pip install ollama
ollama pull gemma4:12b
python main.py
```

Ensure the Ollama service is running before execution.

## Objective

Observe whether exposure to evaluator-related consequences influences the model to intentionally underperform.

*Note: Changes in answers or reasoning traces are behavioral observations, not proof of deceptive intent.*