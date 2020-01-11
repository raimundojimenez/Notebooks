from IPython.core.display import display, HTML

def table_style():
   # To style tables over-riding Jupyter css script styles (Jupyter lab, nbviewer)
    display(HTML("<style>\
        .jp-RenderedHTMLCommon table { font-size: 14px;display:inline-block;text-align:left;}.jp-RenderedHTMLCommon th { min-width:90px;max-width:80%;text-align:left;}\
        .rendered_html table { font-size: 14px;display:inline-block;text-align:left;}.rendered_html th { min-width:90px;max-width:80%;text-align:left;}\
    </style>"))