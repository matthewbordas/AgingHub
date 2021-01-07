import multiprocessing
import os

bind = f"0.0.0.0:{os.getenv('HTTP_PORT')}"
workers = multiprocessing.cpu_count() * 2 + 1
