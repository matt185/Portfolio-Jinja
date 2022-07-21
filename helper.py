 def to_lower(text):
    return str(text).lower()

def searchByTech (items, term):
  return items.filter(item => toLower(item.techStack).includes(toLower(term)));
