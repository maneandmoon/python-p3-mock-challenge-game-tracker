class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title   
    @title.setter
    def title(self, new_title):
        if(not hasattr(self, 'title') and isinstance(new_title, str) and len(new_title) > 0):
            self._title = new_title
       
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        player_scores = [result.score for result in self.results() if result.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0
        

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        # else:
        #     raise ValueError("Username must be a string between 2 and 16 characters.")    


    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in self.results()]))

# FAILED Player in many_to_many.py player knows if a game has been played - assert None == True
# FAILED Player in many_to_many.py player knows how many times a game has been played - assert None == 2


    def played_game(self, game):
        return any([result.game == game for result in self.results()])

    def num_times_played(self, game):
        return sum([1 for result in self.results() if result.game == game])

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score   
    @score.setter
    def score(self, new_score):
        if(not hasattr(self, 'score') and isinstance(new_score, int) and 1 <= (new_score) <= 5000):
            self._score = new_score

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, new_player):
        if(isinstance(new_player, Player)):
            self._player = new_player        

    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, new_game):
        if(isinstance(new_game, Game)):
            self._game = new_game