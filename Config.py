import os

# always must be caps lock for the variable!
class Config:
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = 'Fakebook Rest Api'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/docs'
    OPENAPI_SWAGGER_UI_URL = '/docs'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLDATABASE_URL')
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")