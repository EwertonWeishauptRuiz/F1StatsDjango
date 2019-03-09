from f12018.models import (
    Driver,
    Team,
    Race,
    Country,
    Position,
    get_race_winner
)
from f12018.test_utilities import F1TestUtilities


class Testf1Stats(F1TestUtilities):
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

        actual = get_race_winner(race=race)
        expected = Driver.objects.get(driver_name='Mock Driver 1')
        self.assertEqual(expected, actual)
