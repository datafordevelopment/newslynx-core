"""
Generate Markdown documentation from a SousChef configurations.
"""

from jinja2 import Template

from newslynx.lib import doc
from newslynx.exc import SousChefDocError
from newslynx.models.sous_chef_schema import SOUS_CHEF_DEFAULT_OPTIONS

# template for Sous Chef documentation.
SC_OPTS_TMPL = Template("""
### {{ name }}


* {{ description }}
* This Sous Chef runs the python module `{{ runs }}`.
* API Slug: `{{ slug }}`


#### Options


`{{ slug }}` accepts the following options when creating Recipes


{% for name, params in options.iteritems() %}
{% if name not in default_options %}
- `{{ name }}`
{% if params.description is defined %}
\t* {{ params.description }}
{% endif %}
{% if params.required is defined %}
\t* **Required**
{% endif %}
\t* Should be rendered with a `{{params.input_type}}` form.
{% if params.input_options is defined %}
\t* Choose from:
{% for o in params.input_options %}
\t\t- `{{ o }}`
{% endfor %}
{% endif %}
\t* Accepts inputs of type:
{% for t in params.value_types %}
\t\t- `{{ t }}`
{% endfor %}
{% if params.default is defined %}
\t* Defaults to `{{params.default}}`
{% endif %}
{% if params.help.link is defined %}
\t* More details on this option can be found [here]({{ params.help.link  }})
{% endif %}
{% endif %}
{% endfor %}
""")

SC_METRICS_TMPL = Template("""
{% if metrics is defined %}
#### Metrics


`{{ slug }}` generates the following Metrics


{% for name, params in metrics.iteritems() %}
- `{{ name }}`
{% if params.description is defined %}
\t* {{ params.description }}
{% endif %}
\t* Display name: `{{ params.display_name }}`
{% if params.faceted is defined and params.faceted %}
\t* This is a **faceted** metric.
{% endif %}
{% if params.type == 'computed' %}
\t* This is a **computed** metric with the formula:
\t\t- {{ params.formula }}
{% else %}
\t* Type: `{{ params.type }}`
{% endif %}
{% if params.content_levels is defined and params.content_levels|length > 0 %}
\t* Content Levels:
{% for l in params.content_levels %}
\t\t- `{{ l }}`
{% endfor %}
{% endif %}
{% if params.org_levels is defined and params.org_levels|length > 0 %}
\t* Org Levels:
{% for l in params.org_levels %}
\t\t- `{{ l }}`
{% endfor %}
{% endif %}
{% endfor %}
{% endif %}
""")


def create(sc, fp, format='md'):
    """
    Create documentation for a SousChef from it's configurations.
    """
    try:
        sc['default_options'] = SOUS_CHEF_DEFAULT_OPTIONS.keys()
        opts = SC_OPTS_TMPL.render(**sc).strip().replace('\n\n', '\n')
        metrics = SC_METRICS_TMPL.render(**sc).strip().replace('\n\n', '\n')
        content = "\n{}\n\n{}\n".format(opts, metrics)
        return doc.convert(content, 'md', format)

    except Exception as e:
        msg = """
        Documentation for Sous Chef {slug} located at {0}
        failed to generate for the following reason:
        {1}
        """.format(fp, e.message, **sc)
        raise SousChefDocError(msg)
