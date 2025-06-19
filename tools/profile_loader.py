import yaml

profile_path = "data/user_profile.yaml"
session_profile_path = "data/session_profile.yaml"
profile_items = [
    "name",
    "education",
    "work_experience",
    "projects",
    "research",
    "skills",
    "summary",
]


class ProfileLoader:
    def __init__(self):
        self._profile = {}
        self._load_profile(profile_path)

    def _load_profile(self, profile_path: str):
        with open(profile_path, encoding="utf-8") as f:
            user_profile = yaml.safe_load(f)

        print("## Loading User's Profile ##")
        for item in profile_items:
            try:
                self._profile[item] = user_profile[item]
                print(f"Loaded {item}")
            except KeyError:
                self._profile[item] = None
                print(f"No such item {item}")

    def profile(self):
        """ get all profiles """
        return self._profile

    def formed_profile(self) -> str:
        """ get formed profiles text """
        profile_text = f"""
        Name: {self._profile['name']}
        Summary: {self._profile['summary']}
        Skills: {", ".join(self._profile['skills'])}\n
        """

        # Education info.
        profile_text += "Education:\n"
        for i in self._profile['education']:
            profile_text += f"School: {i['school']}\n"
            profile_text += f"Degree: {i['degree']}\n"
            profile_text += f"Major: {i['major']}\n"
            profile_text += f"Duration: {i['duration']}\n"
            profile_text += "\n"

        # Work experience info.
        profile_text += "Work Experience:\n"
        for i in self._profile['work_experience']:
            profile_text += f"Company: {i['company']}\n"
            profile_text += f"Position: {i['position']}\n"
            profile_text += f"{i['duration']} | {i['location']}\n"
            for desc in i['description']:
                profile_text += f"- {desc}\n"
            profile_text += "\n"

        # Projects info.
        profile_text += "Projects:\n"
        for i in self._profile['projects']:
            profile_text += f"Project name: {i['title']} ({i['type']})\n"
            profile_text += f"Duration: {i['duration']}\n"
            for desc in i['description']:
                profile_text += f"- {desc}\n"
            profile_text += "\n"

        profile_text += "Research:\n"
        for i in self._profile['research']:
            profile_text += f"Organization: {i['organization']}\n"
            profile_text += f"{i['duration']} | {i['type']}"
            profile_text += f"Title: {i['title']}\n"
            for desc in i['description']:
                profile_text += f"- {desc}\n"
            profile_text += "\n"

        return profile_text.strip()

if __name__ == "__main__":
    loader = ProfileLoader()