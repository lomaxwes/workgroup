class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goals=1):
        self.goals = goals
        return self.goals

    def make_assist(self, assists=1):
        self.assists += assists
        return self.assists

    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")

leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()