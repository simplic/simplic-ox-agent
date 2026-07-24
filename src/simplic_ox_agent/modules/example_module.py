"""Example logistics-export module.

Demonstrates the correct module contract:
* Accept a :class:`~simplic_ox_agent.core.context.ModuleContext`.
* Use only relative API paths via ``context.http``.
* Never select or override the simplic.ox environment.
* Never hard-code a simplic.ox hostname.
* Include structured context in every log entry.
"""

from __future__ import annotations

from ..core.context import ModuleContext


async def run(context: ModuleContext) -> None:
    """Export a logistics batch to the simplic.ox API."""
    context.logger.info(
        "Logistics export started",
        extra={
            "module_id": context.module_id,
            "instance_name": context.instance_name,
            "simplic_ox_environment": str(context.simplic_ox_environment),
            "application_environment": context.application_environment,
        },
    )

    payload = {
        "customer_id": context.global_settings.get("customer_id"),
        "site_id": context.global_settings.get("site_id"),
        "batch_size": context.module_settings.get("batch_size", 100),
    }

    response = await context.http.post(
        context.module_settings.get("target_endpoint", "/api/integrations/logistics"),
        json=payload,
    )

    context.logger.info(
        "Logistics export completed",
        extra={
            "module_id": context.module_id,
            "simplic_ox_environment": str(context.simplic_ox_environment),
            "http_status": response.status_code,
        },
    )
