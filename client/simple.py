import sys, json, random

def move(command):
    record = { 'moves': [command] }
    f.write(json.dumps(record) + '\n')
    f.flush()
    print(json.dumps(record))
    sys.stdout.flush()

f_name = f"bots/bot{random.randint(0, 10)}.txt"
f = open(f_name,"w+")
f.flush()

for line in sys.stdin:
    state = json.loads(line)
    # find planet with most ships
    my_planets = [p for p in state['planets'] if p['owner'] == 1]
    other_planets = [p for p in state['planets'] if p['owner'] != 1]

    if not my_planets or not other_planets:
        move(None)
    else:
        planet = max(my_planets, key=lambda p: p['ship_count'])
        dest = min(other_planets, key=lambda p: p['ship_count'])
        move({
            'origin': planet['name'],
            'destination': dest['name'],
            'ship_count': planet['ship_count'] - 1
        })
