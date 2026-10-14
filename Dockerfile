# Step 1: Base image choose karo - Python already installed wala
FROM python:3.13-slim

# Step 2: Container ke andar working folder banao
WORKDIR /app

# Step 3: requirements.txt ko copy karo container ke andar
COPY requirements.txt .

# Step 4: Libraries install karo
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Pura project code copy karo
COPY . .

# Step 6: Batao kaunsa port use hoga
EXPOSE 8000

# Step 7: Jab container start ho, ye command chalao
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]