import time
from threading import Event

TIME_FOR_ELIXIR = 2.8
TIME_FOR_ELIXIR_DOUBLE = 1.4
TIME_FOR_ELIXIR_TRIPLE = 0.9
TIME_FOR_ELIXIR_COLLECTOR = 8.5
MAX_ELIXIR = 10

DOUBLE_AFTER = 120
TRIPLE_AFTER = 240

OWN_ELIXIR = 5
ENEMY_ELIXIR = 5

OWN_COLLECTORS = 0
ENEMY_COLLECTORS = 0

def reset_state():
    global OWN_ELIXIR, ENEMY_ELIXIR, OWN_COLLECTORS, ENEMY_COLLECTORS
    OWN_ELIXIR = 5
    ENEMY_ELIXIR = 5
    OWN_COLLECTORS = 0
    ENEMY_COLLECTORS = 0

def start_elixir_counting(stop_event: Event):
    global OWN_ELIXIR, ENEMY_ELIXIR
    current_tick = 0
    OWN_ELIXIR = 5
    ENEMY_ELIXIR = 5
    while not stop_event.is_set():
        if current_tick > 700:
            reset_state()
            break
        if current_tick < DOUBLE_AFTER:
            time.sleep(TIME_FOR_ELIXIR)
            current_tick += TIME_FOR_ELIXIR
            OWN_ELIXIR += 1 + calculate_collector_add(TIME_FOR_ELIXIR, True)
            ENEMY_ELIXIR += 1 + calculate_collector_add(TIME_FOR_ELIXIR, False)
        elif current_tick < TRIPLE_AFTER:
            time.sleep(TIME_FOR_ELIXIR_DOUBLE)
            current_tick += TIME_FOR_ELIXIR_DOUBLE
            OWN_ELIXIR += 2 + calculate_collector_add(TIME_FOR_ELIXIR_DOUBLE, True)
            ENEMY_ELIXIR += 2 + calculate_collector_add(TIME_FOR_ELIXIR_DOUBLE, False)
        else:
            time.sleep(TIME_FOR_ELIXIR_TRIPLE)
            current_tick += TIME_FOR_ELIXIR_TRIPLE
            OWN_ELIXIR += 3 + calculate_collector_add(TIME_FOR_ELIXIR_TRIPLE, True)
            ENEMY_ELIXIR += 3 + calculate_collector_add(TIME_FOR_ELIXIR_TRIPLE, False)
        OWN_ELIXIR = min(OWN_ELIXIR, MAX_ELIXIR)
        ENEMY_ELIXIR = min(ENEMY_ELIXIR, MAX_ELIXIR)


def reduce_elixir(elixir_type, amount):
    global OWN_ELIXIR, ENEMY_ELIXIR
    if elixir_type == "own":
        OWN_ELIXIR = max(0, OWN_ELIXIR - amount)
    elif elixir_type == "enemy":
        ENEMY_ELIXIR = max(0, ENEMY_ELIXIR - amount)

def collector_placed(is_own):
    global OWN_COLLECTORS, ENEMY_COLLECTORS
    if is_own:
        OWN_COLLECTORS += 1
    else:
        ENEMY_COLLECTORS += 1

def collector_removed(is_own):
    global OWN_COLLECTORS, ENEMY_COLLECTORS
    if is_own:
        OWN_COLLECTORS -= 1
    else:
        ENEMY_COLLECTORS -= 1

def calculate_collector_add(tick, is_own):
    if is_own:
        return (TIME_FOR_ELIXIR_COLLECTOR / tick) * OWN_COLLECTORS
    else:
        return (TIME_FOR_ELIXIR_COLLECTOR / tick) * ENEMY_COLLECTORS