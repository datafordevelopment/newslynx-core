"""
Create, Manage, and Install Sous Chef modules
"""

from newslynx.sc import module
from newslynx.util import here
from newslynx.lib.text import slug


def setup(parser):
    parser = parser.add_parser('sc-create')
    parser.add_argument('module_name',
                        type=str, help='The name / relative directory of the SousChef to create.')
    parser.add_argument('-g', '--github-user', dest='github_user',
                        type=str, help='The author\'s github user name.',
                        default='newslynx')
    parser.add_argument('-d', '--description', dest='description', type=str,
                        help='A short description of the Sous Chef module', default="")
    parser.add_argument('-a', '--author', type=str,
                        dest='author', default='Merlynne')
    parser.add_argument('-t', '--template', dest='template', type=str,
                        help='A path to a module template. Defaults to built-in template.', default=None)
    return 'sc-create', run


def run(opts, log, **kw):
    _slug = slug(opts.module_name)
    root_dir = here('.')
    kw.update({
        'root_dir': root_dir,
        'name': _slug.replace('-', '_'),
        'slug': _slug,
        'description': opts.description,
        'github_user': opts.github_user,
        'author': opts.author,
    })
    if opts.template:
        kw['tmpl_dir'] = opts.template
    log.info(
        'Creating Sous Chef Module: {}'.format(opts.module_name))
    module.create(**kw)
