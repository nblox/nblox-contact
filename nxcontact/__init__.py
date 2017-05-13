# Including `APP` here allows the `flask run` command to work.
from nxcontact.app import APP  # noqa

# Import all views to enable loading into Flask.
import nxcontact.views  # noqa
