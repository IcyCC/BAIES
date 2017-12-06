from app import db
from app.model.comm import ActionMixin

# 社会经济信息

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
    output_volume = db.Column(db.Float)
    trade_surplus = db.Column(db.Float)

    def to_json(self):
        d = {
            'trade_volume': self.trade_volume,
            'import_volume': self.import_volume,
            'output_volume': self.output_volume,
            'trade_surplus': self.trade_surplus
        }
        d.update(self.get_socioeconomic_json())
        return d

class ReserveProfiles(db.Model, SocioeconomicMixin):
    # 储备概况
    __tablename__ = "reserve_profiles"
    total = db.Column(db.Float)
    bank_asset_capital_rate = db.Column(db.Float)
    often_account_balance = db.Column(db.Float)
    private_transfer_employee_salary = db.Column(db.Float)
    currency_pre_currency = db.Column(db.Float)

    def to_json(self):
        d = {
            'total': self.total,
            'bank_asset_capital_rate': self.bank_asset_capital_rate,
            'often_account_balance': self.often_account_balance,
            'private_transfer_employee_salary': self.private_transfer_employee_salary,
            'currency_pre_currency':self.currency_pre_currency
        }
        d.update(self.get_socioeconomic_json())
        return d

class LoanProfiles(db.Model, SocioeconomicMixin):
    # 贷款概况
    __tablename__ = "loan_profiles"

    ibrd_loan = db.Column(db.Float)
    imf_loan = db.Column(db.Float)
    bank_bad_loan_rate = db.Column(db.Float)
    loan_rate = db.Column(db.Float)
    loan_risk_premium = db.Column(db.Float)
    bank_domestic_loan = db.Column(db.Float)

    def to_json(self):
        d = {
            'ibrd_loan': self.ibrd_loan,
            'imf_loan': self.imf_loan,
            'bank_bad_loan_rate': self.bank_bad_loan_rate,
            'loan_rate': self.loan_rate,
            'loan_risk_premium':self.loan_risk_premium.table,
            'bank_domestic_loan':self.bank_domestic_loan
        }
        d.update(self.get_socioeconomic_json())
        return d


class HealthyProfiles(db.Model, SocioeconomicMixin):
    # 健康概况
    __tablename__ = "healthy_profiles"

    population_in_0_14 = db.Column(db.Integer)
    population_in_15_64 = db.Column(db.Integer)
    population_over_65 = db.Column(db.Integer)
    urban_health_improvement_facilities = db.Column(db.Integer)

    def to_json(self):
        d = {
            'population_in_0_14': self.population_in_0_14,
            'population_in_15_64': self.population_in_15_64,
            'population_over_65': self.population_over_65,
            'city_health_improvement_facilities': self.city_health_improvement_facilities
        }
        d.update(self.get_socioeconomic_json())
        return d


class BirthDeathRate(db.Model, SocioeconomicMixin):
    # 出生(死亡率)
    __tablename__ = "birth_death_rate"

    death_rate = db.Column(db.Float)
    baby_death_rate = db.Column(db.Float)
    children_death_rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'death_rate': self.death_rate,
            'baby_death_rate': self.baby_death_rate,
            'children_death_rate': self.children_death_rate
        }
        d.update(self.get_socioeconomic_json())
        return d

class BirthProfiles(db.Model, SocioeconomicMixin):
    # 生育概况
    __tablename__ = "birth_profiles"

    birth_rate = db.Column(db.Float)
    pregnant_death_rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'birth_rate': self.birth_rate,
            'pregnant_death_rate': self.pregnant_death_rate
        }
        d.update(self.get_socioeconomic_json())
        return d


class AgeProfiles(db.Model, SocioeconomicMixin):
    # 年龄概况
    __tablename__ = "age_profiles"

    excepted_life_woman = db.Column(db.Float)
    excepted_life_man = db.Column(db.Float)

    def to_json(self):
        d = {
            'excepted_life_woman': self.excepted_life_woman,
            'excepted_life_man': self.excepted_life_man
        }
        d.update(self.get_socioeconomic_json())
        return d

class EntryExitProfiles(db.Model, SocioeconomicMixin):
    # 出入境概况
    __tablename__ = "entry_exit_profiles"

    international_tourism_entry = db.Column(db.Integer)
    international_tourism_exit = db.Column(db.Integer)

    def to_json(self):
        d = {
            'international_tourism_entry': self.international_tourism_entry,
            'international_tourism_exit': self.international_tourism_exit
        }
        d.update(self.get_socioeconomic_json())
        return d


