from datetime import date, timedelta

from f12018.models import (
    Driver,
    Team,
    Race,
    Country,
    Position,
)
from f12018.test_utilities import F1TestUtilities


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

        actual = Position.get_race_winner()
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

        actual = Driver.get_win_number(driver)
        expected = amount_of_wins
        self.assertEqual(expected, actual)
