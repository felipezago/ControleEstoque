import os

from fpdf import FPDF
from Funcoes.utils import retirar_formatacao, formatar_cnpj


class PDF(FPDF):
    def __init__(self, empresa, cliente):
        super(PDF, self).__init__()

        self.empresa = empresa
        self.cliente = cliente

        if not os.path.isdir('temp'):
            os.makedirs('temp')

        self.add_page()
        self.informacoes_cliente()

    def header(self):
        from datetime import datetime

        self.linha_header()
        self.imagex()
        self.set_font('helvetica', 'B', 10)

        # 1 COLUNA
        self.text(35, 12, self.empresa[0])
        self.text(35, 17, f"{self.empresa[1]}, N° {self.empresa[2]}")
        self.text(35, 22, self.empresa[3])
        self.text(35, 27, self.empresa[4])
        self.text(35, 32, f"CNPJ: {self.empresa[5]}")

        # 2 COLUNA
        self.text(85, 27, f"{self.empresa[6]} - {self.empresa[7]}")
        self.text(85, 32, f"IE: {self.empresa[8]}")

        # 3 COLUNA
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
        self.text(159, 12, f"DATA: {data_e_hora_em_texto}")
        self.ln(5)

    def linha_header(self):
        self.set_fill_color(255, 255, 255)
        self.rect(4, 4, 202, 33)

    def footer(self):
        self.set_y(34)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(255, 255, 255)
        self.cell(380, 520, 'Pagina ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def imagex(self):
        from Model.Empresa import Empresa
        import os

        self.set_xy(5, 5)
        emp = Empresa()
        emp.cnpj = retirar_formatacao(self.empresa[5])
        emp.nome_fantasia = self.empresa[0]

        emp.ler_imagem_empresas_pdf("temp/")
        nome_img = emp.nome_fantasia.upper().strip().replace(' ', '').replace('.', '')
        dir_img = f"temp/{nome_img}.png"

        if os.path.isfile(dir_img):
            self.image(dir_img, link='', type='', w=28, h=31)
            os.remove(dir_img)
        else:
            self.image("Imagens/logo_fzr.png", link='', type='', w=28, h=31)

    def informacoes_cliente(self):
        self.set_font('helvetica', 'B', 10)

        self.text(5, 45, "Informações do Cliente:")
        self.text(150, 50, "Endereço:")

        self.set_font('helvetica', 'I', 10)
        self.text(5, 55, f"Nome: {self.cliente[0]}")
        cpf_cnpj = retirar_formatacao(self.cliente[1])
        if len(cpf_cnpj) >= 14:
            self.text(5, 60, f"CNPJ: {formatar_cnpj(cpf_cnpj)}")
        else:
            self.text(5, 60, f"CPF: {self.cliente[1]}")

        if self.cliente[2] != 'IS.ENT.O-':
            self.text(5, 65, f"RG: {self.cliente[2]}")
        else:
            self.text(5, 65, f"RG: {retirar_formatacao(self.cliente[2])}")
        self.text(5, 70, f"Celular: {self.cliente[3]}")

        self.text(80, 55, f"Fone: {self.cliente[4]}")
        self.text(80, 60, f"Email: {self.cliente[5]}")

        self.text(150, 55, f"{self.cliente[6]} N° {self.cliente[8]}")
        self.text(150, 60, f"{self.cliente[7]}")
        self.text(150, 65, f"{self.cliente[9]} - {self.cliente[10]}")

        self.line(5, 75, 205, 75)

    def create_table(self, table_data, title='', data_size=10, title_size=12, align_data='L', align_header='L',
                     cell_width='even', x_start='x_default', emphasize_data=[], emphasize_style=None,
                     emphasize_color=(0, 0, 0)):

        """
        table_data:
                    list of lists with first element being list of headers
        title:
                    (Optional) title of table (optional)
        data_size:
                    the font size of table data
        title_size:
                    the font size fo the title of the table
        align_data:
                    align table data
                    L = left align
                    C = center align
                    R = right align
        align_header:
                    align table data
                    L = left align
                    C = center align
                    R = right align
        cell_width:
                    even: evenly distribute cell/column width
                    uneven: base cell size on lenght of cell/column items
                    int: int value for width of each cell/column
                    list of ints: list equal to number of columns with the widht of each cell / column
        x_start:
                    where the left edge of table should start
        emphasize_data:
                    which data elements are to be emphasized - pass as list
                    emphasize_style: the font style you want emphaized data to take
                    emphasize_color: emphasize color (if other than black)

        """

        epw = self.w - 2 * self.l_margin

        default_style = self.font_style
        if emphasize_style == None:
            emphasize_style = default_style

        # default_font = self.font_family
        # default_size = self.font_size_pt
        # default_style = self.font_style
        # default_color = self.color # This does not work

        # Get Width of Columns
        def get_col_widths():
            col_width = cell_width
            if col_width == 'even':
                col_width = epw / len(data[
                                               0]) - 1  # distribute content evenly   # epw = effective page width (width of page not including margins)
            elif col_width == 'uneven':
                col_widths = []

                # searching through columns for largest sized cell (not rows but cols)
                for col in range(len(table_data[0])):  # for every row
                    longest = 0
                    for row in range(len(table_data)):
                        cell_value = str(table_data[row][col])
                        value_length = self.get_string_width(cell_value)
                        if value_length > longest:
                            longest = value_length
                    col_widths.append(longest + 4)  # add 4 for padding
                col_width = col_widths

                ### compare columns

            elif isinstance(cell_width, list):
                col_width = cell_width  # TODO: convert all items in list to int
            else:
                # TODO: Add try catch
                col_width = int(col_width)
            return col_width

        # Convert dict to lol
        # Why? because i built it with lol first and added dict func after
        # Is there performance differences?
        if isinstance(table_data, dict):
            header = [key for key in table_data]
            data = []
            for key in table_data:
                value = table_data[key]
                data.append(value)
            # need to zip so data is in correct format (first, second, third --> not first, first, first)
            data = [list(a) for a in zip(*data)]

        else:
            header = table_data[0]
            data = table_data[1:]

        line_height = self.font_size * 2.5

        col_width = get_col_widths()

        # Get starting position of x
        # Determin width of table to get x starting point for centred table
        if x_start == 'C':
            table_width = 0
            if isinstance(col_width, list):
                for width in col_width:
                    table_width += width
            else:  # need to multiply cell width by number of cells to get table width
                table_width = col_width * len(table_data[0])
            # Get x start by subtracting table width from pdf width and divide by 2 (margins)
            margin_width = self.w - table_width
            # TODO: Check if table_width is larger than pdf width

            center_table = margin_width / 2  # only want width of left margin not both
            x_start = center_table
            self.set_x(x_start)
        elif isinstance(x_start, int):
            self.set_x(x_start)
        elif x_start == 'x_default':
            x_start = self.set_x(self.l_margin)

        # TABLE CREATION #

        # add title
        if title != '':
            self.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=self.font_size)
            self.ln(line_height)  # move cursor back to the left margin

        # add header
        y1 = self.get_y()
        if x_start:
            x_left = x_start
        else:
            x_left = self.get_x()
        x_right = epw + x_left
        if not isinstance(col_width, list):
            if x_start:
                self.set_x(x_start)
            for datum in header:
                self.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3,
                                max_line_height=self.font_size)
                x_right = self.get_x()
            self.ln(line_height)  # move cursor back to the left margin
            y2 = self.get_y()
            self.line(x_left, y1, x_right, y1)
            self.line(x_left, y2, x_right, y2)

            for row in data:
                if x_start:  # not sure if I need this
                    self.set_x(x_start)
                for datum in row:
                    if datum in emphasize_data:
                        self.set_text_color(*emphasize_color)
                        self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3,
                                        max_line_height=self.font_size)
                        self.set_text_color(0, 0, 0)
                    else:
                        self.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3,
                                        max_line_height=self.font_size)  # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                self.ln(line_height)  # move cursor back to the left margin

        else:
            if x_start:
                self.set_x(x_start)
            for i in range(len(header)):
                datum = header[i]
                self.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3,
                                max_line_height=self.font_size)
                x_right = self.get_x()
            self.ln(line_height)  # move cursor back to the left margin
            y2 = self.get_y()
            self.line(x_left, y1, x_right, y1)
            self.line(x_left, y2, x_right, y2)

            for i in range(len(data)):
                if x_start:
                    self.set_x(x_start)
                row = data[i]
                for i in range(len(row)):
                    datum = row[i]
                    if not isinstance(datum, str):
                        datum = str(datum)
                    adjusted_col_width = col_width[i]
                    if datum in emphasize_data:
                        self.set_text_color(*emphasize_color)
                        self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3,
                                        max_line_height=self.font_size)
                        self.set_text_color(0, 0, 0)
                    else:
                        self.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3,
                                        max_line_height=self.font_size)  # ln = 3 - move cursor to right with same vertical offset # this uses an object named self
                self.ln(line_height)  # move cursor back to the left margin
        y3 = self.get_y()
        self.line(x_left, y3, x_right, y3)
