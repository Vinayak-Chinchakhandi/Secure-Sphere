import re
from urllib.parse import urlparse

def extract_features_from_url(url):
    features = []

from urllib.parse import urlparse

def extract_features_from_url(url):
    features = []

    # 1. Length of the URL
    features.append(len(url))

    # 2. HTTPS check
    features.append(1 if url.startswith("https") else 0)

    # 3. Presence of '@' symbol
    features.append(1 if "@" in url else 0)

    # 4. Long URL check (arbitrary threshold, e.g., 75)
    features.append(1 if len(url) > 75 else 0)

    # 5. Suspicious keywords
    suspicious_keywords = ['login', 'secure', 'bank', 'verify']
    features.append(1 if any(word in url.lower() for word in suspicious_keywords) else 0)

    return features

