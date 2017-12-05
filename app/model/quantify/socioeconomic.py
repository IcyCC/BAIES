from app import db
from app.model.comm import ActionMixin


class SocioeconomicMixin:

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country = db.Column(db.String(64), index=True)
    time = db.Column(db.DateTime)

    def get_socioeconomic_json(self):
        return {
            'id': self.id,
            'country': self.country,
            'time': self.time,
        }


class CountryProfiles(db.Model, SocioeconomicMixin):

    # 金砖国家概况
    __tablename__ = "country_profiles"

    area = db.Column(db.Float)
    population = db.Column(db.BigInteger)
    population_density = db.Column(db.Float)

    def to_json(self):
        d = {
            'area': self.area,
            'population': self.population,
            'population_density': self.population_density
        }
        d.update(self.get_socioeconomic_json())
        return d

class PopulationProfiles(db.Model, SocioeconomicMixin):

    # 人口概况
    __tablename__ = "population_profiles"

    population = db.Column(db.Integer)
    men = db.Column(db.Integer)
    women = db.Column(db.Integer)
    city_population = db.Column(db.Integer)
    village_population = db.Column(db.Integer)

    def to_json(self):
        d = {
            'population': self.population,
            'men': self.men,
            'women': self.women,
            'city_population': self.city_population,
            'village_population': self.village_population
        }
        d.update(self.get_socioeconomic_json())
        return d


class SexDistributionProfiles(db.Model, SocioeconomicMixin):

    # 性别分布概况
    __tablename__ = "sex_distribution_profiles"

    men = db.Column(db.Integer)
    women = db.Column(db.Integer)

    def to_json(self):
        d = {
            'men': self.men,
            'women': self.women,
        }
        d.update(self.get_socioeconomic_json())
        return d


class LaborPopulationProfiles(db.Model, SocioeconomicMixin):
    # 劳动人口概况
    __tablename__ = "labor_population_profiles"

    labor = db.Column(db.Integer)
    employment = db.Column(db.Integer)
    employment_in_population = db.Column(db.Float)
    unemployment_rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'labor': self.time,
            'employment': self.employment,
            'employment_in_population': self.employment_in_population,
            'unemployment_rate': self.unemployment_rate
        }
        d.update(self.get_socioeconomic_json())
        return d

class EconomicProfiles(db.Model, SocioeconomicMixin):

    # 经济概况
    __tablename__ = "economic_profiles"

    gdp = db.Column(db.Integer)
    per_capita_gdp = db.Column(db.Float)
    gdp_increase_rate = db.Column(db.Float)
    first_industry = db.Column(db.Float)
    second_industry = db.Column(db.Float)
    third_industry = db.Column(db.Float)

    def to_json(self):
        d = {
            'gdp': self.gdp,
            'per_capita_gdp': self.per_capita_gdp,
            'gdp_increase_rate': self.gdp_increase_rate,
            'first_industry': self.first_industry,
            'second_industry': self.second_industry,
            'third_industry': self.third_industry
        }
        d.update(self.get_socioeconomic_json())
        return d


class EconomicIndexProfiles(db.Model, SocioeconomicMixin):
    # 经济指数概况
    __tablename__ = "economic_index_profiles"

    consumer_price_index = db.Column(db.Float)
    food_production_index = db.Column(db.Float)
    agriculture_production_index = db.Column(db.Float)
    average_national_total_expenditure = db.Column(db.Float)
    real_effective_exchange_rate_index = db.Column(db.Float)

    def to_json(self):
        d = {
            'consumer_price_index': self.consumer_price_index,
            'food_production_index': self.food_production_index,
            'agriculture_production_index': self.agriculture_production_index,
            'average_national_total_expenditure': self.average_national_total_expenditure,
            'real_effective_exchange_rate_index': self.real_effective_exchange_rate_index
        }
        d.update(self.get_socioeconomic_json())
        return d


class LivingStandardOfResidents(db.Model, SocioeconomicMixin):
    # 居民生活水平
    __tablename__ = "living_standard_of_residents"

    cellular_network_system_telephone_renting = db.Column(db.Integer)
    every_one_hundred_people_have_telephone_lines = db.Column(db.Integer)
    secure_internet_server = db.Column(db.Integer)
    internet_user = db.Column(db.Integer)

    def to_json(self):
        d = {
            'cellular_network_system_telephone_renting': self.cellular_network_system_telephone_renting,
            'every_one_hundred_people_have_telephone_lines': self.every_one_hundred_people_have_telephone_lines,
            'secure_internet_server': self.secure_internet_server,
            'internet_user': self.internet_user
        }
        d.update(self.get_socioeconomic_json())
        return d

class ConsumerSpendingResidents(db.Model, SocioeconomicMixin):
    # 居民消费水平
    __tablename__ = "consumer_spending_residents"

    residents_final_consumer = db.Column(db.Float)
    final_consumer = db.Column(db.Float)
    medical_final_consumer = db.Column(db.Float)
    per_capita_medical_consumer = db.Column(db.Float)
    public_education_consumer = db.Column(db.Float)

    def to_json(self):
        d = {
            'residents_final_consumer': self.residents_final_consumer,
            'final_consumer': self.final_consumer,
            'per_capita_medical_consumer': self.per_capita_medical_consumer,
            'public_education_consumer': self.public_education_consumer
        }
        d.update(self.get_socioeconomic_json())
        return d

class TradeProfiles(db.Model, SocioeconomicMixin):
    # 贸易概况
    __tablename__ = "trade_profiles"

    trade_volume = db.Column(db.Float)
    import_volume = db.Column(db.Float)