class TourismIncomeSpendProfiles(db.Model, SocioeconomicMixin):
    # 路由支出收入概况
    __tablename__ = "tourism_income_spend_profiles"

    international_tourism_income_num = db.Column(db.Float)
    international_tourism_spend_num = db.Column(db.Float)

    international_tourism_income_rate = db.Column(db.Float)
    international_tourism_spend_rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'international_tourism_income_num': self.international_tourism_income_num,
            'international_tourism_spend_num': self.international_tourism_spend_num,
            'international_tourism_income_rate': self.international_tourism_income_rate,
            'international_tourism_spend_rate': self.international_tourism_spend_rate
        }
        d.update(self.get_socioeconomic_json())
        return d


class TourismProjectIncomeSpendProfiles(db.Model, SocioeconomicMixin):
    # 旅游项目支出收入概况
    __tablename__ = "tourism_project_income_spend_profiles"

    international_tourism_project_income = db.Column(db.Float)
    international_tourism_project_spend = db.Column(db.Float)


    def to_json(self):
        d = {
            'international_tourism_project_income': self.international_tourism_project_income,
            'international_tourism_project_spend': self.international_tourism_project_spend,
        }
        d.update(self.get_socioeconomic_json())
        return d


class PassengerTransportProjectIncomeSpendProfiles(db.Model, SocioeconomicMixin):
    # 客运项目支出收入概况
    __tablename__ = "passenger_transport_project_income_spend_profiles"

    passenger_transport_project_income = db.Column(db.Float)
    passenger_transport_project_spend = db.Column(db.Float)


    def to_json(self):
        d = {
            'passenger_transport_project_income': self.passenger_transport_project_income,
            'passenger_transport_project_spend': self.passenger_transport_project_spend,
        }
        d.update(self.get_socioeconomic_json())
        return d

class ForeignDebtProfiles(db.Model, SocioeconomicMixin):
    # 外债概况
    __tablename__ = "foreign_debt_profiles"

    total_pure_foreign_debt_fluent = db.Column(db.Float)
    total_pure_short_foreign_debt_fluent = db.Column(db.Float)
    public_long_guarantee_foreign_debt = db.Column(db.Float)
    private_long_unguarantee_foreign_debt = db.Column(db.Float)



    def to_json(self):
        d = {
            'total_pure_foreign_debt_fluent': self.total_pure_foreign_debt_fluent,
            'total_pure_short_foreign_debt_fluent': self.total_pure_short_foreign_debt_fluent,
            'public_long_guarantee_foreign_debt':self.public_long_guarantee_foreign_debt,
            'private_long_unguarantee_foreign_debt':self.private_long_unguarantee_foreign_debt
        }
        d.update(self.get_socioeconomic_json())
        return d


class EnvironmentalResourcesProfiles(db.Model, SocioeconomicMixin):
    # 环境概况
    __tablename__ = "environmental_resources_profiles"

    woodland_area = db.Column(db.Float)
    co2_discharge = db.Column(db.Float)
    forest_area = db.Column(db.Float)
    per_capita_renewable_water = db.Column(db.Float)
    total_renewable_water = db.Column(db.Float)
    fossil_fuel_cost = db.Column(db.Float)

    def to_json(self):
        d = {
            'woodland_area': self.woodland_area,
            'co2_discharge': self.co2_discharge,
            'forest_area':self.forest_area,
            'per_capita_renewable_water':self.per_capita_renewable_water,
            'total_renewable_water': self.total_renewable_water,
            'fossil_fuel_cost':self.fossil_fuel_cost
        }
        d.update(self.get_socioeconomic_json())
        return d

