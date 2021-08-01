import json

def add(name, score, filename = 'highscore.json'):
    with open(filename,'w+') as file:
        try:
            highscores = json.load(file)
        except:
            highscores = {}
        highscores[name] = score
        highscores = dict(sorted(highscores.items(), key = lambda x: x[1], reverse = True))
        json.dump(highscores, file)

def get(filename = 'highscore.json'):
        try:
            with open(filename,'r') as file:
                highscores = json.load(file)
                return dict(sorted(highscores.items(), key = lambda x: x[1], reverse = True))
        except:
            with open(filename,'w') as file:
                json.dump({}, file)
            return {}

if __name__ == '__main__':
    pass