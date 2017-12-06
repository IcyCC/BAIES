import re
from app.model.quantify import socioeconomic,agriculture_products
from app.model.qualitative import information
from app.model import user
from jinja2 import Template





class Extractor:

    def __init__(self, input_file):

        self.input_file = input_file
        self.pm = r'class (.*?)\('

    def parser(self):
        body = ''
        with open(self.input_file, 'r') as f:
            body = f.read()

        result = re.findall(self.pm, body)
        return result


class Generator:
    def __init__(self, out_put):

        self.out_put = out_put
        with open("./code_base.html", "r") as f:
            b = f.read()
            self.template = Template(b)

    def gen(self, items, bp, table, permisson):
        with open(self.out_put, "a+") as f:
            for item in items:
                f.write(self.template.render(Table=getattr(table,item), BP=bp,Permisson=permisson))




if __name__ == '__main__':

    e = Extractor("/home/suchang/Code/Proj/BAIES/app/model/quantify/socioeconomic.py")
    g = Generator("/home/suchang/Code/Proj/BAIES/app/view/quantify/socioeconomic_a.py")
    g.gen(e.parser(), "quantify_blueprint",table=socioeconomic, permisson="QUANTIFY")

    e = Extractor("/home/suchang/Code/Proj/BAIES/app/model/quantify/agriculture_products.py")
    g = Generator("/home/suchang/Code/Proj/BAIES/app/view/quantify/agriculture_products_a.py")
    g.gen(e.parser(), "quantify_blueprint",table=agriculture_products, permisson="QUANTIFY")

    e = Extractor("/home/suchang/Code/Proj/BAIES/app/model/user/__init__.py")
    g = Generator("/home/suchang/Code/Proj/BAIES/app/view/user/user.py")
    g.gen(e.parser(), "user_blueprint", table=user, permisson="USER")

    e = Extractor("/home/suchang/Code/Proj/BAIES/app/model/qualitative/information.py")
    g = Generator("/home/suchang/Code/Proj/BAIES/app/view/qualitative/information.py")
    g.gen(e.parser(), "qualitative_blueprint",table=information, permisson="QUALITATIVE")
