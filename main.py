from pathlib import Path
import yaml
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StrOutputParser

# ====== 确认JD内容 ======
# TODO

# ====== 用户输入 ======
print("=== Entry Sheet生成 Agent ===")
es_question = input("📌 请输入ES问题：\n> ")

# ====== 加载用户 profile ======
with open("data/user_profile.yaml", encoding="utf-8") as f:
    user_profile = yaml.safe_load(f)

# ====== 加载模板 prompt ======
prompt_template = Path("prompts/es_template.txt").read_text(encoding="utf-8")
prompt = ChatPromptTemplate.from_template(prompt_template)

# ====== LLM Model（你可以换成 GPT-4 等） ======
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# ====== 构建链条 ======
chain = prompt | llm | StrOutputParser()

# ====== 构建填入内容 ======
lang_choice = input("🌐 请选择输出语言（ja / en）：\n> ") or "ja"
output_limitation = input("  是否有字数限制？ (默认为没有)") or "No limitation"

# NOTE: 这里我们模拟 user_profile 的字符串形式，未来可以换成更精细的字段选择
profile_text = f"""
氏名: {user_profile['name']}
学校: {user_profile['school']}
学位: {user_profile['degree']}（{user_profile['graduation_year']}年卒業予定）
スキル: {', '.join(user_profile['skills'])}
概要: {user_profile['summary']}

主なプロジェクト:
"""
for proj in user_profile['projects']:
    profile_text += f"- {proj['title']}（{proj['duration']}）: {proj['description']}\n"



# ====== 运行 Agent ======
result = chain.invoke({
    "user_profile": profile_text.strip(),
    "es_question": es_question.strip(),
    "language": lang_choice.strip(),
    "output_limitation": output_limitation.strip(),
})

print("\n=== ✨ 生成的ES草案：===\n")
print(result.strip())