class PowerGenerationProfiles(db.Model, SocioeconomicMixin):
    # 发电概况
    __tablename__ = "power_generation_profiles"

    oil_gas_carbon_power_generation = db.Column(db.Float)
    renewable_power_generation = db.Column(db.Float)
    renewable_without_water_power_generation_num = db.Column(db.Float)
    renewable_without_water_power_generation_rate = db.Column(db.Float)
    water_power_generation = db.Column(db.Float)
    oil_power_generation = db.Column(db.Float)
    carbon_power_generation = db.Column(db.Float)
    atom_power_generation = db.Column(db.Float)
    gas_power_generation = db.Column(db.Float)

    def to_json(self):
        d = {
            'oil_gas_carbon_power_generation': self.oil_gas_carbon_power_generation,
            'renewable_power_generation': self.renewable_power_generation,
            'renewable_without_water_power_generation_num':self.renewable_without_water_power_generation_num,
            'renewable_without_water_power_generation_rate':self.renewable_without_water_power_generation_rate,
            'water_power_generation':self.water_power_generation,
            'oil_power_generation':self.oil_power_generation,
            'carbon_power_generation': self.carbon_power_generation,
            'atom_power_generation':self.atom_power_generation,
            'gas_power_generation': self.gas_power_generation
        }
        d.update(self.get_socioeconomic_json())
        return d


class EducationProfiles(db.Model, SocioeconomicMixin):
    # 教育概况
    __tablename__ = "education_profiles"

    primary_school_teacher_student_rate = db.Column(db.Float)
    literacy_rate = db.Column(db.Float)
    per_capita_university_spend = db.Column(db.Float)
    university_entry_rate = db.Column(db.Float)
    middle_school_entry_rate = db.Column(db.Float)
    primary_school_entry_rate = db.Column(db.Float)


    def to_json(self):
        d = {
            'primary_school_teacher_student_rate': self.primary_school_teacher_student_rate,
            'literacy_rate': self.literacy_rate,
            'per_capita_university_spend':self.per_capita_university_spend,
            'university_entry_rate':self.university_entry_rate,
            'middle_school_entry_rate':self.middle_school_entry_rate,
            'primary_school_entry_rate':self.primary_school_entry_rate,
        }
        d.update(self.get_socioeconomic_json())
        return d


class FuelCostProfiles(db.Model, SocioeconomicMixin):
    # 燃料消耗概况
    __tablename__ = "fuel_cost_profiles"

    fossil_fuel_cost = db.Column(db.Float)
    fuel_pure_import = db.Column(db.Float)
    fuel_pure_cost = db.Column(db.Float)

    def to_json(self):
        d = {
            'fossil_fuel_cost': self.fossil_fuel_cost,
            'fuel_pure_import': self.fuel_pure_import,
            'fuel_pure_cost':self.fuel_pure_cost
        }
        d.update(self.get_socioeconomic_json())
        return d


class TransportProfiles(db.Model, SocioeconomicMixin):
    # 交通概况
    __tablename__ = "transport_profiles"

    railway_import_output = db.Column(db.Float)
    wharf_import_output = db.Column(db.Float)

    def to_json(self):
        d = {
            'railway_import_output': self.railway_import_output,
            'wharf_import_output': self.wharf_import_output
        }
        d.update(self.get_socioeconomic_json())
        return d


class InvestmentProfiles(db.Model, SocioeconomicMixin):
    # 投资概况
    __tablename__ = "investment_profiles"

    stock_portfolio_import = db.Column(db.Float)
    foreign_investment_import = db.Column(db.Float)

    def to_json(self):
        d = {
            'stock_portfolio_import': self.stock_portfolio_import,
            'foreign_investment_import': self.foreign_investment_import
        }
        d.update(self.get_socioeconomic_json())
        return d


class AssistanceProfiles(db.Model, SocioeconomicMixin):
    # 援助概况
    __tablename__ = "assistance_profiles"

    received_per_capita_development_official_assistance = db.Column(db.Float)
    received_pure_development_official_assistance = db.Column(db.Float)

    def to_json(self):
        d = {
            'received_per_capita_development_official_assistance': self.received_per_capita_development_official_assistance,
            'received_pure_development_official_assistance': self.received_pure_development_official_assistance
        }
        d.update(self.get_socioeconomic_json())
        return d


