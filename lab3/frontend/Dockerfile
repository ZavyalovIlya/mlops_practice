FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt streamlit_app.py /app/
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["streamlit_app.py"]