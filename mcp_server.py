from mcp.server.fastmcp import FastMCP
import os, requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import List, Optional
from google import genai

class JD(BaseModel):
    company: str
    role: str
    must_have_skills: List[str]
    nice_to_have_skills: List[str] = []
    min_cgpa: Optional[float] = None
    locations: List[str] = []
    package_lpa: Optional[float] = None

mcp = FastMCP('placement-data')
client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

def fetch_jd(url):
    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10).text
    return BeautifulSoup(html, 'html.parser').get_text(separator='\n', strip=True)[:6000]

@mcp.tool()
def get_jd_summary(url: str) -> dict:
    """Fetch a job description URL and return a structured summary as JSON.
    Returns: {company, role, must_have_skills, nice_to_have_skills, min_cgpa, locations, package_lpa}"""
    text = fetch_jd(url)
    resp = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f'Extract a JD JSON: {text}',
        config={
            'response_mime_type': 'application/json',
            'response_schema': JD.model_json_schema(),
        },
    )
    return JD.model_validate_json(resp.text).model_dump()

if __name__ == '__main__':
    mcp.run()  # default stdio transport