class MineralProfiles(db.Model, SocioeconomicMixin):
    # 矿物概况
    __tablename__ = "mineral_profiles"

    asbestos = db.Column(db.Float)
    bauxite = db.Column(db.Float)
    ferrochrome = db.Column(db.Float)
    carbon = db.Column(db.Float)
    cobalt = db.Column(db.Float)
    copper = db.Column(db.Float)
    fluorspar = db.Column(db.Float)
    gold = db.Column(db.Float)
    graphite = db.Column(db.Float)
    gypsum = db.Column(db.Float)
    iron_ore = db.Column(db.Float)
    kaolin = db.Column(db.Float)
    lead = db.Column(db.Float)
    magnesite = db.Column(db.Float)
    manganese = db.Column(db.Float)
    gas = db.Column(db.Float)
    nickel = db.Column(db.Float)
    columbium = db.Column(db.Float)
    oil = db.Column(db.Float)
    phosphorus = db.Column(db.Float)
    rare_earth = db.Column(db.Float)
    talc = db.Column(db.Float)
    tantalum = db.Column(db.Float)
    tin = db.Column(db.Float)
    titanium = db.Column(db.Float)
    uranium = db.Column(db.Float)
    vermiculite = db.Column(db.Float)
    zinc = db.Column(db.Float)
    zirconium = db.Column(db.Float)

    def to_json(self):
        d = {
            'asbestos': self.asbestos,
            'bauxite': self.bauxite,
            'ferrochrome':self.ferrochrome,
            'carbon': self.carbon,
            'cobalt': self.cobalt,
            'fluorspar': self.fluorspar,
            'gold': self.gold,
            'graphite':self.graphite,
            'gypsum':self.gypsum,
            'iron_ore':self.iron_ore,
            'kaolin': self.kaolin,
            'lead': self.lead,
            'magnesite':self.magnesite,
            'manganese':self.manganese,
            'gas': self.gas,
            'nickel':self.nickel,
            'columbium':self.columbium,
            'oil':self.oil,
            'phosphorus':self.phosphorus,
            'rare_earth':self.rare_earth,
            'talc':self.talc,
            'tantalum':self.tantalum,
            'tin':self.tin,
            'titanium':self.titanium,
            'uranium':self.uranium,
            'vermiculite':self.vermiculite,
            'zinc':self.zinc,
            'zirconium':self.zirconium
        }
        d.update(self.get_socioeconomic_json())
        return d


class AgricultureInvestmentCountry(db.Model, SocioeconomicMixin):
    # 农业对外投资主要投资国
    __tablename__ = "agriculture_investment_country"

    nl_num = db.Column(db.Float)
    nl_rate = db.Column(db.Float)

    dk_num = db.Column(db.Float)
    dk_rate = db.Column(db.Float)

    lu_num = db.Column(db.Float)
    lu_rate = db.Column(db.Float)

    usa_num = db.Column(db.Float)
    usa_rate = db.Column(db.Float)

    pa_num = db.Column(db.Float)
    pa_rate = db.Column(db.Float)

    es_num = db.Column(db.Float)
    es_rate = db.Column(db.Float)

    bhmland_num = db.Column(db.Float)
    bhmland_rate = db.Column(db.Float)

    ar_num = db.Column(db.Float)
    ar_rate = db.Column(db.Float)

    pe_num = db.Column(db.Float)
    pe_rate = db.Column(db.Float)

    pt_num = db.Column(db.Float)
    pt_rate = db.Column(db.Float)

    uy_num = db.Column(db.Float)
    uy_rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'nl_num': self.nl_num,
            'nl_rate': self.nl_rate,
            'dk_num': self.dk_num,
            'dk_rate': self.dk_rate,
            'lu_num': self.lu_num,
            'lu_rate': self.lu_rate,
            'usa_num': self.usa_num,
            'usa_rate': self.usa_rate,
            'pa_num': self.pa_num,
            'pa_rate': self.pa_rate,
            'es_num': self.es_num,
            'es_rate': self.es_rate,
            'bhmland_num': self.bhmland_num,
            'bhmland_rate':self.bhmland_rate,
            'ar_num': self.ar_num,
            'ar_rate':self.ar_rate,
            'pe_num': self.pe_num,
            'pe_rate': self.pe_rate,
            'pt_num': self.pt_num,
            'pt_rate':self.pt_rate,
            'uy_num':self.uy_num,
            'uy_rate':self.uy_rate
        }
        d.update(self.get_socioeconomic_json())
        return d


class ForeignInvestmentAgricultureForestryFisheriesPlace(db.Model, SocioeconomicMixin):
    # 农林木鱼对外直接投资额
    __tablename__ = "foreign_investment_agriculture_forestry_fisheries_place"

    global_ = db.Column(db.Float)
    africa = db.Column(db.Float)
    oceania = db.Column(db.Float)
    eu = db.Column(db.Float)
    asean = db.Column(db.Float)
    usa = db.Column(db.Float)
    au = db.Column(db.Float)
    ru = db.Column(db.Float)
    hk = db.Column(db.Float)


    def to_json(self):
        d = {
            'global_': self.global_,
            'africa': self.africa,
            'oceania': self.oceania,
            'eu':self.eu,
            'asean':self.asean,
            'usa':self.usa,
            'au':self.au,
            'ru':self.ru,
            'hk':self.hk
        }
        d.update(self.get_socioeconomic_json())
        return d


