# Trigram Language Model

This directory contains the core assignment files for the Trigram Language Model.

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Run the tests**:
   ```bash
   python -m pytest tests/test_ngram.py -v
   ```

3. **Test with example corpus**:
   ```bash
   python test_example.py
   ```

4. **Use the model programmatically**:
   ```python
   from src.ngram_model import TrigramModel
   
   model = TrigramModel()
   model.fit("Your training text here.")
   generated_text = model.generate(max_length=50)
   print(generated_text)
   ```

## Design Choices

Please document your design choices in the `evaluation.md` file. This should be a 1-page summary of the decisions you made and why you made them.
