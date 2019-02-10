from f12018.models import Driver, Point

sv = Driver.objects.get(driver_name='Sebastian Vettel')
Point.get_total_points_season(sv)