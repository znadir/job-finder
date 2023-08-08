must_keywords = input("Must include in title (stage, informatique): ") or "stage, informatique"
must_keywords = must_keywords.replace(" ", "").split(",")
print(must_keywords)