import json, os, datetime

FILE="ownership.json"

def load():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE,"r",encoding="utf-8"))

def register(token, owner):
    data=load()
    data.append({
        "token":token,
        "owner":owner,
        "time":datetime.datetime.utcnow().isoformat()+"Z"
    })
    json.dump(data,open(FILE,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print("🧾 Ownership recorded:",token,"→",owner)

if __name__=="__main__":
    import sys
    register(sys.argv[1] if len(sys.argv)>1 else "🧱⭐🧱",
             sys.argv[2] if len(sys.argv)>2 else "researcher")
