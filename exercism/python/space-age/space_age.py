class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year = 365.25
        self.seconds_per_day = 86400

    def on_mercury(self):
        mercury_earth_years = 0.2408467
        return self.calculate_years(self.seconds, mercury_earth_years)

    def on_venus(self):
        venus_earth_years = 0.61519726
        return self.calculate_years(self.seconds, venus_earth_years)

    def on_earth(self):
        earth_year = 1
        return self.calculate_years(self.seconds, earth_year)

    def on_mars(self):
        mars_earth_years = 1.8808158
        return self.calculate_years(self.seconds, mars_earth_years)

    def on_jupiter(self):
        jupiter_earth_years = 11.862615
        return self.calculate_years(self.seconds, jupiter_earth_years)

    def on_saturn(self):
        saturn_earth_years = 29.447498
        return self.calculate_years(self.seconds, saturn_earth_years)

    def on_uranus(self):
        uranus_earth_years = 84.016846
        return self.calculate_years(self.seconds, uranus_earth_years)

    def on_neptune(self):
        neptune_earth_years = 164.79132
        return self.calculate_years(self.seconds, neptune_earth_years)

    def calculate_years(self, seconds, planet_to_earth_years):
        return round(((self.seconds/self.seconds_per_day)/self.earth_year)/planet_to_earth_years, 2)


if __name__ == "__main__":
    print(SpaceAge(2329871239).on_mars())