class ForeignInvestmentAgricultureForestryFisheries(db.Model, SocioeconomicMixin):
    # 援对外直接净投资
    __tablename__ = "foreign_investment_agriculture_forestry_fisheries"

    money = db.Column(db.Float)
    rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'money': self.money,
            'rate': self.rate
        }
        d.update(self.get_socioeconomic_json())
        return d


class FDIInvestmentCountry(db.Model, SocioeconomicMixin):
    # fdi 主要来源国投资存量
    __tablename__ = "fdi_investment_country"

    nl_num = db.Column(db.Float)
    nl_rate = db.Column(db.Float)

    usa_num = db.Column(db.Float)
    usa_rate = db.Column(db.Float)

    ukwjland_num = db.Column(db.Float)
    ukwjland_rate = db.Column(db.Float)

    es_num = db.Column(db.Float)
    es_rate = db.Column(db.Float)

    pa_num = db.Column(db.Float)
    pa_rate = db.Column(db.Float)

    lu_num = db.Column(db.Float)
    lu_rate = db.Column(db.Float)

    jp_num = db.Column(db.Float)
    jp_rate = db.Column(db.Float)

    fr_num = db.Column(db.Float)
    fr_rate = db.Column(db.Float)

    ch_num = db.Column(db.Float)
    ch_rate = db.Column(db.Float)

    de_num = db.Column(db.Float)
    de_rate = db.Column(db.Float)

    uk_num = db.Column(db.Float)
    uk_rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'nl_num': self.nl_num,
            'nl_rate': self.nl_rate,
            'usa_num':self.usa_num,
            'usa_rate':self.usa_rate,
            'ukwjland_num':self.ukwjland_num,
            'ukwjland_rate':self.ukwjland_rate,
            'es_num':self.es_num,
            'es_rate':self.es_rate,
            'pa_num':self.pa_num,
            'pa_rate':self.pa_rate,
            'lu_num': self.lu_num,
            'lu_rate':self.lu_rate,
            'jp_num': self.jp_num,
            'jp_rate':self.jp_rate,
            'fr_num':self.fr_num,
            'fr_rate':self.fr_rate,
            'ch_num':self.ch_num,
            'ch_rate':self.ch_rate,
            'de_num':self.de_num,
            'de_rate':self.de_rate,
            'uk_num':self.uk_num,
            'uk_rate':self.uk_rate
        }
        d.update(self.get_socioeconomic_json())
        return d


class AgriculturalForeignInvestmentCountry(db.Model, SocioeconomicMixin):
    # 农业利用外资主要国家
    __tablename__ = "agricultural_foreign_investment_country"

    hk = db.Column(db.Float)
    ukwjland = db.Column(db.Float)
    tw = db.Column(db.Float)
    sg = db.Column(db.Float)
    kmland = db.Column(db.Float)
    usa = db.Column(db.Float)
    kr = db.Column(db.Float)
    ca = db.Column(db.Float)
    jp = db.Column(db.Float)
    se = db.Column(db.Float)
    smy = db.Column(db.Float)
    nz = db.Column(db.Float)
    msrland = db.Column(db.Float)
    mu = db.Column(db.Float)
    au = db.Column(db.Float)

    def to_json(self):
        d = {
            'hk': self.hk,
            'ukwjland': self.ukwjland,
            'tw':self.tw,
            'sg':self.sg,
            'kmland':self.kmland,
            'usa':self.usa,
            'kr':self.kr,
            'ca':self.ca,
            'jp':self.jp,
            'se':self.se,
            'smy':self.smy,
            'nz':self.nz,
            'msrland': self.msrland,
            'mu':self.mu,
            'au':self.au
        }
        d.update(self.get_socioeconomic_json())
        return d

class ForeignDirectInvestment(db.Model, SocioeconomicMixin):
    # 援对外直接净投资
    __tablename__ = "foreign_direct_investment"

    money = db.Column(db.Float)
    total = db.Column(db.Float)
    rate = db.Column(db.Float)

    def to_json(self):
        d = {
            'money': self.money,
            'rate': self.rate,
            'total': self.total
        }
        d.update(self.get_socioeconomic_json())
        return d