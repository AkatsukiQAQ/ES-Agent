from pathlib import Path
import yaml
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools.jd_parser import JDParser
from tools.profile_loader import ProfileLoader
import openai

from dotenv import load_dotenv
load_dotenv()

es_generation_template_path = "prompts/es_generation_template.txt"
job_description_path = "data/job_description.txt"


class ES_Agent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)
        self.jd_parser = JDParser(self.llm)
        self.profile_loader = ProfileLoader()

    def comfirm_jd(self):
        """ Ask user to comfirm JD """
        while True:
            jd = Path(job_description_path).read_text(encoding="utf-8")
            try:
                comfirm = input(f"Is this JD the position you are applying? (yes or no)\n"
                                f"{self.jd_parser.check_jd(jd)}\n>")
            except openai.RateLimitError:
                comfirm = input(f"Is this JD the position you are applying? (yes or no)\n"
                                f"{jd}\n>")

            while True:
                if "yes" in comfirm.lower() or comfirm.lower() in ["y", "yes"]:
                    break
                elif "no" in comfirm.lower() or comfirm.lower() in ["n", "no"]:
                    print("Please try again.")
                else:
                    print("Please answer yes or no.")

            if "yes" in comfirm.lower() or comfirm.lower() in ["y", "yes"]:
                return jd

    def generate_answer(self, job_description: str,
                        es_question,
                        profile_text: str,
                        lang_choice: str,
                        output_limitation: str,
                        ):
        prompt_template = Path(es_generation_template_path).read_text(encoding="utf-8")
        prompt = PromptTemplate.from_template(prompt_template)
        chain = prompt | self.llm | StrOutputParser()
        p = prompt.format(
            user_profile=profile_text.strip(),
            job_description=job_description.strip(),
            es_question=es_question.strip(),
            language=lang_choice.strip(),
            output_limitation=output_limitation.strip(),
        )
        print(p)
        return chain.invoke({
            "user_profile": profile_text.strip(),
            "job_description": job_description.strip(),
            "es_question": es_question.strip(),
            "language": lang_choice.strip(),
            "output_limitation": output_limitation.strip(),
        })

    def start(self):
        # check JD
        jd = self.comfirm_jd()

        # get ES question
        es_question = input("📌 Please input ES Question：\n> ")

        # ask generation details
        lang_choice = input("🌐 Please select the output language（ja / en）：\n> ") or "en"
        output_limitation = input("  Is there any limitation of the output? (Default is no)") or "No limitation"

        # load user's profile
        profile_text = self.profile_loader.formed_profile()

        try:
            response = self.generate_answer(
                job_description=jd,
                es_question=es_question,
                profile_text=profile_text,
                lang_choice=lang_choice,
                output_limitation=output_limitation,
            )
            print("\n=== ✨ Generated ES Answer：===\n")
            print(response)
        except openai.RateLimitError:
            print("Somthing went wrong with your openai account.")