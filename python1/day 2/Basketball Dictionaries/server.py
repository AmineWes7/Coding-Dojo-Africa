class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

# Challenge 2: Create instances using individual player dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age": 33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age": 16, 
        "position": "P", 
        "team": "en"
    }
]

new_team = []
for player in players:
    new_team.append(Player(player))

# NINJA BONUS: Add a get_team(cls, team_list) @class method
@classmethod
def get_team(cls, team_list):
    return [cls(player) for player in team_list]

# Test the get_team method
new_team = Player.get_team(players)