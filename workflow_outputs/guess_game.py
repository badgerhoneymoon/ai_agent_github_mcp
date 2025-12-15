# Minimal deterministic Guess the Number game API

class GameState:
    __slots__ = ('target', 'finished')
    def __init__(self, target):
        self.target = target
        self.finished = False


def start_game(target):
    """Start a new game with a fixed target number.
    Returns a GameState object used by guess()."""
    return GameState(target)


def guess(game_state, value):
    """Make a guess against the provided GameState.
    Returns one of "low", "high", or "correct"."""
    if game_state.finished:
        raise RuntimeError("Game already finished")
    if not isinstance(value, int):
        raise TypeError("Guess value must be an int")
    if value == game_state.target:
        game_state.finished = True
        return "correct"
    if value < game_state.target:
        return "low"
    return "high"
