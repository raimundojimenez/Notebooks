from IPython.core.display import display, HTML

def table_style():
   # To style tables
    display(HTML("<style>\
        .jp-RenderedHTMLCommon table { font-size: 14px;display:inline-block;}.jp-RenderedHTMLCommon th { min-width:90px;max-width:80%;}\
        .rendered_html table { font-size: 14px;display:inline-block;}.rendered_html th { min-width:90px;max-width:80%;}\
    </style>"))