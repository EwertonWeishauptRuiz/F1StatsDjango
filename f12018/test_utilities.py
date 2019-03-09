from datetime import date

from django.test import TestCase

from f12018.models import Driver, Team, Race, Country


class F1TestUtilities(TestCase):
    def mock_country(self):
        country_name = 'Mock Country'
        Country.objects.create(country_name=country_name)

    def mock_team(self):
        team_name = 'Mock Team'
        team_nationality = Country.objects.first()
        Team.objects.create(
            team_name=team_name, team_nationality=team_nationality)

    def mock_driver(self):
        driver_name = 'Mock Driver'
        driver_team = Team.objects.first()
        driver_nationality = Country.objects.first()
        Driver.objects.create(
            driver_name=driver_name,
            driver_team=driver_team,
            driver_nationality=driver_nationality,
            )

    def mock_race(self):
        grand_prix_name = 'Mock Grand Prix'
        circuit_name = 'Mock Circuit'
        grand_prix_date = date.today()
        circuit_nationality = Country.objects.create(
            country_name='Circuit Country Name')
        Race.objects.create(
            grand_prix_name=grand_prix_name,
            circuit_name=circuit_name,
            circuit_nationality=circuit_nationality,
            grand_prix_date=grand_prix_date,
            )
