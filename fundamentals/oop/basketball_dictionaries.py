class Player:
    new_team = []

    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
        self.new_team.append(self)

    @classmethod
    def get_team(cls, team_list):
        for  player in team_list:
                Player(player)

    @classmethod
    def print_team(cls):
        for team_list in (cls.new_team):
                print(f"\nPlayer Name: {team_list.name} \nAge: {team_list.age} \nPosition: {team_list.position} \nTeam: {team_list.team}")


# ------ Start Individual Player Instantiation ------
# kevin = {
#         "name": "Kevin Durant", 
#         "age":34, 
#         "position": "small forward", 
#         "team": "Brooklyn Nets"
# }
# jason = {
#         "name": "Jason Tatum", 
#         "age":24, 
#         "position": "small forward", 
#         "team": "Boston Celtics"
# }
# kyrie = {
#         "name": "Kyrie Irving", 
#         "age":32, 
#         "position": "Point Guard", 
#         "team": "Brooklyn Nets"
# }

# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)

# print(player_kevin.position) # prints small forward
# print(player_jason.position) # prints small forward
# print(player_kyrie.position) # prints point guard
# ------ End Individual Player Instantiation ------

players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

# ------ Start Dictionary Player Instantiation ------
# for player in players:
#         Player(player)

# ------ Start Dictionary Player Instantiation via class method ------
Player.get_team(players)

Player.print_team()