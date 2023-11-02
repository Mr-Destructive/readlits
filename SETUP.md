

```bash
# Add dependencies in requirements.in

# Generate entire dependencies tree in requirements.txt
pip-compile requirements.in

# Install all nested dependencies from requirements.txt
pip install -r requirements.txt
```
