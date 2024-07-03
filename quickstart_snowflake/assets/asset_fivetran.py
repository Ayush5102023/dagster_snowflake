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


# Use the fivetran_instance resource we defined in Step 1
fivetran_assets = load_assets_from_fivetran_instance(fivetran_instance)
