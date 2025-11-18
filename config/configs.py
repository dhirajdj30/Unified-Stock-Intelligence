import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv
load_dotenv()


@dataclass
class LLMConfig:
    model_name: str
    api_key: str
    url: str = None
    cert_path: Optional[str] = None
    max_tokens: int = 512
    temperature: float = 0.0
    timeout: float = 50.0



def get_mistral_config() -> LLMConfig:
    """Get LLM configuration from environment or defaults"""
    
    # Find certificate path
    cert_path = _find_cert_path()
    
    return LLMConfig(
        url=os.getenv(
            "MISTRAL_API_URL", 
            "https://kubeingress.p31.eng.sjc01.qualys.com/mistral12b/v1"
        ),
        model_name=os.getenv("MISTRAL_MODEL_NAME", "mistral12b"),
        api_key=os.getenv("MISTRAL_API_KEY", "token-abc123"),
        cert_path=os.getenv("MISTRAL_CERT_PATH", cert_path),
        max_tokens=int(os.getenv("MISTRAL_MAX_TOKENS", "512")),
        temperature=float(os.getenv("MISTRAL_TEMPERATURE", "0.0")),
        timeout=float(os.getenv("MISTRAL_TIMEOUT", "50"))
    )

def get_gemini_config() -> LLMConfig:
    """Get Gemini LLM configuration from environment or defaults"""
    api_key = os.getenv("GOOGLE_API_KEY", "your-google-api-key")
    return LLMConfig(
        model_name="gemini-2.0-flash",  
        api_key=api_key
    )


def _find_cert_path() -> Optional[str]:
    """Find certificate path automatically"""
    
    # Check common certificate locations
    cert_locations = [
        # Project certificates (moved to root)
        "ops_bundle.pem",
        _get_certifi_path()
    ]
    
    for cert_path in cert_locations:
        if cert_path and Path(cert_path).exists():
            return str(cert_path)
    
    return None

def _get_certifi_path() -> Optional[str]:
    """Get certifi certificate path"""
    try:
        import certifi
        return certifi.where()
    except ImportError:
        return None

# def load_env_file():
#     """Load .env file if it exists"""
#     env_file = ".env"
#     if env_file.exists():
#         with open(env_file) as f:
#             for line in f:
#                 line = line.strip()
#                 if line and not line.startswith('#') and '=' in line:
#                     key, value = line.split('=', 1)
#                     os.environ[key.strip()] = value.strip()

# # Load environment variables on import
# load_env_file()
