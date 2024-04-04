# Hedgehog (Transformer) - homemade transformers (for inference)

This project is a no-frills, hackable implementation of transformer inference, on CPU and GPU.

## Development

```sh
python3 -m venv .venv
echo 'export PYTHONPATH="${PYTHONPATH}:$(dirname ${VIRTUAL_ENV})"' >> .venv/bin/activate
source .venv/bin/activate
pip install --upgrade pip wheel
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-dev.txt
```