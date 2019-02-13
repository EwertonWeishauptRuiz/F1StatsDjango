from f12018.models import Driver

sv = Driver.objects.get(driver_name='Sebastian Vettel')
sv.get_total_points_season()
