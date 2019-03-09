from datetime import date, timedelta

from f12018.models import (
    Driver,
    Team,
    Race,
    Country,
    Position,
)
from f12018.test_utilities import F1TestUtilities
from f12018.position_to_points import POSITIONS_TO_POINTS


class TestF1Stats(F1TestUtilities):
    def test_number_of_victories(self):
        self.mock_country()
        self.mock_team()
        self.mock_race()
        race = Race.objects.first()

        for i in range(10):
            driver_name = 'Mock Driver {}'.format(i+1)
            Driver.objects.create(
                driver_name=driver_name,
                driver_team=Team.objects.first(),
                driver_nationality=Country.objects.first(),
            )
            Position.objects.create(
                position=i+1,
                driver_position=Driver.objects.get(pk=i+1),
                race_position=race,
            )

        actual = Position.get_race_winner(race)
        expected = Driver.objects.get(driver_name='Mock Driver 1')
        self.assertEqual(expected, actual)

    def test_number_of_wins_driver(self):
        self.mock_country()
        self.mock_team()
        self.mock_driver()
        driver = Driver.objects.first()

        amount_of_wins = 5

        for i in range(amount_of_wins):
            Race.objects.create(
                grand_prix_name='Race {}'.format(i+1),
                circuit_name='Circuit {}'.format(i+1),
                circuit_nationality=Country.objects.first(),
                grand_prix_date=date.today() + timedelta(days=i),
                )
            Position.objects.create(
                position=1,
                race_position=Race.objects.get(pk=i+1),
                driver_position=Driver.objects.first(),
                )

        Driver.get_win_number(driver)
        actual = driver.wins
        expected = amount_of_wins
        self.assertEqual(expected, actual)

    def test_total_points_season(self):
        self.mock_country()
        self.mock_team()
        self.mock_driver()
        driver = Driver.objects.first()

        race_position = '1'
        amount_of_wins = 5

        for i in range(amount_of_wins):
            Race.objects.create(
                grand_prix_name='Race {}'.format(i+1),
                circuit_name='Circuit {}'.format(i+1),
                circuit_nationality=Country.objects.first(),
                grand_prix_date=date.today() + timedelta(days=i),
                )
            Position.objects.create(
                position=race_position,
                race_position=Race.objects.get(pk=i+1),
                driver_position=Driver.objects.first(),
                )

        Driver.get_total_points_season(driver)
        actual = driver.driver_season_points
        expected = amount_of_wins * int(POSITIONS_TO_POINTS[race_position])
        self.assertEqual(expected, actual)
