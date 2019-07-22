from extract.pages import Pages
import jinja2


def page_to_html(pages: Pages = None):
    templateLoader = jinja2.FileSystemLoader(searchpath="./extract/html")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template('page.html')

    pageNodes = []
    for page in pages.pages:
        pageNode = {
            'bbox': page.bbox,
            'width': page.bbox.lower_right_coordinate.x,
            'height': page.bbox.lower_right_coordinate.y,
            'textNodes': []
        }
        for text in page.texts():
            pageNode['textNodes'].append({
                'bbox': text.bbox,
                'contents': text.contents,
                'width': text.width(),
                'height': text.height() - 2,
                'left': text.space_left(0),
                'top': page.bbox.lower_right_coordinate.y - text.bbox.upper_left_coordinate.y,
                'font_size': text.style.font_size - 6,
            })

        pageNodes.append(pageNode)

    return template.render(pageNodes=pageNodes)