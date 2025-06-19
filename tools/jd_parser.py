from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path

jd_template_path = "prompts/jd_template.txt"

class JDParser:
    def __init__(self, llm):
        self.llm = llm

    def check_jd(self, jd: str) -> str:
        prompt_template = Path(jd_template_path).read_text(encoding="utf-8")
        prompt = PromptTemplate.from_template(prompt_template)
        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"jd_text": jd})
