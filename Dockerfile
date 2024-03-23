FROM python:3.9
ENV USER=appuser

COPY . .

COPY --chown=$USER:$USER requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
