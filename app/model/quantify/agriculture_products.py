from app import db


class AgricultureMixin:
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country = db.Column(db.String(64), index=True)
    time = db.Column(db.DateTime)
    kind = db.Column(db.String(64))

    def get_agriculture_json(self):
        return {
            'id': self.id,
            'county': self.country,
            'time': self.time,
            'kind': self.kind
        }


class AgriculturalProductionValueProfiles(db.Model,AgricultureMixin):
    # 农业生产总值
    __tablename__ = "agricultural_production_value_profiles"
    total = db.Column(db.Float)

    def to_json(self):
        return {
           'total':self.total
        }.update(self.get_agriculture_json())


class AgriculturalProductionProfiles(db.Model,AgricultureMixin):
    # 农业生产总量
    __tablename__="agricultural_production_profiles"
    total = db.Column(db.Float)

    def to_json(self):
        return {
           'total':self.total
        }.update(self.get_agriculture_json())


class GrainProductionProfiles(db.Model, AgricultureMixin):
    # 谷物生产概况
    __tablename__="grain_production_profiles"

    area = db.Column(db.Float)
    total = db.Column(db.Float)
    average = db.Column(db.Float)

    def to_json(self):
        return {
           'area':self.area,
            'total':self.total,
            'average':self.average
        }.update(self.get_agriculture_json())


class OtherCropProductionProfiles(db.Model, AgricultureMixin):
    # 其他作物生产概况
    __tablename__ = "other_crop_production_profiles"

    area = db.Column(db.Float)
    total = db.Column(db.Float)
    average = db.Column(db.Float)

    def to_json(self):
        return {
            'area': self.area,
            'total': self.total,
            'average': self.average
        }.update(self.get_agriculture_json())


class MeatProductionProfiles(db.Model, AgricultureMixin):
    # 肉类生产概况
    __tablename__ = "meat_production_profiles"

    total = db.Column(db.Float)

    def to_json(self):
        return {
            'total': self.total,
        }.update(self.get_agriculture_json())


class AnimalHusbandryProfiles(db.Float, AgricultureMixin):
    # 畜牧业Animal husbandry
    __tablename__ = "animal_husbandry_profiles"

    grown = db.Column(db.Float)
    growing = db.Column(db.Float)

    def to_json(self):
        return {
            'grown': self.grown,
            'growing':self.growing
        }.update(self.get_agriculture_json())


class AquaticProductsProfiles(db.Model,AgricultureMixin):

    # 水产概况

    __tablename__ = "aquatic_products_profiles"

    fishing = db.Column(db.Float)
    breed = db.Column(db.Float)

    def to_json(self):
        return {
            'fishing': self.fishing,
            'breed':self.breed
        }.update(self.get_agriculture_json())


class PlantProfiles(db.Model, AgricultureMixin):
    # 种植业概况

    __tablename__ = "plant_profiles"

    area = db.Column(db.Float)
    total = db.Column(db.Float)
    average = db.Column(db.Float)

    def to_json(self):
        return {
            'area': self.area,
            'total': self.total,
            'average': self.average
        }.update(self.get_agriculture_json())


class AnimalHusbandryAquaticProducts(db.Model,AgricultureMixin):

    # 水产和畜牧概况

    __tablename__ = "animal_husbandry_aquatic_products"

    total = db.Column(db.Float)
    rank = db.Column(db.Integer)

    def to_json(self):
        return {
            'area': self.area,
            'total': self.total,
        }.update(self.get_agriculture_json())


class AgriculturalProductsTradeProfiles(db.Model, AgricultureMixin):
    # 农产品贸易

    __tablename__ = "agricultural_products_trade_profiles"

    import_num = db.Column(db.Float)
    output_num = db.Column(db.Float)

    trade_num = db.Column(db.Float)

    import_rate = db.Column(db.Float)
    output_rate = db.Column(db.Float)

    def to_json(self):
        return {
            'import_num': self.import_num,
            'output_num': self.output_num,
            'trade_num':self.trade_num,
            'import_rate':self.import_rate,
            'output_rate':self.output_rate
        }.update(self.get_agriculture_json())


class KindAgriculturalProductsTradeMoneyProfiles(db.Model, AgricultureMixin):
    # 分品种农产品贸易

    __tablename__ = "kind_agricultural_products_trade_money_profiles"

    import_num = db.Column(db.Float)
    output_num = db.Column(db.Float)

    trade_num = db.Column(db.Float)

    import_rate = db.Column(db.Float)
    output_rate = db.Column(db.Float)

    def to_json(self):
        return {
            'import_num': self.import_num,
            'output_num': self.output_num,
            'trade_num': self.trade_num,
            'import_rate': self.import_rate,
            'output_rate': self.output_rate
        }.update(self.get_agriculture_json())


class KindAgriculturalProductsTradeNumProfiles(db.Model, AgricultureMixin):
    # 分品种农产品贸易

    __tablename__ = "kind_agricultural_products_num_money_profiles"

    import_num = db.Column(db.Float)
    output_num = db.Column(db.Float)

    trade_num = db.Column(db.Float)

    import_rate = db.Column(db.Float)
    output_rate = db.Column(db.Float)

    def to_json(self):
        return {
            'import_num': self.import_num,
            'output_num': self.output_num,
            'trade_num': self.trade_num,
            'import_rate': self.import_rate,
            'output_rate': self.output_rate
        }.update(self.get_agriculture_json())


class AgricultureForeignInvestmentStock(db.Model, AgricultureMixin):
    # 农业对外投资存量

    __tablename__ = "agriculture_foreign_investment_stock"

    money = db.Column(db.Float)

    def to_json(self):
        return {
            'money': self.money,
        }.update(self.get_agriculture_json())


class AgricultureForeignInvestmentStockStructure(db.Model, AgricultureMixin):
    # 农业对外投资存量结构

    __tablename__ = "agriculture_foreign_investment_stock_structure"

    money = db.Column(db.Float)

    def to_json(self):
        return {
            'money': self.money,
        }.update(self.get_agriculture_json())


class AgricultureForeignInvestmentFluent(db.Model, AgricultureMixin):
    # 农业对外投资存量流量

    __tablename__ = "agriculture_foreign_investment_fluent"

    money = db.Column(db.Float)

    def to_json(self):
        return {
            'money': self.money,
        }.update(self.get_agriculture_json())


class AgricultureForeignInvestmentImport(db.Model, AgricultureMixin):
    # 农业对外投资存量流入

    __tablename__ = "agriculture_foreign_investment_import"

    money = db.Column(db.Float)

    def to_json(self):
        return {
            'money': self.money,
        }.update(self.get_agriculture_json())


class AgricultureForeignInvestmentUsedStructure(db.Model, AgricultureMixin):
    # 农业对外投资存量使用结构

    __tablename__ = "agriculture_foreign_investment_used_structure"

    money = db.Column(db.Float)

    def to_json(self):
        return {
            'money': self.money,
        }.update(self.get_agriculture_json())