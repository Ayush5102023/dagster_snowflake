from dagster import (
    AssetKey,
    AutoMaterializePolicy,
    AutoMaterializeRule,
    EnvVar,
    load_assets_from_current_module,
)
from dagster_fivetran import FivetranResource, load_assets_from_fivetran_instance

fivetran_instance = FivetranResource(
    api_key=EnvVar("BB1TZASKQX4nSvPM"),
    api_secret=EnvVar("FjgGxo0ysYMGtKrrxUSp3gAgHOdqthNY"),
)
