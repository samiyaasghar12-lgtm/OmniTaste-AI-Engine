import sys
import os

# Backend path ko system path mein add karein taake app module easily import ho sakay
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app.main import app