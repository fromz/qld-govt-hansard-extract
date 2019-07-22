from extract.page import Page
import jinja2


def page_to_html(page: Page = None):
    templateLoader = jinja2.FileSystemLoader(searchpath="./extract/html")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template('test.html')
    pageNode = {
        'width': page.bbox.lower_right_coordinate.x,
        'height': page.bbox.lower_right_coordinate.y,
    }

    textNodes = []
    for text in page.texts():
        textNodes.append({
            'contents': text.contents,
            'width': text.width(),
            'height': text.height() - 2,
            'left': text.space_left(0),
            'top': page.bbox.lower_right_coordinate.y - text.bbox.upper_left_coordinate.y,
            'font_size': text.style.font_size - 6,
        })
    return template.render(pageNode=pageNode, textNodes=textNodes)