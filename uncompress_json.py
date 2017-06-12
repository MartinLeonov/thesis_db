from common import save_json, Thesis, get_file_text
import sys
import json

INPUT_FILE = "theses.json"
OUTPUT_UNCOMPRESSED_FILE = "theses.json"

reload(sys)
sys.setdefaultencoding("utf8")
db_text = get_file_text(INPUT_FILE)
theses = json.loads(db_text,encoding="utf8")

def uncompress():  # makes the json big and readable again
  print("uncompressing")

  def uncompressed_person(person):
    if person == None:
      return

    for word in ["name_first","name_last","sex"]:
      if not word in person:
        person[word] = None

    if not "degrees" in person:
      person["degrees"] = []

  reference_thesis = Thesis()

  uncompressed = []

  for thesis in theses:
    new_thesis = {}

    for attr in reference_thesis.__dict__:
      new_thesis[attr] = thesis[attr] if attr in thesis else None

    new_thesis["keywords"] = thesis["keywords"] if "keywords" in thesis else []
    new_thesis["opponents"] = thesis["opponents"] if "opponents" in thesis else []

    uncompressed_person(new_thesis["author"])
    uncompressed_person(new_thesis["supervisor"])

    for opponent in new_thesis["opponents"]:
      uncompressed_person(opponent)

    uncompressed.append(new_thesis)

  save_json(uncompressed,OUTPUT_UNCOMPRESSED_FILE)

uncompress()
