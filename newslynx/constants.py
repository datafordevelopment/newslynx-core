"""
Global defaults. These are non-configurable.
"""

# METRICS
METRIC_AGGREGATIONS = [
    'median', 'avg', 'min',
    'max', 'sum'
]

METRIC_LEVELS = [
    'org', 'content_item', 'all'
]

METRIC_FACET_KEYS = [
    'facet', 'value'
]

# EVENTS
EVENT_STATUSES = [
    'approved', 'pending', 'deleted'
]

EVENT_TYPES = [
    'promotion', 'alert', 'manual'
]

EVENT_PROVENANCES = [
    'manual', 'recipe'
]

EVENT_FACETS = [
    'tags', 'content_items', 'levels',
    'categories', 'sous_chefs',
    'recipes', 'statuses', 'provenances'
]

EVENT_SEARCH_VECTORS = [
    'meta', 'body', 'title',
    'authors', 'description', 'all'
]


# CONTENT ITEMS
CONTENT_ITEM_TYPES = [
    'video', 'article',
    'slideshow', 'interactive',
    'podcast'
]

CONTENT_ITEM_EVENT_FACETS = [
    'events', 'categories',
    'levels', 'event_statuses'
]

CONTENT_ITEM_FACETS = [
    'tags', 'provenances',
    'sous_chefs', 'recipes',
    'types', 'domains'
    ] + CONTENT_ITEM_EVENT_FACETS

CONTENT_ITEM_PROVENANCES = [
    'manual', 'recipe'
]

CONTENT_ITEM_SEARCH_VECTORS = [
    'meta', 'body', 'title',
    'authors', 'description', 'all'
]

# SOUS CHEFS
SOUS_CHEF_CREATES = [
    'events', 'content', 'tags',
    'metrics', 'series', 'reports',
    'external', 'internal'
]

# RECIPES
RECIPE_STATUSES = [
    'running', 'error', 'stable',
    'uninitialized', 'inactive'
]

# fields which we will remove before validation
RECIPE_REMOVE_FIELDS = [
    'id', 'sous_chef_id', 'user_id', 'org_id',
    'created', 'updated', 'scheduled', 'sous_chef'
]

# field which will not validate but will passthrough.
RECIPE_INTERNAL_FIELDS = [
    'status', 'last_run', 'last_job'
]

SOUS_CHEF_RESERVED_FIELDS = RECIPE_REMOVE_FIELDS + RECIPE_INTERNAL_FIELDS

# TAGS
TAG_TYPES = [
    'impact', 'subject'
]

IMPACT_TAG_CATEGORIES = [
    'promotion', 'citation', 'change',
    'achievement', 'other'
]

IMPACT_TAG_LEVELS = [
    'institution', 'media',
    'community', 'individual', 'internal'
]

# boolean parsing.
TRUE_VALUES = [
    'y', 'yes', '1', 't', 'true', 'on', 'ok'
]

FALSE_VALUES = [
    'n', 'no', '0', 'f', 'false', 'off'
]

NULL_VALUES = [
    'null', 'na', 'n/a', 'nan', 'none'
]
