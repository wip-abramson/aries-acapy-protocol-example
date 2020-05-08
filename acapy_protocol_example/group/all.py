"""Load all plugins."""

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.protocol_registry import ProtocolRegistry

from acapy_protocol_example.protocolexample.v1_0.setup import setup as examplesetup


async def setup(context: InjectionContext):
    """Setup Toolbox Plugin."""
    protocol_registry = await context.inject(ProtocolRegistry)
    await examplesetup(context, protocol_registry)
