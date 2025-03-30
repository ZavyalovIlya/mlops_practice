FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt make_prediction.py fastapi_app.py  /app/
COPY models/linreg.pkl models/scaler_X.pkl models/scaler_y.pkl /app/models/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]