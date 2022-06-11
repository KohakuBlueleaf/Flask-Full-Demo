from typing import Callable
from flask import Blueprint, render_template


def create_page_app(
    name: str
) -> tuple[Blueprint, Callable[[str, ], str]]:
    '''Create the blueprint app and template renderer for a page'''

    app = Blueprint(
        name,
        __name__,
        root_path='pages/',
        template_folder='',
        static_folder=f'{name}/static',
        url_prefix=f'/{name}'
    )

    def renderer(template_name: str, *args, **kwargs):
        return render_template(
            f'{name}/templates/{template_name}',
            *args, **kwargs
        )

    return app, renderer
