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
    team_nationality = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True)


class Driver(models.Model):
    def __str__(self):
        return self.driver_name
    driver_name = models.CharField(max_length=200)
    driver_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    driver_nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    driver_race_position = models.ManyToManyField('Position', blank=True)
    driver_season_points = models.IntegerField(default=0)

    @classmethod
    def get_win_number(self, driver):
        return Position.objects.filter(
            driver_position=driver, position=1).count()

    @classmethod
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
    circuit_nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    grand_prix_date = models.DateTimeField('Race Date')
    position_driver_race = models.ManyToManyField('Position', blank=True)


class Position(models.Model):
    def __str__(self):
        return str(self.position)
    position = models.CharField(max_length=50, blank=True)
    driver_position = models.ForeignKey(
        Driver, blank=False, on_delete=models.CASCADE)
    race_position = models.ForeignKey(
        Race, blank=False, on_delete=models.CASCADE)

    @classmethod
    def get_race_winner(self, race):
        return Position.objects.get(
            race_position=race, position=1).driver_position
