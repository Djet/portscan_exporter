FROM python:3.8.7-alpine3.13
RUN pip3 install pyaml python3-nmap prometheus_client \
    && apk add nmap sudo 
COPY portscan_exporter.py .
ENTRYPOINT ["python","portscan_exporter.py"] 
