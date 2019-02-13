from django.db import models
from f12018.position_to_points import POSITIONS_TO_POINTS


class Country(models.Model):
    def __str__(self):
        return self.country_name

    country_name = models.CharField(max_length=100)


class Team(models.Model):
    def __str__(self):
        return self.team_name
    team_name = models.CharField(max_length=200)
    team_nationality = models.ForeignKey(Country, on_delete=models.CASCADE)


class Driver(models.Model):
    def __str__(self):
        return self.driver_name
    driver_name = models.CharField(max_length=200)
    driver_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    driver_nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    driver_race_position = models.ManyToManyField('Position', blank=True)
    driver_season_points = models.IntegerField(default=0)

    def get_win_number(self):
        wins = Driver.objects.filter(driver_name=self.driver_name,
                                     position=1).count()
        return wins

    def get_total_points_season(self):
        positions = self.driver_race_position.all()
        points = 0
        for place in positions:
            points += int(POSITIONS_TO_POINTS[place.position])

        self.driver_season_points = points
        self.save()


class Race(models.Model):
    def __str__(self):
        return self.grand_prix_name
    grand_prix_name = models.CharField(max_length=200)
    circuit_name = models.CharField(max_length=200)
    cirtcuit_nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    grand_prix_date = models.DateTimeField('Race Date')
    position_driver_race = models.ManyToManyField('Position', blank=True)

    def get_race_winner(self):
        return self.position_driver_race.filter(race_position=self, position=1).first().driver_position


class Position(models.Model):
    def __str__(self):
        return str(self.position)
    position = models.CharField(max_length=50, blank=True)
    driver_position = models.ForeignKey(
        Driver, blank=False, on_delete=models.CASCADE)
    race_position = models.ForeignKey(
        Race, blank=False, on_delete=models.CASCADE)
