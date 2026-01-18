#!/bin/bash
set -e
pip install -r requirements.txt
exec streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
