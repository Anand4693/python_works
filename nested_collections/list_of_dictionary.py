
frame_works = [
    {"name":"django","language":"python","rating":5},
    {"name":"oodo","language":"python","rating":4},
    {"name":"fastapi","language":"python","rating":5},
    {"name":"spring","language":"java","rating":5},
    {"name":"angular","language":"javascript","rating":5},
    {"name":"nest","language":"javascript","rating":5},
    {"name":"express","language":"javascript","rating":5}
]

# all framework name

all_fw_names = [fw.get("name") for fw in frame_works]
print(all_fw_names)

# all languages

all_languages = [fw.get("language")for fw in frame_works]
print(all_languages)

# popular frameworks
popular_frameworks = [fw.get("rating")for fw in frame_works]
print(popular_frameworks)