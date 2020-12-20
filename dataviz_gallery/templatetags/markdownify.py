from django import template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import pathlib

register = template.Library()

# Additional very precise and helpful reference for pygments https://overiq.com/pygments-tutorial/ 
class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        # for reference see https://pygments.org/docs/formatters/  
        formatter = HtmlFormatter(full=False, style="friendly", linenos=False, noclasses=True)
        return highlight(code, lexer, formatter)


@register.simple_tag
def code_block_from_markdown(file_name):
    """ Return code block originally formatted in markdown as html """
    markdown_filepath = pathlib.Path.cwd() / "plot" / "scripts" / file_name
    with open(markdown_filepath, "r") as md_file:
        markdown_text = md_file.read()

    markdown = mistune.Markdown(renderer=HighlightRenderer())
    html_text = markdown(markdown_text)  # convert markdown to html
    return html_text

